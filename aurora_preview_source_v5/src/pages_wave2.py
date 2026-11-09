"""Pipe, building, pump, and specialty pages. Specialty pages state their limits."""

from markup import qas
from pages_wave import _page


def pipe(site):
    del site
    body = """
    <article class="sheet">
      <p class="eyebrow">One section, not the whole house</p>
      <h1>Pipe repair and replacement in Aurora</h1>
      <p class="lede">Pipe repair replaces a bad section. It is not a new water service from the main, and it is not a whole-house repipe, unless the evidence says the rest of the pipe is failing the same way.</p>
      <h2>Inside the house or under the yard</h2>
      <p>A pinhole under a sink, a split elbow in a crawl space, or a leaking joint in a ceiling is an indoor repair. The quote should name the material, the length, and how the wall or ceiling will be closed, or say that patching the drywall is excluded. Underground pipe in the yard may be the water service or the sewer. Those are <a href="/services/water-line-repair/">water line repair</a> and <a href="/services/sewer-line-repair/">sewer line repair</a>. Do not let one word, "pipe," cover both.</p>
      <p>In Aurora the sewer from the building through the tap is yours, including street repair if you open it. The water service to the city main is also yours on an Aurora Water account, and it cannot be camera'd. Locate before you dig. Call 811. If the address is in Lakewood, find the district first. The city's own sewer graphic applies to about 8,000 north Lakewood customers, not to every district on the city's provider list.</p>
      <h2>When the section is no longer the job</h2>
      <p>Repeated pinholes on several branches, or a crawl space full of the same failing pipe, is the conversation for <a href="/services/whole-house-repiping/">whole-house repiping</a>. One repair that went well is not that conversation. A liner or a burst of a sewer is <a href="/services/trenchless-sewer-repair/">trenchless sewer repair</a>, and only after a camera.</p>
      <p>Englewood lists changes to water lines and drains as permit work. Aurora's inspection rules apply when the work is permitted. Ask which office has the parcel.</p>
      """ + qas([
        ("Is underground pipe the water line or the sewer?", "It can be either. The water service is under pressure and cannot be filmed like a drain. The sewer can be camera'd, and in Aurora you maintain it to the tap. A wet yard does not tell you which pipe. Locate both before anyone digs."),
        ("One pinhole showed up. Should the house be repiped?", "Not from one hole. Repair that section and ask whether other pipe of the same age and material is already leaking. Whole-house repiping is a different scope, with more wall repair. Approve it only when the evidence is more than a single elbow."),
        ("Who patches the drywall?", "Whoever the quote names. Plumbers often leave paint and drywall out. If the ceiling is open, ask for that line in writing. An underground repair should instead name pavement, sidewalk, and landscape."),
        ("Does Lakewood use Aurora's tap rule?", "No. Lakewood has many water and sewer providers. The city's own graphic, for its north Lakewood sewer customers, says the owner keeps the lateral to the main under the street. Other districts on the city's list are not that graphic. Look up the address."),
      ]) + "</article>"
    return _page("/services/pipe-repair-replacement/", "Pipe repair and replacement in Aurora | Aurora Plumbing Guide", "Spot pipe repair versus the buried water service, the sewer, and a whole-house repipe.", "Pipe repair and replacement in Aurora", "Pipe repair", "pipe repair and replacement Aurora CO", "service", body)


