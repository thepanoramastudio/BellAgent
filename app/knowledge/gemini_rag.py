import logging
import asyncio
import re
import shutil
import tempfile
from pathlib import Path
from typing import Optional

from google import genai
from google.genai import types

logger = logging.getLogger(__name__)

PDF_DIR = Path(__file__).parent.parent.parent / "knowledge_base" / "pdfs"

_client: Optional[genai.Client] = None
_kb_files: list = []

MODEL = "gemini-2.5-flash"


def init(api_key: str):
    global _client
    _client = genai.Client(api_key=api_key)


def _safe_name(filename: str) -> str:
    return re.sub(r"[^a-zA-Z0-9_\-]", "_", filename) + ".pdf"


def _upload_files():
    global _kb_files
    if _kb_files:
        return

    if not PDF_DIR.exists() or not any(PDF_DIR.glob("*.pdf")):
        logger.warning("No PDFs in knowledge_base/pdfs/ — Gemini RAG unavailable")
        return

    with tempfile.TemporaryDirectory() as tmpdir:
        for i, pdf in enumerate(sorted(PDF_DIR.glob("*.pdf"))):
            # copy to ASCII temp filename to avoid encoding issues
            tmp_path = Path(tmpdir) / f"doc_{i:02d}.pdf"
            shutil.copy2(pdf, tmp_path)
            display = _safe_name(pdf.stem)
            try:
                f = _client.files.upload(
                    file=str(tmp_path),
                    config=types.UploadFileConfig(
                        display_name=display,
                        mime_type="application/pdf",
                    ),
                )
                _kb_files.append(f)
                logger.info(f"Gemini uploaded: {pdf.name}")
            except Exception as e:
                logger.warning(f"Could not upload {pdf.name}: {e}")

    logger.info(f"Gemini KB ready: {len(_kb_files)} PDF(s)")


def _search_sync(query: str) -> str:
    if _client is None:
        logger.error("Gemini client not initialized")
        return ""

    _upload_files()

    if not _kb_files:
        return ""

    prompt = (
        f"จากเอกสารที่แนบมาทั้งหมด ให้ดึงข้อมูลที่เกี่ยวข้องกับคำถามต่อไปนี้ออกมาให้ครบถ้วน:\n\n"
        f"คำถาม: {query}\n\n"
        "ตอบเป็นข้อเท็จจริงจากเอกสาร ครบถ้วน ตรงประเด็น รวมขั้นตอน ราคา และรายละเอียดที่เกี่ยวข้อง "
        "ถ้าไม่มีข้อมูลในเอกสารให้ตอบว่า 'ไม่พบข้อมูลในเอกสาร'"
    )

    try:
        response = _client.models.generate_content(
            model=MODEL,
            contents=[*_kb_files, prompt],
        )
        return response.text
    except Exception as e:
        logger.error(f"Gemini search error: {e}")
        return ""


async def search(query: str) -> str:
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, _search_sync, query)
