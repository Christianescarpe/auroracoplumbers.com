"""Water heater, leak, and supply pages for Aurora."""

from markup import INSPECT, PERMIT, qas


def replacement(site: dict) -> dict:
    del site
    body = f"""
    <article class="sheet">
      <p class="eyebrow">Storage tank · Aurora, Colorado</p>
      <h1>Water heater replacement in Aurora</h1>
      <p class="lede">Replacing a storage tank is a permitted appliance swap, not a promise that the City inspector will arrive the same day. If the new unit is tankless, or the fuel changes, you are on a different job. Start here only when the next heater is still a tank of the same fuel.</p>
      <h2>Repair it or replace it</h2>
      <p>A tank that is leaking from the shell is usually finished. A wet fitting, a bad valve, or no hot water with a dry floor can still be a repair. That diagnosis is <a href="/services/water-heater-repair/">water heater repair</a>. Do not let a replacement quote skip the question of where the water is coming from. A pan full of water is not, by itself, a ruined tank.</p>
      <p>Switching from a tank to a tankless unit changes venting, gas or electrical capacity, and condensate. That scope is <a href="/services/tankless-water-heater-installation/">tankless installation</a>. Aurora's inspection staff describe a same-day path for replacement water heaters. They do not describe it as a bypass of plan review for a fuel conversion.</p>
      <h2>What Aurora actually says about the inspection</h2>
      <p>The City's <a href="{INSPECT}" rel="noopener noreferrer">inspections page</a> says permitted work is inspected, and that the permit card and approved plans have to be on site. For replacement water heaters and furnaces, a licensed plumbing or HVAC contractor can ask the Building Division for a same-day inspection when both the contractor and the homeowner will be there. The City says it will try, and it reserves the right to come another day depending on volume and staff. A quote that promises a same-day City sign-off is promising something the City did not promise.</p>
      <p>Scheduling details on that page are about the next inspection day, not about this website. Registered, licensed contractors can request inspections online up to 5:45 a.m. the day of the inspection. Phone requests to the permit center, 303-739-7420, are taken Monday, Tuesday, Thursday, and Friday from 7:30 a.m. to 4:30 p.m., and Wednesday from 8:30 a.m. to 4:30 p.m. Requests after 4:30 p.m. are not added to the next day. Those hours and that phone number belong to the City. This guide does not call them for you.</p>
      <p>The City's permitting landing page lists building permits and points people to contractor licensing. A residential handbook that search tools describe as asking for heater capacity and gas or electric was not downloaded for this draft, because the file request was refused. Do not treat a secondhand description as the form in your hand. Use the <a href="{PERMIT}" rel="noopener noreferrer">permitting page</a> and the <a href="/guides/aurora-water-heater-permits/">permit guide</a> to see what to confirm.</p>
      <h2>What belongs on the quote</h2>
      <p>This site will not name a price. The items that change the job are the ones to put in writing. Who pulls the permit, and will a licensed contractor be the one requesting the inspection. Whether the new tank matches the old one in type, fuel, and input. Where the tank sits, and whether a pan, a drain, combustion air, or a vent change is required by the listing and the inspector. Removal and disposal of the old tank. How long you will be without hot water. What is excluded, including a gas-line change or a new vent that would push the job off a simple replacement.</p>
      <p>If the house is not inside Aurora, stop using this page as the rule. <a href="/areas/centennial/">Centennial</a> does not supply water, and its published review schedule treats a residential water heater as a one-stop item with a stated business-day target that is still not a guarantee. <a href="/areas/castle-rock/">Castle Rock</a> may skip plan review for a tank heater and then add review when the heater is tankless. Those are different cities.</p>
      {qas([
        (
            "Will Aurora inspect a new tank the same day?",
            "Maybe. The inspections page says a licensed contractor can request a same-day visit when the contractor and the homeowner are both present. The City also says it may inspect on another day if volume or staffing does not allow it. Ask the contractor to request the inspection. Do not treat same-day as a term of the quote.",
        ),
        (
            "Does a like-for-like tank still need a permit?",
            "Treat it as permitted work. Aurora's inspection rules for replacement heaters assume a permit and a contractor who can request the inspection. A handbook description of the application was not retrieved as a file here. Confirm the current form with the Building Division, including capacity and whether the unit is gas or electric, before you rely on an old checklist.",
        ),
        (
            "The company wants to switch me to tankless. Is that this job?",
            "No. A tankless unit is a conversion. It can change the gas supply, the vent, the condensate drain, and the electrical circuit. Castle Rock, for example, adds a plan review and asks for the manufacturer sheet and gas-load calculations. Ask for that scope in writing, on the tankless page, instead of folding it into a tank swap.",
        ),
        (
            "What should the written quote include?",
            "Permit and who pulls it, match of type and fuel, vent and combustion air if the inspector will look at them, pan and drain if the location needs them, haul-away, and the exclusions. A price with none of those lines is not comparable to a price that includes them. This guide still will not invent the dollar amount.",
        ),
        (
            "I live in a nearby city. Can I use Aurora's inspection rule?",
            "No. Centennial publishes its own one-stop list and does not provide water or sewer. Castle Rock publishes a different tankless review. Highlands Ranch is unincorporated Douglas County, not an Aurora permit. Use the city page for the address, or the jurisdiction guide, before you compare quotes.",
        ),
      ])}
    </article>
    """
    return _meta(
        "/services/water-heater-replacement/",
        "Water heater replacement in Aurora | Aurora Plumbing Guide",
        "How an Aurora storage-tank replacement is permitted and inspected, and why same-day inspection is not a guarantee.",
        "Water heater replacement in Aurora",
        "Water heater replacement",
        "water heater replacement Aurora CO",
        "service",
        body,
    )