def repipe(site):
    del site
    body = """
    <article class="sheet">
      <p class="eyebrow">Supply pipes through the house</p>
      <h1>Whole-house repiping in Aurora</h1>
      <p class="lede">Repiping replaces the supply pipes inside the building. It is not a single elbow, and it is not the buried pipe from the water main to the house.</p>
      <h2>What would justify it</h2>
      <p>You want more than one leak, in more than one place, on the same aging pipe, or a documented restriction that fixture repairs will not fix. A plumber should show you those locations or the failed sections already cut out. A sales visit that jumps from a wet ceiling to a whole-house price, without that evidence, is skipping <a href="/services/pipe-repair-replacement/">pipe repair</a> and <a href="/services/leak-detection/">leak detection</a>.</p>
      <p>The buried water service is <a href="/services/water-line-repair/">a different pipe</a>. On Aurora Water it runs to the city main and the street repair can be yours. Replacing indoor copper or galvanized pipe does not replace that yard line unless the quote says so. The sewer is not part of a supply repipe at all.</p>
      <h2>What the quote has to include</h2>
      <p>Material of the new pipe. Which rooms. Whether shutoffs are added. How long the water is off. Who opens and closes walls and ceilings. Whether the water heater connections are included. What is excluded, including the yard service and any permit fee. Englewood treats water-line changes as permit work. Ask Aurora's building division if the repipe in the house needs a permit and an inspection. Do not guess from a neighboring city.</p>
      <p>This is a large job. It is still information, not a dispatch. No price is printed here.</p>
      """ + qas([
        ("Does repiping include the pipe in the yard?", "Only if the quote says the water service to the main is included. Indoor repiping and the buried service are different pipes, different digs, and often different ownership. In Aurora the service to the main is the owner's on an Aurora Water account. Read that page before you assume it is in the house price."),
        ("One leak means the whole house is done, right?", "No. One leak is a repair until more of the same pipe is failing. Ask for the other locations. A whole-house number without that list is not comparable to a repair quote."),
        ("Will the walls be finished?", "Ask. Many plumbing quotes stop at the pipe. Drywall, texture, and paint can be another trade. If they are excluded, the house is livable only after someone else closes it. Put that in the scope."),
        ("Is the sewer replaced at the same time?", "Not as part of a supply repipe. The sewer is a drain line. In Aurora you maintain it to the tap, which is its own project after a camera. Do not let the two share one vague 'pipes' line."),
      ]) + "</article>"
    return _page("/services/whole-house-repiping/", "Whole-house repiping in Aurora | Aurora Plumbing Guide", "When indoor supply replacement is the job, and why it is not the yard water service or the sewer.", "Whole-house repiping in Aurora", "Repiping", "whole house repiping Aurora CO", "service", body)


def commercial(site):
    del site
    body = """
    <article class="sheet">
      <p class="eyebrow">A business, not a spare bath</p>
      <h1>Commercial plumbing in Aurora</h1>
      <p class="lede">A shop, a kitchen, or an office has occupants, a clock, and usually a longer permit path than a house water heater. The pipe in the ground can still be the owner's.</p>
      <h2>Time and access</h2>
      <p>Ask when the water or the drains can be off without stopping the business, and who will be on site to open roofs, ceilings, and locked rooms. A restaurant grease problem is not a house sink. Aurora's service-line page tells people to keep grease out of drains. A commercial quote should say whether a grease interceptor is in scope or excluded. This guide does not invent interceptor sizes.</p>
      <p>In Aurora, a building permit for a commercial space goes through plan review. The permitting page points structural permits at that review. It is not the same-day house water-heater path, and even that house path is not guaranteed. Centennial publishes the contrast clearly: a residential water heater can be one-stop, while commercial alterations are listed at 10 business days and new commercial at 15, after a complete submittal. Those are Centennial's targets, not a promise, and they are not Aurora's clock. Use them only for a Centennial address. See <a href="/areas/centennial/water-heater-replacement/">Centennial water heater replacement</a> for the house side of that city.</p>
      <h2>The service line does not become the city's because the customer is a business</h2>
      <p>Aurora Water's wastewater page covers homes and buildings. The owner still maintains the sewer service line from the tap to the address, including the connection and related street repair. A backup in a first-floor restroom can still be private. Camera it. Lakewood's city sewer crew, at the number on the city's graphic, inspects the city main for its own north Lakewood customers, about 8,000 of them. A Lakewood business on another district is not that crew. Look up the provider.</p>
      <p>This page explains the decision. It does not mean a contractor is standing by.</p>
      """ + qas([
        ("Is a commercial water heater a one-stop permit?", "Not as a rule you can carry from city to city. Centennial's schedule puts a house water heater on the one-stop list and commercial alterations on a longer review. Aurora's same-day note is about house replacement heaters and is not guaranteed. Ask the building department that has the suite, not the nearest city's chart."),
        ("Who owns the sewer under a shop in Aurora?", "The building owner still maintains the service line from the tap to the address, including the connection, under Aurora Water's wastewater page. The city keeps the main and the manholes. A backup is not automatically the city's bill. Get a camera and ask where the defect sits."),
        ("Can the work wait until after close?", "That is a scheduling term, not a code section. Put the hours in the quote: when water can be off, who meets the plumber, and what happens if a part is not on the truck. After-hours work can cost more. This site does not set that rate."),
        ("Does Lakewood's 24-hour sewer number cover every business?", "No. The city's graphic offers main-line inspection day and night for the city sewer that serves about 8,000 north Lakewood customers. Other districts are on the provider list. Call the utility that actually serves the address, not a number from a different row."),
      ]) + "</article>"
    return _page("/services/commercial-plumbing/", "Commercial plumbing in Aurora | Aurora Plumbing Guide", "How a business plumbing job differs from a house: access, permit path, grease, and who owns the service line.", "Commercial plumbing in Aurora", "Commercial", "commercial plumbing Aurora CO", "service", body)


