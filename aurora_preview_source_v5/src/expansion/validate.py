"""Refuse thin city pages and city-name swaps.

Aurora is the only place published. Adding a suburb means passing these checks
and writing a decision that Aurora's page does not already make.
"""

from __future__ import annotations

import re
from difflib import SequenceMatcher


class ExpansionError(Exception):
    pass


def _words(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


def publishable_location(record: dict) -> None:
    required = (
        "id",
        "place",
        "state",
        "permit_authority",
        "sewer_utility",
        "water_utility",
        "sources",
        "infrastructure",
        "housing_or_corridor",
    )
    missing = [key for key in required if not record.get(key)]
    if missing:
        raise ExpansionError(f"{record.get('id', '?')} missing {', '.join(missing)}")
    if record["state"] != "Colorado":
        raise ExpansionError("This catalog is Colorado only.")
    if len(record["sources"]) < 2:
        raise ExpansionError(f"{record['id']} needs at least two sources.")
    if len(record["infrastructure"]) < 3:
        raise ExpansionError(f"{record['id']} needs at least three infrastructure notes.")
    for note in record["infrastructure"]:
        if not note.get("fact") or not note.get("source"):
            raise ExpansionError(f"{record['id']} has an infrastructure note without a fact and source.")
    if len(record["housing_or_corridor"]["fact"].split()) < 12:
        raise ExpansionError(f"{record['id']} housing or corridor note is too thin.")
    if not record["housing_or_corridor"].get("source"):
        raise ExpansionError(f"{record['id']} housing note needs a source.")


def publishable_overlay(overlay: dict, aurora_page_text: str) -> None:
    """A suburb service page must change the decision, not rename Aurora."""
    delta = overlay.get("decision_delta", "").strip()
    if len(_words(delta)) < 80:
        raise ExpansionError(
            f"{overlay.get('id', '?')} decision note is under 80 words."
        )
    required_fact = overlay.get("local_fact", "").strip().lower()
    if len(required_fact.split()) < 8:
        raise ExpansionError("Overlay needs its own local fact.")
    if required_fact and required_fact in aurora_page_text.lower():
        raise ExpansionError("Overlay fact is already the Aurora page.")
    swapped = overlay.get("body", "")
    place = overlay.get("place", "")
    if swapped and place:
        normalized = re.sub(re.escape(place), "Aurora", swapped, flags=re.I)
        ratio = SequenceMatcher(None, normalized, aurora_page_text).ratio()
        if ratio > 0.82:
            raise ExpansionError(
                f"{overlay.get('id')} is an Aurora page with the city name swapped ({ratio:.2f})."
            )


AURORA = {
    "id": "aurora-co",
    "place": "Aurora",
    "state": "Colorado",
    "permit_authority": "City of Aurora Building Division and Development Center",
    "sewer_utility": "Aurora Water, for city sewer mains; the property owner maintains the service line to the tap",
    "water_utility": "Aurora Water; the owner maintains the water service line from the building to the city main",
    "sources": [
        "https://www.auroragov.org/residents/water/wastewater",
        "https://www.auroragov.org/residents/water/pay_my_water_bill/service_line_protection_plan_information",
        "https://www.auroragov.org/business_services/development_center/inspections___certificate_of_occupancy",
    ],
    "infrastructure": [
        {
            "fact": "Aurora Water maintains more than 1,200 miles of sanitary sewer and only the city mains and manholes in streets, alleys, and easements.",
            "source": "https://www.auroragov.org/residents/water/wastewater",
        },
        {
            "fact": "Sewage and stormwater are separate systems.",
            "source": "https://www.auroragov.org/residents/water/wastewater",
        },
        {
            "fact": "The owner maintains the sewer service line from the tap to the building, including the tee or saddle and related street or property repair.",
            "source": "https://www.auroragov.org/residents/water/wastewater",
        },
    ],
    "housing_or_corridor": {
        "fact": "The City says homes built before 1985 can have clay sewer laterals and homes built after 1985 generally have PVC, while water service lines are generally copper. The actual pipe still has to be inspected.",
        "source": "https://www.auroragov.org/residents/water/pay_my_water_bill/service_line_protection_plan_information",
    },
}


def assert_catalog() -> None:
    publishable_location(AURORA)
    # The published site has no suburb overlays. The checks exist so a later
    # city cannot be added by renaming this record.
    if AURORA["place"] != "Aurora":
        raise ExpansionError("Published catalog place changed without a new sourced record.")