def repair(site: dict) -> dict:
    del site
    body = f"""
    <article class="sheet">
      <p class="eyebrow">Existing tank · diagnose before you replace</p>
      <h1>Water heater repair in Aurora</h1>
      <p class="lede">Repair is the right conversation when the tank you have might still be sound. It is the wrong conversation when the steel shell is leaking, or when someone has already decided to change fuel or go tankless.</p>
      <h2>What a repair visit is sorting</h2>
      <p>No hot water can be a control, a thermostat, a gas supply, or a failed element on an electric tank. Lukewarm water can be a dip tube or sediment. Water on the floor can be a fitting, a valve, a pan drain, or the tank itself. Those are different parts and different decisions. A technician who quotes a new tank without saying which of those they checked has skipped the diagnosis this page is about.</p>
      <p>If the tank wall is wet, or the pan is filling from a split seam, replacement is the honest next step. Go to <a href="/services/water-heater-replacement/">water heater replacement</a> and ask about the permit. If the proposal is a tankless unit, go to <a href="/services/tankless-water-heater-installation/">tankless installation</a>. An error code on a tankless unit you already own is <a href="/services/tankless-water-heater-repair/">tankless repair</a>, not this page.</p>
      <h2>Gas and electric stay with the contractor</h2>
      <p>This guide will not tell you how to light a pilot, size a connector, or open an electrical panel. Aurora's inspection list includes heat rough, gas pipe, and plumbing final among the inspections the City can require on permitted work. A repair that replaces a gas control or a connector can be the moment a simple service call becomes permitted work. Ask the contractor whether the repair stays a service call or needs a permit and an inspection. The City's same-day language is written for replacement heaters, and even then it is not guaranteed. Do not assume a repair inherits that path.</p>
      <h2>What to ask before you approve parts</h2>
      <p>Ask what failed, and what would still be true if that part is replaced. Ask the age of the tank and whether the leak is above the water line of the steel. Ask whether the flue, the connector, and the shutoff are part of the visit. Ask what is excluded. A rebuilt gas valve on a tank that is already weeping from the bottom is a parts bill on the way to a replacement. Put that in the notes you take to the <a href="/guides/plumbing-quote-checklist/">quote checklist</a>.</p>
      <p>None of this is a City diagnosis. Aurora Water's pages are about pipes in the ground, not about the tank in the closet. If the wet spot is in the yard, or the meter is spinning with the house shut off, use <a href="/services/leak-detection/">leak detection</a> instead of opening the heater.</p>
      {qas([
        (
            "When is a repair a waste of money?",
            "When the tank itself is leaking. A fitting, a valve, or a thermostat can be worth replacing. A split shell is not. Ask the technician to show you the source of the water before you buy parts, and to say whether the next failure is still likely this season. If the shell is done, move the conversation to a permitted replacement.",
        ),
        (
            "Does Aurora promise a same-day inspection for a repair?",
            "No. The same-day sentence on the inspections page is about replacement water heaters and furnaces, and the City reserves another day. A repair may not be on that path at all. Ask whether this visit needs a permit. Do not expect the City to clear a gas control the afternoon you call.",
        ),
        (
            "Can I relight the heater from instructions online?",
            "Do not use this site for that. Gas and electrical work on the heater belong with someone licensed to do them. If you smell gas, leave the house and call the gas utility's emergency line and, if needed, emergency services. A repair quote can wait. A gas odor cannot.",
        ),
        (
            "How is this different from no hot water on a tankless unit?",
            "A tank stores heated water. A tankless unit makes it as it passes through, and it fails with error codes, scale, and vent or ignition faults that a tank does not have. Use the tankless repair page for an existing tankless heater. Using tank parts logic on that unit wastes the visit.",
        ),
      ])}
    </article>
    """
    return _meta(
        "/services/water-heater-repair/",
        "Water heater repair in Aurora | Aurora Plumbing Guide",
        "How to tell an Aurora storage-tank repair from a replacement, without gas or electrical how-to steps.",
        "Water heater repair in Aurora",
        "Water heater repair",
        "water heater repair Aurora CO",
        "service",
        body,
    )


