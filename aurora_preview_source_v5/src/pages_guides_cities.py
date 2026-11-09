"""Guides and city hubs added from sources read for this build."""

from markup import qas
from pages_wave import _page


def g_tankless(site):
    del site
    body = """
    <article class="sheet">
      <p class="eyebrow">What the quote has to show</p>
      <h1>Tankless conversion quote checklist</h1>
      <p class="lede">A tankless quote is complete only when it names the gas or electrical supply, the vent, the condensate, and the permit path. A price with none of those is a guess.</p>
      <p>Ask for the model and the manufacturer's sizing page for your fixtures. Ask whether the existing flue can be reused. Most cannot. Ask where condensate drains. Ask who pulls the permit. In Aurora, same-day inspection is a request for replacement heaters, not a guarantee, and a conversion may not be that request. In Castle Rock the Town requires plan review, the specification sheet, and gas piping load calculations. That packet is <a href="/areas/castle-rock/tankless-water-heater-installation/">the Castle Rock tankless page</a>. Do not send an Aurora-only quote to that counter.</p>
      <p>This list does not size the pipe and does not promise savings. No hardness number and no altitude percentage are printed here. The hiring page is <a href="/services/tankless-water-heater-installation/">tankless installation</a>.</p>
      """ + qas([
        ("What has to be on the quote?", "The model, the vent type, the gas or electrical change, the condensate drain, who pulls the permit, and what is excluded. Without those, two prices are not the same job. This page still will not print a dollar figure."),
        ("Does Aurora guarantee the inspection day?", "No. The City may inspect a replacement heater the same day when a licensed contractor and the homeowner are both there, and it may come another day. A tankless conversion can be a different review. Ask which path this submittal is."),
        ("What does Castle Rock add?", "Plan review, the manufacturer's specification sheet, and gas piping load calculations. A storage-tank heater there may skip that review. A tankless unit may not. Use the Castle Rock page if the house is in the Town."),
      ]) + "</article>"
    return _page("/guides/tankless-conversion-quote-checklist/", "Tankless quote checklist | Aurora Plumbing Guide", "Gas, vent, condensate, and permit items a tankless quote should name, including Castle Rock's extra review.", "Tankless conversion quote checklist", "Tankless quotes", "tankless conversion quote", "guide", body)


def g_drain(site):
    del site
    body = """
    <article class="sheet">
      <p class="eyebrow">Clog or broken pipe</p>
      <h1>Drain cleaning versus sewer repair</h1>
      <p class="lede">Cleaning removes a blockage. Repair replaces or patches a pipe that is broken. In Aurora the expensive version of the second job includes the service line to the tap and the street if you open it.</p>
      <p>One slow fixture, with the rest of the house fine, is usually <a href="/services/drain-cleaning/">drain cleaning</a>. Several fixtures, or sewage at the lowest drain, may be the building drain or the lateral. Then you want a <a href="/services/sewer-camera-inspection/">camera</a> before <a href="/services/sewer-line-repair/">sewer repair</a>. Aurora Water keeps the main. You keep the line from the tap to the building. A second cleaning the same week, without a video, often misses a crack or a belly.</p>
      <p>Jetting is still cleaning. It is not a patch. See <a href="/services/hydro-jetting/">hydro-jetting</a>.</p>
      """ + qas([
        ("The clog came back in two days. Now what?", "Stop repeating the same cable. Ask for a camera from a cleanout toward the tap. If the pipe is open and round, another cleaning or a jet may be enough. If it is cracked or offset, you are in repair, and in Aurora that repair can include the tap and the street."),
        ("Who pays if the main is clear and my floor drain is not?", "You do, if the defect is on your service line. Aurora Water's page says the owner maintains that line from the tap to the building. Ask them to confirm the main was checked. Do not pay for their main, and do not expect them to pay for yours."),
        ("Is jetting a repair?", "No. It washes the pipe. A broken joint is still broken when the hose comes out. Camera first on older pipe. Aurora says pre-1985 homes can have clay, which is a reason to look, not a reason to blast."),
      ]) + "</article>"
    return _page("/guides/drain-cleaning-vs-sewer-repair/", "Drain cleaning versus sewer repair | Aurora Plumbing Guide", "When an Aurora clog is still a cleaning and when the service line to the tap is the real job.", "Drain cleaning versus sewer repair", "Cleaning or repair", "drain cleaning versus sewer repair", "guide", body)


