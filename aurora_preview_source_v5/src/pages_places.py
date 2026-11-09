"""City hubs whose permit or utility rules were read for this build.

Lakewood is not here. Its provider list and sewer graphic were not re-read,
so the hub stays gated.
"""

from markup import qas


def centennial(site: dict) -> dict:
    del site
    body = f"""
    <article class="sheet">
      <p class="eyebrow">City of Centennial · not Aurora Water</p>
      <h1>Plumber Centennial CO</h1>
      <p class="lede">Centennial does not run your water or your sewer. The City's own utilities page says so. The building department does review permits, and a residential water heater is not reviewed like a new store. Those two facts change the call you make before a plumber quotes the job.</p>
      <h2>Find the district before you argue about the pipe</h2>
      <p>The City tells residents to use Centennial Property Search to identify the electric and gas provider and the water and sanitation district for the address. Several districts serve the city. A rule you heard about an Aurora tap, or about a Denver main, is not automatically the district on your bill. <a href="https://www.centennialco.gov/Residents/Living-Here/Trash-Utilities" rel="noopener noreferrer">Trash and utilities</a> also notes that much of Centennial's water comes through Denver Water distributors, and it points to Denver Water's lead program. That program is about eligible lines. It is not a reason to buy a private replacement before you check the address.</p>
      <p>Because the district, not the City, owns the utility question, this page will not tell you that you maintain the pipe to a tap. That sentence is Aurora's. Ask the district named on your property record.</p>
      <h2>What the building counter treats as one-stop</h2>
      <p>Centennial's <a href="https://www.centennialco.gov/Government/Departments/Building/Building-Review-Schedule" rel="noopener noreferrer">review schedule</a> lists water heaters, gas lines, and residential sewer line replacements among one-stop permits that need no plan review. It states one business day for that group. New commercial work and new houses are listed at 15 business days after the plan-review fee is paid. Commercial alterations are listed at 10. The page says timelines for first comments start when a complete submittal is in, and it encourages a pre-submittal meeting. The Building Division number printed there is 303-754-3321. Those are the City's targets, not a promise from this website that your heater will be approved tomorrow.</p>
      <p>A one-stop water heater is still not a tankless conversion in another town's worksheet, and it is not a multifamily project. If the job is a new building or a commercial tenant finish, you are on the longer list. For an Aurora address, ignore this schedule and use <a href="/services/water-heater-replacement/">Aurora water heater replacement</a>. For a house that might be Castle Rock, the tankless review is different again: <a href="/areas/castle-rock/">Castle Rock</a>.</p>
      <h2>How that should show up in the quote</h2>
      <p>Ask which district serves the address, and for the sewer or water repair, ask that district who maintains the line before you fund a street cut. Ask whether the building permit is the one-stop residential item or a reviewed commercial set. Ask who pulls it. A <a href="/services/sewer-line-repair/">sewer repair</a> quoted as if Aurora Water owned the main in the street is the wrong city. Camera first, then the district's rule.</p>
      {qas([
        (
            "Does the City of Centennial fix the water or sewer line?",
            "The City says it does not provide water or sewer. Districts do. Use the property search on the City's site to see which district covers the address before you accept a story about who owns the pipe. Aurora's tap rule is for Aurora Water customers. It is not a Centennial ordinance.",
        ),
        (
            "How long does a water heater permit take?",
            "The published schedule puts a residential water heater in the one-stop group and states one business day. That clock is the City's target for a complete submittal, not a guarantee, and it is not the 15-business-day line used for a new house or a new commercial building. Ask the contractor which list this permit is on.",
        ),
        (
            "Is a Centennial mailing address always this city?",
            "No. Confirm the parcel is inside Centennial before you use this schedule. A nearby Aurora or county address has a different counter. The property search and the building department, at 303-754-3321 on the review page, are the City's tools. This website does not look up the parcel for you.",
        ),
      ])}
    </article>
    """
    return _place(
        "/areas/centennial/",
        "Plumber Centennial CO | Aurora Plumbing Guide",
        "Centennial does not supply water or sewer. The City's permit schedule treats a house water heater differently from a commercial job.",
        "Plumber Centennial CO",
        "Centennial",
        "plumber Centennial CO",
        body,
    )