def remodel(site):
    del site
    body = """
    <article class="sheet">
      <p class="eyebrow">Rough-in before the walls close</p>
      <h1>Remodel and addition plumbing in Aurora</h1>
      <p class="lede">Adding a bathroom, moving a kitchen, or finishing a basement is rough-in, inspection, and then fixtures. It is not a Saturday faucet swap.</p>
      <h2>Sequence</h2>
      <p>Drains and vents go in while the framing is open. Supply pipes follow. Inspection happens before insulation and drywall cover the work. Aurora's inspections page says the area has to be open and the permit card on site. If the plumber is scheduled after the rock is hung, you are paying to open it again. Ask for the inspection type, often a plumbing rough, and who meets the inspector.</p>
      <p>Centennial's review schedule puts residential additions at 10 business days and basement finishes at five, after a complete submittal. A house water heater there can be one-stop. An addition is not that list. See <a href="/guides/centennial-heater-vs-remodel-permit/">Centennial heater versus remodel</a>. Aurora does not publish that same chart. Use Aurora's permitting page for an Aurora parcel.</p>
      <h2>What changes the plumbing scope</h2>
      <p>Every new fixture needs a drain, a vent, and hot and cold water, and the existing pipes have to be large enough. This guide will not calculate fixture units. The plumber should say whether the current building drain and water service can take the new bath. A basement bath below the sewer leaving the house needs a pump. That pump is a <a href="/services/sewer-ejector-pumps/">sewer ejector</a>, not a groundwater <a href="/services/sump-pump-repair-installation/">sump</a>.</p>
      <p>Keep fixture setting, the tub or shower, and the water heater as their own lines if they are not in this rough-in. <a href="/services/bathtub-shower-installation/">Tub and shower</a> work fails when nobody owns the valve access.</p>
      """ + qas([
        ("Can the plumber rough in after drywall?", "They can, and then the wall comes back off for the inspection. Aurora wants permitted work open and the permit card on site. Schedule the rough inspection before insulation. Closing early is how you pay twice."),
        ("A basement toilet is below the street sewer. What then?", "Gravity will not carry the waste up. The fixture needs a pump, maintained by the owner, which Littleton's code also says for buildings that sit too low. That is an ejector, not a sump pump for groundwater. Ask which basin and where it discharges."),
        ("Is an addition the same permit as a water heater?", "No. Centennial lists additions on a multi-day review and house water heaters as one-stop. Aurora's same-day language is about replacement heaters, not a new bathroom. Ask which application this drawing is."),
        ("Who buys the fixtures?", "Say so. Rough-in can exclude the toilet, the faucet, and the tub, which show up later as a second invoice. If the plumber supplies them, the model numbers belong on the quote so the valve and the trim match."),
      ]) + "</article>"
    return _page("/services/remodel-addition-plumbing/", "Remodel plumbing in Aurora | Aurora Plumbing Guide", "Rough-in, inspection, and fixture order for an Aurora addition or basement, including when a pump is required.", "Remodel and addition plumbing in Aurora", "Remodels", "remodel and addition plumbing Aurora CO", "service", body)