def g_trench(site):
    del site
    body = """
    <article class="sheet">
      <p class="eyebrow">Open the ground or not</p>
      <h1>Trenchless versus open-cut sewer repair</h1>
      <p class="lede">Open cut digs up the line. Trenchless tries to line or replace it with less trench. Neither is automatically cheaper, and neither is automatically allowed by the condition of the pipe.</p>
      <p>Start with the <a href="/services/sewer-camera-inspection/">video</a>. A liner needs a host pipe. A collapse may force a dig. Pits at each end are still digging. In Aurora, if those pits or the tap are in the street, the owner's duty on the wastewater page includes the street repair. Say that in the quote. The method page is <a href="/services/trenchless-sewer-repair/">trenchless repair</a>. The ownership page is <a href="/guides/aurora-sewer-line-responsibility/">who owns the line</a>.</p>
      <p>No city program pays for the method. No success rate is printed here.</p>
      """ + qas([
        ("Which one should I buy?", "The one the video supports. If the pipe is round enough to line, ask for pit locations and restoration. If it is collapsed, ask for the open repair and the same restoration. Two prices that hide the street patch are not comparable."),
        ("Does trenchless mean the city does the work?", "No. Aurora's free offer is a review of your video, not a lining crew. You still maintain the service line to the tap. The method is a contractor's tool."),
        ("Are pits a trench?", "They are holes. Ask how many, how wide, and who fills them, including asphalt. A no-dig slogan that still needs two pits in the parking strip is an open-cut job at the ends."),
      ]) + "</article>"
    return _page("/guides/trenchless-vs-open-cut/", "Trenchless versus open cut | Aurora Plumbing Guide", "How to compare a liner and an open sewer repair in Aurora, including pits and street restoration.", "Trenchless versus open-cut sewer repair", "Trench or liner", "trenchless versus open cut", "guide", body)


def g_supply(site):
    del site
    body = """
    <article class="sheet">
      <p class="eyebrow">Two pipes in the yard</p>
      <h1>Water line versus sewer line</h1>
      <p class="lede">The water service brings drinking water in under pressure. The sewer lateral takes wastewater out. A camera works in the second. It does not work in the first. Aurora assigns them differently, and other cities assign them differently again.</p>
      <p>On Aurora Water, you maintain the water service to the city main, and you maintain the sewer from the building through the tap, including the tee or saddle and related street repair. The city keeps the sewer main and the manholes. Water lines are generally copper and cannot be videotaped. Read <a href="/services/water-line-repair/">water line repair</a> and <a href="/services/sewer-line-repair/">sewer line repair</a> before you let one dig find both by accident. Call 811.</p>
      <p>Castle Rock Water says the Town maintains water service to the property-line connection and owns the curb stop. Littleton's code says the owner maintains the sewer from the public sewer to the building, including the tap, while Denver Water supplies the drinking water. Parker is unresolved on purpose. Do not export one sentence to every town. The map of who decided what is <a href="/guides/city-county-utility-jurisdiction/">which office controls the address</a>.</p>
      """ + qas([
        ("Can one camera inspect both?", "No. Aurora says water service lines cannot be videotaped. The sewer can. A company that offers a camera for a hissing water leak is using the wrong tool. Locate the water line another way before you cut."),
        ("Who pays for the street in Aurora?", "If the cut is your water service or your sewer tap, the city's pages put that restoration on the owner. The city repairs the street when the work is its main. Ask which pipe and whose main before you accept the patch."),
        ("Does Castle Rock match Aurora?", "Not on the water line. Castle Rock's FAQ says the Town keeps water service to the property-line connection and the curb stop. Aurora's owner keeps the water service to the main. Confirm you are on that town's water before you use the FAQ."),
      ]) + "</article>"
    return _page("/guides/water-line-vs-sewer-line/", "Water line versus sewer line | Aurora Plumbing Guide", "How Aurora, and a few neighboring utilities, split the drinking-water service from the sewer lateral.", "Water line versus sewer line", "Water or sewer", "water line versus sewer line", "guide", body)


def g_juris(site):
    del site
    body = """
    <article class="sheet">
      <p class="eyebrow">The parcel, not the mailing city</p>
      <h1>Which city, county, or district controls the job</h1>
      <p class="lede">The mailing address is not the permit counter, and it is not the sewer utility. These are the offices actually read for this guide. If your town is not on the list, its rules are not copied from Aurora.</p>
      <ul class="link-list">
        <li><a href="/">Aurora</a> permits through the city. Aurora Water: you keep the sewer to the tap and the water service to the main.</li>
        <li><a href="/areas/centennial/">Centennial</a> does not sell water or sewer. Districts do. The city reviews building permits.</li>
        <li><a href="/areas/parker/">Parker</a> permits inside the town. The sanitation district's boundary is not settled here.</li>
        <li><a href="/areas/highlands-ranch/">Highlands Ranch</a> is unincorporated Douglas County.</li>
        <li><a href="/areas/castle-rock/">Castle Rock</a> has its own permits and Town water rules.</li>
        <li><a href="/areas/lakewood/">Lakewood</a> has many districts. The city sewer graphic is the north side utility.</li>
        <li><a href="/areas/arvada/">Arvada</a> says you maintain the service line on your property. It does not give a right-of-way rule.</li>
        <li><a href="/areas/englewood/">Englewood</a> permits water heaters and water-line changes. A proposed ownership rewrite was not treated as current law.</li>
        <li><a href="/areas/littleton/">Littleton</a> sewer code includes the tap. Denver Water supplies drinking water.</li>
        <li><a href="/areas/westminster/">Westminster</a> says you keep the lateral to the city's main, including under a driveway.</li>
      </ul>
      <p>A Census point within 50 straight-line miles is not a service area and not a utility. Towns missing from this list were not given Aurora's sentences.</p>
      """ + qas([
        ("My mail says Aurora. Am I in the city?", "Not always. Confirm the parcel. Centennial, county land, and Aurora can share a postal name. The permit counter and the sewer bill are the proof. Using Aurora's tap rule on the wrong parcel bills the wrong party."),
        ("Who do I call for a sewer backup?", "The utility on the sewer bill, and a plumber. Aurora Water's published backup number is 303-326-8645 for its system. Westminster collections is 303-658-2500 for its mains. Lakewood's city crew is only for the city's own north-side customers. Match the number to the bill."),
        ("Why isn't every suburb listed?", "A place name is not a permit office. The cities on this page are ones where a city, a county, or a utility has published a rule that changes the job. A name on a map, by itself, does not tell you who permits the house."),
      ]) + "</article>"
    return _page("/guides/city-county-utility-jurisdiction/", "Which office controls the plumbing job | Aurora Plumbing Guide", "Permit counters and utilities that were actually read, and why a mailing city is not enough.", "Which office controls the plumbing job", "Jurisdiction", "plumbing permit jurisdiction", "guide", body)


