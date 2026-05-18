import anthropic
from app.config import settings
from app.knowledge import gemini_rag

client = anthropic.Anthropic(api_key=settings.anthropic_api_key)

gemini_rag.init(settings.google_api_key)

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
        "description": (
            "Use this ONLY when the case requires a human to take a real system action — "
            "such as: creating or modifying a customer account, investigating a technical bug, "
            "handling an API/code error, or accessing customer-specific backend data. "
            "Do NOT escalate for: how-to questions, pricing questions, package renewal steps, "
            "feature explanations, or any question that can be answered from the knowledge base. "
            "If the answer exists in the knowledge base, always use answer_customer instead."
        ),
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

## ราคาแพ็กเกจ WePOS (ข้อมูลถูกต้อง 100% — ใช้ตัวเลขนี้เสมอ)

💰 ค่าบริการแพ็กเกจ WePOS Standard Plan (รวม VAT 7%):
- 1 เดือน = **฿533.93**
- 6 เดือน (ลด 5%) = **฿3,043.40**
- 12 เดือน (ลด 20%) = **฿5,125.73**

ขั้นตอนต่ออายุแพ็กเกจ:
1. โอนเงินเข้า บริษัท แอสเซนด์ คอมเมิร์ซ จำกัด — ธนาคารไทยพาณิชย์ (SCB) บัญชีออมทรัพย์ เลขที่ 106-242085-2
2. กรอกฟอร์มยืนยันที่ https://tinyurl.com/wepospackagenew พร้อมแนบสลิป
3. เจ้าหน้าที่ต่ออายุภายใน 30 นาที (ช่วง 09:00–18:00 วันทำการ)

## กฎการตัดสินใจ: ตอบเอง vs ส่งต่อ (Answer vs Escalate)

**ตอบเองเสมอ (answer_customer)** สำหรับ:
- วิธีใช้งาน WePOS ทุกฟีเจอร์ (เพิ่มสินค้า, ขายสินค้า, รายงาน ฯลฯ)
- ขั้นตอนต่ออายุแพ็กเกจ, ราคาแพ็กเกจ, วิธีชำระเงิน
- วิธี reset PIN, วิธีเข้าสู่ระบบ
- ข้อมูล Serial Number, การรับประกัน, ช่องทางติดต่อ
- คำถามทั่วไปที่มีคำตอบใน Knowledge Base

**ส่งต่อ (escalate) เฉพาะเมื่อ:**
- ต้องการให้ทีมงานดำเนินการในระบบจริง (สร้างร้านใหม่, แก้ข้อมูล account)
- ปัญหา Hardware ที่แก้เบื้องต้นแล้วยังไม่หาย และต้องส่งซ่อม / เคลม / เปลี่ยนเครื่อง → route_to: Human-L1 (ทีม L1 คนจะประสาน supplier ต่อ)
- มี software error หรือ bug ที่ต้องให้ทีม tech ตรวจสอบ → route_to: L2-Tech
- ปัญหาระดับ code/API/integration → route_to: L2-Dev
- ไม่มีคำตอบใน Knowledge Base เลย และต้องการข้อมูลเฉพาะบุคคลของลูกค้า

**แนวทาง Hardware:**
- ก่อน escalate ให้ลองแนะนำ troubleshoot เบื้องต้นจาก KB ก่อนเสมอ (restart เครื่อง, ตรวจสอบการเชื่อมต่อ, reset กระดาษพิมพ์ ฯลฯ)
- ถ้าลูกค้าทำแล้วยังไม่หาย หรือเครื่องเสียหายทางกายภาพ → escalate: Human-L1 พร้อมแจ้งลูกค้าว่า "ทีมงานจะติดต่อกลับเพื่อประสานงานซ่อมให้ค่ะ"
- แยกให้ออกว่า: Software (app/system) หรือ Hardware (ตัวเครื่อง, printer, scanner, cash drawer)

**ห้าม escalate** เพียงเพราะคำถามเกี่ยวกับ "account", "billing", หรือ "แพ็กเกจ" — หากมีคำตอบใน KB ให้ตอบเองทันที

## Knowledge Base (ข้อมูลอ้างอิงจากเอกสาร)
ใช้ข้อมูลด้านล่างเพื่อตอบคำถามลูกค้า:

{knowledge_base}
"""


class AgentResult:
    def __init__(self, action: str, payload: dict):
        self.action = action    # "answer" or "escalate"
        self.payload = payload


async def run(message: str, conversation_history: list[dict] = None) -> AgentResult:
    knowledge_base = await gemini_rag.search(message)
    system = SYSTEM_PROMPT.format(knowledge_base=knowledge_base or "No relevant information found in knowledge base.")

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
