"""Assemble the published Aurora preview."""

from pages_guides_cities import CITIES, GUIDES, SX
from pages_hubs_rest import HUB_FUNCS
from pages_places import castle_rock, centennial, highlands, parker
from pages_sewer import camera, drains, jetting, responsibility, second_opinion, sewer_repair
from pages_site import (
    about,
    areas_index,
    checklist,
    contact,
    guides_index,
    home,
    how,
    missing,
    permit_guide,
    privacy,
    services_index,
    terms,
)
from pages_water import leak, repair, replacement, tankless_install, tankless_repair, water_line
from pages_wave import ALL
from pages_wave2 import ALL2_A
from pages_wave3 import WAVE3_SERVICES


def pages(site: dict) -> list[dict]:
    built = [
        home(site),
        services_index(site),
        replacement(site),
        repair(site),
        tankless_install(site),
        tankless_repair(site),
        sewer_repair(site),
        camera(site),
        drains(site),
        jetting(site),
        leak(site),
        water_line(site),
    ]
    built.extend(fn(site) for fn in ALL)
    built.extend(fn(site) for fn in ALL2_A)
    built.extend(fn(site) for fn in WAVE3_SERVICES)
    built.extend(
        [
            permit_guide(site),
            responsibility(site),
            second_opinion(site),
            checklist(site),
        ]
    )
    built.extend(fn(site) for fn in GUIDES)
    built.append(areas_index(site))
    built.extend(
        [
            centennial(site),
            parker(site),
            highlands(site),
            castle_rock(site),
        ]
    )
    built.extend(fn(site) for fn in CITIES)
    built.extend(fn(site) for fn in HUB_FUNCS)
    built.extend(fn(site) for fn in SX)
    built.extend(
        [
            guides_index(site),
            about(site),
            how(site),
            contact(site),
            privacy(site),
            terms(site),
            missing(site),
        ]
    )
    return built