def g_cent(site):
    del site
    body = """
    <article class="sheet">
      <p class="eyebrow">Centennial's own schedule</p>
      <h1>Centennial heater permits versus a remodel</h1>
      <p class="lede">In Centennial a house water heater is on the one-stop list. An addition, a basement finish, and commercial work are not. The city still does not supply your water.</p>
      <p>The building review schedule says one-stop permits need no plan review and states one business day for water heaters, gas lines, and residential sewer replacements, among other items. New houses and new commercial buildings are listed at 15 business days after the fee is paid. Residential additions are 10. Basement finishes are five. Those clocks start on a complete submittal. They are not a promise from this website. The hiring page for a house tank is <a href="/areas/centennial/water-heater-replacement/">Centennial water heater replacement</a>. The city hub is <a href="/areas/centennial/">Centennial</a>.</p>
      <p>Districts, not the city, provide water and sewer. Responsibility varies by utility. Confirm the district before you authorize work.</p>
      """ + qas([
        ("Is a water heater one business day?", "That is what the city's schedule says for the one-stop list, after a complete submittal. It is a target, not a guarantee, and it is not the 15-day line for a new house. Ask which list the application is on."),
        ("Does the same clock cover a basement bath?", "No. A basement finish is on the five-business-day residential line in that schedule, and an addition is on the 10-day line. A water heater does not pull the bathroom onto the one-stop list."),
        ("Who owns the water line?", "Not the City of Centennial. The city says it does not provide water or sewer. Use the property search to find the district. Aurora's owner-to-the-main sentence is the wrong city."),
      ]) + "</article>"
    return _page("/guides/centennial-heater-vs-remodel-permit/", "Centennial heater versus remodel permits | Aurora Plumbing Guide", "Centennial's one-stop water heater list versus additions, basements, and commercial review.", "Centennial heater permits versus a remodel", "Centennial permits", "Centennial water heater permit", "guide", body)


def g_cr(site):
    del site
    body = """
    <article class="sheet">
      <p class="eyebrow">Town of Castle Rock</p>
      <h1>Castle Rock tankless permit papers</h1>
      <p class="lede">The Town adds a plan review when the water heater is tankless. You submit the manufacturer's specification sheet and gas piping load calculations. A storage tank may avoid that review. The codes the Town adopted took effect June 30, 2026.</p>
      <p>Read the full contrast on <a href="/areas/castle-rock/tankless-water-heater-installation/">Castle Rock tankless installation</a> and the town hub <a href="/areas/castle-rock/">Castle Rock</a>. Do not use Aurora's same-day sentence. The building phone published on the residential permit page is 720-733-3527. It is the Town's number, not a link here, and it is not this guide's referral line.</p>
      <p>Water-line ownership for Town water customers is a separate FAQ: the Town maintains service to the property-line connection. That is not the tankless packet, and it is not Aurora's sewer tap.</p>
      """ + qas([
        ("What do I hand the Town for a tankless heater?", "The manufacturer's specification sheet and gas piping load calculations, with the plan review the residential permit page describes. A tank heater is listed among types that may not need that review. Confirm the current application. Do not submit an Aurora checklist instead."),
        ("Did the code change?", "The Town says adopted building-code amendments took effect June 30, 2026. Do not rely on an older metro list. Ask the counter if a submittal prepared earlier still matches."),
        ("Is the gas-load sheet the same as a water-line repair?", "No. The sheet is about the heater's fuel demand. The Town's water FAQ is about who owns the service to the curb. A tankless install can involve both only if the quote says the water piping changes too."),
      ]) + "</article>"
    return _page("/guides/castle-rock-tankless-permit/", "Castle Rock tankless permit | Aurora Plumbing Guide", "Manufacturer sheet and gas-load calculations Castle Rock requires for a tankless water heater.", "Castle Rock tankless permit papers", "Castle Rock papers", "Castle Rock tankless permit", "guide", body)


