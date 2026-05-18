import logging
from pathlib import Path

logger = logging.getLogger(__name__)

KB_DIR = Path(__file__).parent.parent.parent / "knowledge_base"

MAX_CHARS_PER_FILE = 20000  # limit per file
MAX_TOTAL_CHARS = 150000    # total knowledge base size cap (~37k tokens, well within 200k limit)


def _read_pdf(path: Path) -> str:
    try:
        import pdfplumber
        text_parts = []
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages[:20]:   # max 20 pages per PDF
                text = page.extract_text()
                if text:
                    text_parts.append(text.strip())
        return "\n".join(text_parts)
    except Exception as e:
        logger.warning(f"Could not read PDF {path.name}: {e}")
        return ""


def _read_excel(path: Path) -> str:
    try:
        import openpyxl
        wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
        text_parts = []
        for sheet in wb.worksheets:
            rows = []
            for i, row in enumerate(sheet.iter_rows(values_only=True)):
                if i >= 200:   # max 200 rows per sheet
                    break
                row_text = "  |  ".join(str(c) for c in row if c is not None)
                if row_text.strip():
                    rows.append(row_text)
            if rows:
                text_parts.append(f"[Sheet: {sheet.title}]\n" + "\n".join(rows))
        return "\n\n".join(text_parts)
    except Exception as e:
        logger.warning(f"Could not read Excel {path.name}: {e}")
        return ""


def _read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8").strip()
    except Exception as e:
        logger.warning(f"Could not read {path.name}: {e}")
        return ""


def load_knowledge_base() -> str:
    if not KB_DIR.exists():
        return ""

    readers = {
        ".pdf":  _read_pdf,
        ".xlsx": _read_excel,
        ".xls":  _read_excel,
        ".md":   _read_text,
        ".txt":  _read_text,
    }

    chunks = []
    total_chars = 0

    # Priority: core manuals first, training/transfer slides last
    PRIORITY = [
        "faq",                   # FAQ — highest priority
        "sample",                # sample_faq.md
        "service catalog",       # issue resolution guide
        "user manual",           # WePOS user manual
        "web backend",           # web backend guide
        "สร้างร้าน",              # new store setup
        "serial",                # serial number check
        "aftersale",             # after-sales support
        "falcon",                # iMIN Falcon installation
        "swan",                  # iMIN Swan installation
        "product introduction",  # product overview
        "cs transfer",           # training slides — lowest priority
    ]

    def sort_key(p):
        if not p.stat().st_size:  # skip empty files
            return 999
        name = p.name.lower()
        for i, keyword in enumerate(PRIORITY):
            if keyword in name:
                return i
        return len(PRIORITY)

    for path in sorted(KB_DIR.iterdir(), key=sort_key):
        if path.suffix.lower() not in readers:
            continue

        content = readers[path.suffix.lower()](path)
        if not content:
            continue

        # trim per-file limit
        if len(content) > MAX_CHARS_PER_FILE:
            content = content[:MAX_CHARS_PER_FILE] + "\n... [truncated]"

        chunk = f"## [{path.name}]\n{content}"
        chunks.append(chunk)
        total_chars += len(chunk)

        if total_chars >= MAX_TOTAL_CHARS:
            logger.info("Knowledge base total size cap reached — some files omitted")
            break

    logger.info(f"Knowledge base loaded: {len(chunks)} files, ~{total_chars} chars")
    return "\n\n---\n\n".join(chunks)
