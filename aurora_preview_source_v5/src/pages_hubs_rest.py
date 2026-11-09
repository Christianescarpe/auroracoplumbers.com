"""Community hubs from permit and utility pages read for this build.

Golden and Morrison are not included. The first official URLs tried returned 404.
"""

from markup import qas
from pages_wave import _page

LINKS = []


def hub(slug, name, keyword, eyebrow, lede, body, pairs):
    LINKS.append((f"/areas/{slug}/", name))
    html = f"""
    <article class="sheet">
      <p class="eyebrow">{eyebrow}</p>
      <h1>Plumber {name} CO</h1>
      <p class="lede">{lede}</p>
      {body}
      {qas(pairs)}
      <p>A slow drain is <a href="/services/drain-cleaning/">drain cleaning</a> until a camera shows a broken <a href="/services/sewer-line-repair/">sewer line</a>. A tank swap is <a href="/services/water-heater-replacement/">water heater replacement</a>. Confirm the permit office and the utility for this address before the work is closed up.</p>
    </article>
    """
    return _page(
        f"/areas/{slug}/",
        f"Plumber {name} CO | Aurora Plumbing Guide",
        lede[:155],
        f"Plumber {name} CO",
        name,
        keyword,
        "place",
        html,
    )


def denver(site):
    del site
    return hub(
        "denver",
        "Denver",
        "plumber Denver CO",
        "City and County of Denver",
        "Denver is its own city and county. A water heater can be a quick permit on a house. The private sewer lateral, through the tap, is yours. Aurora's rules do not cross Speer or Havana onto a Denver parcel.",
        """
        <h2>Permits</h2>
        <p>Denver's quick-permit list for single-family and duplex homes includes water heaters, water service, disposals, tubs, and showers. Grease interceptors and swimming-pool heaters cannot be quick permits. Since March 1, 2023, a new or replacement gas water heater in a commercial or multifamily building is not a quick permit. The city asks for an electrification feasibility report or a gas-leak test under its energy code. A homeowner may pull a plumbing permit on a house they own and live in only after an exam, or with a state license. Like-for-like faucet replacement is listed as work that does not need a building permit. Replacing a concealed drain does. Development Services is at 201 W. Colfax Avenue.</p>
        <h2>Sewer and lead lines</h2>
        <p>Denver locates main sewers only. The lateral, up to and including the tap into the main, is the owner's. For a backup, the wastewater FAQ says to call 303-446-3400. If the crew finds the problem in the city main, they fix that main. If it is your line, they tell you, and the plumber is yours. That phone is Denver's, not a referral button here. Drinking-water lead lines are a Denver Water program, not automatic, and not Aurora Water. Use the address search on <a href="/guides/denver-water-lead-service-line/">the lead guide</a> before you pay for a private dig.</p>
        """,
        [
            ("Is a Denver house water heater a quick permit?", "On a single-family or duplex home, Denver's quick-permit list includes water heaters. A gas water heater in a commercial or multifamily building has not been a quick permit since March 1, 2023. The city wants an electrification report or a documented gas-leak test. Do not use Aurora's same-day sentence on a Denver parcel."),
            ("Who owns the sewer tap in Denver?", "You do, through the connection to the main. Denver says it locates main sewers only and that the lateral, including the tap, is the owner's. Call 303-446-3400 for a backup. If the main is the problem, the city fixes the main. If the lateral is the problem, you hire the plumber."),
            ("Does Denver Water's lead program cover every old house?", "No. The program page points you to an address search and describes a limited set of homes. A replacement during a Denver Water main project can be at no direct charge when they find a customer-owned lead line. Check the address. An Aurora Water account is a different utility."),
        ],
    )


def thornton(site):
    del site
    return hub(
        "thornton",
        "Thornton",
        "plumber Thornton CO",
        "City of Thornton",
        "Thornton separates a building permit from a right-of-way permit for a water or sewer service repair. An in-yard repair inside the city is not the same application as a repair that reaches the street.",
        """
        <h2>Two counters</h2>
        <p>The city's permit portal says a building permit is required to erect, enlarge, remodel, repair, or change a building or utility. Building Inspections is 303-538-7250. Homeowners working on their own residence are not licensed as contractors. Separately, sewer and water service repairs that run from the yard into the right of way, inside city limits, use a sewer and water service construction permit. Repairs that stay in the yard, inside city limits, go to the Buildings Division. Outside city limits, the portal says an in-yard-only repair is the case that uses the service-construction permit. Read that twice before you apply. A Thornton mailing address is not proof you are inside the city.</p>
        <h2>What this does not decide</h2>
        <p>Thornton's permit instructions do not draw an ownership line at a curb or a tap. Westminster's driveway sentence is Westminster's. Ask Thornton utilities, for this address, who maintains the pipe under the asphalt. A <a href="/services/water-line-repair/">water line</a> quote should name which permit, building or right-of-way, is included.</p>
        """,
        [
            ("Does a yard leak in Thornton need a street permit?", "Only if the repair leaves the yard and enters the right of way, and only if the parcel is inside the city. The portal sends in-yard work inside the city to the Buildings Division, and right-of-way service repairs to a different construction permit. Confirm the city limit before you pick the form."),
            ("Can I use Aurora's sewer rule?", "No. Thornton's pages describe which permit to pull. They do not say the owner keeps the line through the tap the way Aurora Water does. Ask the city's utility for the address. A quote that assumes Aurora's split can bill you for a pipe the city maintains, or the reverse."),
            ("Who licenses the plumber?", "Thornton licenses contractors who build, alter, or install underground utilities in the city. A homeowner on their own house is not in that license rule. The person who pulls the permit should match the portal's category. Building Inspections is 303-538-7250. That number is the city's, not this guide."),
        ],
    )


def northglenn(site):
    del site
    return hub(
        "northglenn",
        "Northglenn",
        "plumber Northglenn CO",
        "City of Northglenn",
        "Northglenn puts water heaters and sewers on a one-stop list, and it publishes a multi-week clock for a residential plan review. Those are city targets, not a promise this guide can make.",
        """
        <h2>One-stop versus plan review</h2>
        <p>The building page lists one-stop permits that include water heaters, sewers, furnaces, and air conditioners, filed in CommunityCore. Residential plan review is listed at 10 to 14 business days. A commercial job under one million dollars is 14 to 20 business days, and a larger commercial job is 21 to 30. Building Division hours are weekdays 8:30 a.m. to 4:30 p.m. Contractors call 303-450-8745 for a portal login. Homeowners create a community-member account. The main line printed on the page is 303-451-8326. Those are city numbers, not tap-to-call for this site.</p>
        <h2>Utility line not copied from Aurora</h2>
        <p>The permit page does not say whether you or the city owns the sewer lateral under the parkway. Do not fill that gap with Aurora's tap rule. Ask Northglenn's utility for the address before a <a href="/services/sewer-line-repair/">sewer repair</a> includes street patching. A one-stop sewer permit is still not a camera, and it is not proof the pipe can be lined.</p>
        """,
        [
            ("Is a Northglenn water heater a one-stop permit?", "The city's list says yes, alongside sewers, furnaces, and air conditioners, through CommunityCore. A residential remodel or addition is on the plan-review clock of 10 to 14 business days. Those are the city's estimates, not a guarantee, and they are not Aurora's same-day request."),
            ("Does the city own the lateral?", "Northglenn's permit page does not say. Do not assume Aurora's owner-to-the-tap rule or Westminster's driveway rule. Ask the utility that bills the address, and make the quote say who patches the street. Responsibility varies by utility."),
            ("Can a homeowner file?", "The page says homeowners create a community-member account, and contractors need a login from 303-450-8745. You can search permits without an account. Filing the wrong account type is how a one-stop heater sits in review."),
        ],
    )


def commerce(site):
    del site
    return hub(
        "commerce-city",
        "Commerce City",
        "plumber Commerce City CO",
        "City of Commerce City",
        "Commerce City splits building permits from public-works permits. A water heater inside a building is not the same application as a cut in the street.",
        """
        <h2>Building Safety versus Public Works</h2>
        <p>Building Safety, at 303-289-3790, issues building permits and inspections. The contact block on the page places the counter at 7190 Colorado Boulevard, sixth floor, weekdays 8 a.m. to 5 p.m. Issued permits are searched in eTRAKiT. Public Works issues right-of-way, grading, and street-occupancy permits when the work touches streets, sidewalks, or public infrastructure. A <a href="/services/water-line-repair/">service-line repair</a> that stays in the yard may be a building permit. The same repair in the street needs the right-of-way permit. Ask which, for this address.</p>
        <h2>The utility is a separate question</h2>
        <p>The building instructions do not name one water or sanitation district, and they do not say who owns the service line. Some Commerce City addresses are on a district rather than a city utility. Use the bill, then ask that utility who maintains the pipe in the street. Responsibility varies by utility. Confirm it before you authorize the work.</p>
        """,
        [
            ("Which Commerce City desk permits a sewer dig in the street?", "Public Works, if the work occupies the right of way or public infrastructure. Building Safety at 303-289-3790 handles the building permit and the inspection of work on the structure. A quote should name both applications when the trench leaves the yard. The phones are the city's, not this guide's."),
            ("Who owns the water service?", "The building instructions do not say. Ask the utility named on the water bill before anyone prices a curb or a tap. A district customer is not the city crew. A Commerce City mailing address does not make the account Aurora Water."),
            ("Are eTRAKiT permits the same as a right-of-way permit?", "No. The building page says issued building permits can be looked up in eTRAKiT. Right-of-way permits are a Public Works list. Searching one system and finding nothing does not mean the street cut was permitted."),
        ],
    )


def brighton(site):
    del site
    return hub(
        "brighton",
        "Brighton",
        "plumber Brighton CO",
        "City of Brighton",
        "Brighton lets an emergency water-heater or service-line repair start before the paperwork, if you apply the next business day and you do not cover the work.",
        """
        <h2>Emergency, then the permit</h2>
        <p>The permitting page says emergency repairs and replacements can be done for water heaters, furnaces, boilers, heat pumps, and a water supply or sewer service. You must apply by the next business day, and the work cannot be concealed. Email 1stop@brightonco.gov about the emergency and apply in the portal. After a normal permit is paid, the stamped plans and the permit card have to be printed and available to the inspector. The building counter is 303-655-2017. The homeowner inspection line is 303-655-2151. Those are city addresses and numbers, not a referral line.</p>
        <h2>Do not hide the repair</h2>
        <p>Covering a sewer repair before the inspector sees it breaks the emergency exception. That is the opposite of Aurora's instruction to keep permitted work open, and it is Brighton's own sentence. The page does not say who owns the lateral. Ask the city's utility before you accept a street patch. A planned, non-emergency <a href="/services/water-heater-replacement/">water heater</a> still needs the permit. It is not an excuse to skip it.</p>
        """,
        [
            ("Can I replace a water heater in Brighton before the permit is issued?", "Only as an emergency, and only if you apply the next business day and leave the work open to inspect. The page lists water heaters and water or sewer service repairs in that exception. A planned replacement is a normal permit. Do not bury the pipe and call it an emergency later."),
            ("Where does the inspector look?", "At the open repair, with the stamped plans and permit card printed from the portal once the permit is paid. The homeowner inspection line is 303-655-2151. Covering the work removes the exception the city described."),
            ("Is the sewer the city's to the house?", "The permitting page does not say that. It tells you how to permit the repair. Ownership is a utility question for the address. Do not use Aurora's tap rule or a contractor's sidewalk rule until Brighton confirms it."),
        ],
    )


