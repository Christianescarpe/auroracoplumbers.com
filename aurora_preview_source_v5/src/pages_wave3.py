"""Treatment, gas, trenchless, specialty limits, guides, and newly sourced cities."""

from markup import qas
from pages_wave import _page


def treat_install(site):
    del site
    body = """
    <article class="sheet">
      <p class="eyebrow">Only after a test</p>
      <h1>Water treatment installation in Aurora</h1>
      <p class="lede">A filter or a softener is a response to a test of the water at the house, not to a slogan about the Front Range. This guide did not review an Aurora hardness report and will not invent one.</p>
      <h2>What has to be known first</h2>
      <p>Ask what was measured, at which tap, and on which utility. Aurora Water, a Denver Water distributor in Centennial, and Castle Rock Water are not the same supply. A whole-house softener on a house with a single bad faucet cartridge is the wrong tool. Taste or odor at one tap can be that faucet. Read <a href="/services/faucet-sink-fixture-repair/">fixture repair</a> before you plumb a system into the main.</p>
      <p>The installer should say what the unit removes, what it does not, where it sits relative to the water heater, and how it backwashes or regenerates. A drain for that discharge has to go somewhere allowed. Do not send brine into a place the city has not accepted. This page does not size the unit.</p>
      <h2>Not a repair of a unit you already own</h2>
      <p>If a softener is already in the garage and it is stuck, overflowing, or beeping, that is <a href="/services/water-treatment-repair/">treatment repair</a>. Selling a second system without saying the first one failed is a new sale. Pressure problems are <a href="/services/water-pressure-problems/">pressure</a>, not hardness.</p>
      <p>No contractor is dispatched from this page.</p>
      """ + qas([
        ("Is Aurora water hard enough to need a softener?", "This guide will not say. No citywide hardness figure was used here. Houses on different utilities do not share one number. Ask for a test at your tap and for the contaminant the equipment claims to treat. A softener sold without that test is a guess."),
        ("Where should it connect?", "The quote should say whether it treats the whole house or one faucet, and whether the water heater and the outside hose bibs are included or bypassed. A unit that backwashes needs a drain. Ask where that water goes."),
        ("Can it fix low pressure?", "Not if the pressure problem is a regulator, a closed valve, or the utility. Treatment adds equipment. It does not replace a failed pressure valve. Measure the problem before you add a tank."),
        ("Is this the same as a backflow test?", "No. Treatment changes the water you chose to treat. A backflow preventer keeps irrigation or other water out of the drinking supply. Different device, different letter from the utility."),
      ]) + "</article>"
    return _page("/services/water-treatment-installation/", "Water treatment installation in Aurora | Aurora Plumbing Guide", "Filters and softeners only after a test at the house, with no citywide hardness claim.", "Water treatment installation in Aurora", "Treatment installation", "water filtration and treatment installation Aurora CO", "service", body)