def parker(site: dict) -> dict:
    del site
    body = f"""
    <article class="sheet">
      <p class="eyebrow">Town of Parker · district boundary not settled here</p>
      <h1>Plumber Parker CO</h1>
      <p class="lede">Inside the Town of Parker, the Building Division permits the work. The water and sewer pipes may be a different agency's, and two of that district's published descriptions do not draw the customer's line in the same place. This page will not pick a winner.</p>
      <h2>The town line is not the postal city</h2>
      <p>The Town's <a href="https://parkerco.gov/448/Building-Permits" rel="noopener noreferrer">building permits page</a> says the Building Division handles permits and inspections within incorporated Parker, and that permits are required for practically any work. Applications go through eTRAKiT. The page's phone is 303-841-0353, at 20120 E Mainstreet. That authority stops at the town limit. A Parker mailing address in unincorporated Douglas County is a county permit, which is the situation described for <a href="/areas/highlands-ranch/">Highlands Ranch</a>, not an automatic Town of Parker permit.</p>
      <h2>Do not inherit a sidewalk rule</h2>
      <p>Parker Water and Sanitation District is not the Town, and it does not serve every address that says Parker. A 2025 district rules document has been described as putting the customer's water, sewer, and fire service line, including the public right of way, on the customer. A district FAQ about lead and service lines has been described as stopping ownership at the property line. Those two readings were not reconciled by calling the district, and they are not reconciled here. No contractor should tell you the sidewalk is always the dividing line, and this guide will not say the customer always owns the pipe under the street.</p>
      <p>Ask the district, for the specific tap, which document it will apply. Until you have that answer, a quote for a <a href="/services/water-line-repair/">water line</a> or a <a href="/services/sewer-line-repair/">sewer line</a> should say "boundary to be confirmed" instead of borrowing Aurora's tap rule or Castle Rock's curb stop. <a href="/areas/castle-rock/">Castle Rock</a> publishes a clearer town-water split. Parker does not, on the documents compared for this page.</p>
      <p>An older Town plumbing handout has been indexed with retired code years and with water heaters kept off an over-the-counter list. Those years are not repeated here as the code in force. Use the current Town counter for whether a heater is a simple permit or a review. Aurora's same-day inspection sentence does not apply.</p>
      {qas([
        (
            "Who permits a plumbing job in Parker?",
            "The Town of Parker, if the property is inside the incorporated town. The Building Division says it handles permits there and that practically any work needs one. A Parker ZIP outside the town is not that counter. Check the parcel before you assume eTRAKiT at the Town is the right door.",
        ),
        (
            "Does the homeowner own the sewer line to the main?",
            "Do not take that as a yes or a no from this page. Parker Water and Sanitation District materials indexed for this project describe the customer line differently, one of them including the public right of way and a FAQ stopping at the property line. Ask the district for the address. Aurora's tap-and-saddle rule is a different city.",
        ),
        (
            "Can I use Aurora's water-heater inspection promise?",
            "No, and Aurora does not promise same-day inspection either. Parker has its own building division. An old handout that shuffled water heaters off an over-the-counter path also cited old code years, so it is not quoted here as current. Ask the Town what the heater submittal requires now.",
        ),
      ])}
    </article>
    """
    return _place(
        "/areas/parker/",
        "Plumber Parker CO | Aurora Plumbing Guide",
        "Town of Parker permits incorporated Parker. The water district's service-line boundary is not settled on this page.",
        "Plumber Parker CO",
        "Parker",
        "plumber Parker CO",
        body,
    )