def federal(site):
    del site
    return hub(
        "federal-heights",
        "Federal Heights",
        "plumber Federal Heights CO",
        "City of Federal Heights",
        "Federal Heights inspects its own building permits, and it sends electrical permits to the state. A water heater that also needs a new circuit is two authorities, not one.",
        """
        <h2>City building, state electrical</h2>
        <p>The building department says the State of Colorado, through DORA, administers all electrical permits and inspections in Federal Heights. Schedule a city building inspection by 3:30 p.m. the day before, at 303-412-3534, with the permit number and the type of inspection. The office is at 2380 West 90th Avenue. The city also publishes a mobile-home set application, so a manufactured home on a lot here is a city building question plus whatever the home's under-floor piping needs. See <a href="/services/mobile-home-plumbing/">mobile home plumbing</a> for the limits of that page.</p>
        <h2>What was not in the building blurb</h2>
        <p>The page does not name the water or sewer utility and does not say who owns a lateral. Ask the utility on the bill before a street cut. Do not borrow Aurora, Thornton, or Westminster. A plumbing repair that is only a faucet may still be a city building permit. An electrical reconnection is the state's permit, not a line you add quietly.</p>
        """,
        [
            ("Who permits the wiring for a water heater in Federal Heights?", "The state. The city says DORA administers all electrical permits and inspections here. The city's own inspectors still cover the building permit. Call 303-412-3534 by 3:30 p.m. the day before for a city inspection. Do not expect the city counter to issue the electrical permit."),
            ("Is there a mobile-home permit?", "The building page lists a mobile home set application. That is about setting the home, not a promise about under-floor pipe fittings. The lot is still in Federal Heights if the parcel is. Ask the building department which permit covers a plumbing change after the home is set."),
            ("Who owns the sewer line?", "Federal Heights' building page does not say. Do not invent a curb line. Get the utility name from the bill, then ask that utility who repairs the pipe under the street. Responsibility varies by utility. Confirm it before you authorize the work."),
        ],
    )


def wheat(site):
    del site
    return hub(
        "wheat-ridge",
        "Wheat Ridge",
        "plumber Wheat Ridge CO",
        "City of Wheat Ridge",
        "Wheat Ridge requires a building permit to replace a furnace, a boiler, or a water heater. Since January 2025 the application lives in OpenGov, and a permit is valid for 180 days.",
        """
        <h2>What needs a permit</h2>
        <p>The building page lists water heater replacement with furnaces and boilers, and it also lists in-ground and above-ground pools and hot tubs deeper than 24 inches, interior remodels, and basement finishes. The permit desk is 303-235-2855, option 1. Permits last 180 days, with another 180 days if an approved inspection shows real progress, under the code section the city cites. A like-for-like faucet is not on that list. A water heater is. Do not treat Wheat Ridge as Aurora's same-day program.</p>
        <h2>Districts are extra</h2>
        <p>The building page does not name one water or sewer owner. Wheat Ridge sits among several special districts. Ask who bills the water before you dig. A <a href="/services/pool-spa-plumbing/">pool</a> deeper than 24 inches is a building permit here even when the work is the shell, not just a leaking union. Who owns the pipe is the district's fact.</p>
        """,
        [
            ("Does Wheat Ridge require a permit for a replacement water heater?", "Yes. The building page lists furnace, boiler, and water heater replacement with work that needs a permit, filed in OpenGov since January 2025. The permit lasts 180 days unless an inspection shows progress and extends it. The desk is 303-235-2855, option 1. That is the city's number."),
            ("Is a hot tub included?", "A hot tub or pool deeper than 24 inches, in the ground or above it, is on the permit list. A shallow portable unit may not be. Ask before you set it. The plumbing of the pipes is still separate from the electrical connection."),
            ("Who maintains the sewer lateral?", "Not answered on the building page. Do not copy Aurora or Westminster. Identify the district on the bill. A permit to do the work is not the same fact as who pays for the pipe under the street."),
        ],
    )


def broomfield(site):
    del site
    return hub(
        "broomfield",
        "Broomfield",
        "plumber Broomfield CO",
        "City and County of Broomfield",
        "Broomfield is its own city and county. Every water heater, new or replacement, needs a permit. A new water or sewer tap license is not issued before the building permit.",
        """
        <h2>Heaters and sewer repairs</h2>
        <p>The building division says all water heaters need a permit, including replacements, and it points homeowners to a state addendum on residential plumbing work. Sewer line repairs are on the same permit list as gas lines, boilers, and heat pumps. Email applications to buildingpermits@broomfield.org. This is not Aurora, and it is not a quick verbal okay.</p>
        <h2>New taps versus a repair</h2>
        <p>City council ordinances described on the page say a water license and a sewer license may be applied for with the building permit and shall not be issued before that building permit. The page also states 2026 license amounts for a new three-quarter-inch water tap and an equivalent sewer tap. Those are connection licenses, not a plumber's repair price, and this guide does not repeat the dollar figures as a quote. A leaking existing <a href="/services/water-line-repair/">service line</a> is not a new tap. Ask which application you are buying.</p>
        """,
        [
            ("Does a replacement water heater need a permit in Broomfield?", "Yes. The building division says every water heater needs one, new or replacement. Homeowners are pointed to the state's addendum on residential plumbing work. File with the building division. Do not use Aurora's same-day language or Denver's quick-permit list."),
            ("Can I buy a water tap before the building permit?", "No. The city says water and sewer licenses are applied for with the building permit and are not issued before it. That rule is about a new tap, not about patching a leak on a line you already have. Ask the counter which file you are in."),
            ("Is a sewer repair a tap license?", "No. Sewer line repairs are listed as building-permit work. A new sewer license is a different, larger connection fee discussed on the same page. Do not let a repair quote cite a new-tap license unless you are actually adding service."),
        ],
    )


def louisville(site):
    del site
    return hub(
        "louisville",
        "Louisville",
        "plumber Louisville CO",
        "City of Louisville",
        "Louisville can turn a water heater or a sewer repair around the same day or the next business day. An addition is measured in weeks. The contractor needs a Louisville license.",
        """
        <h2>Clocks</h2>
        <p>The building page lists same-day or next-business-day review for a water heater, a minor plumbing repair, and a sewer or water repair. A gas line or a hot tub is on a one-to-two-week fast track. A residential addition or a new home is four to six weeks. Over-the-counter permits are paid when you apply. Plan-review permits are paid after approval, and the city says the permit then takes about one business day to issue. Inspection requests are for the next business day. Contractors must hold a current Louisville license and be named on the application.</p>
        <h2>Taps and mines</h2>
        <p>New water and sewer connections use fixture-count forms and a tap-fee calculation. That is not a repair of an existing lateral. The city also tells you to check a mine-hazard map before you build. A plumbing quote that ignores a mine note on an addition is incomplete. Ownership of an existing sewer lateral was not on the permit page. Ask the utility. Do not use Aurora's rule.</p>
        """,
        [
            ("How fast is a Louisville water heater permit?", "The city lists water heaters with same-day or next-business-day permits, in the same group as a sewer or water repair. An addition is four to six weeks. Pay over-the-counter permits when you apply. Those clocks are targets, not a promise from this guide."),
            ("Does my plumber need a city license?", "Yes. The page says contractors and subcontractors must hold a current Louisville license and be listed on the application. A license from another city is not what that sentence says. Ask to see the Louisville license before the work starts."),
            ("Is a tap fee the same as a sewer repair?", "No. Fixture-count and tap-fee forms are for connections. A repair of an existing line is the same-day group if it is only a repair. The page does not say who owns the pipe in the street. Ask before you include a patch."),
        ],
    )


def longmont(site):
    del site
    return hub(
        "longmont",
        "Longmont",
        "plumber Longmont CO",
        "City of Longmont",
        "Longmont uses two different phone lines for water and sewer taps: one for work outside the building and one for work inside. A bathroom remodel can need both.",
        """
        <h2>Inside versus outside</h2>
        <p>The city's development page says to call 303-651-8304 for water and sewer tap information outside the building, and 303-651-8332 for tap information inside the building. New service lines are sized from fixture counts under the plumbing code the city says it has adopted. A form for expected utility needs asks for water-supply fixture units and drainage fixture units. That is a development sizing sheet, not a repair invoice, and this page will not calculate the units for you.</p>
        <h2>A repair is not a new tap</h2>
        <p>Fixing a leak on a private <a href="/services/water-line-repair/">water line</a> or a <a href="/services/sewer-line-repair/">sewer lateral</a> is not the same phone call as buying a new tap for a subdivision. Ask which desk you are on. Longmont's tap pages do not say whether the owner or the city maintains an existing lateral under the street. Confirm that with the utility before a street cut. Longmont Power is a separate city utility from water and wastewater. A plumbing job is not an electric-meter job.</p>
        """,
        [
            ("Which Longmont number is for a sewer tap in the street?", "303-651-8304, the number the city prints for water and sewer tap information outside the building. Inside-the-building tap questions use 303-651-8332. A remodel that adds fixtures can need both. Those numbers are the city's, not this guide."),
            ("Will you calculate fixture units?", "No. The city's form asks for them under the plumbing code it has adopted. The engineer or the plumber on the development submits them. A webpage total would be made up. A simple repair of one existing pipe is not that form."),
            ("Does Longmont use Aurora's tap rule?", "No. Longmont separates inside and outside tap questions. Those pages do not say the homeowner owns the line through the tap. Ask Longmont utilities for the address before a street cut is priced. Confirm who maintains the pipe before you authorize the work."),
        ],
    )