def treat_repair(site):
    del site
    body = """
    <article class="sheet">
      <p class="eyebrow">The unit you already have</p>
      <h1>Water treatment repair in Aurora</h1>
      <p class="lede">Repair means the filter or softener that is already installed is leaking, stuck, or out of salt and still not working. A new system is a different sale.</p>
      <h2>What failed</h2>
      <p>A softener can stick in regeneration and send water to the drain all day, or it can stop drawing brine. A filter can clog and cut pressure to the house. Ask which of those the technician saw. A clogged filter that drops pressure should not become a <a href="/services/whole-house-repiping/">repipe</a>. A softener that never should have been installed, because nobody tested the water, is still a repair of that machine, plus a hard look at whether you need it. New equipment is <a href="/services/water-treatment-installation/">installation</a>.</p>
      <p>This guide still has no Aurora hardness number. Do not let a repair visit invent one to sell a larger tank.</p>
      <h2>Leaks and drains</h2>
      <p>A unit that overflows can rot the floor. The quote should say whether the leak is a fitting, a valve, or the tank. The drain line should still go to an allowed outlet. If the only symptom is low pressure at one faucet, start with <a href="/services/water-pressure-problems/">pressure</a> and the faucet, not the softener.</p>
      """ + qas([
        ("It is using salt but the water still spots. Is it broken?", "Maybe the unit is not regenerating, or it is bypassed, or the spots are not hardness. Ask for a test before and after the unit. Replacing it without that test repeats the original guess. This page will not call the city's water hard."),
        ("Water runs to the floor from the softener.", "That is a leak or a drain line that came loose, not a reason to repipe the house. Ask which fitting failed. If the unit is in regeneration all day, the control or the valve may be stuck. Those are repairs of this machine."),
        ("Should I replace it during the repair?", "Only when parts are gone or the tank is failed, and only if you still want treatment after a test. A functioning repair is cheaper to compare when the quote shows the part. A new system is the installation page."),
        ("Will a repair fix city pressure?", "No. A softener is not the utility's main. If the whole neighborhood is low, call the water utility. If only the pipes after the softener are weak, the unit may be clogged. Say which side of the softener was measured."),
      ]) + "</article>"
    return _page("/services/water-treatment-repair/", "Water treatment repair in Aurora | Aurora Plumbing Guide", "Repair of an existing filter or softener, kept separate from selling a new system.", "Water treatment repair in Aurora", "Treatment repair", "water treatment system repair Aurora CO", "service", body)


def gas(site):
    del site
    body = """
    <article class="sheet">
      <p class="eyebrow">No do-it-yourself steps</p>
      <h1>Gas line work in Aurora</h1>
      <p class="lede">If you smell gas, leave. Call the gas utility's emergency line or emergency services from outside. This page will not tell you how to find a leak, tighten a fitting, or size a pipe.</p>
      <h2>What a plumber or a gas fitter is being asked to do</h2>
      <p>Adding a line for a range, moving a meter set, or replacing a corroded section is permitted work in the cities that publish plumbing and gas rules. Englewood lists adding or altering heating or plumbing, and replacing a water heater, among jobs that need a permit. Aurora's inspection list includes gas-pipe inspections on permitted work. Centennial's one-stop schedule names a gas line among items that can be a short review, which is not permission to skip the permit. Castle Rock wants gas-load calculations when the appliance is a tankless water heater. None of those sentences is a field manual.</p>
      <p>The quote should say who pulls the permit, who shuts the meter with the utility's knowledge, and which appliances are reconnected. It should not include a how-to for you. A water-heater replacement that also replaces a connector can brush this scope. Ask. The heater pages do not teach gas either.</p>
      <h2>What this site will not do</h2>
      <p>It will not describe soap tests, flame color, or pipe sizing. It will not tell you to open a union. After the utility says the building is safe to enter, a licensed person does the repair. If the smell is strong, do not stay to read the rest of this page.</p>
      """ + qas([
        ("I smell gas. What do I do?", "Leave the building. Do not switch lights or hunt for the fitting. From outside, call the gas utility's emergency number or emergency services. This website is not that number, and it will not describe how to tighten or light anything."),
        ("Does a new gas line need a permit?", "Plan on yes. Englewood lists alterations to plumbing and fuel-burning appliances as permit work. Aurora inspects gas pipe on permitted jobs. Centennial lists a gas line on its one-stop schedule, which is still a permit. Ask the building department for the address. Do not start from a blog."),
        ("Can the water-heater plumber add a gas line?", "Only if the quote says so and they are allowed to pull that permit. A tank swap and a new gas run are different scopes. Castle Rock adds gas-load math for tankless heaters. Ask for that sheet when the appliance is tankless there."),
        ("Will you give sizing steps if I measure the pipe?", "No. Sizing, threading, and testing stay with the person who will sign the permit. Measuring your own pipe does not make this page a manual."),
      ]) + "</article>"
    return _page("/services/gas-line-repair-installation/", "Gas line work in Aurora | Aurora Plumbing Guide", "Permit boundaries for gas piping, and what to do if you smell gas. No installation steps.", "Gas line work in Aurora", "Gas lines", "gas line repair and installation Aurora CO", "service", body)