def g_denver(site):
    del site
    body = """
    <article class="sheet">
      <p class="eyebrow">Denver Water customers only</p>
      <h1>Denver Water lead service lines</h1>
      <p class="lede">Denver Water's Lead Reduction Program can replace an eligible lead service line at no direct charge to the customer. It is not a coupon for every house near Denver, and it is not a reason to buy a private replacement before you check the address.</p>
      <p>The program page says an address search shows whether a home is among an estimated 60,000 to 64,000 with a possible lead service line. Replacement areas are planned, with notice often a month or two before work. Outside that schedule, Denver Water says it will also replace a customer-owned lead line with copper, at no direct charge, when it finds one during a water-main project. There is a partial reimbursement path if a customer replaces sooner. Customer care on that page is 303-893-2444. Emergencies are 303-628-6801. Those are Denver Water's numbers, not this guide's, and they are not tap-to-call links here.</p>
      <p>Littleton says Denver Water supplies its potable water. Centennial says much of its water comes through Denver Water distributors and points at the same program. Being near Aurora does not put you on the program. Aurora Water is a different utility. Use the address tool on Denver Water's site before anyone sells you a dig. The ordinary private repair, when the line is not in the program, is <a href="/services/water-line-repair/">water line repair</a>.</p>
      """ + qas([
        ("Will Denver Water replace my line for free?", "Only if the address is in the program or they find a customer-owned lead line during their own main work. The page says there is no direct charge in those cases. Check the address. Do not pay for a private replacement until that answer is no."),
        ("Does this cover Aurora Water customers?", "No. The program is Denver Water's. Aurora Water is a different system. Centennial and Littleton may be Denver Water distributors or customers. The bill and the address search decide. A ZIP code does not."),
        ("Can I replace it myself and get the money back?", "The page says a partial reimbursement program exists for customers who replace sooner. It is partial, and it is theirs to approve. This guide does not quote the amount and does not describe how to dig the line."),
      ]) + "</article>"
    return _page("/guides/denver-water-lead-service-line/", "Denver Water lead service lines | Aurora Plumbing Guide", "How Denver Water's lead program works, and why an Aurora Water account is not automatically in it.", "Denver Water lead service lines", "Lead lines", "Denver Water lead service line", "guide", body)


def g_lake(site):
    del site
    body = """
    <article class="sheet">
      <p class="eyebrow">Look up the address</p>
      <h1>Who serves water and sewer in Lakewood</h1>
      <p class="lede">Lakewood is not one utility. The city published a provider list in December 2024. Some districts sell both water and sewer. Some sell one. The city's own utility is a single row, and its sewer drawing covers that row's customers.</p>
      <p>The drawing says Public Works keeps the mains for about 8,000 customers in north Lakewood, and the owner keeps the lateral from the building to the main under the street. It says never connect a sump or a roof drain to that sewer. It gives 303-987-7955 for water and sewer maintenance and 303-980-7300 for emergencies and after hours, for that city system. Consolidated Mutual, Green Mountain, Bancroft-Clover, Denver Water, and the sanitation districts on the list are other rows. A backup on those systems is not automatically the city's crew.</p>
      <p>Use the list, then the bill, then <a href="/areas/lakewood/">the Lakewood hub</a>. Do not use <a href="/guides/aurora-sewer-line-responsibility/">Aurora's tap rule</a>.</p>
      """ + qas([
        ("Is every Lakewood house on city sewer?", "No. The December 2024 list names many districts. The city's graphic is for about 8,000 north Lakewood customers. Green Mountain, Bancroft-Clover, and others are separate. Match the address before you call the city's emergency number."),
        ("Who fixes the lateral on city sewer?", "The graphic says the owner maintains the entire lateral to the main under the street. The city keeps the main. That is not Aurora's wording, and it is not a promise about a district that only appears as another row on the list."),
        ("Can I hook a sump to the sewer?", "The city's graphic says no, for that system. Groundwater and roof drains stay out of the sanitary sewer. An ejector for a basement toilet is a different, sanitary pump. Do not use the sump rule to send sewage into the yard."),
      ]) + "</article>"
    return _page("/guides/lakewood-water-sewer-provider/", "Lakewood water and sewer providers | Aurora Plumbing Guide", "Lakewood's December 2024 provider list and the north-side sewer graphic that does not cover every district.", "Who serves water and sewer in Lakewood", "Lakewood utilities", "Lakewood water sewer provider", "guide", body)


def g_freeze(site):
    del site
    body = """
    <article class="sheet">
      <p class="eyebrow">Before or after</p>
      <h1>Frozen pipes versus winterization</h1>
      <p class="lede">Winterization is the work you do so a pipe does not freeze. Frozen-pipe repair is the visit after it has frozen or split. Booking the wrong one wastes the emergency.</p>
      <p>If water is on the floor, use <a href="/services/frozen-pipe-repair/">frozen pipe repair</a>. Close the indoor shutoff if you already know it. Do not use a flame. Do not operate a utility's street valve. Castle Rock tells its customers to call 720-733-6000 for the curb. If the house is empty next month and nothing is leaking today, use <a href="/services/plumbing-winterization/">winterization</a>: hoses off, a plan for heat or a drain-down, irrigation only if it is in the quote.</p>
      <p>Neither page is a gas-line manual.</p>
      """ + qas([
        ("The pipe is spraying. Which page?", "Frozen pipe repair. Stop the water at the indoor shutoff if you can, and call a plumber. Winterization will not close a split. Do not thaw it with an open flame."),
        ("I am leaving the house empty in January. Which page?", "Winterization, before you go. Ask what will be drained and whether the heat stays on. A burst while you are gone becomes the repair page, after the fact."),
        ("Does one visit do both?", "It can, if the quote says the burst is repaired and the other exposed lines are protected. Those are two scopes. A drain-down does not patch a hole, and a patch does not disconnect the garden hose."),
      ]) + "</article>"
    return _page("/guides/frozen-pipe-vs-winterization/", "Frozen pipes versus winterization | Aurora Plumbing Guide", "Emergency freeze repair versus draining and protecting a house before the cold.", "Frozen pipes versus winterization", "Freeze or prevent", "frozen pipe versus winterization", "guide", body)