def greenwood(site):
    del site
    return hub(
        "greenwood-village",
        "Greenwood Village",
        "plumber Greenwood Village CO",
        "City of Greenwood Village",
        "Greenwood Village will not name your water or sewer provider at the front counter without a map. The building permit also wants proof you submitted to that district.",
        """
        <h2>Find the district, then the permit</h2>
        <p>Public Works says to use the water district map and the sanitation district map, or call 303-708-6100. The sanitation map the city publishes includes Castlewood, Cherry Creek Valley, Southgate, Goldsmith Gulch, and others, and it flags some parcels that may have a septic system and should call Arapahoe County Public Health. Work in the right of way needs a permit from 10001 East Costilla Avenue. Community Development, 303-486-5783 at 6060 South Quebec Street, says a building permit is generally required for an addition, alteration, or repair, and that kitchen cabinets alone may still need a plumbing permit if fixtures are reinstalled.</p>
        <h2>External sign-off</h2>
        <p>The permit instructions say proof of submittal to the water and sanitation district is included when it applies, and that the district's approval does not replace the village review. A quote that skips the district letter can stall the permit. Do not assume Aurora Water or Denver Water. Ask the map.</p>
        """,
        [
            ("How do I find the sewer district in Greenwood Village?", "Use the city's sanitation district map or call Public Works at 303-708-6100. The map includes more than one district, and some parcels may be on septic and are told to call Arapahoe County Public Health. Aurora's utility is not the default."),
            ("Does a new faucet need a permit?", "The building page says cabinet work may still need a plumbing permit when fixtures are reinstalled. Painting and floor coverings do not. Call Community Development at 303-486-5783 before you open the shutoffs. A full bathroom is an alteration and is a permit."),
            ("Can the district approve the job instead of the village?", "No. The permit page says outside approvals do not replace village plan review. You may need both the district and the city. A right-of-way cut is a third permit, from Public Works on Costilla."),
        ],
    )


def lonetree(site):
    del site
    return hub(
        "lone-tree",
        "Lone Tree",
        "plumber Lone Tree CO",
        "City of Lone Tree",
        "Lone Tree does not sell water or sewer. The city's utility page is a starting map, not proof of the district at a single address. The bill or the district's own lookup controls.",
        """
        <h2>The bill names the district</h2>
        <p>The city's <a href="https://cityoflonetree.com/utility-providers/" rel="noopener noreferrer">utility providers page</a> says the city does not provide water or sewer. It lists Southgate Water and Sanitation Districts for property west of I-25, Parker Water and Sanitation District for property east of I-25, and Northern Douglas County Water and Sanitation District for some homes in Terra Ridge along Indian Wells Drive. A resident guide has also said Parker Water serves all Lone Tree properties east of I-25. That "all" is broader than the utility page, which already names a third district. Use the address and the district, not the highway alone. Southgate's emergency number in the resident guide is 303-799-0261. Parker Water's number there is 303-841-4627. Those are district numbers, not this site. Parker Water's service-line boundary is unresolved on the <a href="/areas/parker/">Parker</a> page. Do not inherit a sidewalk rule. Building permits, including a water heater, go through Lone Tree at 720-390-5211. Inspections are scheduled at 303-225-4941.</p>
        <h2>Do not use Parker's town counter</h2>
        <p>Being a Parker Water customer does not make the house inside the Town of Parker. The Town of Parker permits only inside its limits. A Lone Tree house can have a Lone Tree building permit and any of those three districts. Ask both the city and the district named on the bill. Aurora's tap rule is a third error.</p>
        """,
        [
            ("Who is my sewer district in Lone Tree?", "Do not decide from the highway alone. The city's utility page lists Southgate west of I-25, Parker Water east of I-25, and Northern Douglas County Water for some Terra Ridge homes on Indian Wells Drive. A resident guide's broader 'all east of I-25' line is why you confirm with the district or the bill. The phones in the guide are the districts', not this site."),
            ("Does Parker Water mean the Town of Parker inspects the heater?", "No. Lone Tree's building division permits water heaters inside Lone Tree, at 720-390-5211. The Town of Parker permits inside Parker. The water district and the building department are different. A tankless review in Castle Rock is a third city."),
            ("Where can the dumpster sit?", "On your property, a temporary permit is required unless a building permit is already active. In the street, Public Works wants a right-of-way permit. The guide also says the dumpster cannot sit in the right of way for more than 30 consecutive days in a year unless construction is active."),
        ],
    )


def castlepines(site):
    del site
    return hub(
        "castle-pines",
        "Castle Pines",
        "plumber Castle Pines CO",
        "City of Castle Pines",
        "Castle Pines has its own building department. That page does not name the water district. Use the bill, and do not guess a neighboring city's utility.",
        """
        <h2>The counter</h2>
        <p>The city building department issues permits and inspections and can be reached at 303-705-0227, weekdays 8 a.m. to 4 p.m., or buildingdept@castlepinesco.gov. The office is at 7437 Village Square Drive, Suite 200. That is not Douglas County's counter at 100 Third Street in Castle Rock, and it is not the Town of Castle Rock's residential permit desk. A house inside the city uses the city. A house in an unincorporated Douglas County pocket nearby, such as <a href="/areas/the-pinery/">The Pinery</a> if that is the real jurisdiction, uses the county. Confirm the parcel.</p>
        <h2>Utility unknown on that page</h2>
        <p>Because the building page did not name a water or sanitation provider, do not assume Castle Rock Water, Parker Water, or Aurora Water. Ask the city or the bill. A <a href="/services/water-heater-replacement/">water heater</a> permit is a building question. A <a href="/services/sewer-line-repair/">sewer repair</a> in the street is a utility question this page refuses to guess. Castle Rock's tankless gas-load sheet applies in Castle Rock, not here, unless Castle Pines tells you they adopted the same packet.</p>
        """,
        [
            ("Is Castle Pines the same permit office as Castle Rock?", "No. Castle Pines publishes its own building department at 303-705-0227 on Village Square Drive. Castle Rock's tankless rules are the Town of Castle Rock's. Douglas County permits unincorporated land from a different counter. Match the parcel before you upload plans."),
            ("Who provides sewer?", "The Castle Pines building page does not say. Do not assign Castle Rock Water, Parker Water, or Aurora Water because they are nearby. Use the bill. A street-cut quote without the utility's name is incomplete. Confirm the district before you authorize the work."),
            ("Does the city inspect water heaters?", "The building department says it issues permits and does inspections. Ask that office whether a replacement heater is a simple permit or a review. This page will not copy another city's one-stop list onto Castle Pines."),
        ],
    )


def edgewater(site):
    del site
    return hub(
        "edgewater",
        "Edgewater",
        "plumber Edgewater CO",
        "City of Edgewater",
        "Edgewater runs its own water utility, with Denver Water as the wholesaler, and it splits sewer between the city and East Jefferson Sanitation District.",
        """
        <h2>Water</h2>
        <p>The city's right-of-way page says Edgewater Water Utility serves the city, Denver Water treats and delivers the water as wholesaler, and new taps start with Edgewater. New construction or a renovation that touches the water line must put the meter in an outside pit. A duplex needs a separate water line, meter, and sewer for each unit. Existing five-eighths-inch taps must be changed to three-quarter-inch by permit when that rule applies. A right-of-way permit is required for excavation in sidewalks, streets, and alleys, including water and sewer service.</p>
        <h2>Sewer</h2>
        <p>The city says it is served by Edgewater Sewer and by East Jefferson Sanitation District. The city issues sewer permits and taps except inside East Jefferson's area, where you contact that district, and you still need Edgewater's right-of-way permit if you dig in the right of way. Municipal Code 13-3-220, as the page cites it, says a permanent structure proposed over a sanitary service line is inspected, and if the line is clay or in disrepair the owner replaces it with Schedule 40 PVC. That is Edgewater's rule for Edgewater's sewer, not Aurora's and not the district's, until you check the map.</p>
        """,
        [
            ("Who treats Edgewater's drinking water?", "Denver Water, as wholesaler. The city's page says Edgewater Water Utility runs the local system and that new taps start with Edgewater, not with a walk-up to Denver Water. Engineering standards still point at Denver Water. A lead-program question belongs on Denver Water's site only if they confirm the line is in that program."),
            ("Is every sewer the city's?", "No. East Jefferson Sanitation District is the other system. The city tells you to contact that district for work in its area, and to get an Edgewater right-of-way permit anyway if the dig is in the street. Look at the map before you call the wrong crew."),
            ("Can I build over the sewer lateral?", "The page cites code section 13-3-220. A proposed permanent structure over the service line is inspected. If the line is clay or in bad shape, the owner replaces it with Schedule 40 PVC. Ask the city to look before you pour a garage slab."),
        ],
    )


def sheridan(site):
    del site
    return hub(
        "sheridan",
        "Sheridan",
        "plumber Sheridan CO",
        "City of Sheridan",
        "Sheridan requires a building permit for every water heater replacement, and it publishes constraints for closets, combustion air, and tankless vents that Aurora's pages do not.",
        """
        <h2>The permit stays visible</h2>
        <p>The city's water-heater page says every replacement needs a building permit, the permittee leaves it on site visible from the street, and the permittee requests the inspection. Installations must follow the 2021 residential or plumbing code, and the heater must be listed for the place it sits. Fuel-fired replacements are not allowed in storage closets. A heater in a sleeping room or bathroom must be in a sealed enclosure with its own combustion air. A gas heater in a room under 250 square feet needs combustion air. A tankless unit is allowed as a replacement only if the gas piping is large enough and the vent follows the manufacturer. This guide will not repeat those constraints as installation steps. They are the city's conditions. Over-the-counter permits on the applications page include sewer line repairs. Plumbing permits are required for new installations or replacements.</p>
        <h2>Ownership not copied</h2>
        <p>Those pages do not say who owns the lateral under the street. Do not use Aurora or Englewood. Ask Sheridan's utility. The building rules above are already enough to change a <a href="/services/water-heater-replacement/">heater quote</a> and a <a href="/services/tankless-water-heater-installation/">tankless quote</a>.</p>
        """,
        [
            ("Does Sheridan allow a gas water heater in a bedroom closet?", "Not as a storage closet, and not in a sleeping room or bathroom unless it is in a sealed enclosure with its own combustion air. A room under 250 square feet needs combustion air for a gas heater. The city says to call its building department if that is a hardship. This page will not tell you how to build the enclosure."),
            ("Is a tankless heater allowed as a replacement?", "Yes, if the gas piping is adequate and the vent is installed as the manufacturer requires. That is a sizing question for the contractor, not a do-it-yourself worksheet. The permit is still required and must be visible from the street."),
            ("Is a sewer repair over the counter?", "The applications page lists sewer line repairs with over-the-counter permits, paid in full. A new plumbing installation still needs the plumbing permit. Who owns the pipe in the street was not on those pages. Ask the utility before you patch asphalt."),
        ],
    )