def trenchless(site):
    del site
    body = """
    <article class="sheet">
      <p class="eyebrow">A method, after the video</p>
      <h1>Trenchless sewer repair in Aurora</h1>
      <p class="lede">Trenchless repair means a liner or a bursting tool instead of an open trench along the whole lateral. It is a method. It is not a promise that your pipe qualifies, and it is not a city program.</p>
      <h2>What has to be true</h2>
      <p>Someone has to see the pipe. A <a href="/services/sewer-camera-inspection/">camera</a> should show material, the breaks, the offsets, and whether the camera reached the tap. A collapsed section, a belly full of water, or a joint pulled apart can rule a liner out. Clay, which Aurora says is possible on older homes, is a reason to look, not a reason to pick a product from the year the house was built. Compare the open-cut option on <a href="/guides/trenchless-vs-open-cut/">trenchless versus open cut</a>.</p>
      <p>In Aurora you still own the service line through the tap, including street repair if the work opens the street. A "trenchless" quote that still needs a pit at each end should say where those pits are and who restores them. If the tap itself is being replaced, the street may be open anyway. <a href="/services/sewer-line-repair/">Sewer line repair</a> is the broader decision. This page is only the no-trench-or-less-trench choice.</p>
      <h2>What not to believe</h2>
      <p>No method is safe for every pipe. No price is printed here. The City's free video review can be a second opinion before you approve a liner. We do not submit the file. A contractor is not dispatched from this page.</p>
      """ + qas([
        ("Does trenchless avoid digging entirely?", "Often no. Many methods still need access pits. Ask where they are, how big they are, and who patches the yard or the street. In Aurora, street damage from your service line or tap is the owner's. A slogan that says no dig is not a scope."),
        ("Will it work on a collapsed clay pipe?", "Not as a blanket yes. A liner needs a path and a host pipe that can hold it. A collapse or a large offset can force an open repair. The camera, not the brochure, decides. Aurora's note that older homes can have clay is only a hint."),
        ("Is this cheaper because the city helps?", "Aurora does not publish a trenchless program that pays for the lateral. You still maintain the service line to the tap. The free help Aurora offers is a review of your video, not a crew to line the pipe. Confirm that limit before you compare quotes."),
        ("How is this different from jetting?", "Jetting cleans roots and grease. It does not rebuild a broken pipe. Trenchless repair is supposed to replace or line the structure. Do the camera before either one is sold as the fix."),
      ]) + "</article>"
    return _page("/services/trenchless-sewer-repair/", "Trenchless sewer repair in Aurora | Aurora Plumbing Guide", "When a liner or burst might fit an Aurora lateral, and what the camera has to show first.", "Trenchless sewer repair in Aurora", "Trenchless", "trenchless sewer repair Aurora CO", "service", body)


