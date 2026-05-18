import os
from pathlib import Path

KB_DIR = Path(__file__).parent.parent.parent / "knowledge_base"


def load_knowledge_base() -> str:
    if not KB_DIR.exists():
        return ""

    chunks = []
    for file in sorted(KB_DIR.glob("**/*.md")) or sorted(KB_DIR.glob("**/*.txt")):
        content = file.read_text(encoding="utf-8").strip()
        if content:
            chunks.append(f"## [{file.name}]\n{content}")

    return "\n\n".join(chunks)