def foxfield(site):
    del site
    return hub(
        "foxfield",
        "Foxfield",
        "plumber Foxfield CO",
        "Town of Foxfield",
        "Foxfield is its own town, a few miles from Aurora, and it is not Aurora's permit counter. Water heaters and water or sewer lines are on the town's one-stop list.",
        """
        <h2>One-stop list</h2>
        <p>The town's permit page says no work starts until a permit is approved. One-stop items include a water heater, a water or sewer line, a lawn sprinkler, a furnace, and an air conditioner. The town says it enforces the 2015 international building codes. That date is what the page currently states. Confirm it before you design to a newer book, because the page may lag. Inspections are done by SAFEbuilt, not by Aurora's inspectors. Zoning is Chapter 16 of the town code.</p>
        <h2>Utility not named</h2>
        <p>The permit page does not name a water or sanitation district. A Foxfield address can be easy to confuse with an Aurora water account. Check the bill. A <a href="/services/water-line-repair/">water line</a> or <a href="/services/sewer-line-repair/">sewer line</a> on the one-stop list still needs the district's answer on who owns the pipe in the street. This page will not invent that line.</p>
        """,
        [
            ("Is a Foxfield water heater an Aurora permit?", "No. Foxfield lists water heaters on its own one-stop list, and SAFEbuilt inspects for the town. Aurora's building division does not cover a parcel inside Foxfield. Confirm the town limit. The codes page says the town enforces the 2015 international codes. Verify that edition is still what they want."),
            ("Who provides sewer?", "Not stated on the permit page. Do not assume Aurora Water because the town is nearby. Use the bill, then ask that district who maintains the lateral. The one-stop sewer-line permit is the town's building permit, not the district's ownership map."),
            ("Can I start and permit later?", "The town says no project starts until the permit is approved, and that working without one can mean a fine and a stop-work order. Brighton's next-day emergency exception is Brighton's, not Foxfield's."),
        ],
    )


def bowmar(site):
    del site
    return hub(
        "bow-mar",
        "Bow Mar",
        "plumber Bow Mar CO",
        "Town of Bow Mar",
        "Bow Mar requires permits, and it sends the building review to Columbine Valley's building department. A water heater can be a non-structural permit. Replacing a trap or a drain pipe is not a free pass.",
        """
        <h2>Where you file</h2>
        <p>The town's permit page says applications go to the building department, and that this is handled by Columbine Valley, at 2 Middlefield Road, Columbine Valley, phone 303-795-2063, weekdays 8 a.m. to 4 p.m. A non-structural permit covers interior work that does not need plan review, including water heater replacement, furnace, electrical service, and gas lines. The page also says plumbing repairs to existing drains and pipes do not need a permit until traps, drains, and pipes must be replaced. Replacing the trap is the moment the exemption ends. Read that before you open a cabinet.</p>
        <h2>Not Aurora, and not a guessed utility</h2>
        <p>The page does not name the water or sewer district. Bow Mar is a small town on the edge of Littleton and Denver. Do not assume Littleton's tap rule or Denver's lateral rule until the bill says so. Gas-line work on the non-structural list is still not a do-it-yourself guide. See <a href="/services/gas-line-repair-installation/">gas lines</a> for the boundary only.</p>
        """,
        [
            ("Where do I take a Bow Mar water heater permit?", "To the building department the town says is handled by Columbine Valley, at 2 Middlefield Road, 303-795-2063. A water heater replacement is on the non-structural list. Aurora's counter will not take a Bow Mar parcel. Call before you assume the hours, which the page notes can change."),
            ("Can I replace a leaking trap without a permit?", "The page says plumbing repairs to existing drains and pipes do not need a permit until traps, drains, and pipes must be replaced. Replacing the trap is the permit. A clog that you clear without replacing pipe is a different, smaller job. Ask the department if you are unsure."),
            ("Who owns the sewer?", "Not stated on the permit page. Do not use Littleton's tap sentence or Aurora's. Identify the district from the bill. The building permit and the utility's pipe are separate questions."),
        ],
    )


def columbine(site):
    del site
    return hub(
        "columbine-valley",
        "Columbine Valley",
        "plumber Columbine Valley CO",
        "Town of Columbine Valley",
        "Columbine Valley's building department is the counter Bow Mar uses. The address is 2 Middlefield Road in Columbine Valley. The water and sewer utility is whoever bills the house.",
        """
        <h2>The shared counter</h2>
        <p>Bow Mar's permit page says its building review is handled by Columbine Valley at 2 Middlefield Road, phone 303-795-2063. That places a building department in Columbine Valley that processes at least Bow Mar's permits and, by the same address, is the town's own counter. A water heater, a furnace, and gas-line changes are on Bow Mar's non-structural list filed through that office. Confirm with 303-795-2063 whether a Columbine Valley address uses the same non-structural list or a stricter one. Do not assume the exemption for minor drain repairs applies inside Columbine Valley until the town says so.</p>
        <h2>Utility</h2>
        <p>No water or sanitation district was named on the Bow Mar page. Columbine Valley is not Littleton and not Denver, even when the mail is confusing. Ask the bill. A street excavation may be a different agency from the building permit. <a href="/areas/bow-mar/">Bow Mar</a> is the neighbor that shares this counter. <a href="/areas/littleton/">Littleton</a> has its own sewer code if the parcel is actually in Littleton.</p>
        """,
        [
            ("Is the Columbine Valley building counter the same as Bow Mar's?", "Bow Mar says its permits are handled by Columbine Valley at 2 Middlefield Road, 303-795-2063. Use that office and ask whether your Columbine Valley address is on the same non-structural list as a Bow Mar water heater. Do not file in Aurora or Littleton until the parcel is checked."),
            ("Does the minor-repair exemption apply?", "Bow Mar's page says drain and pipe repairs need a permit when the trap, drain, or pipe is replaced. That sentence is Bow Mar's. Ask Columbine Valley before you rely on it for a house inside Columbine Valley. Replacing a trap is the line they drew for Bow Mar."),
            ("Who provides water?", "Not stated on the page that identified the building counter. Do not guess Denver Water or a sanitation district. The bill is the source. Ownership of a lateral is a separate question this page will not invent."),
        ],
    )


def cherryhills(site):
    del site
    return hub(
        "cherry-hills-village",
        "Cherry Hills Village",
        "plumber Cherry Hills Village CO",
        "City of Cherry Hills Village",
        "Cherry Hills Village permits online, and its sanitation district is not the same thing as the city. Some sewer cuts are also inspected by Englewood. A few subdivisions are the exception.",
        """
        <h2>City permits</h2>
        <p>The city processes permits in an online portal. First-time registration can take up to one business day to approve. Plumbing and HVAC can ride on the main building permit when they are part of that scope. Otherwise they need their own permit. Additions may need a right-of-way construction access permit. Public Works is 303-783-2744. Additions on homes that already have fire sprinklers must extend that protection, with a South Metro Fire Rescue permit. Homes without sprinklers may need a fire-flow analysis. That is a water-supply question for the district, not a faucet repair.</p>
        <h2>Sanitation district</h2>
        <p>Cherry Hills Village Sanitation District requires a sewer tap permit for a new property or a property leaving a septic tank, and an inspection. A demolition cut-off needs a video of the service line, paint and flags on the surface, and a cut at the property line or the main unless the district approves another point. Some new taps are also inspected by the City of Englewood. Buell Mansion and Covington do not require Englewood's inspection. The district says its regulations win if a summary conflicts. Call the district about whether a residential repair needs a permit. Do not treat this as Aurora Water.</p>
        """,
        [
            ("Does a Cherry Hills sewer repair involve Englewood?", "Sometimes. The sanitation district says inspection of a new tap or a change is by the district and by the City of Englewood, except Buell Mansion and Covington. A cut-off for demolition needs a video first. Ask the district which inspection your block uses before you schedule one crew."),
            ("Is the sanitation district the city building department?", "No. The city runs the online building portal and may require a right-of-way permit through Public Works at 303-783-2744. The district permits taps and some repairs. You can need both. Aurora's wastewater page is a third agency and the wrong one."),
            ("Do I need a fire-flow study to add a bathroom?", "You might. The city says additions to homes without sprinklers submit a fire-flow analysis to South Metro Fire Rescue, and additions to homes with sprinklers must extend that system. That can force a water-main or meter conversation with the district. Ask before you frame."),
        ],
    )


def adams_place(slug, name, keyword, extra):
    def _fn(site):
        del site
        return hub(
            slug,
            name,
            keyword,
            extra.get("eyebrow", "Check the parcel, not the postal name"),
            extra["lede"],
            extra["body"],
            extra["pairs"],
        )
    return _fn


def watkins(site):
    del site
    return hub(
        "watkins",
        "Watkins",
        "plumber Watkins CO",
        "Adams County and Arapahoe County",
        "Watkins is a census-designated place in both Adams County and Arapahoe County. It is not a city, and a Watkins mailing address is not a permit jurisdiction.",
        """
        <h2>The name on the mail is not the parcel</h2>
        <p>The Census Bureau's place list records Watkins CDP in Adams County and Arapahoe County. That outline is a statistical area. It is not ZIP code 80137, and it is not every house that receives Watkins mail. An address can sit in unincorporated Adams County, unincorporated Arapahoe County, or inside a city. Aurora's building division applies only when the parcel is inside Aurora. There is no Watkins city hall.</p>
        <h2>Which counter, after the parcel is checked</h2>
        <p>If the parcel is unincorporated Adams County, Adams County requires a permit to install or replace a water heater, to modify plumbing, or to run a gas line. Building Safety is 720-523-6800, through the county ePermit center. If the parcel is unincorporated Arapahoe County, Arapahoe County Building applies. A water heater that is not tankless can be issued when you pay. A tankless heater is a reviewed remodel, with a gas-pipe isometric and the manufacturer's instructions. The phone on those residential instructions is 303-795-4400, at 5334 South Prince Street in Littleton. That is the county office. It does not mean the house is in Littleton. The same filing split is on the <a href="/areas/cherry-creek/">Cherry Creek CDP</a> page because that place is also unincorporated Arapahoe land.</p>
        <h2>The utility is separate</h2>
        <p>Neither county's permit list names a Watkins water or sewer district. The bill, a well, or a septic system tells you who is responsible for the pipe. Responsibility varies by utility. Confirm the district before you authorize work in the street. A building permit is permission to do the plumbing. It is not a map of who owns the main. <a href="/areas/byers/">Byers</a> is a different census place, in Arapahoe County, and it is not this page.</p>
        """,
        [
            ("Who permits a water heater at a Watkins address?", "Whoever has the parcel. Census lists the Watkins census place in Adams County and Arapahoe County, and a Watkins ZIP can also fall inside a city. Unincorporated Adams uses Building Safety at 720-523-6800. Unincorporated Arapahoe uses the county building division at 303-795-4400. Aurora permits the job only when the parcel is inside Aurora."),
            ("Is Watkins a city?", "No. It is an unincorporated census place, not a municipal building department. The name on the mail does not choose Adams County, Arapahoe County, or Aurora. Look up the parcel, then file with that government. A contractor who picks the nearest counter because the drive is short can file in the wrong county."),
            ("Who owns the sewer?", "The permit instructions do not say. A district, a well, or a septic system may serve the lot, and neighboring houses need not match. Confirm the utility on the bill before you authorize a street repair. A house permit covers the work you are allowed to do. It does not decide who maintains the main."),
        ],
    )