def tankless_install(site: dict) -> dict:
    del site
    body = f"""
    <article class="sheet">
      <p class="eyebrow">Conversion · not a tank swap</p>
      <h1>Tankless water heater installation in Aurora</h1>
      <p class="lede">A tankless heater is a different appliance, not a thinner tank. The quote has to survive gas or electrical capacity, the vent, condensate, and the manufacturer's instructions. Aurora will not guarantee the inspection day, and this guide will not promise an energy saving.</p>
      <h2>What has to be true before the unit is ordered</h2>
      <p>Ask whether the gas meter and the pipe can feed the input the manufacturer lists, or whether the electrical circuit can. Ask where the vent will terminate and whether the old tank's atmospheric flue can be reused. Many tankless vents cannot. Ask where condensate will drain, because a condensing unit makes water the old tank did not. Ask how many showers and appliances the sizing assumes. If any of those answers are "we'll see after we open the wall," the price is not finished.</p>
      <p>Elevation changes how some gas appliances are rated. This draft did not review a citywide derating table or a hardness report for Aurora, and it will not invent either one. The contractor should apply the installation manual for the model, at the address, and show you that page. A percentage saved on a proposal, with no manual behind it, is not a local fact.</p>
      <h2>Permits, and the city you are actually in</h2>
      <p>Inside Aurora, use the <a href="/guides/aurora-water-heater-permits/">permit guide</a>. The City's same-day inspection offer is for replacement heaters when a licensed contractor and the homeowner can both be there, and the City may still come another day. A conversion that changes venting or gas load is a weak candidate for "same as the old tank." Confirm that with the Building Division rather than assuming the one-stop habit of a different city.</p>
      <p><a href="/areas/castle-rock/">Castle Rock</a> is explicit: tankless heaters require plan review, the manufacturer's specification sheet, and gas piping load calculations. A tank heater there may avoid that review. Do not bring Castle Rock's worksheet to an Aurora counter, and do not skip it on a Castle Rock house because an Aurora page did not mention it. <a href="/areas/centennial/">Centennial</a> lists a residential water heater on its one-stop schedule. Read that city's page before you treat a Centennial address as Aurora.</p>
      <p>If you already own a tankless unit that is faulting, you do not need an installation. Use <a href="/services/tankless-water-heater-repair/">tankless repair</a>. If you want another tank, use <a href="/services/water-heater-replacement/">tank replacement</a>.</p>
      {qas([
        (
            "Is tankless just a smaller replacement?",
            "No. The water is heated as it flows, so the gas or electrical supply, the vent, and often a condensate drain have to match the new unit. A quote that reuses the old flue and the old connector without checking the manual is guessing. Ask for those three items in writing before you compare prices.",
        ),
        (
            "Will I save a set percentage in Aurora?",
            "This guide will not say so. No Aurora water-hardness study or altitude derating table was reviewed for a citywide claim. Savings depend on how you use hot water and on the unit's manual. Ask the contractor to show the manufacturer's sizing page for your elevation and fixtures, not a metro average.",
        ),
        (
            "Does Aurora guarantee a same-day inspection for a conversion?",
            "No. The City's same-day language covers replacement heaters when both the contractor and the homeowner are present, and staff may still defer the visit. A tankless conversion can add review the tank swap did not. Ask the Building Division which path this submittal is on. Do not put a guaranteed inspection time in the contract.",
        ),
        (
            "What if the house is in Castle Rock?",
            "The Town requires a plan review for tankless heaters and asks for the manufacturer sheet plus gas piping load calculations. That is not the Aurora process. Use the Castle Rock page for a house inside that town, and do not assume a tank-heater shortcut covers the tankless unit.",
        ),
      ])}
    </article>
    """
    return _meta(
        "/services/tankless-water-heater-installation/",
        "Tankless water heater installation in Aurora | Aurora Plumbing Guide",
        "What a tankless conversion in Aurora has to prove about gas, venting, and inspection, with no savings promise.",
        "Tankless water heater installation in Aurora",
        "Tankless installation",
        "tankless water heater installation Aurora CO",
        "service",
        body,
    )