def g_well(site):
    del site
    body = """
    <article class="sheet">
      <p class="eyebrow">Read the bill first</p>
      <h1>Well pump versus city water</h1>
      <p class="lede">A well has a pump and a pressure tank. City or district water has a meter and a main. Aurora's in-city customers are on a utility. Do not buy a well pump for a metered house.</p>
      <p>Check the bill and the property. Douglas County says to verify water, sewer, well, and septic before you dig, which matters on unincorporated lots such as <a href="/areas/highlands-ranch/">Highlands Ranch</a>. If the source is a well, repair is <a href="/services/well-pump-repair/">well pump repair</a> and a new pump string is <a href="/services/well-pump-installation/">installation</a>. If the source is a utility, low pressure is <a href="/services/water-pressure-problems/">pressure</a> or <a href="/services/water-line-repair/">the service line</a>. A state well permit was not copied onto this page. Ask before anyone drills.</p>
      """ + qas([
        ("How do I tell which one I have?", "The bill. A city or district account is not a well. A pressure tank and no water bill can mean a well. If you are unsure, do not order a pump. Douglas County's permit page tells owners to verify the source before they dig."),
        ("Can Aurora Water customers ignore this page?", "Yes, for the pump itself. Your outage or pressure problem goes to Aurora Water or to the house plumbing, not to a well casing. This page exists so a rural lot is not given city-main advice, and a city house is not sold a well."),
        ("Does a new well need a permit?", "Often yes, from the state, and this guide does not quote that rule line by line. Drilling is not the same as replacing a pump in a well that already exists. Ask before the rig is booked."),
      ]) + "</article>"
    return _page("/guides/well-pump-vs-city-water/", "Well versus city water | Aurora Plumbing Guide", "How to tell a private well from a metered utility before you price a pump.", "Well pump versus city water", "Well or utility", "well versus city water", "guide", body)


def lakewood(site):
    del site
    body = """
    <article class="sheet">
      <p class="eyebrow">Many districts, one map</p>
      <h1>Plumber Lakewood CO</h1>
      <p class="lede">Lakewood does not have one water department for every address. The city printed a provider list in December 2024. The sewer drawing people pass around is for the city's own north Lakewood customers, about 8,000 of them, not for every name on that list.</p>
      <h2>Look up the row before you assign the bill</h2>
      <p>The list includes districts that provide both water and sewer, water only, or sewer only. Lakewood's own water and sewer utility is one row, at 480 S. Allison Parkway. Consolidated Mutual, Denver Water, Green Mountain, Bancroft-Clover, Bear Creek, and several sanitation districts are others. A backup on Green Mountain's system is not a call to the city's crew. The full lookup is the <a href="/guides/lakewood-water-sewer-provider/">provider guide</a>. Do not paste Aurora's tap rule over any of these rows.</p>
      <h2>What the city graphic actually says</h2>
      <p>For that north Lakewood city sewer, Public Works keeps the mains. The owner keeps the lateral from the home or business to the main under the street. Half of that system, the city says, is private lateral, and those laterals cause many backups. Never connect a sump pump or a roof drain to that sewer. A device to stop sewage from entering the house is described as required by the plumbing code for some properties, not as a product this website sells. Maintenance is 303-987-7955. Emergencies and after hours are 303-980-7300. Those numbers are the city's, for that system, and they are not this guide's referral phone.</p>
      <p>A house water heater is still a building permit question for the City of Lakewood's building division, separate from which district sells the water. This page does not invent that permit timeline. For an Aurora comparison, use <a href="/services/water-heater-replacement/">Aurora replacement</a> only when the parcel is in Aurora.</p>
      """ + qas([
        ("Does the city own my sewer lateral?", "Not on the city's own graphic. You maintain the lateral to the main under the street. The city maintains the main, for about 8,000 north Lakewood customers. If your bill is a district, this graphic may not be your utility at all. Check the December 2024 list."),
        ("Whose number do I call for a backup?", "The utility on the bill. The city's after-hours line, 303-980-7300, is for the city system. It is printed so you do not call Aurora Water by mistake. It is not a button on this website."),
        ("Can I connect the sump to the sewer?", "The graphic says no. Groundwater and gutters stay out of that sanitary sewer. A basement toilet that cannot reach the sewer by gravity needs an ejector, which is sewage equipment, not a sump. Do not swap them."),
      ]) + "</article>"
    return _page("/areas/lakewood/", "Plumber Lakewood CO | Aurora Plumbing Guide", "Lakewood's many water and sewer providers, and the north-side lateral rule that does not cover every district.", "Plumber Lakewood CO", "Lakewood", "plumber Lakewood CO", "place", body)


