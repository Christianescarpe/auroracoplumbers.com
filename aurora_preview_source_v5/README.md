# Aurora Plumbing Guide

Unpublished, noindex preview for homeowners in Aurora, Colorado. It explains plumbing decisions and points at city rules. It is not a plumbing contractor. Calls and forms are off.

The chosen domain name is not registered and is not the canonical host. The preview canonical host is `http://127.0.0.1:43217`.

## Run

```bash
python3 src/build.py
python3 serve.py
```

Open `http://127.0.0.1:43217/`.

```bash
python3 -m unittest tests.test_preview
```

## What is published

This build writes the 111-URL architecture as separate HTML pages, plus a 404. That is the built architecture. It is not a keyword-volume study, and it is not a claim that every page is a deep local investigation. A larger planning envelope of 271 adds unvalidated ideas and is not a build target.

A census place and a ZIP code are not a permit jurisdiction. Byers CDP is in Arapahoe County. Watkins, Strasburg, and the Town of Bennett are listed in both Adams County and Arapahoe County. Franktown, Sedalia, The Pinery, Stonegate, Meridian, and Roxborough Park each keep their own page because a shared county building counter does not make the water district the same.

`reports/build-phases.md` is the page list. `docs/content-depth.md` is the word-count and repetition audit. `docs/source-ledger.md` names the official pages.

Neighboring cities are published only after their permit office or utility was read. Parker’s service-line boundary, and Golden’s and Morrison’s, stay unresolved where the official page did not state one. Lone Tree’s water district is the bill or the district lookup, not Interstate 25 by itself.

The site is not deployed. The `dist/` folder is a static download. Opening it needs the local server above, or any static host you run yourself. There is no public URL.

## Add a city later

Put a sourced record through `src/expansion/validate.py`. A page that only renames Aurora is rejected. Do not cross every service with every city.