def inspection(site):
    del site
    body = """
    <article class="sheet">
      <p class="eyebrow">A report, not a repair</p>
      <h1>Plumbing inspection in Aurora</h1>
      <p class="lede">A plumbing inspection here means a person walks the fixtures and visible pipes and writes what they found. It is not the city's permit inspection, and it is not a sewer camera by itself.</p>
      <h2>Three different inspections</h2>
      <p>A buyer or an owner may want a condition report: leaks, old valves, the water heater's age and whether it is leaking, and what could not be seen. That report should list exclusions. Slab pipes, closed walls, and the buried sewer are not visible from a hallway. A <a href="/services/sewer-camera-inspection/">camera</a> is a separate line if you want the service line. Aurora residents can later ask the City to review that video. The condition report does not include that review unless someone orders it.</p>
      <p>The city's own inspection happens after a permit, with a card on site. That inspector is not writing you a remodel shopping list. They are checking the permitted work. Read the <a href="/guides/aurora-water-heater-permits/">heater permit guide</a> for how Aurora schedules those visits. Same-day is not guaranteed.</p>
      <h2>What to ask the report to include</h2>
      <p>Each fixture that was operated. The water heater, without taking it apart. Visible supply leaks. Whether drains were tested by running water, not by guessing. What was locked, buried, or covered. Photos of defects. A price to fix is a second document. Do not let an inspection fee quietly become a repair authorization.</p>
      <p>For a sale, match the report to the city's rules only after you know the city. An Aurora sewer note does not describe a Centennial district. The <a href="/guides/city-county-utility-jurisdiction/">jurisdiction guide</a> is the checklist for that.</p>
      """ + qas([
        ("Is this the city inspector?", "No. A private condition report is someone you hire to look and write. Aurora's inspector comes because a permit is open, and they are checking that work. You can need both on a remodel. You do not satisfy a permit by paying for a home inspection."),
        ("Will they see the sewer line?", "Not unless a camera is included and there is a cleanout. Walls and slabs stay hidden. Ask for those limits in writing. If the sewer matters, order the camera and keep the file."),
        ("Can the same person fix what they find?", "Only if you approve a separate scope. An inspection that turns into a repair without a new price is hard to compare. The report should stand alone. The repair quote should name the items you chose."),
        ("Does the report tell me who owns the pipe?", "It can describe what is on the property. Ownership comes from the utility, not from the inspector's opinion. In Aurora, the wastewater page puts the service line to the tap on the owner. Other cities differ. Do not let a one-page report overwrite the utility."),
      ]) + "</article>"
    return _page("/services/plumbing-inspection/", "Plumbing inspection in Aurora | Aurora Plumbing Guide", "A condition report versus a city permit inspection versus a sewer camera.", "Plumbing inspection in Aurora", "Inspections", "plumbing inspection Aurora CO", "service", body)


def pressure(site):
    del site
    body = """
    <article class="sheet">
      <p class="eyebrow">Too little or too much, at the tap</p>
      <h1>Water pressure problems in Aurora</h1>
      <p class="lede">Low pressure at one faucet is not low pressure in the street. High pressure that hammers the pipes is not a clogged aerator. The fix depends on which of those you have.</p>
      <h2>One fixture or the whole house</h2>
      <p>One slow faucet, with normal flow everywhere else, is usually that faucet's aerator, cartridge, or supply stop. That is <a href="/services/faucet-sink-fixture-repair/">fixture repair</a>. Every cold fixture weak, or every fixture weak, can be a pressure-reducing valve, a partly closed house valve, a crushed line, or the utility's supply. Ask whether neighbors on the same main are affected. If they are, call the water utility before you replace a valve. Arvada asks its customers to report low pressure, main breaks, and dirty water at 720-898-7070. That is Arvada's number, for Arvada utility customers, not a link and not Aurora's desk.</p>
      <p>This guide does not claim Aurora's water is hard, and it does not blame pressure on scale without a test. A softener is <a href="/services/water-treatment-installation/">treatment</a>, a different decision.</p>
      <h2>High pressure and water hammer</h2>
      <p>A reducing valve that has failed open can feed the house more pressure than fixtures like. The symptom is a loud closure, weeping stops, or a relief valve that drips at the water heater. Ask for a pressure reading at a hose bib with no water running, and ask what number the plumber thinks is too high. Do not let a reading become a repipe. A buried leak can also drop pressure. If the meter moves with the house off, go to <a href="/services/leak-detection/">leak detection</a> before you replace the regulator.</p>
      """ + qas([
        ("Only the kitchen faucet is weak. Is the main failing?", "Unlikely. One fixture points to that faucet, its aerator, or its stop. Check the other sinks and a tub. Whole-house weakness is when several rooms, hot and cold or all cold, drop together. Then look at the regulator, the house valve, and the utility."),
        ("Neighbors have no pressure either. Who do I call?", "The water utility on the bill, before a plumber replaces parts in the house. Arvada publishes 720-898-7070 for its customers to report low pressure and main breaks. Aurora Water and Denver Water publish their own numbers. Use the utility that serves the address."),
        ("Can high pressure mean I need new pipes?", "Not by itself. A failed reducing valve is a valve. Pipes get replaced when they are leaking or damaged, not because a gauge read high for an afternoon. Ask for the reading and the valve, and approve pipe only where it is actually failing."),
        ("Is this a water-quality problem?", "No. Pressure is flow and force. Taste, odor, and hardness are treatment questions, and this guide will not call Aurora's water hard without a test. Do not buy a softener to fix a clogged aerator."),
      ]) + "</article>"
    return _page("/services/water-pressure-problems/", "Water pressure problems in Aurora | Aurora Plumbing Guide", "One weak faucet versus whole-house pressure, a failed regulator, and when to call the utility first.", "Water pressure problems in Aurora", "Water pressure", "water pressure repair Aurora CO", "service", body)