def highlands(site: dict) -> dict:
    del site
    body = f"""
    <article class="sheet">
      <p class="eyebrow">Unincorporated Douglas County · not a city building department</p>
      <h1>Plumber Highlands Ranch CO</h1>
      <p class="lede">Highlands Ranch is not a city with its own building counter. Permits for the unincorporated community go through Douglas County. The water and sewer provider is a separate question, and the County tells owners to verify it before they dig.</p>
      <h2>The permit desk is the County's</h2>
      <p>Douglas County's <a href="https://www.douglas.co.us/building-division/permits/" rel="noopener noreferrer">building permits page</a> says permits are issued for unincorporated areas of the county. Contractors who apply have to be in the County's registration program. The owner or permit holder is responsible for verifying utilities and easements, including water, sewer, well, septic, electric, and gas, before excavation. The Building Division phone on that page is 303-660-7497, at 100 Third Street in Castle Rock. Applications can go to eplans@douglasco.gov. That email is the County's, not an inbox for this website, and there is no link here that sends a message.</p>
      <p>Do not drive the job to Aurora's permit center, and do not assume the Town of Castle Rock's eTRAKiT account covers a Highlands Ranch house. Castle Rock's tankless worksheet is for the Town. It is linked from <a href="/areas/castle-rock/">Castle Rock</a> because the towns are easy to confuse when the County's office sits in Castle Rock's downtown.</p>
      <h2>What this changes on a plumbing quote</h2>
      <p>A <a href="/services/water-heater-replacement/">water heater</a> or a <a href="/services/sewer-line-repair/">sewer repair</a> needs the County permit path, not Aurora's same-day sentence and not Centennial's one-stop list. Ask the contractor to name Douglas County as the building authority when the parcel is unincorporated. Ask which water or sanitation district, or which well, serves the lot. This page does not name a single Highlands Ranch utility, because the County's instruction is to verify the address. A well is possible in Douglas County and is not the default. Do not order well-pump work because the community sounds suburban.</p>
      <p>Dumpsters, the County notes, stay on the property or the driveway, not on a public road. That is a small access fact that belongs in a replacement or a sewer dig, not a landmark tour.</p>
      <h2>What the County lists, and what it does not decide</h2>
      <p>The permit page lists mechanical and plumbing work as its own application type, next to electrical, roofs, and new homes. It does not publish, on that page, a one-stop water-heater exception like Centennial's schedule, and it does not publish Aurora's same-day heater sentence. Treat a Highlands Ranch heater as a County mechanical or plumbing permit until the counter says otherwise. The page also says applications received after 4 p.m. are post-dated to the next business day. That is a scheduling fact, not a service promise. Fees are on a separate County table that this guide does not copy, because fee tables go stale.</p>
      {qas([
        (
            "Is there a Highlands Ranch building department?",
            "Not as a city counter for this community. Douglas County issues building permits in unincorporated areas, and Highlands Ranch is unincorporated. The phone on the County permit page is 303-660-7497. An Aurora or Castle Rock permit assumption is the wrong office until someone shows the parcel is inside one of those cities.",
        ),
        (
            "Who is the water utility?",
            "This page will not name one for every Highlands Ranch address. The County says the owner or permit holder must verify water, sewer, well, and septic locations before digging. Ask for the district or the well record on the quote. Aurora Water's tap rule does not come with the mailing address.",
        ),
        (
            "Why is the County office in Castle Rock?",
            "The Building Division's published address is 100 Third Street, Castle Rock. That is the County's office location. It does not mean the Town of Castle Rock is permitting a Highlands Ranch house. Town tankless reviews and County mechanical permits are different stacks. Match the permit to the parcel.",
        ),
      ])}
    </article>
    """
    return _place(
        "/areas/highlands-ranch/",
        "Plumber Highlands Ranch CO | Aurora Plumbing Guide",
        "Highlands Ranch permits go through unincorporated Douglas County. Confirm the water or sewer district for the lot.",
        "Plumber Highlands Ranch CO",
        "Highlands Ranch",
        "plumber Highlands Ranch CO",
        body,
    )


