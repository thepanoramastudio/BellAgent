"""
Convert all Excel files in knowledge_base/ to Markdown tables.
Service Catalog is slimmed to essential columns only.
Run: python tools/excel_to_md.py
"""

from pathlib import Path
from typing import Optional, List
import openpyxl

KB_DIR = Path(__file__).parent.parent / "knowledge_base"

# For files matching these keywords, keep only specified column indexes
SLIM_RULES = {
    "service catalog": [0, 1, 2, 3, 4],  # Category, Sub-Category, Issue, Description, 1st Action
}


def get_slim_cols(filename: str) -> Optional[List[int]]:
    name = filename.lower()
    for keyword, cols in SLIM_RULES.items():
        if keyword in name:
            return cols
    return None


def sheet_to_markdown(sheet, keep_cols: Optional[List[int]] = None) -> str:
    rows = []
    for row in sheet.iter_rows(values_only=True):
        if all(v is None for v in row):
            continue
        if keep_cols is not None:
            row = tuple(row[i] if i < len(row) else None for i in keep_cols)
        rows.append(row)

    if not rows:
        return ""

    def cell(v) -> str:
        if v is None:
            return ""
        # clean up newlines inside cells for markdown table compatibility
        return str(v).replace("\n", " ").replace("|", "/").strip()

    lines = []
    header = rows[0]
    lines.append("| " + " | ".join(cell(c) for c in header) + " |")
    lines.append("| " + " | ".join("---" for _ in header) + " |")
    for row in rows[1:]:
        # skip rows where all kept cells are empty
        if all(v is None or str(v).strip() == "" for v in row):
            continue
        lines.append("| " + " | ".join(cell(c) for c in row) + " |")

    return "\n".join(lines)


def excel_to_md(xlsx_path: Path) -> Path:
    keep_cols = get_slim_cols(xlsx_path.name)
    wb = openpyxl.load_workbook(xlsx_path, read_only=True, data_only=True)
    sections = []

    for sheet in wb.worksheets:
        md = sheet_to_markdown(sheet, keep_cols)
        if md:
            sections.append(f"## {sheet.title}\n\n{md}")

    if not sections:
        print(f"  ⚠️  No data found in {xlsx_path.name}")
        return None

    out_path = xlsx_path.with_suffix(".md")
    out_path.write_text("\n\n---\n\n".join(sections), encoding="utf-8")
    return out_path


def main():
    xlsx_files = list(KB_DIR.glob("**/*.xlsx")) + list(KB_DIR.glob("**/*.xls"))

    if not xlsx_files:
        print("No Excel files found in knowledge_base/")
        return

    print(f"Found {len(xlsx_files)} Excel file(s)\n")

    for xlsx in xlsx_files:
        print(f"Converting: {xlsx.name}")
        out = excel_to_md(xlsx)
        if out:
            size = len(out.read_text(encoding="utf-8"))
            print(f"  ✅  Saved: {out.name} ({size:,} chars)\n")

    print("Done!")


if __name__ == "__main__":
    main()