def sump(site):
    del site
    body = """
    <article class="sheet">
      <p class="eyebrow">Groundwater, not sewage</p>
      <h1>Sump pump repair and installation in Aurora</h1>
      <p class="lede">A sump pump lifts groundwater out of a basin so it does not sit under the slab. It is not the pump that lifts toilet waste. Connecting it to the sanitary sewer is a mistake Lakewood states in plain language for its own customers.</p>
      <h2>What it should discharge to</h2>
      <p>The discharge should go where the local rules allow storm or groundwater to go, often outside, not into the sanitary sewer. Lakewood's sewer graphic says never connect a sump pump to the sewer system, for the city sewer serving about 8,000 north Lakewood customers. Aurora keeps stormwater and sewage in separate systems. A pump that sends groundwater into the sanitary lateral is dumping the wrong water into a pipe you may own to the tap. Ask the plumber where the pipe daylights, and ask the building department if that outlet is allowed.</p>
      <p>A basin that smells like sewage, or that receives a toilet or a laundry line from a low basement, is not this pump. That is a <a href="/services/sewer-ejector-pumps/">sewer ejector</a>. Replacing a sump will not fix a sewage backup.</p>
      <h2>Repair versus a new pump</h2>
      <p>A pump that hums, a stuck switch, or a frozen discharge line can be a repair. A pump that burned up, or a basin with no pump where water enters, is an installation. Ask about a battery or water-powered backup only if you understand it needs maintenance. This page does not describe electrical wiring. If the only problem is a tripped breaker, an electrician may be the right trade. Say that on the quote.</p>
      <p>The check valve on the discharge should be part of the conversation so water does not run back into the basin. Ask who tests it.</p>
      """ + qas([
        ("Can the sump discharge into the sewer?", "Do not plan on it. Lakewood's city sewer graphic says never to connect a sump to the sewer. Aurora treats stormwater and sewage as separate systems. Groundwater in the sanitary line is the wrong pipe. Ask where the discharge will outlet and whether that city allows it."),
        ("The basement smells like sewage. Is the sump the problem?", "Maybe the basin is actually a sewage ejector, or a drain is backing up into a sump that should have stayed clean. A groundwater pump does not macerate toilet waste. If fixtures downstairs are involved, read the ejector page and the sewer page."),
        ("Do I need a backup pump?", "Only if you want coverage when the power fails, and only if someone will maintain it. A backup is an extra scope, not a code fact this guide is inventing. Ask what happens to the water if the primary pump stops during a storm."),
        ("Who wires it?", "If it is a plug into an existing outlet, say so. A new circuit is electrical work, and this page does not describe wiring. Put the electrical line on the quote or hire it separately so the pump is not left sitting in the box."),
      ]) + "</article>"
    return _page("/services/sump-pump-repair-installation/", "Sump pump repair in Aurora | Aurora Plumbing Guide", "Groundwater sump pumps, where they should not discharge, and how they differ from a sewage ejector.", "Sump pump repair and installation in Aurora", "Sump pumps", "sump pump repair and installation Aurora CO", "service", body)