def mobile(site):
    del site
    body = """
    <article class="sheet">
      <p class="eyebrow">The lot still has a building department</p>
      <h1>Mobile home plumbing in Aurora</h1>
      <p class="lede">A manufactured home is not a basement house. The pipes are often under the floor, behind skirting, and the fittings may not match a site-built residence. The permit still belongs to the city or county where the lot sits. This guide did not retrieve a separate manufactured-housing plumbing code, and it will not invent one.</p>
      <h2>Access and parts</h2>
      <p>Ask whether the repair is above the floor, like a faucet, or under the home. Under-home work needs a safe way in, a sound belly board, and sometimes a different connector than a copper stub in a crawl space. If the skirting has to come off, say who puts it back. A quote that assumes a basement will be wrong on the day.</p>
      <p>The water and sewer leaving the home still meet a utility. In Aurora, an Aurora Water customer still has the city's service-line rules for the pipes in the ground: sewer to the tap is the owner's, and the water service to the main is the owner's. The factory-built piping under the floor is not that buried service. Do not blend them into one price without saying which failed. If the lot is in unincorporated Douglas County, the permit counter is the county, as with <a href="/areas/highlands-ranch/">Highlands Ranch</a>, not a fictional mobile-home city.</p>
      <h2>What was not verified</h2>
      <p>HUD or state manufactured-home rules for plumbing alterations were not read for this draft. Do not treat this page as those rules. Ask the building department whether a licensed plumber, a manufacturer-approved method, or both are required before you open the floor. Ordinary fixture repairs that match <a href="/services/faucet-sink-fixture-repair/">faucets</a> or <a href="/services/toilet-repair-installation/">toilets</a> may still be the right scope when the failure is the fixture, not the under-home trunk.</p>
      """ + qas([
        ("Does Aurora have a separate mobile-home plumbing permit?", "Not one this guide retrieved. The lot is still in a city or a county. An Aurora address uses Aurora's building division. A home on a lot in unincorporated Douglas County uses the county. Ask which parcel you are on before you assume a park office is the permit counter."),
        ("Is the pipe under the floor the city's?", "No. Under-floor piping belongs with the home. The buried water service and sewer lateral are the utility question. In Aurora those buried lines follow Aurora Water's split, which is not a rule for the belly of the house. The quote should name which pipe failed."),
        ("Can you use the same parts as a site-built house?", "Not always. Supply connectors under manufactured homes are often a different material and a different fitting. A plumber who brings only house copper may be guessing. Ask what is under there before the parts are purchased."),
        ("Was a special code checked for this page?", "No. A manufactured-housing plumbing code was not retrieved. This page only separates access, fittings, and the utility line, and it tells you to ask the building department. It is not a waiver and not a spec."),
      ]) + "</article>"
    return _page("/services/mobile-home-plumbing/", "Mobile home plumbing in Aurora | Aurora Plumbing Guide", "Under-home access and fittings, the lot's real permit office, and what this guide did not verify.", "Mobile home plumbing in Aurora", "Mobile homes", "mobile home plumbing Aurora CO", "service", body)


def pool(site):
    del site
    body = """
    <article class="sheet">
      <p class="eyebrow">Pipes and leaks only</p>
      <h1>Pool and spa plumbing in Aurora</h1>
      <p class="lede">This page is about the pipes, valves, and leaks on a pool or spa. It is not chemical care, and it is not electrical work on a pump motor or a heater element.</p>
      <h2>What a plumbing scope can include</h2>
      <p>A leaking union, a cracked valve, a suction or return line that will not hold, and the piping at the equipment pad. Ask whether the leak is above ground, where you can see it, or underground between the pad and the pool. An underground water line to the house is <a href="/services/water-line-repair/">a domestic water service</a>, not pool plumbing. A drinking-water <a href="/services/backflow-preventers/">backflow preventer</a> on the fill line is its own test.</p>
      <p>Centennial's review schedule lists a residential swimming pool or spa with additions at 10 business days, and a multifamily pool on the commercial-style list. That is a construction permit, not a weekly vacuum. Aurora's published permit pages do not give a matching pool timetable. Ask Aurora's building division before you pour a new shell. Do not copy Centennial's calendar onto an Aurora lot.</p>
      <h2>What this guide will not claim</h2>
      <p>It will not balance chemicals, open a breaker panel, or size a gas pool heater. Gas work stays on <a href="/services/gas-line-repair-installation/">the gas page</a>, which has no steps. If the only problem is green water, you do not need this page. If the pump will not prime because a pipe sucks air, you might.</p>
      """ + qas([
        ("Do you cover pool chemicals or the pump wiring?", "No. This page is pipes, valves, and leaks. Motors, heaters, and water chemistry are other trades. A quote that mixes them should say who does the electrical and who does the gas. This site will not describe either."),
        ("A new pool in Centennial is a quick permit, right?", "The city's schedule lists a residential pool or spa with additions at 10 business days after a complete submittal, not on the one-stop water-heater list. Multifamily pools are on another line. Those clocks are Centennial's, not Aurora's, and they are not a guarantee."),
        ("The autofill line keeps running. Is that the pool pipe?", "It may be the fill valve or the drinking-water backflow on that line. It may be a leak in the pool shell that is not a plumbing fitting at all. Ask which pipe was isolated. Do not repipe the house supply because the pool level drops."),
        ("Is an underground return line a sewer repair?", "No. Pool circulation water is not sewage. The Aurora sewer lateral is a different pipe, owned by you to the tap. A leak in the yard still needs to be identified before anyone digs, so the sewer and the water service are not cut by mistake."),
      ]) + "</article>"
    return _page("/services/pool-spa-plumbing/", "Pool and spa plumbing in Aurora | Aurora Plumbing Guide", "Pool and spa pipes and leaks only. Not chemicals, not pump wiring, not a copied permit calendar.", "Pool and spa plumbing in Aurora", "Pools and spas", "pool spa and hot tub plumbing Aurora CO", "service", body)


