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

SYSTEM_PROMPT = """You are Bell, an AI customer support agent for a tech company.
You communicate via LINE Official Account. Be friendly, concise, and professional.
Always reply in the same language the customer uses (Thai or English).

You have access to the company knowledge base below.
Use it to answer customer questions accurately.

If the knowledge base does not contain enough information to answer confidently,
or if the issue requires system access, code-level investigation, or account changes
— escalate instead of guessing.

Knowledge Base:
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
        max_tokens=1024,
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