def castle_rock(site: dict) -> dict:
    del site
    body = f"""
    <article class="sheet">
      <p class="eyebrow">Town of Castle Rock · tankless review is not optional</p>
      <h1>Plumber Castle Rock CO</h1>
      <p class="lede">In Castle Rock a storage-tank water heater and a tankless heater are not the same permit. The Town also describes a water-line split that is not Aurora's sewer tap. Use this page only when the house is inside the Town and on Town water.</p>
      <h2>Tank versus tankless at the counter</h2>
      <p>The Town's <a href="https://www.crgov.com/1893/Residential-Permits" rel="noopener noreferrer">residential permits page</a> says some residential types may not need plan review, and it names a residential water heater in that group, then adds the exception in the same breath: if the heater is tankless, a review is added for gas piping load calculations. A later note is blunt. Tankless water heaters require a plan review. Provide the manufacturer's specification sheet and the gas piping load calculations. The building phone on that page is 720-733-3527. Building codes adopted by the Town took effect June 30, 2026. Do not recycle an older metro code list.</p>
      <p>That is why an <a href="/services/tankless-water-heater-installation/">Aurora tankless page</a> is not enough for a Castle Rock install. The Aurora page can tell you the conversion is a different machine. This page tells you the Town wants the gas-load math in the submittal. A tank replacement that stays a tank may avoid that review. Ask the counter. Do not promise the homeowner a same-day Aurora-style inspection. Aurora's sentence does not apply, and even Aurora does not guarantee the day.</p>
      <h2>Water lines, if Castle Rock Water serves the house</h2>
      <p>The Town's meter FAQ says the Town owns and maintains water service lines to the connection at the property line. The meter pit or curb stop is the Town's, even if the meter sits on the property. Lines from that valve into the home, and the lines in the home, including sewer, are described as the owner's. The FAQ cites Municipal Code 13.12.050. It also says not to close the street valve. For a curb shutoff, the published number is 720-733-6000. Those numbers are the Town's. They are not links on this site.</p>
      <p>Read that sewer clause narrowly. It is attached to a water-meter answer. It is not a full map of who repairs a sewer lateral under a Town street. Ask the Town before you open the road. It is still a different picture from <a href="/guides/aurora-sewer-line-responsibility/">Aurora</a>, where the owner keeps the service line through the tap. <a href="/areas/parker/">Parker</a> is unresolved on purpose. Do not mix the three in one quote.</p>
      {qas([
        (
            "Does a tankless heater in Castle Rock need plan review?",
            "Yes, according to the Town's residential permit page. Submit the manufacturer's specification sheet and gas piping load calculations. A storage-tank water heater is listed among types that may not require plan review, with tankless called out as the exception. Confirm the current application. Do not use an Aurora checklist in place of that sheet.",
        ),
        (
            "Who owns the water line?",
            "For Castle Rock Water, the Town's FAQ says the Town maintains the service to the property-line connection and owns the curb stop or meter pit. Piping from that valve into the house is the owner's. Do not operate the street valve. Call 720-733-6000 if you need the Town to shut the curb. Confirm the house is on Town water first.",
        ),
        (
            "Does the Town also own the sewer in the street?",
            "Do not treat the meter FAQ as a complete sewer map. It says lines in the home, including sewer, are the owner's, in the same answer as the water valve. It does not walk the lateral to the main. Ask the Town before a street cut. Aurora's tap rule and Parker's unsettled boundary are other cities' questions.",
        ),
      ])}
    </article>
    """
    return _place(
        "/areas/castle-rock/",
        "Plumber Castle Rock CO | Aurora Plumbing Guide",
        "Castle Rock requires tankless plan review and gas-load calculations. Town water service runs to the property-line connection.",
        "Plumber Castle Rock CO",
        "Castle Rock",
        "plumber Castle Rock CO",
        body,
    )


def _place(path, title, description, h1, crumb, keyword, body) -> dict:
    return {
        "path": path,
        "title": title,
        "description": description,
        "h1": h1,
        "breadcrumb": crumb,
        "intended_keyword": keyword,
        "keyword_status": "Place hub. Straight-line screen only. No search-volume study.",
        "kind": "place",
        "body": body,
    }
