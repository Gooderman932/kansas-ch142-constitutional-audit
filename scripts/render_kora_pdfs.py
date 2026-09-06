#!/usr/bin/env python3
"""Render the seven final-review KORA Markdown drafts as print-ready PDFs."""

from __future__ import annotations

import html
import re
from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import KeepTogether, Paragraph, SimpleDocTemplate, Spacer
from pypdf import PdfWriter


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "KORA-requests"
OUTPUT_DIR = ROOT / "exports" / "kora-pdfs"

FILES = {
    "KORA-01-attorney-general.md": (
        "KORA-01-Kansas-Attorney-General.pdf",
        "Kansas Attorney General",
        [
            (
                "Kansas Attorney General Open Government",
                "https://www.ag.ks.gov/divisions/administration/open-government",
            )
        ],
    ),
    "KORA-04-olathe-incident.md": (
        "KORA-04-Olathe-July-11-Incident.pdf",
        "Olathe Police Department",
        [
            (
                "Olathe Police Records",
                "https://www.olatheks.gov/government/police/records",
            ),
            (
                "Olathe public-records portal",
                "https://olatheks-self.govplatform.com/service/Public_Records_Request",
            ),
        ],
    ),
    "ready-20260903-cherokee-county.md": (
        "KORA-02-Cherokee-County.pdf",
        "Cherokee County",
        [
            (
                "Cherokee County Sheriff administration",
                "https://www.cherokeecountykssheriff.com/administration",
            ),
            (
                "Cherokee County KORA form",
                "https://cherokeecountyks.gov/main/images/KORA_-_Clerks_Request_Form.pdf",
            ),
        ],
    ),
    "ready-20260903-johnson-county.md": (
        "KORA-02-Johnson-County.pdf",
        "Johnson County",
        [
            (
                "Johnson County Sheriff's Records",
                "https://www.jocogov.org/johnson-county-sheriff/public-information/sheriffs-records",
            )
        ],
    ),
    "ready-20260903-sedgwick-county.md": (
        "KORA-02-Sedgwick-County.pdf",
        "Sedgwick County",
        [
            (
                "Sedgwick County open-records requests",
                "https://www.sedgwickcounty.org/kora/request-sedgwick-county-government-records/open-records-request/",
            )
        ],
    ),
    "ready-20260903-shawnee-county.md": (
        "KORA-02-Shawnee-County.pdf",
        "Shawnee County",
        [
            (
                "Shawnee County Sheriff records requests",
                "https://www.shawneesheriff.org/sh/request_for_records.php",
            ),
            (
                "Shawnee County Clerk KORA",
                "https://www.snco.gov/clerk/kora.php",
            ),
        ],
    ),
    "ready-20260903-wyandotte-county.md": (
        "KORA-02-Wyandotte-County.pdf",
        "Wyandotte County",
        [
            (
                "Wyandotte County Sheriff's Office",
                "https://www.wycokck.org/Departments/Sheriffs-Office",
            ),
            (
                "Unified Government records portal",
                "https://wycokck.nextrequest.com/",
            ),
        ],
    ),
}

KORA_SOURCES = [
    ("Kansas Open Records Act", "https://ksrevisor.gov/statutes/ksa_ch45.html"),
    (
        "K.S.A. 45-218",
        "https://www.ksrevisor.gov/statutes/chapters/ch45/045_002_0018.html",
    ),
    (
        "K.S.A. 45-221",
        "https://www.ksrevisor.gov/statutes/chapters/ch45/045_002_0021.html",
    ),
]


def register_fonts() -> None:
    pdfmetrics.registerFont(
        TTFont("NotoSans", "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf")
    )
    pdfmetrics.registerFont(
        TTFont("NotoSans-Bold", "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf")
    )


def inline_markup(text: str) -> str:
    value = html.escape(text, quote=False)
    value = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", value)
    value = re.sub(r"`(.+?)`", r'<font name="NotoSans">\1</font>', value)
    value = re.sub(
        r"\[([^\]]+)\]\((https?://[^)]+)\)",
        r'<a href="\2" color="#01696F">\1</a>',
        value,
    )
    value = value.replace(
        "K.S.A. 45-215 et seq.", "K.S.A. 45-215 et seq.<super>1</super>"
    )
    value = value.replace("K.S.A. 45-218(d)", "K.S.A. 45-218(d)<super>2</super>")
    value = value.replace(
        "K.S.A. 45-221(a)(10)", "K.S.A. 45-221(a)(10)<super>3</super>"
    )
    return value