def tankless_repair(site: dict) -> dict:
    del site
    body = f"""
    <article class="sheet">
      <p class="eyebrow">Existing tankless unit</p>
      <h1>Tankless water heater repair in Aurora</h1>
      <p class="lede">An existing tankless heater that codes out, short-cycles, or gives up mid-shower is a repair problem. Replacing it with a new model, or going back to a tank, is a different permit conversation.</p>
      <h2>What the visit should identify</h2>
      <p>Ask for the error code and what the manufacturer says it means. Ignition, vent blockage, scale, a failed sensor, and a bad flow sensor are not the same part. Descaling is maintenance. It is not proof the heat exchanger is sound. A company that sells a new unit without reading the code is skipping the page you are on.</p>
      <p>Scale is a reason to ask what water the house actually gets. This guide does not claim Aurora's water is uniformly hard. No current city hardness table was used here. If someone recommends a softener or a filter as part of the repair, that recommendation needs a test of your water, not a metro slogan. Treatment equipment is a separate decision and is not written up as a product page in this preview.</p>
      <h2>When repair should stop</h2>
      <p>Repeated exchanger failures, a discontinued model with no parts, or a vent that was never right are reasons to talk about <a href="/services/tankless-water-heater-installation/">a new installation</a> or a return to <a href="/services/water-heater-replacement/">a tank</a>. Either change can alter gas, venting, and the inspection. Aurora's same-day inspection note is about replacement heaters and is not a guarantee. A repair that opens the gas train may still need a permit. Ask. Do not use internet steps to open the burner.</p>
      <p>If the unit is gas and you smell gas, leave and call the gas utility. This website is not an emergency desk, and the quote checklist will not send your address anywhere.</p>
      <h2>What a repair quote should list</h2>
      <p>Ask for the model, the code, the part, and whether the heat exchanger is included or excluded. Ask whether the vent, the gas connector, and the condensate drain were inspected or only the circuit board. Ask who pulls a permit if the gas train is opened. A flush, a sensor, and a new heater are three prices. They should not share one line. If the house is in Castle Rock, a replacement tankless unit also needs the Town's manufacturer sheet and gas-load calculations. A repair that leaves the same unit in place does not automatically skip that question when the vent or the gas pipe changes. Write the exclusion down before you compare the number with a company that is selling a new heater.</p>
      {qas([
        (
            "Is descaling the same as a repair?",
            "No. Flushing scale is maintenance. It can restore flow when the heat exchanger is coated and otherwise sound. It does not fix a cracked exchanger, a failed fan, or a vent that cannot breathe. Ask which fault the code names, and whether the part is available, before you approve a flush as the whole visit.",
        ),
        (
            "Should I replace the unit because Aurora has hard water?",
            "Not from this guide. A citywide hardness number was not established here, and houses do not all see the same supply. Ask for a test if treatment is being sold with the repair. The repair itself should stand on the error code and the condition of this unit.",
        ),
        (
            "Does a parts repair need the same inspection as a new tankless heater?",
            "Ask the Building Division. Aurora describes a same-day request for replacement heaters, with the right to come another day. A parts repair is not automatically that visit, and a new tankless install can need a fuller review. Get the permit answer for the work actually being done.",
        ),
        (
            "The company wants to convert me back to a tank. Which page is that?",
            "Tank replacement, if you are leaving tankless, or a new tankless install if you are staying with tankless but changing the unit in a way that changes venting or gas. Repair stays on this page only while the heater you have is the one being fixed. Make them name which of the three the quote is.",
        ),
      ])}
    </article>
    """
    return _meta(
        "/services/tankless-water-heater-repair/",
        "Tankless water heater repair in Aurora | Aurora Plumbing Guide",
        "How to separate an Aurora tankless repair from a new install, without a hardness or savings claim.",
        "Tankless water heater repair in Aurora",
        "Tankless repair",
        "tankless water heater repair Aurora CO",
        "service",
        body,
    )