def arvada(site):
    del site
    body = """
    <article class="sheet">
      <p class="eyebrow">On your property, not a guessed right of way</p>
      <h1>Plumber Arvada CO</h1>
      <p class="lede">Arvada's utility FAQ says you are responsible for the portion of the water or sewer service line on your property. It does not say you own the pipe under the street, and this page will not add that sentence.</p>
      <h2>What the city actually published</h2>
      <p>City Code section 102.76, as the billing FAQ cites it, puts the on-property portion of the service line on the owner. Private line insurance is not required. Companies that mail insurance offers are not the city. Report main breaks, service leaks, frozen meters, low pressure, or dirty water at 720-898-7070 if you are an Arvada utility customer. The city says it maintains more than 600 miles of water pipe and more than 450 miles of wastewater pipe, buys about 75 percent of its drinking water from Denver Water, and sends wastewater to Metro Water Recovery. Drought limits follow Denver Water's restrictions. None of that is an Aurora Water account.</p>
      <h2>What not to invent</h2>
      <p>Do not draw the ownership line at a curb, a sidewalk, or a meter pit from this FAQ. It stops at "on their property." A leak in the right of way needs the city's answer for that address, not Aurora's tap rule and not Castle Rock's curb stop. Building permits are a separate counter from utility billing. This page did not restate a plumbing fee schedule.</p>
      <p>Low pressure that is only your faucet is <a href="/services/water-pressure-problems/">a house problem</a>. A leak you cannot see is <a href="/services/leak-detection/">detection</a> before a dig. Lead-line replacement through Denver Water applies only if Denver Water, not Arvada's own plants, owns that service and the address is in the program. Read <a href="/guides/denver-water-lead-service-line/">the lead guide</a> before you pay for a private dig.</p>
      """ + qas([
        ("Do I own the sewer under the street in Arvada?", "The FAQ does not say that. It says you maintain the portion on your property and cites section 102.76. It does not give a right-of-way boundary. Ask the utility before you accept a street-cut price. Do not copy Aurora, where the owner keeps the line through the tap."),
        ("Is water-line insurance required?", "No. The city says it is not required and that mail offers are not from the city. You can still choose a policy. The FAQ is not a recommendation for a brand."),
        ("Who do I call for low pressure?", "If you are an Arvada utility customer and the problem may be their system, the FAQ says 720-898-7070. If only one faucet is weak, start with that faucet. The number is the city's, not this guide's phone, and it is not a link."),
      ]) + "</article>"
    return _page("/areas/arvada/", "Plumber Arvada CO | Aurora Plumbing Guide", "Arvada holds the owner responsible for the service line on the property, and does not publish a street boundary here.", "Plumber Arvada CO", "Arvada", "plumber Arvada CO", "place", body)


def englewood(site):
    del site
    body = """
    <article class="sheet">
      <p class="eyebrow">City of Englewood permits</p>
      <h1>Plumber Englewood CO</h1>
      <p class="lede">Englewood's building division says a permit is required to replace a water heater, to change water lines or drains or a bath valve, and to add or replace a backflow preventer. The utilities department runs water and wastewater for the city. A 2024 proposal to rewrite service-line ownership was not treated as the law on this page.</p>
      <h2>What needs a permit</h2>
      <p>The city's "to permit or not to permit" page includes replacing a water heater, changing water lines, drains, or bath and shower valves, and adding or replacing backflow preventers. The Building Division phone on that page is 303-762-2357, at 1000 Englewood Parkway. That is the city's number, not a tap-to-call for this guide. A faucet swap that does not change the pipe may not be on that list. A bathroom valve change is. Ask if you are between the two. Do not use Aurora's same-day heater sentence.</p>
      <h2>Water and sewer, without a guessed boundary</h2>
        <p>The utilities department says it provides water and the sanitary collection system, and that wastewater goes to South Platte Renew, a joint venture with Littleton. Emergency utility numbers are published on the city's contact page, 303-762-2635 in business hours and 303-762-2650 after hours. A 2024 council packet discussed changing where customer and utility ownership of the water service is measured, including curb stops and meter pits. That packet is a proposal. It is not treated here as a change to the code. Ask Englewood Utilities what applies today before you pay for a street cut. South Englewood Sanitation District maintains some sewers under a contract with the city. Your backup may not be the same main as your neighbor's.</p>
      <p>Backflow work belongs on <a href="/services/backflow-preventers/">backflow preventers</a>. A water heater belongs on <a href="/services/water-heater-replacement/">replacement</a> only after you confirm the permit is Englewood's.</p>
      """ + qas([
        ("Does a new water heater need a permit in Englewood?", "The city's permit page lists replacing a water heater as work that needs one. It also lists bath and shower valve changes and water-line changes. Call the Building Division at 303-762-2357 if the job is only a faucet on the same stops. Do not borrow Aurora's inspection promise."),
        ("Who owns the water line at the curb?", "Not answered here. A 2024 council bill proposed refining that line, including curb stops and meter pits. The packet read for this page is a proposal, not a statement that the code already changed. Ask the utility what is in force before you dig."),
        ("Is every sewer the city's?", "The utilities department runs the city's collection system, and South Englewood Sanitation District also has pipes, including some inside the city that the city maintains under contract. Ask which main you connect to. Aurora's tap rule is the wrong document."),
      ]) + "</article>"
    return _page("/areas/englewood/", "Plumber Englewood CO | Aurora Plumbing Guide", "Englewood permits water heaters and water-line changes. Service-line ownership was not taken from an unadopted proposal.", "Plumber Englewood CO", "Englewood", "plumber Englewood CO", "place", body)