def ejector(site):
    del site
    body = """
    <article class="sheet">
      <p class="eyebrow">Sewage that cannot drain by gravity</p>
      <h1>Sewer ejector pumps in Aurora</h1>
      <p class="lede">An ejector or grinder pump lifts wastewater from fixtures that sit too low to reach the sewer by gravity. It is sewage equipment. A sump pump in a groundwater basin is the other machine.</p>
      <h2>When you actually need one</h2>
      <p>A basement bath, a low laundry, or a fixture added below the building drain needs a pump if the pipe cannot fall toward the sewer. Littleton's code says that when a structure sits too low for gravity, the owner installs and maintains the lifting facility. Aurora's pages used here do not publish a separate ejector ordinance, so do not pretend they do. The practical test is the elevation: if the new toilet is below the line leaving the house, gravity will not do the job. That shows up in <a href="/services/remodel-addition-plumbing/">remodels</a>.</p>
      <p>The basin, the pump, the vent, and the check valve are the scope. What it discharges to is the building drain and then the sewer, not the yard like a sump. Lakewood tells its city-sewer customers never to tie a sump into the sewer. An ejector is the device that is supposed to send sewage into the sanitary line. Do not swap the names on the invoice.</p>
      <h2>Failures</h2>
      <p>A pump that runs and does not empty, an alarm, or sewage at a low floor drain can be a failed pump, a stuck float, or a check valve. It can also be a clogged <a href="/services/sewer-line-repair/">service line</a> downstream, which no new pump will fix. If upstairs fixtures drain and only the basement comes back, look at the pump. If the whole building backs up, look at the lateral. In Aurora that lateral is yours to the tap.</p>
      <p>Electrical connections and alarms are not described here. Ask who services them.</p>
      """ + qas([
        ("Is an ejector a sump pump?", "No. A sump moves groundwater and should not tie into the sanitary sewer. An ejector moves sewage from fixtures that are too low for gravity, into the sanitary drain. The basins are not interchangeable. A quote that uses one word for both is unclear."),
        ("The basement toilet backs up but upstairs is fine.", "That pattern fits the ejector or the short run from those fixtures, more than the street lateral. If every floor backs up, stop and camera the service line. In Aurora you maintain that line to the tap. A new pump will not open a collapsed lateral."),
        ("Who maintains it?", "You do, once it is on the property. Littleton's code says the owner keeps the lift facility when gravity will not reach the public sewer. Aurora does not need a copied sentence to make the same practical point: the city main is not the basin in your floor."),
        ("Does this need a permit?", "Adding a bathroom that needs a pump is remodel plumbing, and permitted work in Aurora is inspected before it is covered. Replacing a failed pump in an existing basin may be a repair. Ask the building department which one this is before the floor is closed."),
      ]) + "</article>"
    return _page("/services/sewer-ejector-pumps/", "Sewer ejector pumps in Aurora | Aurora Plumbing Guide", "Pumps for below-grade sewage, kept separate from groundwater sump pumps and from a broken lateral.", "Sewer ejector pumps in Aurora", "Ejector pumps", "sewer ejector pump repair Aurora CO", "service", body)


def backwater(site):
    del site
    body = """
    <article class="sheet">
      <p class="eyebrow">Sewage, not drinking water</p>
      <h1>Backwater valves in Aurora</h1>
      <p class="lede">A backwater valve is meant to stop sewage from flowing back into the building. It is not the backflow preventer on a drinking-water or irrigation line. Buying the wrong device does not solve the backup you have.</p>
      <h2>What it does and what it does not</h2>
      <p>If the city main surcharges, a valve on your building drain can close so sewage does not enter the lowest fixtures. It does not clear a clog in your own lateral. It does not replace a broken pipe. In Aurora, if the break is on your service line, you still maintain that line to the tap. A valve downstream of a collapse does not fix the collapse. Camera first: <a href="/services/sewer-camera-inspection/">sewer camera</a>, then <a href="/services/sewer-line-repair/">repair</a> if the pipe is broken.</p>
      <p>Lakewood's sewer graphic, for its north Lakewood city customers, shows a backflow prevention device that shuts to keep sewage out of the house, and it says the Colorado Plumbing Code requires that kind of device for some properties. It also shows a sewer relief valve and cleanout that can send water to the yard if the main is blocked. Those are Lakewood's drawing for Lakewood's city sewer, about 8,000 customers, not a map of every district and not an Aurora ordinance. Do not install from the drawing. Ask a plumber whether this building is one of the "some properties," and ask the inspector.</p>
      <h2>Not a potable backflow assembly</h2>
      <p>Irrigation and fire lines use <a href="/services/backflow-preventers/">backflow preventers</a> so yard water does not enter the drinking supply. Different test, different plumber skill, different utility letter. If a water district wrote you about a test on a lawn assembly, you are not on this page.</p>
      """ + qas([
        ("Will a backwater valve fix a broken lateral?", "No. It can block sewage from coming back in during a main surcharge. It does not open a collapsed or rooted pipe. If the camera shows a defect on your Aurora service line, you still own the repair to the tap. The valve is an add-on, not a substitute."),
        ("Is this required on every Aurora house?", "This guide will not say that. Lakewood's city graphic says the plumbing code requires a sewage backflow device for some properties, and that graphic is for the city's own north Lakewood customers. Aurora's wastewater page does not repeat that sentence. Ask the inspector for the address."),
        ("The utility sent a test notice. Is it this valve?", "Probably not. Test notices are usually for drinking-water backflow assemblies on irrigation or fire lines. A sewer backwater valve is in the drain. Read the notice. If it names a lawn or a fire line, use the backflow page."),
        ("Can I maintain it myself?", "You can be the person who knows it exists and who calls when it sticks. This page will not give installation or service steps. A stuck valve can either let sewage in or stop your own drains. Ask the installer where it sits and how you will know it failed."),
      ]) + "</article>"
    return _page("/services/backwater-valve-installation/", "Backwater valves in Aurora | Aurora Plumbing Guide", "Sewage backwater valves versus drinking-water backflow preventers, and why a valve does not fix a broken lateral.", "Backwater valves in Aurora", "Backwater valves", "backwater valve installation Aurora CO", "service", body)


