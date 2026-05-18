import anthropic
from app.config import settings
from app.knowledge.loader import load_knowledge_base

client = anthropic.Anthropic(api_key=settings.anthropic_api_key)

TOOLS = [
    {
        "name": "answer_customer",
        "description": "Use this when you can confidently answer the customer's question from the knowledge base.",
        "input_schema": {
            "type": "object",
            "properties": {
                "answer": {
                    "type": "string",
                    "description": "The full reply to send to the customer. Match the customer's language (Thai or English).",
                },
                "resolution_type": {
                    "type": "string",
                    "enum": ["FCR"],
                    "description": "Always FCR when resolved by AI.",
                },
            },
            "required": ["answer", "resolution_type"],
        },
    },
    {
        "name": "escalate",
        "description": "Use this when you cannot confidently answer and the case needs a human or specialist.",
        "input_schema": {
            "type": "object",
            "properties": {
                "reason": {
                    "type": "string",
                    "description": "Brief internal reason why escalation is needed (in English, for the ticket).",
                },
                "route_to": {
                    "type": "string",
                    "enum": ["Human-L1", "L2-Tech", "L2-Dev"],
                    "description": (
                        "Human-L1: general/account/billing. "
                        "L2-Tech: product bugs, config, feature not working. "
                        "L2-Dev: code, API, integration, data issues."
                    ),
                },
                "customer_message": {
                    "type": "string",
                    "description": "Holding message to send to the customer. Match their language (Thai or English).",
                },
            },
            "required": ["reason", "route_to", "customer_message"],
        },
    },
]

SYSTEM_PROMPT = """## ตัวตนและบุคลิกภาพ (Identity & Personality)

คุณคือ เบลล์ (Bell) — ไม่ใช่แค่ AI แต่คือ "ตัวแม่" ในโลก Customer Support ของ WePOS
คุณเป็นตัวแทนจาก Ascend Commerce ผู้ให้บริการ WePOS ซึ่งเป็น Odoo Gold Partner และ Strategic Partner เพียงรายเดียวในประเทศไทย

**Tone:** มั่นใจ (Confident), เฉียบคม (Sharp), อ่อนน้อมและจริงใจ (Authentic & Humble)
**ภาษา:** ภาษาไทยระดับ Business Casual — ดูแพง น่าเชื่อถือ ไม่เป็นทางการเกินไป
**หลักการตอบ:** ทุกคำตอบต้องมี Next Step เสมอ — ไม่ตอบแบบปิดตาย

## กรอบความคิด (Thinking Framework)

ก่อนตอบทุกครั้ง เบลล์จะกรองผ่าน 4 เลนส์:
1. **Strategic Discovery** — ขุดหา Root Cause จริงๆ ไม่ตอบแค่สิ่งที่ถาม
2. **Accountability** — ไม่รับปากในสิ่งที่ทำไม่ได้ รักษาภาพลักษณ์ WePOS เสมอ
3. **Value-Driven** — เชื่อมทุกคำตอบกับ "เพิ่มกำไร / ลดงาน / ประหยัดเวลา"
4. **Thai Compliance** — แม่นยำเรื่อง VAT, WHT, กรมสรรพากร, PDPA

## ความเชี่ยวชาญ (Expertise)
- WePOS POS System (ทุกฟีเจอร์)
- Odoo ERP (โครงสร้าง, การใช้งาน)
- Hardware: iMIN Falcon1, iMIN Swan2 และอุปกรณ์ WePOS
- Integrations: EGG CRM, Axons CRM
- Thai Tax: VAT, WHT, e-Tax Invoice

## ข้อมูลอ้างอิง (Credibility)
- ลูกค้ากว่า 3,000 รายทั่วประเทศ
- พาร์ทเนอร์ระดับประเทศ: ไก่ย่าง 5 ดาว (Five Star), Makro FR Club (1,000+ ร้านค้า)
- รองรับทุกขนาดธุรกิจ: SME ถึง Enterprise

## ช่องทาง Support
- LINE @wepos: 07:00–22:00 ทุกวัน
- Call Center: 02-0202364 กด 1 (09:00–18:00 ทุกวัน)

## ข้อจำกัด (Limitations)
- หากข้อมูลใน Knowledge Base ไม่เพียงพอ → แจ้งตรงๆ ว่าจะหาข้อมูลที่ถูกต้องมาให้ อย่าเดา
- หากปัญหาต้องการการแก้ไขระบบ, เข้าถึง account, หรือ technical investigation → escalate ทันที
- อย่าสัญญาในสิ่งที่ไม่แน่ใจ

## Knowledge Base (ข้อมูลอ้างอิงจากเอกสาร)
ใช้ข้อมูลด้านล่างเพื่อตอบคำถามลูกค้า:

{knowledge_base}
"""


class AgentResult:
    def __init__(self, action: str, payload: dict):
        self.action = action    # "answer" or "escalate"
        self.payload = payload


async def run(message: str, conversation_history: list[dict] = None) -> AgentResult:
    knowledge_base = load_knowledge_base()
    system = SYSTEM_PROMPT.format(knowledge_base=knowledge_base or "No documents loaded yet.")

    messages = conversation_history or []
    messages = messages + [{"role": "user", "content": message}]

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4096,
        system=system,
        tools=TOOLS,
        messages=messages,
    )

    for block in response.content:
        if block.type == "tool_use":
            if block.name == "answer_customer":
                return AgentResult("answer", block.input)
            elif block.name == "escalate":
                return AgentResult("escalate", block.input)

    # fallback if Claude replies in text without using a tool
    text = " ".join(b.text for b in response.content if hasattr(b, "text"))
    return AgentResult("answer", {"answer": text, "resolution_type": "FCR"})
