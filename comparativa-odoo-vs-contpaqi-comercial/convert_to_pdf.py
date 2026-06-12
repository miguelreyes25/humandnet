#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Convierte report.md a report.pdf con formato profesional (markdown -> HTML -> PDF)."""
import os
import markdown
from xhtml2pdf import pisa

BASE = os.path.dirname(os.path.abspath(__file__))
MD_PATH = os.path.join(BASE, "report.md")
PDF_PATH = os.path.join(BASE, "report.pdf")

with open(MD_PATH, encoding="utf-8") as f:
    md_text = f.read()

html_body = markdown.markdown(
    md_text,
    extensions=["tables", "toc", "sane_lists"],
)

CSS = """
@page { size: a4 portrait; margin: 1.4cm 1.2cm; @frame footer { -pdf-frame-content: footerContent; bottom: 0.7cm; margin-left: 1.2cm; margin-right: 1.2cm; height: 1cm; } }
body { font-family: Helvetica, Arial, sans-serif; font-size: 9pt; color: #1a1a1a; line-height: 1.4; }
h1 { font-size: 19pt; color: #0B5394; border-bottom: 3px solid #0B5394; padding-bottom: 5px; margin-bottom: 10px; }
h2 { font-size: 13pt; color: #0B5394; border-bottom: 1px solid #cfd8e3; padding-bottom: 3px; margin-top: 16px; margin-bottom: 6px; -pdf-keep-with-next: true; }
h3 { font-size: 10.5pt; color: #333333; margin-top: 10px; margin-bottom: 3px; -pdf-keep-with-next: true; }
blockquote { color: #555555; font-style: italic; font-size: 8.5pt; border-left: 3px solid #cfd8e3; padding: 2px 8px; margin: 6px 0; }
p { margin: 4px 0; }
table { width: 100%; border-collapse: collapse; margin: 6px 0; }
th, td { border: 1px solid #b9c2cf; padding: 4px 6px; text-align: left; vertical-align: top; font-size: 8pt; }
th { background-color: #0B5394; color: #ffffff; font-weight: bold; }
ol, ul { margin: 4px 0 4px 14px; }
li { margin: 2px 0; font-size: 9pt; }
a { color: #0B5394; text-decoration: none; }
hr { border: none; border-top: 1px solid #e0e0e0; margin: 10px 0; }
.footer { color: #888888; font-size: 7.5pt; text-align: center; }
"""

html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><style>{CSS}</style></head>
<body>
<div id="footerContent" class="footer">Comparativa ERP — Hum&amp;Net · Confidencial · generado 2026-06-11 · pag. <pdf:pagenumber> de <pdf:pagecount></div>
{html_body}
</body></html>"""

with open(PDF_PATH, "wb") as out:
    result = pisa.CreatePDF(html, dest=out, encoding="utf-8")

if result.err:
    print(f"ERRORES: {result.err}")
else:
    size = os.path.getsize(PDF_PATH)
    print(f"OK -> {PDF_PATH} ({size:,} bytes)")