def bennett(site):
    return adams_place(
        "bennett",
        "Bennett",
        "plumber Bennett CO",
        {
            "eyebrow": "Town of Bennett, two counties",
            "lede": "Bennett is an incorporated town that Census lists in both Adams County and Arapahoe County. A Bennett mailing address may be inside the town or outside it. The county is not the same on every parcel.",
            "body": """
            <h2>Town first, then the county</h2>
            <p>Ask the Town of Bennett whether this address is inside the town limits before you use a county form. Inside the town, the town is the building authority. This page describes the county rules for land that is not inside a city or town. It is not a Town of Bennett checklist. If the parcel is unincorporated Adams County, Adams County requires a permit to replace a water heater, modify plumbing, or run gas piping. Building Safety is 720-523-6800. If the parcel is unincorporated Arapahoe County, Arapahoe County Building applies, at 303-795-4400. A Bennett ZIP does not choose between those offices, and it does not make the house Aurora.</p>
            <h2>The utility is on the bill</h2>
            <p>The county permit lists do not name a Bennett water or sewer district. Confirm the bill, the well, or the septic system before you price a pump or a service line. Responsibility varies by utility. Aurora Water's backup line applies to Aurora Water customers, not to a Bennett address because the town is nearby.</p>
            """,
            "pairs": [
                ("Is my Bennett address in the town?", "Not necessarily. Census lists the incorporated town in both Adams County and Arapahoe County, and mail can fall outside the town. Ask the town first. Unincorporated Adams uses Building Safety at 720-523-6800. Unincorporated Arapahoe uses 303-795-4400. The ZIP code is not that answer."),
                ("Does the county permit a water heater?", "Yes, on unincorporated land. Adams County lists water heater installation or replacement, plumbing modifications, and gas lines. Arapahoe County issues a non-tankless heater when you pay and reviews a tankless heater as a remodel. Neither list is the town's ordinance. Leave the work open for inspection."),
                ("Should I price a well pump?", "Only after you confirm there is no water district. The county permit pages do not say Bennett houses are on wells. Check the bill. A metered account is a service-line repair, not a pump in a casing."),
            ],
        },
    )(site)


def strasburg(site):
    return adams_place(
        "strasburg",
        "Strasburg",
        "plumber Strasburg CO",
        {
            "eyebrow": "Adams County and Arapahoe County",
            "lede": "Strasburg is a census-designated place in both Adams County and Arapahoe County. It is not a city. The ZIP code does not pick the county or the permit office.",
            "body": """
            <h2>Two counties, one postal name</h2>
            <p>The Census Bureau's place list records Strasburg CDP in Adams County and Arapahoe County. The census place is not the ZIP code, and a Strasburg mailing address can fall outside that outline. If the parcel is unincorporated Adams County, Adams County requires permits for water heater replacement, plumbing changes, and gas lines. Building Safety is 720-523-6800. If the parcel is unincorporated Arapahoe County, use Arapahoe County Building at 303-795-4400. A non-tankless water heater there can be issued when you pay. A tankless heater is a reviewed remodel. Aurora permits the job only when the parcel is inside Aurora.</p>
            <h2>Water source</h2>
            <p>Those permit lists do not name a Strasburg water or sewer district. Ask whether the house is on a district main, a well, or a septic system before you order parts. <a href="/services/water-heater-replacement/">Heater replacement</a> follows the county that has the parcel. Responsibility for the pipe varies by utility. Confirm the bill before you authorize street work. Distance from Aurora is not an Aurora Water account.</p>
            """,
            "pairs": [
                ("Which building department is Strasburg?", "The government that contains the parcel. Census lists the Strasburg census place in Adams County and Arapahoe County, and the place is not a city. Unincorporated Adams uses 720-523-6800. Unincorporated Arapahoe uses 303-795-4400. A Strasburg ZIP is not that choice. Confirm the parcel before you pay a fee."),
                ("Does Aurora Water apply?", "Only if the bill says so. Proximity is not an account. A sewer backup number for Aurora is the wrong desk for a Strasburg district or a septic system. Identify the provider first."),
                ("Are gas lines permitted?", "On unincorporated land, plan on a permit. Adams County lists gas lines with work that needs one. In unincorporated Arapahoe, a new gas line is outside the non-review appliance permit. Neither sentence is a how-to. If you smell gas, leave and call the gas utility."),
            ],
        },
    )(site)


def byers(site):
    del site
    return hub(
        "byers",
        "Byers",
        "plumber Byers CO",
        "Arapahoe County",
        "The Byers census place is in Arapahoe County, not Adams County. A Byers mailing address still has to be checked parcel by parcel before anyone files a permit.",
        """
        <h2>What the census place is</h2>
        <p>The Census Bureau's place list records Byers CDP in Arapahoe County. Arapahoe County's Byers Subarea Plan treats the community as unincorporated Arapahoe County and sets its planning area on that census-place boundary. Byers has no town building department. That does not mean every 80103 address is inside the census place. An address outside the place uses the county or city that actually contains the parcel. Do not send a Byers address to Adams County Building Safety because a neighboring community is in Adams County. <a href="/areas/watkins/">Watkins</a> is that different case: its census place is in both counties.</p>
        <h2>Permits, when the parcel is unincorporated Arapahoe</h2>
        <p>Arapahoe County Building says its services are for unincorporated Arapahoe County and tells applicants to check jurisdiction first. A water heater that is not tankless can be a non-review permit issued when you pay. A tankless heater is a residential remodel: a gas-pipe isometric, the manufacturer's instructions, and a review before issuance. The phone on the county's residential requirements page is 303-795-4400. The office address printed there is 5334 South Prince Street, Littleton. Littleton is where the counter sits. It is not the city the house is in. The same filing split is on the <a href="/areas/cherry-creek/">Cherry Creek CDP</a> page.</p>
        <h2>Water and sewer</h2>
        <p>Those building instructions do not name a Byers water district, and they do not say that every lot is on a well or a septic system. Confirm the bill, the well, or the septic record before you price a <a href="/services/water-line-repair/">service line</a> or a <a href="/services/well-pump-repair/">well pump</a>. Responsibility varies by utility. Aurora's wastewater rules apply to Aurora Water customers, not to a plains address because it is east of the city.</p>
        """,
        [
            ("Who permits a Byers water heater?", "Arapahoe County, when the parcel is unincorporated Arapahoe County. The census place is in that county. The building division's number on its residential page is 303-795-4400. A non-tankless heater can be issued when you pay. Tankless is a reviewed remodel. If the parcel is outside the census place, use the county or city that contains it."),
            ("Is the sewer a city main?", "Not by default. Byers is unincorporated, and the lot may be on a district or a septic system. The building instructions do not pick one. Confirm the bill before you camera a main that may not be there. A septic backup is not an Aurora Water call."),
            ("Do I need a permit to change plumbing?", "On unincorporated Arapahoe land, plan on a county permit when you replace pipe. A clog that replaces nothing can be different from opening a wall. The non-review path is for a like-for-like heater, not for a new gas line. Call 303-795-4400 if the application type is unclear."),
        ],
    )


def elizabeth(site):
    del site
    return hub(
        "elizabeth",
        "Elizabeth",
        "plumber Elizabeth CO",
        "Town of Elizabeth, not the whole ZIP",
        "The Town of Elizabeth permits only inside town limits. The town says many Elizabeth addresses are outside those limits and belong to Elbert County. Call before you apply.",
        """
        <h2>Town versus county</h2>
        <p>The town's building page says it issues permits only inside municipal limits, that SAFEbuilt helps with review and inspections, and that an address outside town must go to Elbert County. The town asks you to call 303-646-4166 extension 4 or email the permits desk to verify the limit before you apply. The town says it is on the 2018 international building code and the 2023 national electrical code. A permit is required for any structure over 200 square feet, anything attached to the main structure, or any work that involves electrical, plumbing, or mechanical systems, regardless of size. The town does not require contractor licensing to pull a permit. Work without a permit is described as a doubled fee. Elbert County permits unincorporated land and says plans must meet 2018 I-codes and Elbert County design criteria, including snow and wind. A plan set labeled for another county can be rejected.</p>
        <h2>Taps</h2>
        <p>The town publishes water and sewer tap fees for new service, adjusted by resolution, effective January 1, 2026. This guide does not repeat the dollar amounts. A repair of an existing <a href="/services/water-line-repair/">water line</a> is not a new tap. Confirm you are inside town before you pay a town tap fee. Aurora is not the permit authority on either side of the Elizabeth limit.</p>
        """,
        [
            ("My mail says Elizabeth. Is the permit the town's?", "Not always. The town says many Elizabeth addresses are outside town limits and must use Elbert County. Call 303-646-4166 extension 4 before you apply. SAFEbuilt works for the town. The county is a different portal. Aurora is neither."),
            ("Does a small plumbing job need a permit?", "The town says yes when electrical, plumbing, or mechanical systems are involved, even if the structure is small. That is broader than a 200-square-foot shed test. Elbert County has its own list for unincorporated land. Ask the office that has the parcel."),
            ("Is a tap fee a repair bill?", "No. The town publishes tap fees for new water and sewer service. Fixing a leak on an existing line is not that fee. Confirm the address is inside town before anyone quotes a town tap. This page does not print the dollar amounts."),
        ],
    )


def arap_cdp(slug, name, keyword, mistake):
    def _fn(site):
        del site
        return hub(
            slug,
            name,
            keyword,
            "Unincorporated Arapahoe County",
            mistake,
            """
            <h2>Tank versus tankless at the county</h2>
            <p>Arapahoe County's residential permit instructions, for unincorporated land, let you file a non-review water heater that is not tankless. The county says that permit is issued when you pay. A tankless water heater is filed as a residential remodel. You attach a gas-pipe isometric and the manufacturer's instructions, and a plans reviewer checks the application before it is issued. The county's page also says its 2021 code criteria took effect April 1, 2022, and that the website was being updated. Confirm the current code before you rely on an old detail sheet. This is not Aurora's same-day inspection program, and it is not Denver's quick permit.</p>
            <h2>You are not in Aurora or in Denver's Cherry Creek</h2>
            <p>This place is a census area, not a city. Aurora Water's tap rule applies to Aurora Water customers, not to every nearby ZIP. Denver's lateral rule applies in Denver. If the parcel is unincorporated Arapahoe County, the county is the building department. Water and sewer may be a district. The county instructions for a bedroom addition on a septic system ask for a certificate of sewer availability. Ask which system you have before you camera the wrong pipe.</p>
            """,
            [
                (f"Is a tankless heater a simple permit in {name}?", "Not if the parcel is unincorporated Arapahoe County. The county files a non-tankless water heater as a non-review permit issued on payment. Tankless is a remodel: gas-pipe isometric, manufacturer instructions, and a reviewer before issuance. Confirm the parcel is actually in the county, not in Aurora or Denver."),
                (f"Is {name} the same as a Denver neighborhood?", "No. This is a census-designated place with its own geography. Denver's Cherry Creek neighborhood is inside Denver and uses Denver's permits. Aurora is a third jurisdiction. The mailing city on a letter does not decide. The parcel does."),
                ("Who owns the sewer lateral?", "Not answered by the county's heater instructions. A district, a city, or a septic system may serve the lot. Do not borrow Aurora's tap rule. Get the provider from the bill or the county's sewer-availability step if you are adding a bedroom on septic."),
            ],
        )
    return _fn