def leak(site: dict) -> dict:
    del site
    body = f"""
    <article class="sheet">
      <p class="eyebrow">Find it before you open the street</p>
      <h1>Leak detection in Aurora</h1>
      <p class="lede">A leak bill is often the cost of looking in the wrong place. In Aurora, a sewer camera cannot see a pressurized water service, and a water-service repair can include the street. Locate the leak before you approve either dig.</p>
      <h2>Three different wet places</h2>
      <p>Water under a heater is a heater question. Use <a href="/services/water-heater-repair/">repair</a> or <a href="/services/water-heater-replacement/">replacement</a>. Sewage at a floor drain is a drain or a service-line question. Use <a href="/services/drain-cleaning/">drain cleaning</a> or <a href="/services/sewer-line-repair/">sewer repair</a>, and remember Aurora Water's split: you own the line to the tap. A hiss, a warm spot in a slab, or a meter that moves while every faucet is off is a supply leak. That is this page.</p>
      <p>The City's service-line page says water service lines are generally copper and cannot be videotaped. Anyone who offers a "sewer camera" for a yard water leak is using the wrong tool. Ask what method they will use, acoustic, tracer gas, or otherwise, and what it will not see. This guide will not teach those methods or invent a meter test Aurora Water did not publish.</p>
      <h2>Who might own the pipe</h2>
      <p>On an Aurora Water account, the service-line page assigns the pipe from the home to the city main, plus street or sidewalk repair after that work, to the homeowner. The city main is not that pipe. Ask Aurora Water to say whether the leak they hear is on your service or on their main before a contractor cuts pavement you may have to replace. Get the answer for the address. A neighbor's district is not your answer.</p>
      <p>If the address is in <a href="/areas/castle-rock/">Castle Rock</a> and on Town water, the Town's FAQ describes a different line: the Town maintains water service to the property-line connection, and the curb-stop valve is the Town's. Do not shut that street valve yourself. That rule is not Aurora's, and it is not a sewer map. <a href="/areas/parker/">Parker</a> is less settled on paper. Do not let a contractor invent a sidewalk boundary there.</p>
      {qas([
        (
            "Can a sewer camera find a water leak?",
            "No. Aurora's service-line page says water service lines cannot be videotaped. A sewer camera belongs in the drain. A supply leak needs a method meant for a pipe that is under pressure. Ask which method, and what it cannot see, before you approve a hole in the slab or the street.",
        ),
        (
            "Should I open the street because the yard is wet?",
            "Not yet. The wet spot is not a map. On Aurora Water, a leak on your service can still be your street repair. Ask the utility whether the main is involved, and ask the locator to mark both the water service and the sewer so a dig does not hit the wrong pipe. 811 is the call the City tells owners to make before excavation.",
        ),
        (
            "Is a spinning meter an official Aurora test?",
            "This guide will not call it one. Aurora Water's pages reviewed here do not publish a meter-dial procedure. A moving meter with fixtures off is a reason to get a leak located. It is not, by itself, a map of where to cut. Let the person who will warranty the location explain the method.",
        ),
        (
            "How is this different from repiping the house?",
            "Detection finds one leak. Repiping replaces the supply piping through the building. A single wet ceiling does not prove every pipe in the house is done. Ask for the location first. A whole-house replacement is a wider scope and is not the automatic next line on a leak quote.",
        ),
      ])}
    </article>
    """
    return _meta(
        "/services/leak-detection/",
        "Leak detection in Aurora | Aurora Plumbing Guide",
        "How to separate an Aurora supply leak from a sewer backup, and why a water line cannot be camera'd like a drain.",
        "Leak detection in Aurora",
        "Leak detection",
        "leak detection Aurora CO",
        "service",
        body,
    )