def littleton(site):
    del site
    body = """
    <article class="sheet">
      <p class="eyebrow">Sewer to the tap, water from Denver Water</p>
      <h1>Plumber Littleton CO</h1>
      <p class="lede">Littleton's city code says the property owner maintains the sewer service line from the public sewer to the building, including the tap, and restores the right of way. Drinking water is Denver Water's, not the city's.</p>
      <h2>The sewer sentence</h2>
      <p>Section 7-5-24, as published in the city code viewer, makes the owner responsible for that service line including the tap, and for returning the street to city standards. If the building sits too low for gravity, the owner installs and maintains a lifting facility. That is an <a href="/services/sewer-ejector-pumps/">ejector</a>, not a sump. The city's right-of-way page says a sewer-specific construction permit is no longer issued and a right-of-way permit is used when work occupies the street, sidewalk, or alley. Acceptable repair pipe named there includes Schedule 40 PVC or SDR 35, with bedding called out. Those are Littleton's specs, not Aurora's. A mailing address that says Littleton can still be outside the city. Confirm the parcel.</p>
      <h2>The water sentence</h2>
      <p>The city's water-supply page says potable water is provided by Denver Water and that Littleton Public Works does not provide it. Report water breaks to Denver Water, 303-893-2444 in the hours they publish and 303-628-6801 after hours. Lead-line help, if any, is <a href="/guides/denver-water-lead-service-line/">Denver Water's program</a>, not an automatic free dig. A private <a href="/services/water-line-repair/">water line repair</a> is what you buy when the program says no.</p>
      """ + qas([
        ("Who fixes a blocked sewer lateral in Littleton?", "The owner, under the code section that includes the line from the public sewer to the building and the tap, plus street restoration. The city keeps the public sewer. A right-of-way permit covers work in the street. Aurora's version is similar in spirit and still the wrong citation."),
        ("Who do I call for a water-main break?", "Denver Water, using the numbers on Littleton's water page: 303-893-2444 or 303-628-6801 after hours. The city says it does not provide potable water. Those numbers are Denver Water's, not this guide."),
        ("The basement is too low to drain. Whose pump is it?", "Yours. The code says the owner installs and maintains the lift when gravity cannot reach the public sewer. That is a sewer ejector. It is not the city's main, and it is not a groundwater sump."),
      ]) + "</article>"
    return _page("/areas/littleton/", "Plumber Littleton CO | Aurora Plumbing Guide", "Littleton owners maintain the sewer service line including the tap. Denver Water supplies the drinking water.", "Plumber Littleton CO", "Littleton", "plumber Littleton CO", "place", body)


def westminster(site):
    del site
    body = """
    <article class="sheet">
      <p class="eyebrow">Your lateral, their main under the road</p>
      <h1>Plumber Westminster CO</h1>
      <p class="lede">Westminster says you maintain the sewer pipes from the house until they connect to the city's main, including the line under a driveway. The city owns the main under the road.</p>
      <h2>The backup call</h2>
      <p>The city's wastewater FAQ says to call a plumber for a backup on your lateral. If the backup is in the city's main, call Wastewater Collections at 303-658-2500. The same number is for sewage on a street or sidewalk. The city says it maintains more than 400 miles of sewer and that crews jet debris, grease, and roots from those mains. A jet truck in the street is their main, the way Aurora's truck is Aurora's main. It is not a cleaning of your lateral. Your repair is still <a href="/services/sewer-line-repair/">sewer repair</a> if the camera shows your pipe failed, and the ownership sentence is Westminster's, not Aurora's tap-and-saddle wording. Read the code title the FAQ names, Title VIII, Chapter 8, before you rely on a driveway dispute.</p>
      <h2>What this page does not say</h2>
      <p>It does not set a water-service boundary, a water-heater permit timeline, or a price. Building permits are a separate desk. Use <a href="/services/water-heater-replacement/">heater replacement</a> only for the decision, then ask Westminster's building division for the permit. Do not call 303-658-2500 and expect this website to answer. That number is the city's.</p>
      """ + qas([
        ("Is the sewer under my driveway mine?", "The city's FAQ says yes, you maintain the pipes from the house to the city's main, and it answers the driveway question the same way. The city owns the main under the road. If you are unsure, call Wastewater Collections at 303-658-2500. Do not use Aurora's rule or a contractor's sidewalk habit."),
        ("A truck is jetting the street. Did they clean my line?", "No. The FAQ describes city crews cleaning the city's pipes, more than 400 miles of them. Your lateral is still yours. If the backup remains after the main is clear, the plumber and a camera are the next step."),
        ("Who do I call if sewage is in the gutter?", "Wastewater Collections, 303-658-2500, for sewage on public property. A backup inside the house starts with a plumber, then that number if the main is the cause. The number is Westminster's, not a referral line for this guide."),
      ]) + "</article>"
    return _page("/areas/westminster/", "Plumber Westminster CO | Aurora Plumbing Guide", "Westminster owners keep the sewer lateral to the city main, including under the driveway.", "Plumber Westminster CO", "Westminster", "plumber Westminster CO", "place", body)