def radiant_i(site):
    del site
    body = """
    <article class="sheet">
      <p class="eyebrow">Water loops, not a furnace</p>
      <h1>Hydronic radiant floor installation in Aurora</h1>
      <p class="lede">Radiant floor heat in this guide means tubes of water in or under a floor, a manifold, and a heat source. It is not a forced-air furnace, and this page does not size ducts or sell air conditioning.</p>
      <h2>What the install has to decide</h2>
      <p>Where the tubes go, what heats the water, how the manifolds are zoned, and what happens if a loop leaks after the floor is finished. Those choices belong in a design, not in a guess on site. This guide will not calculate loop length or water temperature. A plumber who installs tubing without a layout is hoping. Ask for the layout and for who covers a leak in a finished slab.</p>
      <p>The heat source may be a boiler or another water heater used for heat. That appliance can need a gas line and a permit. Gas steps are not on <a href="/services/gas-line-repair-installation/">the gas page</a> either. Aurora inspects gas pipe and plumbing on permitted work. A radiant job that opens floors is remodel-scale. See <a href="/services/remodel-addition-plumbing/">remodel plumbing</a>. It is not a faucet swap.</p>
      <h2>Limits</h2>
      <p>No Aurora ordinance about radiant floors was retrieved. Do not treat this page as code. Electric floor mats are not this system. If someone is selling mats and a boiler as the same product, ask which one is in the contract. Repair of tubes that are already in the floor is <a href="/services/radiant-floor-heating-repair/">radiant repair</a>.</p>
      """ + qas([
        ("Is this an air-conditioning project?", "No. These are water tubes and a heat source. Furnaces, coils, and refrigerant are not this page. If the quote adds an air handler, ask who is licensed for that work. This guide does not describe it."),
        ("Can you publish loop lengths or water temperatures?", "No. That is a design for the house, from the person who will stamp or install it. A webpage number would be fiction. Ask for the layout, the manifold count, and what a leak in the slab costs to reach."),
        ("Does Aurora have a special radiant permit?", "Aurora's published permit pages do not name a separate radiant-floor permit. Opening a floor and adding plumbing and gas still looks like permitted work under the inspection rules. Ask the building division before the slab is poured. A poured floor is a bad time to discover the rough-in was skipped."),
        ("Electric mats versus water tubes?", "Different systems. This page is water. Mats are electric and are not installed from these instructions, because there are no electrical steps here. The contract should say which floor you are buying."),
      ]) + "</article>"
    return _page("/services/radiant-floor-heating-installation/", "Radiant floor installation in Aurora | Aurora Plumbing Guide", "Hydronic floor loops and manifolds, not forced air, and not a made-up Aurora radiant code.", "Hydronic radiant floor installation in Aurora", "Radiant installation", "hydronic radiant floor heating installation Aurora CO", "service", body)