def water_line(site: dict) -> dict:
    del site
    body = f"""
    <article class="sheet">
      <p class="eyebrow">Pressurized supply · not the sewer</p>
      <h1>Water line repair in Aurora</h1>
      <p class="lede">The water service is the pipe that brings drinking water to the building. It is not the sewer lateral, it cannot be filmed the way a drain can, and on an Aurora Water account the repair can include the street.</p>
      <h2>What Aurora Water's page covers</h2>
      <p>The City's service-line page says homeowners maintain the service line from the home to the city's main, and the street or sidewalk repair after that work. It says water lines are generally copper and much less likely to break than a failing sewer, and that they cannot be videotaped. "Generally" is doing real work in that sentence. A copper line still splits. A line that is not copper still exists. The page is not a coupon for skipping <a href="/services/leak-detection/">leak detection</a>.</p>
      <p>Do not copy the sewer tap language onto this pipe. The wastewater page's tee and saddle are about the sanitary connection. The water service has its own boundary, and the practical question is whether Aurora Water agrees the leak is on your service or on the main. Ask them, at the address, before you accept a street-cut price.</p>
      <h2>What the quote has to name</h2>
      <p>Length and depth. Material, if it can be known without a camera. Where the failure is relative to the meter or the main. Who patches asphalt, curb, and sidewalk. How the house gets water during the repair. What is excluded. A price that says "water line" and does not say whose side of the main is being cut is not comparable to one that does.</p>
      <p>Interior pinhole leaks in several rooms are not automatically this yard pipe. Spot repair inside the house is a different scope from the service in the ground. Whole-house replacement of indoor supply piping is broader again, and this preview does not publish that as a separate sales page yet. Do not let one wet ceiling become a whole-house number without a location.</p>
      <p>Other cities draw the line differently. <a href="/areas/castle-rock/">Castle Rock Water</a> tells its customers the Town maintains the water service to the property-line connection and owns the curb stop. <a href="/areas/parker/">Parker</a> does not have a single published boundary this guide will stand behind. Use the city you are actually in.</p>
      <h2>Restoration and locates</h2>
      <p>Before anyone digs, the Aurora wastewater page tells owners to call 811 for their sewer service and tap, and the service-line page puts street and sidewalk repair on the owner when the work is the owner's water line. Mark both pipes. A crew that locates only the sewer can still hit the water service, and the other way around. Ask the quote to say the marks were called, who patches, and whether the house will be without water while the section is out. If the leak has not been located, the honest previous step is detection, not a trench length guessed from a wet flower bed.</p>
      {qas([
        (
            "Is the water line the same as the sewer lateral?",
            "No. One is under pressure and brings in drinking water. The other carries wastewater to the city main, and in Aurora you maintain that sewer line through the tap. A camera belongs in the sewer. The water service has to be found another way. Mixing the two quotes is how a street cut gets aimed at the wrong pipe.",
        ),
        (
            "Who patches the street in Aurora?",
            "If the cut is your water service, the City's service-line page puts the street or sidewalk repair on the homeowner, along with the pipe from the house to the main. Confirm with Aurora Water that the leak is not on the city main. Ask the quote to include the patch, or to say who else will do it.",
        ),
        (
            "Are Aurora water lines always copper?",
            "The City says they are generally copper, and generally less likely to break than a bad sewer. That is not a survey of your yard. Age, soil, and prior repairs still matter. Do not skip location because the page used the word generally, and do not replace a line that has not been shown to fail.",
        ),
        (
            "Can I shut the city valve in the parkway?",
            "Not from advice on this site. In Castle Rock the Town says the street valve is theirs and tells customers to use the indoor shutoff, or to call the Town for the curb. Aurora's pages reviewed here do not give a homeowner procedure for the water main valve. Call the utility that serves the address.",
        ),
      ])}
    </article>
    """
    return _meta(
        "/services/water-line-repair/",
        "Water line repair in Aurora | Aurora Plumbing Guide",
        "Aurora water service repairs: owner line to the main, no sewer camera, and street repair that has to be in the quote.",
        "Water line repair in Aurora",
        "Water line repair",
        "water line repair Aurora CO",
        "service",
        body,
    )


def _meta(path, title, description, h1, crumb, keyword, kind, body) -> dict:
    return {
        "path": path,
        "title": title,
        "description": description,
        "h1": h1,
        "breadcrumb": crumb,
        "intended_keyword": keyword,
        "keyword_status": "Qualitative topic only. No search-volume study. Preview.",
        "kind": kind,
        "body": body,
    }