def cr_tankless(site):
    del site
    body = """
    <article class="sheet">
      <p class="eyebrow">Castle Rock only</p>
      <h1>Tankless water heater installation in Castle Rock</h1>
      <p class="lede">This is the Town's permit path for a tankless heater, not Aurora's. The residential permit page says tankless units require plan review. You provide the manufacturer's specification sheet and gas piping load calculations. A storage-tank heater is listed separately and may not need that review.</p>
      <h2>What to hand over</h2>
      <p>The sheet for the model you are buying, and the gas-load math for the house, not a sentence that says the old tank was smaller. Building-code amendments took effect June 30, 2026. Ask the counter if a packet drawn earlier still matches. The building phone on that page is 720-733-3527. It is the Town's. This guide's own referral number is not published. The town hub is <a href="/areas/castle-rock/">Castle Rock</a>. The general conversion questions, vent and condensate, stay on <a href="/services/tankless-water-heater-installation/">tankless installation</a> and should be answered in addition to the Town's packet, not instead of it.</p>
      <h2>Water line is a different FAQ</h2>
      <p>If the job also touches the water service, Town water customers are told the Town maintains the line to the property-line connection and owns the curb stop. Do not shut that street valve. That rule is not part of the gas-load sheet, and it is not Aurora's. A quote that changes both the heater and the yard pipe should say so.</p>
      <p>No savings percentage and no price are printed here. No contractor is dispatched.</p>
      """ + qas([
        ("What does Castle Rock require that a tank swap might not?", "Plan review, the manufacturer specification sheet, and gas piping load calculations. The Town's permit page calls tankless out. A storage-tank water heater may avoid that review. Do not submit the tankless unit on a tank assumption."),
        ("Can I use Aurora's same-day inspection instead?", "No. Aurora's sentence is for Aurora, and even there it is not a guarantee. Castle Rock's counter is 720-733-3527 on the permit page. Call that office about the review. It is not this website."),
        ("Do the 2026 codes matter?", "The Town says the adopted amendments took effect June 30, 2026. An older checklist from another metro city is the wrong attachment. Ask if your submittal matches the current packet."),
        ("Does the gas calculation include a water-line repair?", "Only if you are also changing water piping. The calculation is the heater's fuel demand. The curb-stop rule is a separate Town FAQ. Keep the two scopes visible on the quote."),
      ]) + "</article>"
    return _page("/areas/castle-rock/tankless-water-heater-installation/", "Tankless installation in Castle Rock | Aurora Plumbing Guide", "Castle Rock's plan review, manufacturer sheet, and gas-load calculations for a tankless water heater.", "Tankless water heater installation in Castle Rock", "Castle Rock tankless", "tankless water heater installation Castle Rock CO", "service", body)


def cent_heater(site):
    del site
    body = """
    <article class="sheet">
      <p class="eyebrow">Centennial one-stop, not a commercial clock</p>
      <h1>Water heater replacement in Centennial</h1>
      <p class="lede">Centennial's review schedule puts a residential water heater on the one-stop list and states one business day. A new house, an addition, and commercial work are longer lists. The city does not sell the water.</p>
      <h2>The schedule</h2>
      <p>One-stop items, including a water heater, are described as needing no plan review, with one business day stated. New residential and new commercial are 15 business days after the plan-review fee. Additions are 10. The clock is for a complete submittal, and the city encourages a pre-submittal meeting. Building Division contact on that page is 303-754-3321. Those are the city's figures, not a promise that your heater is approved tomorrow, and not Aurora's same-day request. The comparison guide is <a href="/guides/centennial-heater-vs-remodel-permit/">heater versus remodel</a>. The city page is <a href="/areas/centennial/">Centennial</a>.</p>
      <h2>The utility is not the city</h2>
      <p>Centennial does not provide water or sewer. Districts do. Use the property search before you tell a plumber the line is Aurora's or the city's. A like-for-like tank is this page. A tankless conversion still needs the manufacturer's vent and fuel story on <a href="/services/tankless-water-heater-installation/">the tankless page</a>, even if the city listed "water heater" as one-stop. Ask the counter whether tankless stays on that list.</p>
      <p>No price and no referral call are offered here.</p>
      """ + qas([
        ("How long is the Centennial water-heater review?", "The schedule says one business day for the one-stop group that includes a water heater, once the submittal is complete. That is not the 15-day new-building line and not a guarantee. Ask the Building Division, 303-754-3321, which list you are on."),
        ("Does the city own the water line?", "No. The city says it does not provide water or sewer. Identify the district with the property search. Do not use Aurora Water's owner-to-the-main sentence on a Centennial bill."),
        ("Is a bathroom addition the same permit?", "No. Additions are on the 10-business-day line in that schedule. A water heater does not pull an addition onto the one-stop list. Price them separately."),
        ("Does one-stop include tankless?", "The schedule says water heater. It does not walk through gas-load math the way Castle Rock does for tankless. Ask Centennial whether your tankless unit stays one-stop. Bring the manufacturer sheet anyway."),
      ]) + "</article>"
    return _page("/areas/centennial/water-heater-replacement/", "Water heater replacement in Centennial | Aurora Plumbing Guide", "Centennial's one-stop residential water heater review, kept separate from additions and from Aurora.", "Water heater replacement in Centennial", "Centennial water heaters", "water heater replacement Centennial CO", "service", body)


GUIDES = [g_tankless, g_drain, g_trench, g_supply, g_juris, g_cent, g_cr, g_denver, g_lake, g_freeze, g_well]
CITIES = [lakewood, arvada, englewood, littleton, westminster]
SX = [cr_tankless, cent_heater]