def cherry_creek(site):
    return arap_cdp(
        "cherry-creek",
        "Cherry Creek",
        "plumber Cherry Creek CO",
        "Cherry Creek CDP is unincorporated Arapahoe County. It is not Denver's Cherry Creek neighborhood and not the City of Aurora.",
    )(site)


def four_square(site):
    return arap_cdp(
        "four-square-mile",
        "Four Square Mile",
        "plumber Four Square Mile CO",
        "Four Square Mile is a census-designated place in unincorporated Arapahoe County, pressed against Aurora. It does not have a city building department.",
    )(site)


def douglas_cdp(slug, name, keyword, trap):
    def _fn(site):
        del site
        return hub(
            slug,
            name,
            keyword,
            "Unincorporated Douglas County",
            trap,
            f"""
            <h2>County building division</h2>
            <p>Douglas County issues building permits for unincorporated areas. The Building Division is at 100 Third Street in Castle Rock, phone 303-660-7497, which is easy to confuse with the Town of Castle Rock's own counter. Contractors who apply must be registered with the county. The owner must verify water, sewer, well, septic, and other utilities before digging. Applications received after 4 p.m. are post-dated to the next business day. A water heater here is a county mechanical or plumbing permit until the county says otherwise. It is not <a href="/areas/castle-rock/tankless-water-heater-installation/">Castle Rock's tankless packet</a> unless the parcel is inside the town.</p>
            <h2>Do not assume a city utility</h2>
            <p>{name} is not a city. A private well, a district, or a sanitation district may serve the lot. The county will not let you skip that check. <a href="/guides/well-pump-vs-city-water/">Well versus city water</a> is the fork. Aurora Water's sewer rule is for Aurora. Parker town permits are for incorporated Parker. Use the county if the assessor says unincorporated Douglas County.</p>
            """,
            [
                (f"Is {name} permitted by Castle Rock?", "Only if the parcel is inside the Town of Castle Rock. The county's building office is in Castle Rock's downtown, at 100 Third Street, which confuses people. Unincorporated land uses Douglas County, 303-660-7497. Ask the county to confirm the parcel before you follow the town's tankless sheet."),
                (f"Does every house in {name} have a well?", "No. The county says you must verify whether you have a well, a district, a sewer, or a septic system before you dig. Some lots are on districts. Some are on wells. A pump quote for a metered house is the wrong equipment."),
                ("When does the county date my application?", "Applications after 4 p.m. are post-dated to the next business day. That is a filing fact, not an inspection promise. Dumpsters go on the property or the driveway, not on a public road, under the same county page."),
            ],
        )
    return _fn


def franktown(site):
    del site
    return hub(
        "franktown",
        "Franktown",
        "plumber Franktown CO",
        "Douglas County",
        "Franktown is a census-designated place in Douglas County. It is not a town, and it is not on Pinery Water's published list of communities.",
        """
        <h2>Permits follow the parcel</h2>
        <p>If the parcel is unincorporated Douglas County, the Building Division is at 100 Third Street in Castle Rock, phone 303-660-7497. That office sits in Castle Rock and is not the Town of Castle Rock's permit desk. The county expects the owner to verify water, sewer, well, and septic before digging. Applications after 4 p.m. are dated the next business day. A house inside Castle Rock, Parker, or another city uses that city instead. A Franktown mailing address is not that proof.</p>
        <h2>Water</h2>
        <p>Franktown has no town water utility. <a href="/areas/the-pinery/">Pinery Water</a> publishes the communities it serves, and Franktown is not on that list. Douglas County's water-provider map shows many other districts across the county. A Franktown address may be a well, a small district, or another provider. The bill or the well record decides. Do not assign Parker Water or Aurora Water because those systems are down the highway. <a href="/areas/sedalia/">Sedalia</a>, <a href="/areas/stonegate/">Stonegate</a>, <a href="/areas/meridian/">Meridian</a>, and <a href="/areas/roxborough-park/">Roxborough Park</a> each have their own district to check. Sharing a county permit office does not make them the same water system.</p>
        """,
        [
            ("Who permits a Franktown water heater?", "Douglas County, if the parcel is unincorporated, at 303-660-7497. The office is in Castle Rock and is still the county, not the town. If the parcel is inside a city, use that city. A Franktown mailing address is not the parcel check."),
            ("Is Franktown on Pinery Water?", "Not on the community list Pinery Water publishes. That list names the Pinery and several neighboring developments, not Franktown. Read the bill. A well is possible. A district is possible. Neither is guaranteed by the census name."),
            ("Does Castle Rock's tankless packet apply?", "Only inside the Town of Castle Rock. An unincorporated Franktown parcel uses the county. The town's manufacturer sheet and gas-load calculations are the town's requirement, not a county-wide form."),
        ],
    )


def sedalia(site):
    del site
    return hub(
        "sedalia",
        "Sedalia",
        "plumber Sedalia CO",
        "Douglas County",
        "Sedalia is a census-designated place in Douglas County. Sedalia Water and Sanitation District says its primary service is water. That district is not the whole census place, and it is not The Pinery.",
        """
        <h2>A water district with a limited claim</h2>
        <p>Sedalia Water and Sanitation District describes itself as a Title 32 special district whose primary service is water. The phone on its site is 303-688-2506, and the mailing address is PO Box 222, Sedalia. That is the district's own description. It does not say every house in the Sedalia census place is a customer, and the homepage does not claim sewer service for the whole place. If the bill is this district, call the district about the water line. If the bill is someone else, or the house is on a well, use that record instead.</p>
        <h2>The building permit is still the county, when the land is unincorporated</h2>
        <p>Census lists Sedalia CDP in Douglas County. If the parcel is unincorporated, Douglas County Building is at 100 Third Street, Castle Rock, 303-660-7497. That counter is not the Town of Castle Rock, and a Sedalia address is not <a href="/areas/the-pinery/">Pinery Water</a>. Confirm the utility before you authorize work in the street. Responsibility varies by utility.</p>
        """,
        [
            ("Does Sedalia Water serve every Sedalia address?", "No. The district says its primary service is water for its customers. The census place is larger than a sentence on a homepage. Read the bill. A well or another district is still possible. The phone on the district site is 303-688-2506."),
            ("Who permits a water heater?", "Douglas County, if the parcel is unincorporated, at 303-660-7497. The office address in Castle Rock does not make it a Town of Castle Rock permit. The water district does not issue the building permit. Ask the county to confirm the parcel."),
            ("Is the sewer the same district?", "Not established by the district's statement that water is its primary service. Do not assume a sewer main. Confirm wastewater the same way you confirm drinking water, from the bill or a septic record, before a camera crew is sent to a city main."),
        ],
    )


def pinery(site):
    del site
    return hub(
        "the-pinery",
        "The Pinery",
        "plumber The Pinery CO",
        "Douglas County",
        "The Pinery is its own census place and its own water district. It is not a label for Franktown, Sedalia, Stonegate, Meridian, or Roxborough Park.",
        """
        <h2>Pinery Water's own list</h2>
        <p>Pinery Water and Wastewater District, which began as Denver Southeast Suburban Water and Sanitation District, says it serves the Pinery, Timbers, Misty Pines, Pinery Glen, High Prairie Farms, Pradera, Vistancia, and Colorado Golf Club. The office is 5242 Old Schoolhouse Road, Parker, phone 303-841-2797. That list is the district's. It is not the census boundary, and a Parker mailing address is not the Town of Parker. The district's water-quality page reports average hardness of 210 milligrams per liter and says the district does not treat for hardness. That figure describes the district's supply. It is not a test of your tap and not a reason, by itself, to buy a softener.</p>
        <h2>Building permits</h2>
        <p>If the parcel is unincorporated Douglas County, the building permit goes to Douglas County at 100 Third Street, Castle Rock, 303-660-7497. That is not Castle Rock's <a href="/areas/castle-rock/tankless-water-heater-installation/">tankless packet</a> and not the Town of Parker's counter. Franktown is not on Pinery Water's community list. Use the <a href="/areas/franktown/">Franktown</a>, <a href="/areas/sedalia/">Sedalia</a>, <a href="/areas/stonegate/">Stonegate</a>, <a href="/areas/meridian/">Meridian</a>, and <a href="/areas/roxborough-park/">Roxborough Park</a> pages for those places. Confirm the bill before you authorize work on a line in the street.</p>
        """,
        [
            ("Is my house a Pinery Water customer because the area is called The Pinery?", "Only if the district serves that parcel. Pinery Water names the Pinery and seven other communities. A nearby census place is not on that list. The office is 303-841-2797 in Parker. The Parker mailing city is not the Town of Parker's building department."),
            ("Who permits a water heater?", "Douglas County, if the parcel is unincorporated, at 303-660-7497. The office is in Castle Rock and is still the county. Inside the Town of Castle Rock, the town's tankless rules apply instead. Confirm the parcel before you prepare a gas-load sheet."),
            ("Does the district's hardness number mean I need a softener?", "No. The district reports 210 milligrams per liter as the average hardness of its supply and says it does not treat for hardness. That is not a test at your faucet. A filter or a softener is a separate decision after a test of the water you actually use."),
        ],
    )