def radiant_r(site):
    del site
    body = """
    <article class="sheet">
      <p class="eyebrow">An existing water loop</p>
      <h1>Hydronic radiant floor repair in Aurora</h1>
      <p class="lede">Repair means the tubes, manifold, circulator, or mixing valve already in the house are leaking or not moving water. It is not a new floor design, and it is not a furnace repair.</p>
      <h2>Find the leak before you open the floor</h2>
      <p>A wet spot on a slab can be a radiant loop, a domestic water line, or even a drain. <a href="/services/leak-detection/">Leak detection</a> matters here because opening a floor is expensive. Ask how the loop will be isolated from the drinking water and from the other zones. A manifold valve that will not close is a smaller repair than a tube under tile.</p>
      <p>A circulator that is hot and silent, or a zone that never heats, can be the pump or the control. Controls can be electrical. This page does not describe wiring. A boiler that will not fire may be gas. Use <a href="/services/gas-line-repair-installation/">the gas page</a> only as a boundary: leave if you smell gas, and do not expect steps.</p>
      <h2>When it becomes a new install</h2>
      <p>Adding zones or replacing a whole floor of tube is <a href="/services/radiant-floor-heating-installation/">installation</a>. One manifold gasket is not that project. No Aurora radiant-repair ordinance was retrieved.</p>
      """ + qas([
        ("The floor is cold in one room. Is the tube broken?", "Not yet. The manifold valve, the actuator, or air in that loop can leave a room cold with the tube intact. Ask for those checks before anyone cuts tile. A pressure test on that zone tells you more than a guess."),
        ("There is a wet stripe on the slab.", "It might be the loop or a domestic pipe in the same floor. Isolate the heating zone and see if the leak stops. Leak detection is the page for finding it. Do not jackhammer on a hunch, and do not assume it is the sewer."),
        ("Can the same person fix the boiler and the thermostat wiring?", "Ask. Gas appliances and line-voltage controls are not automatically the plumber's scope, and this guide gives no wiring or gas steps. The quote should name who does each part."),
        ("Is a repair a new radiant system?", "No. Repair keeps the tubes you have, unless they are failed and being replaced. A new layout, new zones, and a new floor are installation. Make the quote say which."),
      ]) + "</article>"
    return _page("/services/radiant-floor-heating-repair/", "Radiant floor repair in Aurora | Aurora Plumbing Guide", "Existing hydronic loops, manifolds, and circulators. Not a furnace visit and not a new floor design.", "Hydronic radiant floor repair in Aurora", "Radiant repair", "hydronic radiant floor heating repair Aurora CO", "service", body)


