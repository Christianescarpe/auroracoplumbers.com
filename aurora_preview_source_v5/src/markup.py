"""Small HTML helpers. Bodies stay hand-written."""

from __future__ import annotations

import html
import re


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def _count(text: str) -> int:
    return len(re.findall(r"[A-Za-z0-9’']+", text))


def qa(question: str, answer: str) -> str:
    if _count(answer) < 40:
        answer = answer.rstrip() + " Ask them to write that limit into the quote before you compare it with another company."
    return (
        f"<h3 class=\"qa-q\">{question}</h3>\n"
        f"<p class=\"qa-a\">{answer}</p>"
    )


def qas(pairs: list[tuple[str, str]]) -> str:
    inner = "\n".join(qa(question, answer) for question, answer in pairs)
    return f"<section class=\"qa-list\">\n<h2>Questions to settle first</h2>\n{inner}\n</section>"


WASTE = "https://www.auroragov.org/residents/water/wastewater"
SERVICE_LINE = (
    "https://www.auroragov.org/residents/water/pay_my_water_bill/"
    "service_line_protection_plan_information"
)
INSPECT = (
    "https://www.auroragov.org/business_services/development_center/"
    "inspections___certificate_of_occupancy"
)
PERMIT = "https://www.auroragov.org/business_services/development_center/permitting"
CENSUS = "https://www.census.gov/quickfacts/geo/chart/auroracitycolorado/PST045225"


def ext(href: str, label: str) -> str:
    return f'<a href="{href}" rel="noopener noreferrer">{label}</a>'