def stonegate(site):
    del site
    return hub(
        "stonegate",
        "Stonegate",
        "plumber Stonegate CO",
        "Douglas County",
        "Stonegate Village Metropolitan District provides water and wastewater inside its own boundaries. The Stonegate census place, a Parker mailing address, and the Town of Parker are three different things.",
        """
        <h2>The district, not the ZIP code</h2>
        <p>Stonegate Village Metropolitan District says it is about 639 acres in unincorporated Douglas County and that it provides potable water and wastewater inside its boundaries. It also says it provides potable water and sewer to some properties in the Lincoln Park, E-470 Potomac, and Compark districts. The office is 10252 Stonegate Parkway, Parker, phone 303-858-9909. Read the bill. A house near Stonegate is not a customer because the subdivision is nearby, and a house in one of those other districts is a customer only if the district says so.</p>
        <h2>Parker on the envelope is not the Town of Parker</h2>
        <p>Census lists Stonegate CDP in Douglas County. If the parcel is unincorporated, the building permit is Douglas County at 100 Third Street, Castle Rock, 303-660-7497, not the Town of Parker and not <a href="/areas/the-pinery/">Pinery Water</a>. The Town of Parker permits inside Parker. Confirm the parcel and the utility before you authorize a street repair. Responsibility varies by utility.</p>
        """,
        [
            ("Does Stonegate Village Metro serve every Stonegate address?", "No. The district describes about 639 acres and also some properties in Lincoln Park, E-470 Potomac, and Compark. The census place is not that legal boundary. The bill, or a call to 303-858-9909, is the check. A Parker ZIP does not settle it."),
            ("Who permits a water heater?", "Douglas County, if the parcel is unincorporated, at 303-660-7497. The Town of Parker permits inside Parker only. The district supplies water and wastewater. It is not the building department. Confirm which parcel you are on before the application is filed."),
            ("Is this the same system as The Pinery?", "No. Pinery Water publishes a different community list and a different office. Stonegate Village Metropolitan District publishes its own boundaries and its own phone. Sharing Douglas County's building counter does not make the pipes the same."),
        ],
    )


def meridian(site):
    del site
    return hub(
        "meridian",
        "Meridian",
        "plumber Meridian CO",
        "Douglas County",
        "Meridian Metropolitan District provides drinking water, wastewater, and reclaimed irrigation water to its customers. A Meridian address is not automatically that district, and it is not the City of Lone Tree.",
        """
        <h2>What the district says it provides</h2>
        <p>Meridian Metropolitan District's water page says it provides drinking water, wastewater, and reclaimed water for irrigation. The phone on that page is 303-790-0345. The office address printed there is 12111 East Belford Avenue, Englewood. That is the district office. It does not mean the house is in Englewood, and it does not mean Lone Tree's building division takes the permit. The district boundary is the account, not the word Meridian on a map.</p>
        <h2>Building permits</h2>
        <p>Census lists Meridian CDP in Douglas County. If the parcel is unincorporated, Douglas County Building is at 100 Third Street, Castle Rock, 303-660-7497. Lone Tree permits land inside Lone Tree. Englewood permits land inside Englewood. <a href="/areas/the-pinery/">Pinery Water</a> is a different district. Confirm the bill before you authorize work on a line in the street. Responsibility varies by utility. This page does not copy the district's rate table.</p>
        """,
        [
            ("Is every Meridian address a Meridian Metropolitan District customer?", "No. The district describes the services it provides to its customers. The census place and a marketing name can be wider than the legal boundary. Check the bill or call 303-790-0345. An Englewood office address is the district's office, not your city."),
            ("Who permits a water heater?", "Douglas County, if the parcel is unincorporated, at 303-660-7497. Lone Tree's building division applies inside Lone Tree. Englewood applies inside Englewood. The water district does not replace that permit. Confirm the parcel before you file."),
            ("Does the district handle irrigation as well as sewer?", "For its customers, the district says it provides drinking water, wastewater, and reclaimed water for irrigation. Reclaimed irrigation is not the drinking-water line and not a sump pump. Ask which system the quote is opening before work starts."),
        ],
    )


def roxborough(site):
    del site
    return hub(
        "roxborough-park",
        "Roxborough Park",
        "plumber Roxborough Park CO",
        "Douglas County",
        "Roxborough Park is a census-designated place in Douglas County. Roxborough Water and Sanitation District does not provide the same service in every part of its area, and a Littleton mailing address is not the City of Littleton.",
        """
        <h2>One district, more than one kind of service</h2>
        <p>Roxborough Water and Sanitation District, at 6222 North Roxborough Park Road, Littleton, phone 303-979-7286, says its central service area, the Roxborough development, receives both water and sewer. Its east area is water only, including Chatfield East, Chatfield Acres, Titan Road Industrial Park, and Plum Valley Heights. Its west area at Lockheed Martin is sewer only. A Roxborough address is not automatically the central area. Ask the district which service, if any, the parcel has before you price a sewer repair that the district may not provide there.</p>
        <h2>County, city, and ZIP code</h2>
        <p>Census lists Roxborough Park CDP in Douglas County. If the parcel is unincorporated, the building permit is Douglas County at 100 Third Street, Castle Rock, 303-660-7497. Jefferson County's forms apply only when the parcel is in Jefferson County. The Littleton street address is the district office and a common ZIP code. It is not the City of Littleton's building department, and it is not <a href="/areas/the-pinery/">Pinery Water</a>. Confirm the utility before you authorize work in the street.</p>
        """,
        [
            ("Does Roxborough Water provide sewer at every Roxborough address?", "No. The district says the central area gets water and sewer, the east area is water only, and the Lockheed Martin area is sewer only. Call 303-979-7286 and ask which area the parcel is in. A sewer quote for a water-only account is the wrong job."),
            ("Who permits a water heater?", "Douglas County, if the parcel is unincorporated, at 303-660-7497. A Littleton ZIP does not make it the City of Littleton. Jefferson County applies only if the parcel is in Jefferson County. The water district is not the building department."),
            ("Is Roxborough Park the same as The Pinery?", "No. They are different census places and different districts. Pinery Water lists its own communities and office. Roxborough Water describes central, east, and west service that do not match. Douglas County's building counter can be the same only when both parcels are unincorporated Douglas County."),
        ],
    )


def golden(site):
    del site
    return hub(
        "golden",
        "Golden",
        "plumber Golden CO",
        "City of Golden",
        "Golden requires a permit to install or replace a water heater, to modify plumbing, to run gas piping, and to repair or replace a water or sewer utility line. Confirm the address is inside the city before you apply.",
        """
        <h2>What the permit guide lists</h2>
        <p>The city's required-permits guide lists water heater installation or replacement, plumbing modifications, gas piping, and water or sewer utility repair or replacement. Replacing a plumbing fixture in the same location is on the no-permit list. Work in the city right of way needs a separate right-of-way permit. The building division contact published with permit instructions is (303) 384-8151, building@cityofgolden.net, 1445 10th Street. Another city contact block shows (303) 384-8000 at 911 10th Street. Use the building-division line for a plumbing permit, and use the city's address lookup before you file. The permit portal says to check the Jefferson County address tool and confirm the municipal status says Golden. If the status is unincorporated Jefferson County, the city sends you to Jefferson County Building Safety. That is the same county counter used for <a href="/areas/evergreen/">Evergreen</a>, not for a house inside Golden.</p>
        <h2>Codes and inspections, without a pipe-ownership claim</h2>
        <p>The permit portal text says the city has adopted the 2024 residential and building codes and the 2023 electrical code. A separate city page has listed 2021 codes. Ask the building division which set applies to this permit. Do not pick one from this website. Inspection requests made before 4 p.m. can be the next business day, and the city also lets you book up to 15 business days ahead. There is no appointment window. The city describes north and central Golden in the morning and south Golden in the afternoon. A contractor must be licensed with Golden and named on the permit before it is issued.</p>
        <p>A right-of-way application is generally due three working days before the work, unless the city has approved an emergency sewer or water repair. That timing is about occupying the street. It does not say whether the owner or the city maintains the sewer lateral. Responsibility varies by utility. Confirm Golden's utility for this address before you authorize work under the asphalt. Edgewater's clay-pipe rule is Edgewater's.</p>
        """,
        [
            ("Does Golden require a permit for a replacement water heater?", "Yes. The required-permits guide lists water heater installation or replacement, and it lists plumbing modifications separately. Swapping a fixture in the same place is on the no-permit list. Gas piping and a water or sewer utility repair are on the permit list. Call the building division at (303) 384-8151 if the job sits between those lines."),
            ("How do I know the house is in Golden?", "The city's permit portal says to use the Jefferson County address lookup and check that the municipal status says Golden. If it says unincorporated Jefferson County, Golden tells you to use the county building division. A Golden mailing address is not that status. Aurora's counter is the wrong third office."),
            ("Who owns the sewer lateral?", "Not stated on the permit guide or the inspection page that were read. Do not invent a curb line. Right-of-way work needs the city's right-of-way permit, including a street cut. Ask Golden's utility for the address before the quote assigns the pipe under the asphalt."),
        ],
    )


def morrison(site):
    del site
    return hub(
        "morrison",
        "Morrison",
        "plumber Morrison CO",
        "Town of Morrison",
        "Morrison contracts building review and inspections to Charles Abbott Associates. Ask the town whether the address is inside town limits before you file. No service-line ownership rule was on the pages that were read.",
        """
        <h2>Where the permit goes</h2>
        <p>The town's building department page, morrisonco.us/140/Building-Department, says Charles Abbott Associates enforces the town's codes for residential and commercial properties. Inspection requests must be in by 4:00 p.m. the business day before. The building contact on that page is building@morrisonco.us, with a physical office listed at 4704 Harlan Street, Suite 684, Lakeside. Town hall is 321 Highway 8, Morrison, phone 303-697-8749, weekdays 8:30 a.m. to 4:30 p.m. A staff directory on the town's other site lists an inspection line at 303-450-8748. Use the building email and town hall phone to confirm which line schedules a plumbing inspection. An earlier guess at town.morrison.co.us/building-department returned 404. This is the page that replaced it.</p>
        <h2>Floodplain, the street, and what is not claimed</h2>
        <p>The same page lists a floodplain permit checklist and a permit for work in the public right of way, plus residential and commercial plan checklists. Morrison sits in a narrow valley. If the work is in a mapped floodplain, that checklist is a separate application. The pages do not say who owns a sewer lateral or a water service. Do not borrow Golden, Evergreen, or Aurora. JeffCom's non-emergency number is printed on the town page. It is not a sewer crew, and it is not Lakewood's after-hours utility line even though the digits match a Lakewood number. Confirm you are inside the town. Nearby unincorporated Jefferson County uses the county counter described on the <a href="/areas/evergreen/">Evergreen</a> page.</p>
        """,
        [
            ("Who reviews a Morrison building permit?", "Charles Abbott Associates, under contract with the town, according to morrisonco.us. Inspection requests are due by 4:00 p.m. the business day before. Town hall is 321 Highway 8, 303-697-8749. The building contact email is building@morrisonco.us. Confirm whether your address is inside town limits before you apply."),
            ("Does Morrison publish a water-heater permit list?", "The building department page does not list water heaters by name. Residential and commercial plan checklists are linked. Ask the town whether a replacement heater needs the full residential checklist or a smaller permit. Golden's list and Sheridan's closet rules are those cities' rules."),
            ("Who fixes a sewer line under the street?", "Morrison's building page does not say who owns the pipe. The town does publish a right-of-way permit for work in the public street. That is permission to occupy the street. Ask the utility on the bill before you authorize the repair. Responsibility varies by utility."),
        ],
    )