def well_i(site):
    del site
    body = """
    <article class="sheet">
      <p class="eyebrow">Only if the house is not on a utility</p>
      <h1>Well pump installation in Aurora</h1>
      <p class="lede">Most Aurora city customers are on a water utility, not a private well. A new well pump is a rural or estate question after you confirm the source. This page does not assume your house has a well, and it does not describe drilling.</p>
      <h2>Confirm the source</h2>
      <p>Look at the bill. Aurora Water, Denver Water, Castle Rock Water, and a well share no equipment. Douglas County tells permit holders to verify water, sewer, well, and septic before they dig. That is the right habit in <a href="/areas/highlands-ranch/">Highlands Ranch</a> and other unincorporated lots. <a href="/guides/well-pump-vs-city-water/">Well versus city water</a> is the comparison. If a main and a meter serve the house, you want <a href="/services/water-line-repair/">the water service</a>, not a pump in a casing.</p>
      <p>A Colorado well permit, if one is required for a new hole, was not quoted chapter and verse here. Ask the state engineer’s office and the county before anyone drills. This website will not file that permit.</p>
      <h2>What an installation quote covers</h2>
      <p>Pump, drop pipe, wire, pressure tank, and the switch, if those are included. Electrical from the panel is a separate trade unless the quote says a licensed electrician is in the price. No wiring steps are on this page. A pressure problem on city water is <a href="/services/water-pressure-problems/">not a well</a>.</p>
      """ + qas([
        ("Does a typical Aurora house need a well pump?", "No. City customers get water from a utility. A well is a private source. Check the bill and the property record before you price a pump. Douglas County says to verify well versus utility before you dig. Do not buy well equipment for a metered city service."),
        ("Can you size the pump here?", "No. Depth, recovery, and the permit are the driller's and the owner's facts. A webpage horsepower would be made up. Ask for the existing well record if the hole is already there."),
        ("Who pulls the electrical permit?", "Whoever the quote names. A pump wire is electrical work. This guide does not describe it. If the plumber supplies only the pump, an electrician may still have to connect it."),
        ("Is a new well the same as a new pump?", "No. A pump in an existing well is not a new hole. Drilling can need a state permit this page does not reproduce. Say which one the contract is before the truck is scheduled."),
      ]) + "</article>"
    return _page("/services/well-pump-installation/", "Well pump installation in Aurora | Aurora Plumbing Guide", "Private-well pumps only after you confirm the house is not on a city or district meter.", "Well pump installation in Aurora", "Well installation", "well pump installation Aurora CO", "service", body)


def well_r(site):
    del site
    body = """
    <article class="sheet">
      <p class="eyebrow">An existing private well</p>
      <h1>Well pump repair in Aurora</h1>
      <p class="lede">Repair applies when a private well already serves the house and the pump, the pressure tank, or the control has failed. It does not apply to a house on Aurora Water or another utility.</p>
      <h2>Symptoms that fit</h2>
      <p>No water, a short cycle of the pressure tank, or a pump that runs and never shuts off. Ask whether the tank has lost its air charge, the switch is failed, or the pump in the casing is done. Those are different parts and different prices. A city-water house with the same "no water" symptom should call the utility and read <a href="/services/water-pressure-problems/">pressure</a>, not this page.</p>
      <p>If the well is in unincorporated Douglas County, remember the county's instruction to know where the well and the septic are before you dig. Repairing a pump does not locate a sewer lateral. Do not confuse the two.</p>
      <h2>Limits</h2>
      <p>No wiring procedure and no well-permit citation are printed here. Replacement of the pump in the hole is closer to <a href="/services/well-pump-installation/">installation</a> if the whole string comes out. A contractor is not sent from this website.</p>
      """ + qas([
        ("We are on Aurora Water and the pressure died. Is it the well?", "No. You do not have this pump. Call Aurora Water if the outage is theirs, and use the pressure page for a house valve or regulator. Well repair is for a private well with a pressure tank, not a city meter."),
        ("The pump runs and will not stop.", "That can be a loss of air in the tank, a bad switch, a leak on the house side, or a pump that cannot build pressure. Ask which test they will run first. Replacing the pump before those checks can be the expensive guess."),
        ("Does the repair include the wire in the well?", "Only if the quote says the drop wire and the pipe come out. Some failures are only the tank in the basement. Make them name the part. Electrical reconnection is not described on this page."),
        ("Can a well repair fix a sewer smell?", "No. A well is supply water. Sewage odor is a drain or a septic or a lateral. Douglas County tells you to know which of those is on the lot. Do not pull a pump to solve a sewer backup."),
      ]) + "</article>"
    return _page("/services/well-pump-repair/", "Well pump repair in Aurora | Aurora Plumbing Guide", "Pressure tank and pump failures on a private well only. City-water houses are a different problem.", "Well pump repair in Aurora", "Well repair", "well pump repair Aurora CO", "service", body)


WAVE3_SERVICES = [
    treat_install, treat_repair, gas, trenchless, mobile, pool, radiant_i, radiant_r, well_i, well_r,
]