def parse_markdown(path: Path, styles: dict[str, ParagraphStyle]):
    lines = path.read_text(encoding="utf-8").splitlines()
    story = []
    paragraph: list[str] = []

    def flush() -> None:
        if paragraph:
            story.append(Paragraph(inline_markup(" ".join(paragraph)), styles["body"]))
            paragraph.clear()

    for raw in lines:
        line = raw.strip()
        if not line:
            flush()
            continue
        if line == "---":
            flush()
            story.append(Spacer(1, 5))
            continue
        if line.startswith("# "):
            flush()
            story.append(Paragraph(inline_markup(line[2:]), styles["title"]))
            continue
        if line.startswith("## "):
            flush()
            story.append(Paragraph(inline_markup(line[3:]), styles["h2"]))
            continue
        if line.startswith("### "):
            flush()
            story.append(Paragraph(inline_markup(line[4:]), styles["h3"]))
            continue
        match = re.match(r"^(\d+)\.\s+(.*)", line)
        if match:
            flush()
            story.append(
                Paragraph(
                    f"<b>{match.group(1)}.</b> {inline_markup(match.group(2))}",
                    styles["list"],
                )
            )
            continue
        if line.startswith("- "):
            flush()
            story.append(
                Paragraph(f"• {inline_markup(line[2:])}", styles["list"])
            )
            continue
        if line.startswith("**Delivery"):
            flush()
            story.append(
                Paragraph(f"{inline_markup(line)}<super>4</super>", styles["meta"])
            )
            continue
        if line.startswith("**") and line.endswith("**"):
            flush()
            story.append(Paragraph(inline_markup(line), styles["meta"]))
            continue
        if line.startswith("**"):
            flush()
            story.append(Paragraph(inline_markup(line), styles["meta"]))
            continue
        paragraph.append(line)

    flush()
    return story


def footer_callback(route_sources):
    sources = KORA_SOURCES + route_sources

    def draw(canvas, doc):
        canvas.saveState()
        width, _ = LETTER
        canvas.setStrokeColor(HexColor("#D4D1CA"))
        canvas.setLineWidth(0.5)
        canvas.line(doc.leftMargin, 62, width - doc.rightMargin, 62)

        links = []
        for index, (label, url) in enumerate(sources, 1):
            links.append(
                f'{index}. <a href="{html.escape(url, quote=True)}" '
                f'color="#01696F">{html.escape(label)}</a>'
            )
        source_text = "Sources: " + " | ".join(links)
        source_style = ParagraphStyle(
            "FooterSources",
            fontName="NotoSans",
            fontSize=6.8,
            leading=8.5,
            textColor=HexColor("#5C5A55"),
        )
        footer = Paragraph(source_text, source_style)
        _, footer_height = footer.wrap(width - doc.leftMargin - doc.rightMargin, 38)
        footer.drawOn(canvas, doc.leftMargin, 54 - footer_height)

        canvas.setFont("NotoSans", 7)
        canvas.setFillColor(HexColor("#7A7974"))
        canvas.drawString(doc.leftMargin, 20, "FINAL DRAFT • NOT SENT")
        canvas.drawRightString(width - doc.rightMargin, 20, f"Page {doc.page}")
        canvas.restoreState()

    return draw


def build_pdf(source_name: str, output_name: str, target: str, route_sources) -> None:
    output_path = OUTPUT_DIR / output_name
    styles = {
        "title": ParagraphStyle(
            "Title",
            fontName="NotoSans-Bold",
            fontSize=17,
            leading=21,
            textColor=HexColor("#28251D"),
            spaceAfter=12,
        ),
        "h2": ParagraphStyle(
            "Heading2",
            fontName="NotoSans-Bold",
            fontSize=11.5,
            leading=14,
            textColor=HexColor("#01696F"),
            spaceBefore=9,
            spaceAfter=5,
            keepWithNext=True,
        ),
        "h3": ParagraphStyle(
            "Heading3",
            fontName="NotoSans-Bold",
            fontSize=10,
            leading=13,
            textColor=HexColor("#28251D"),
            spaceBefore=7,
            spaceAfter=4,
            keepWithNext=True,
        ),
        "body": ParagraphStyle(
            "Body",
            fontName="NotoSans",
            fontSize=9.5,
            leading=13.5,
            textColor=HexColor("#28251D"),
            spaceAfter=7,
        ),
        "meta": ParagraphStyle(
            "Meta",
            fontName="NotoSans",
            fontSize=8.7,
            leading=12,
            textColor=HexColor("#4E4C47"),
            spaceAfter=3,
        ),
        "list": ParagraphStyle(
            "List",
            fontName="NotoSans",
            fontSize=9.5,
            leading=13.5,
            leftIndent=18,
            firstLineIndent=-18,
            spaceAfter=6,
        ),
    }

    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=LETTER,
        leftMargin=0.72 * inch,
        rightMargin=0.72 * inch,
        topMargin=0.68 * inch,
        bottomMargin=0.95 * inch,
        title=f"Kansas Open Records Request — {target}",
        author="Perplexity Computer",
        subject="Final draft, not sent",
    )
    story = parse_markdown(SOURCE_DIR / source_name, styles)
    callback = footer_callback(route_sources)
    doc.build(story, onFirstPage=callback, onLaterPages=callback)


def main() -> None:
    register_fonts()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    rendered = []
    for source_name, (output_name, target, route_sources) in FILES.items():
        build_pdf(source_name, output_name, target, route_sources)
        rendered.append(OUTPUT_DIR / output_name)
        print(rendered[-1])

    packet_path = OUTPUT_DIR / "KORA-Request-Packet-All-Seven.pdf"
    writer = PdfWriter()
    for pdf_path in rendered:
        writer.append(str(pdf_path))
    writer.add_metadata(
        {
            "/Title": "Kansas Open Records Request Packet — Seven Final Drafts",
            "/Author": "Perplexity Computer",
            "/Subject": "Final drafts, not sent",
        }
    )
    with packet_path.open("wb") as packet:
        writer.write(packet)
    print(packet_path)


if __name__ == "__main__":
    main()