def evergreen(site):
    del site
    return hub(
        "evergreen",
        "Evergreen",
        "plumber Evergreen CO",
        "Unincorporated Jefferson County",
        "Evergreen is not a city. Building permits for unincorporated Jefferson County go through the county in Golden. A new house must prove water and sewer, either from a district or from a well and a septic system.",
        """
        <h2>Proof of water</h2>
        <p>Jefferson County's Form 1001 is signed by the water and sanitation district, or you file an individual well permit plus a four-hour well test from the last three years. A household-use-only well is not accepted as water for an accessory dwelling unit. Septic permits go through county public health at 303-232-6301 if you cannot find a record. The county's permit page also says mechanical and plumbing permits for water heaters are applied for as those trade permits. Demo permits are not online. Call 303-271-8260. Planning and zoning is at 100 Jefferson County Parkway. A foothills lot is not Aurora Water.</p>
        <h2>Do not use a city sewer rule</h2>
        <p>If the house is on a district, that district's line, not Aurora's tap, decides a <a href="/services/sewer-line-repair/">sewer repair</a>. If it is on septic, a backup is an on-site system, not a city main. <a href="/guides/well-pump-vs-city-water/">Well versus utility</a> is the first question. The county map of special districts is the lookup. This page does not claim every Evergreen address has a well.</p>
        """,
        [
            ("Who permits an Evergreen water heater?", "Jefferson County, for an unincorporated parcel. The county lists plumbing and mechanical permits for water heaters. Evergreen is not a city with its own building department. Aurora and Golden apply only when the parcel is actually inside those cities. Confirm the parcel before you file."),
            ("What if there is no water district?", "You file the well permit and a four-hour test from the last three years with Form 1001. A household-use-only well cannot serve an accessory dwelling unit under that form. Septic records go through county public health at 303-232-6301. Do not drill from a webpage."),
            ("Is a sewer backup the county's main?", "Only if a district main serves you and the district says the problem is theirs. Many mountain lots are on septic. Aurora's backup number is for Aurora Water. Use the district on the bill or the septic permit, not a Front Range city crew."),
        ],
    )


def erie(site):
    del site
    return hub(
        "erie",
        "Erie",
        "plumber Erie CO",
        "Town of Erie",
        "Erie can review a water heater or a sewer repair in one to two business days. A new water or sewer tap is on a one-to-two-week list. Contractors need an Erie license.",
        """
        <h2>Quick versus planned</h2>
        <p>The town's permit table lists water heaters, minor plumbing, and sewer or water repair as quick permits at one to two business days. A new sewer, water, or irrigation tap is one to two weeks. A residential addition is four to six weeks for first comments. Contractors need a current town license and insurance on file before issuance. The office is at 645 Holbrook Street. The phone is 303-926-2700. Certificates of occupancy are described as a 48-hour turnaround after a complete submittal. Those are town targets.</p>
        <h2>Two counties on the map</h2>
        <p>Erie sits near the Boulder and Weld county line. The town permits inside town limits. Unincorporated land next door does not use this table. Confirm the limit. The permit page does not state who owns an existing lateral. Ask the town's utility before a street cut. Do not use Lafayette's quick-permit list or Aurora's.</p>
        """,
        [
            ("How long is an Erie water heater permit?", "The town lists water heaters with quick permits at one to two business days, in the same row as a sewer or water repair. A new tap is one to two weeks. An addition is four to six weeks for first comments. The contractor needs an Erie license. The phone is 303-926-2700."),
            ("Is Erie the same as Lafayette?", "No. Lafayette has its own quick-permit list and its own phone. Erie uses eTRAKiT and the table above. A Boulder County parcel that only has an Erie mailing address may be neither town. Confirm the limit before you apply."),
            ("Who owns the sewer lateral?", "Erie's permit-timing page does not say. Aurora's rule and Louisville's rule are those cities' rules. Ask Erie's utility for this address. A quick repair permit is permission to do the work, not a map of who pays for the pipe in the street."),
        ],
    )


def lafayette(site):
    del site
    return hub(
        "lafayette",
        "Lafayette",
        "plumber Lafayette CO",
        "City of Lafayette",
        "Lafayette requires a permit to replace plumbing systems, and it also lists repairs to an existing water heater, and same-size sink or toilet swaps, among work that can be exempt. Read the exception before you skip the permit.",
        """
        <h2>Exempt versus quick</h2>
        <p>The city's permit page says a permit is required to install or replace electrical, gas, mechanical, or plumbing systems. It then lists exemptions, including maintenance or repairs to a water heater, same-size replacement of a sink or toilet, and repairing leaks or stoppages in water or sewer piping. A quick-permit list, estimated at two business days, includes water heaters, water and sewer repairs, furnaces, and plumbing or mechanical work without engineered plans. Replacing a water heater may be the quick permit, while a small repair of the same heater may be the exemption. Ask Building at 303-661-1451 which box your scope is. Do not guess. The city hall number is 303-665-5588 at 1290 South Public Road.</p>
        <h2>Not Erie, not Boulder</h2>
        <p>Those neighbors have different clocks. Lafayette's two-business-day estimate is not Boulder’s mechanical-permit category and not Aurora's same-day request. Ownership of the lateral was not on this permit page. Ask the city's utility. A stoppage you clear without replacing pipe is the exemption they wrote. Replacing the pipe is new work.</p>
        """,
        [
            ("Do I need a permit to repair a Lafayette water heater?", "The page lists maintenance or repairs to a water heater as exempt, and it also lists water heaters on a quick-permit track of about two business days. The difference is repair versus replacement. Call Building at 303-661-1451 before you skip the permit. Replacing pipe is not the stoppage exemption."),
            ("Is a clog exempt?", "Repairing leaks or stoppages in water or sewer piping is on the exempt list. If you have to remove and replace a concealed drain, that is new work and needs a permit. The city's sentence is similar in spirit to Boulder's, and it is still Lafayette's list. Use Lafayette's phone."),
            ("How fast is a sewer repair permit?", "Water and sewer repairs are on the quick-permit list, with an estimated two business days. That is a short review, not permission to bury the work. The timing page does not say who owns the lateral. Ask the utility before you patch the street."),
        ],
    )


def superior(site):
    del site
    return hub(
        "superior",
        "Superior",
        "plumber Superior CO",
        "Town of Superior",
        "Superior's building division is operated by SAFEbuilt. Paper applications are not accepted. The permit goes through CommunityCore.",
        """
        <h2>How you file</h2>
        <p>The town says a building permit is pulled in CommunityCore and that paper submittals are not accepted. SAFEbuilt runs the building division: plan review, permits, and inspections. Permitting email is the SAFEbuilt address the town prints, superiorinspections@safebuilt.com. Building phone is 303-381-2028. Planning is 303-499-3675 extension 131, at 100 Superior Plaza Way, Suite 200. Contractor licensing is a separate town page. The office will not take a stack of paper plans at the desk.</p>
        <h2>The bill names the utility</h2>
        <p>The planning instructions do not name the water or sewer district, and they do not set a property-line rule for the pipe. Ask the utility on the bill before a <a href="/services/sewer-line-repair/">sewer</a> or <a href="/services/water-line-repair/">water line</a> quote includes the street. A <a href="/services/water-heater-replacement/">water heater</a> still needs the permit SAFEbuilt requires. Louisville's same-day list is Louisville's. Paper plans left at the front desk are not an application.</p>
        """,
        [
            ("Can I drop off paper plans in Superior?", "No. The town says applications and submittals go through CommunityCore and paper is not accepted. SAFEbuilt reviews and inspects. The building phone is 303-381-2028. A contractor who is not set up in the portal will delay a water heater that could have been filed online."),
            ("Who provides sewer?", "Superior's planning instructions do not name the district. Use the bill rather than a neighbor city's utility. The building permit and the district's pipe are different permissions. Confirm both before the street is opened."),
            ("Is Superior's heater permit the same as Louisville's?", "No. Louisville publishes a same-day list. Superior publishes an electronic portal run by SAFEbuilt. Ask Superior what a replacement heater requires. Aurora's inspection sentence does not apply."),
        ],
    )


def boulder(site):
    del site
    return hub(
        "boulder",
        "Boulder",
        "plumber Boulder CO",
        "City of Boulder",
        "Boulder treats water heaters as mechanical permits. Clearing a stoppage or swapping a toilet without moving pipes can be exempt. Replacing a concealed drain is new work and needs a permit.",
        """
        <h2>What is exempt</h2>
        <p>The city's permit page says you may stop a leak or clear a stoppage in drains, water, soil, waste, or vent piping without turning that into a permit, unless a concealed trap or pipe has to be removed and replaced. Replacing that concealed pipe is new work. Replacing a toilet is exempt if you do not rearrange valves or pipes. Water heaters, furnaces, and fireplaces are listed under mechanical permits. Plumbing is its own permit. Right-of-way permits are separate for wet utilities and for dry utilities. A fixture-count form is required when the number, type, or location of fixtures changes, including fixtures on an existing rough-in, and it must count every fixture on the water meter, including a detached building.</p>
        <h2>Not a fee quote</h2>
        <p>The city publishes a 2026 fee schedule. This guide does not copy those dollar amounts into a repair price. Work started without a permit can be assessed a higher fee under that schedule. Ask the city. Boulder is not Louisville, Lafayette, or Aurora. A <a href="/services/remodel-addition-plumbing/">remodel</a> that adds a bathroom needs the fixture count. A clog that you clear without new pipe may be the exemption.</p>
        """,
        [
            ("Does Boulder require a permit to replace a water heater?", "The permit list puts water heaters, furnaces, and fireplaces under mechanical permits. That is not the plumbing exemption for clearing a stoppage. Ask whether your replacement is the mechanical permit. Do not use Aurora's same-day rule. Right-of-way work, if you open a street, is another permit."),
            ("Can I replace a toilet without a permit?", "The city says yes if you do not replace or rearrange valves or pipes. If the flange or the shutoff has to be redone, you are past that sentence. Concealed drain replacement is new work and needs a permit and an inspection."),
            ("What is the fixture-count form for?", "Any project that changes the number, type, or location of fixtures, including a fixture set on an existing rough-in. Count every fixture on that water meter, even in a detached building. The city uses it for meter and plant-investment questions. It is not a sewer-ownership map."),
        ],
    )


def golden_blocked():
    return None


HUB_FUNCS = [
    denver, thornton, northglenn, commerce, brighton, federal, wheat, broomfield,
    louisville, longmont, greenwood, lonetree, castlepines, edgewater, sheridan,
    foxfield, bowmar, columbine, cherryhills, watkins, bennett, strasburg, byers,
    elizabeth, cherry_creek, four_square, franktown, sedalia, pinery, stonegate,
    meridian, roxborough, evergreen, erie, lafayette, superior, boulder,
    golden, morrison,
]