def backflow(site):
    del site
    body = """
    <article class="sheet">
      <p class="eyebrow">Drinking water, kept separate</p>
      <h1>Backflow preventers in Aurora</h1>
      <p class="lede">A backflow preventer stops water from an irrigation system, a boiler, or another non-drinking use from being pulled back into the potable supply. It is not a sewer backwater valve.</p>
      <h2>Why a letter shows up</h2>
      <p>Utilities test these assemblies because a failed device is a cross connection. Englewood's permit page lists adding or replacing backflow preventers among work that needs a permit. This guide did not retrieve Aurora's testing calendar, so it will not invent an annual deadline or a fine. If your water utility mailed you, the deadline and the device location are on that letter. Bring the letter to the tester. Do not assume it is about the sewer.</p>
      <p>The person who tests and signs the report often has to hold a tester certification the utility accepts. Ask for that before you hire a general handyman. This website is not that tester and does not file the report for you.</p>
      <h2>Repair versus a new assembly</h2>
      <p>A test can fail on a check valve or a relief valve that can be repaired, or it can fail because the assembly is the wrong type or frozen and split. Repair and replacement are different prices. Ask which. Irrigation blow-outs for <a href="/services/plumbing-winterization/">winterization</a> should not be forced through an assembly that is not meant to see compressor pressure. Ask the tester.</p>
      <p>Sewage devices stay on <a href="/services/backwater-valve-installation/">the backwater page</a>.</p>
      """ + qas([
        ("Is this the valve in the sewer line?", "No. Backflow preventers are on the drinking-water side, often on irrigation or fire piping. A backwater valve is in the drain to stop sewage. The mail from a water utility is almost always the drinking-water device. Read the location on the notice."),
        ("Does Aurora require a test every year?", "Not from a schedule this guide retrieved. Do not let a contractor invent a city fine. Use the letter from the utility that serves the address. Englewood does say that adding or replacing the device needs a building permit. Ask your own building department too."),
        ("Can anyone with a wrench sign the test?", "The utility usually wants a tester it recognizes. Ask who signs and where the report is sent. This website does not submit tests. A repair without a passing test may not clear the letter."),
        ("The assembly froze. Is that winterization or a replacement?", "Both conversations. Draining irrigation before a freeze is winterization. A split body is a replacement or a repair after the fact. Put the test of the new assembly on the quote so the utility letter actually closes."),
      ]) + "</article>"
    return _page("/services/backflow-preventers/", "Backflow preventers in Aurora | Aurora Plumbing Guide", "Potable backflow assemblies, utility test letters, and why they are not sewer backwater valves.", "Backflow preventers in Aurora", "Backflow", "backflow testing and repair Aurora CO", "service", body)


ALL2_A = [pipe, repipe, commercial, remodel, inspection, pressure, sump, ejector, backwater, backflow]
