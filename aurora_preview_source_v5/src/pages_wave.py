"""Remaining service, guide, and city pages with sourced or plainly bounded advice."""

from markup import qas


def _page(path, title, description, h1, crumb, keyword, kind, body):
    return {
        "path": path,
        "title": title,
        "description": description,
        "h1": h1,
        "breadcrumb": crumb,
        "intended_keyword": keyword,
        "keyword_status": "Qualitative topic. No search-volume study. Informational preview.",
        "kind": kind,
        "body": body,
    }


def bathtub(site):
    del site
    body = f"""
    <article class="sheet">
      <p class="eyebrow">Tub and shower · same spot or a new layout</p>
      <h1>Bathtub and shower installation in Aurora</h1>
      <p class="lede">Replacing a tub or shower in the same place is a different job from moving the drain. The first is often a fixture and valve swap. The second opens the floor or the wall and can become a permitted remodel.</p>
      <h2>Stay in place, or move the plumbing</h2>
      <p>If the new tub or shower base sits on the same drain and the valve stays in the same bay, the work is access, a new valve, a watertight pan or base, and the finishes around it. Ask whether the existing drain arm is sound and whether the valve can be reached later through a panel. A valve buried behind tile with no access is a future wall opening.</p>
      <p>Moving the drain, adding a second shower head that needs a larger pipe, or turning a tub into a curbless shower changes slope, the trap, and sometimes the joists. That is <a href="/services/remodel-addition-plumbing/">remodel plumbing</a>, not a one-day swap. In Aurora, opening walls and changing drains is the kind of work the inspections page treats as permitted construction, with the permit card on site. Englewood's building page lists a change to a bath or shower valve, and a change to drains, among work that needs a permit. Do not assume a showroom quote includes that permit.</p>
      <h2>What the quote should separate</h2>
      <p>Fixture and valve. Drain work, if any. Wall and waterproofing, which may be a tile trade rather than the plumber. Who pulls the permit, and in which city. Haul-away. What is excluded if the subfloor is rotten once the old tub comes out. A single price that hides a rotten floor becomes a fight on demolition day.</p>
      <p>A leak at the valve that has not soaked the ceiling can stay a <a href="/services/faucet-sink-fixture-repair/">fixture repair</a>. Water under the floor, or a slow drain that also affects the sink, is not a new tub by itself. Check <a href="/services/drain-cleaning/">the drain</a> before you buy the surround. Sewage from the lowest shower is a <a href="/services/sewer-line-repair/">service line</a> question in Aurora, where you maintain the line to the tap.</p>
      {qas([
        ("Is a new tub the same permit as a new layout?", "Not always. A same-location replacement can still need a permit when the valve or the drain changes. Moving the drain or opening the structure is remodel work. Ask the building department for the address which of those this drawing is. Aurora, Englewood, and Centennial do not share one counter."),
        ("Who waterproofs the shower?", "Say it in the quote. Some plumbers set the valve and the drain and leave the pan and tile to someone else. If nobody owns the waterproofing, the leak shows up after the walls are closed. Ask who tests the pan and who comes back if it fails."),
        ("The quote includes a new valve. Is that enough?", "Only if you can reach that valve later. Ask for an access panel or a valve that can be serviced from the front. Also ask whether the old drain arm stays. A pretty surround on a cracked arm is a leak under the floor."),
        ("Should I replace the tub because the shower drains slowly?", "Not first. One slow shower can be hair in the trap. If other fixtures are slow, or sewage comes back, stop and look at the building drain or the Aurora service line. A new tub does not repair a broken lateral."),
      ])}
    </article>
    """
    return _page("/services/bathtub-shower-installation/", "Bathtub and shower installation in Aurora | Aurora Plumbing Guide", "Same-spot tub and shower replacement versus moving the drain, and what the quote should separate.", "Bathtub and shower installation in Aurora", "Tub and shower", "bathtub and shower installation Aurora CO", "service", body)


def faucet(site):
    del site
    body = """
    <article class="sheet">
      <p class="eyebrow">Faucets, sinks, and supply stops</p>
      <h1>Faucet and fixture repair in Aurora</h1>
      <p class="lede">A drip at a spout is usually a cartridge or a washer. Water under the sink, or a stain on the ceiling below, may be a supply line, a trap, or a pipe in the wall. Those are not the same visit.</p>
      <h2>What you can describe before anyone arrives</h2>
      <p>Is the water only at the spout, only under the sink, or both? Does it happen with hot, cold, or either handle? Does the ceiling below get wet when the faucet is off? A spout drip with a dry cabinet is a fixture repair. A wet cabinet with the faucet off is a supply stop, a dishwasher line, or a disposal connection. A wet ceiling with everything off under the sink is <a href="/services/leak-detection/">a leak in the wall or ceiling</a>, not a new faucet.</p>
      <p>Replacing the whole faucet is reasonable when the body is corroded or the finish is done. It is a poor substitute for a pinhole in the hot line in the wall. <a href="/services/pipe-repair-replacement/">Pipe repair</a> is that second job. Replacing every supply pipe in the house is <a href="/services/whole-house-repiping/">repiping</a>, and one bad faucet does not prove it.</p>
      <h2>Install versus repair</h2>
      <p>A new faucet on the same holes, with the same supply stops, is a short visit if the stops still shut. Stops that will not close turn the job into a water shutoff for the house. Ask whether the stops work before the day of the work. A new sink that changes the drain height, or a pot filler that needs a new pipe in the wall, is closer to <a href="/services/remodel-addition-plumbing/">a remodel</a>. Englewood lists a change to water lines among work that needs a permit. Aurora treats plumbing changes as permitted work when the inspections rules apply. Ask for the address.</p>
      <p>Toilets are their own page: <a href="/services/toilet-repair-installation/">toilet repair</a>. A disposal that hums or leaks is <a href="/services/garbage-disposal-repair/">the disposal</a>. Do not buy a faucet to solve either one.</p>
      """ + qas([
        ("The faucet drips. Do I need new pipes?", "Usually no. A drip at the spout with a dry cabinet is a cartridge, a seat, or the faucet body. New pipes are for a leak in the wall, a rotten stop, or repeated pinholes on several lines. Ask the plumber to show you the wet part before you approve a repipe."),
        ("Water is under the sink only when the dishwasher runs.", "That points to the dishwasher hose or its connection, not the spout. A new faucet will not stop it. Ask for that hose and the air gap or the drain loop to be checked. If the cabinet is wet with every fixture off, look for a supply leak instead."),
        ("Can I shut the water at the little valves?", "If they turn and the flow stops, yes, those are the stops for that faucet. If they spin or snap, stop forcing them. The house shutoff, not a guessed street valve, is the next step. In Castle Rock the street valve belongs to the Town. Do not dig for it."),
        ("Does a new kitchen faucet need a permit in Aurora?", "A like-for-like faucet on working stops often stays a repair. Moving the pipe, opening the wall, or changing the drain can cross into permitted work. Englewood specifically lists water-line changes as permit work. Ask the building department for your parcel rather than using a neighboring city's list."),
      ]) + """
    </article>
    """
    return _page("/services/faucet-sink-fixture-repair/", "Faucet and fixture repair in Aurora | Aurora Plumbing Guide", "How to tell a faucet drip from a supply leak, and when a new faucet is the wrong scope.", "Faucet and fixture repair in Aurora", "Faucets and fixtures", "faucet sink and fixture repair Aurora CO", "service", body)


def toilet(site):
    del site
    body = """
    <article class="sheet">
      <p class="eyebrow">One toilet, not the whole sewer</p>
      <h1>Toilet repair and installation in Aurora</h1>
      <p class="lede">A toilet that runs, rocks, or leaks at the base is a toilet job. A toilet that fills from below with other drains is a sewer job. Mixing them up buys the wrong repair.</p>
      <h2>Running, rocking, or leaking at the floor</h2>
      <p>A constant hiss or a tank that refills by itself is usually the flapper or the fill valve. Water on the floor only at the base, with the bowl otherwise normal, is often the wax ring or the closet bolts, especially if the toilet rocks. Those are repairs or a reset of the same toilet. A cracked bowl or a toilet that is being replaced for height or for a remodel is an installation: a new wax or seal, new bolts, and a check that the flange is sound.</p>
      <p>If the flange is broken or sitting below the finished floor, the quote should say so before the new toilet goes down. A pretty toilet on a broken flange leaks into the ceiling of the room below. That is still this page, not a <a href="/services/whole-house-repiping/">repipe</a>.</p>
      <h2>When it is not the toilet</h2>
      <p>Sewage that rises in the bowl when the shower or the laundry runs is not a flapper. In Aurora that can be the building drain or the service line you maintain to the tap. Start with <a href="/services/drain-cleaning/">drain cleaning</a> if it is a clog, and <a href="/services/sewer-line-repair/">sewer repair</a> if a camera shows a break. A sink faucet is <a href="/services/faucet-sink-fixture-repair/">a fixture repair</a>. The label that lumps sinks, toilets, and faucets still describes three different parts.</p>
      <p>A toilet set on a new floor as part of a bathroom rebuild belongs with <a href="/services/remodel-addition-plumbing/">the remodel</a> if the flange height changed. Ask who sets the toilet after the floor is done so it is not left out of both quotes.</p>
      """ + qas([
        ("The toilet runs all day. Is the sewer broken?", "Probably not. A running toilet refills the tank. The flapper or the fill valve is the usual cause. A broken sewer shows up as a backup, often in more than one fixture or at the lowest drain. Fix the run first. Call it a sewer only if waste is coming the wrong way."),
        ("There is water at the base. Do I replace the toilet?", "Not automatically. A rock, a loose bolt, or a failed wax ring can wet the floor on a sound bowl. Replace the toilet when the porcelain is cracked or you are changing the fixture. Ask the quote to say whether the flange is included."),
        ("Other drains gurgle when this toilet flushes.", "That is a vent or a drain problem, not a flapper. A new toilet will not add a vent. If the gurgle comes with a backup, look at the building drain and, in Aurora, the owner-maintained service line. Get a camera before you replace porcelain."),
        ("Does a new toilet need a permit?", "Swapping a toilet on a sound flange is often handled as a repair. Changing the drain, the flange in a new floor, or the room layout can need a permit from the city or county of the parcel. Englewood lists drain changes as permit work. Ask for your address."),
      ]) + """
    </article>
    """
    return _page("/services/toilet-repair-installation/", "Toilet repair and installation in Aurora | Aurora Plumbing Guide", "Running toilets, base leaks, and the point where the problem is the sewer instead of the fixture.", "Toilet repair and installation in Aurora", "Toilets", "toilet repair and installation Aurora CO", "service", body)


def disposal(site):
    del site
    body = """
    <article class="sheet">
      <p class="eyebrow">Under the sink</p>
      <h1>Garbage disposal repair in Aurora</h1>
      <p class="lede">A disposal that hums, leaks, or will not turn is a small machine with a plumbing connection and an electrical one. This page will not tell you how to wire it. It will tell you which failure is which.</p>
      <h2>Jam, leak, or a dead unit</h2>
      <p>A hum with no spin is often a jam. Many units have a reset button on the bottom and a hex socket to turn the plate free. If you are comfortable using those, and the power is off at the switch, that is the manufacturer's own reset, not a wiring job. If the unit is silent, trips the breaker, or smells hot, stop. Replacing the electrical connection is not a home project described here.</p>
      <p>A leak from the dishwasher hose or the sink flange is plumbing. A leak from a crack in the disposal body is a replacement. A new unit still has to match the sink opening and the dishwasher connection. Ask the quote to include the cord or the hardwired connection as a separate line so an electrician is not a surprise. This guide does not provide wiring steps.</p>
      <h2>What does not belong in a disposal</h2>
      <p>Aurora's service-line page tells people to keep grease and food scraps out of the drain. Lakewood's sewer graphic, for customers on the city's own sewer, says egg shells, coffee grounds, fat, and grease form a clog and do not belong in the disposal. A new disposal will not cure a grease clog further down the line. If the sink and the dishwasher both back up, read <a href="/services/drain-cleaning/">drain cleaning</a>. If lower fixtures back up too, the problem may be the <a href="/services/sewer-line-repair/">service line</a>.</p>
      <p>A dripping faucet above a working disposal is <a href="/services/faucet-sink-fixture-repair/">the faucet</a>. Do not replace both because one quote bundled them without saying which part failed.</p>
      """ + qas([
        ("It hums and does not spin. Is it dead?", "Not always. A jam can hum. The reset on the unit and a manual turn, with the switch off, are the checks the manufacturer expects. If it is hot, silent, or tripping a breaker, stop and have it replaced or repaired by someone who can deal with the wiring. This page will not walk through that wiring."),
        ("It leaks onto the cabinet floor.", "Find the seam. The sink flange and the dishwasher hose are plumbing connections. A crack in the housing means a new unit. A quote should say which of those it saw. A new faucet does not fix a cracked disposal body."),
        ("Will a new disposal fix a slow drain?", "Only if the blockage is inside the disposal. Grease and food further down the pipe remain. Aurora and Lakewood both warn against putting grease and heavy scraps into the drain. If several fixtures are slow, clean or camera the line instead of buying another disposal."),
        ("Who hooks up the power?", "Ask before the day of the job. Some units plug in. Some are hardwired. Hardwiring is electrical work, and this guide does not describe it. Put that line on the quote so the plumber and the electrician are not each assuming the other will finish."),
      ]) + """
    </article>
    """
    return _page("/services/garbage-disposal-repair/", "Garbage disposal repair in Aurora | Aurora Plumbing Guide", "Jam versus leak versus replacement, without wiring instructions, and what still belongs in the trash.", "Garbage disposal repair in Aurora", "Disposals", "garbage disposal repair and installation Aurora CO", "service", body)


def frozen(site):
    del site
    body = """
    <article class="sheet">
      <p class="eyebrow">A burst or a freeze, right now</p>
      <h1>Frozen pipe repair in Aurora</h1>
      <p class="lede">A frozen pipe and a pipe that has already split are urgent. Thawing it with an open flame is not a method this guide will describe. Preventing a freeze next fall is a different page.</p>
      <h2>Stop the water if you can do it safely</h2>
      <p>If water is spraying, the useful step you can take without tools on a gas appliance is to close the indoor house shutoff, if you already know where it is and it turns. Do not hunt for a street valve. In Castle Rock the Town says the curb stop is theirs, tells customers not to operate it, and publishes 720-733-6000 for a curb shutoff. That number is the Town's, for houses on Castle Rock Water, and it is not a link here. Aurora's pages reviewed for this guide do not give a homeowner procedure for the utility's valve. Call the utility that bills the address.</p>
      <p>Do not use a torch, a grill, or any open flame on a pipe. Do not pour boiling water on a fixture you cannot see behind a wall. If you smell gas, leave and call the gas utility or emergency services. A frozen water line is not a reason to open a gas fitting. Gas work is <a href="/services/gas-line-repair-installation/">its own page</a>, and it is not a set of steps.</p>
      <h2>After the water is stopped</h2>
      <p>The repair is whatever split: a supply line in a crawl space, a hose bib, or a section in an exterior wall. That is <a href="/services/pipe-repair-replacement/">pipe repair</a> unless the failure is the buried service from the main, which is <a href="/services/water-line-repair/">the water service</a>. One burst elbow does not prove the whole house needs new pipe. Ask the plumber to show the split.</p>
      <p>Keeping the house from freezing next time, draining a vacant property, and disconnecting hoses is <a href="/guides/frozen-pipe-vs-winterization/">winterization, not this emergency</a>. Castle Rock publishes freeze tips for its customers. Follow that town's page if you are on their water. Do not treat those tips as a license to thaw a gas line.</p>
      """ + qas([
        ("Can I thaw the pipe with a flame?", "No. This guide will not describe flame, torches, or other open heat on a pipe. If water is spraying, close the indoor shutoff you already know how to use, and call a plumber. If you smell gas, leave the building and call the gas utility or emergency services."),
        ("Should I close the valve at the street?", "Not by guesswork. Castle Rock tells its customers the street valve is the Town's and to call 720-733-6000 instead of operating it. Other utilities are not that sentence. Use the indoor shutoff if you can, and call the utility on your bill for the curb."),
        ("The pipe split. Do I repipe the house?", "Not from one split. Repair the section that failed, then ask whether other exposed pipes are at the same risk. Whole-house repiping is a different project. A buried leak between the main and the house is a water-service repair, not an indoor repipe."),
        ("How is this different from winterization?", "Winterization is what you do before a vacant house or a hose bib freezes. This page is the burst or the freeze that is happening now. Drain-down and hose removal belong on the winterization page. They do not stop water that is already on the floor."),
      ]) + """
    </article>
    """
    return _page("/services/frozen-pipe-repair/", "Frozen pipe repair in Aurora | Aurora Plumbing Guide", "What to do when a pipe freezes or splits, without open-flame thawing, and when the job is the buried water service.", "Frozen pipe repair in Aurora", "Frozen pipes", "frozen pipe repair Aurora CO", "service", body)


def winterization(site):
    del site
    body = """
    <article class="sheet">
      <p class="eyebrow">Before the cold, not during a flood</p>
      <h1>Plumbing winterization in Aurora</h1>
      <p class="lede">Winterization is prevention. You are draining or protecting lines that will sit in a cold house, a crawl space, or an outdoor faucet. If a pipe has already split, you are on the frozen-pipe page instead.</p>
      <h2>What people usually mean</h2>
      <p>Disconnect garden hoses so an outdoor faucet does not stay full. Know where the indoor shutoff is before you need it. Ask a plumber, for a house that will sit empty, which lines they will drain and which fixtures they will leave. A vacant house with the heat off is a different plan from a house you still live in. This guide will not give a valve-by-valve script, because the layout is the house's, not a generic diagram.</p>
      <p>Sprinkler systems are often a separate shutoff and a blow-out. Ask whether that is included. An irrigation blow-out uses a compressor and can damage a backflow assembly if it is done on the wrong side. <a href="/services/backflow-preventers/">Backflow preventers</a> are drinking-water devices. Do not treat them as a hose bib.</p>
      <h2>What this is not</h2>
      <p>It is not <a href="/services/frozen-pipe-repair/">a burst that is happening today</a>. It is not a sewer cleaning. It is not a reason to open a gas line. Castle Rock's water utility publishes its own cold-weather notes for customers on Town water, including not operating the street valve. If that is your utility, use their page. Aurora Water's pages used here do not publish a homeowner winterization procedure, so this guide will not invent one and call it Aurora's.</p>
      <p>Compare the two jobs on <a href="/guides/frozen-pipe-vs-winterization/">frozen pipe versus winterization</a> before you book the wrong visit.</p>
      """ + qas([
        ("The pipe already burst. Is this the right job?", "No. Shut the indoor water if you can do that safely and read the frozen-pipe page. Winterization is the visit before a freeze, or the drain-down of a house that will be empty. It does not repair a split that is already spraying."),
        ("Should the plumber blow out the sprinklers too?", "Only if the quote says so. Irrigation shutoff and a compressor blow-out are easy to leave off a 'winterize the house' line. Ask whether the backflow assembly on the irrigation is included, and do not run a compressor through a device that is not built for it."),
        ("Does Aurora Water publish a winterizing checklist?", "Not on the wastewater or service-line pages used for this guide. Do not treat a generic list as the utility's rule. Castle Rock does publish cold-weather notes for its own customers. Match the advice to the utility on the bill."),
        ("Do I drain the water heater?", "Ask before you do it. Draining a tank that is your only heat source for hot water, or a tank with a closed valve and a flame, is not a casual step. If the house will be empty and unheated, the plumber should say whether the tank stays full, gets drained, or is turned off, and who relights a gas heater later. This site will not give relighting steps."),
      ]) + """
    </article>
    """
    return _page("/services/plumbing-winterization/", "Plumbing winterization in Aurora | Aurora Plumbing Guide", "Drain-down and hose-bib protection before a freeze, kept separate from an emergency burst pipe.", "Plumbing winterization in Aurora", "Winterization", "plumbing winterization Aurora CO", "service", body)


def general(site):
    del site
    body = """
    <article class="sheet">
      <p class="eyebrow">Several small problems, one visit</p>
      <h1>General plumbing repair in Aurora</h1>
      <p class="lede">Use this page when you have more than one ordinary fixture problem and none of them is a sewer backup, a gas leak, or a buried water main. It is not a second homepage, and it is not a junk drawer for every pipe in the house.</p>
      <h2>What fits in one service call</h2>
      <p>A dripping <a href="/services/faucet-sink-fixture-repair/">faucet</a>, a running <a href="/services/toilet-repair-installation/">toilet</a>, a stuck stop, and a sweating supply line under a bath can be one list. The quote should name each item and say what is excluded if something else is found. A trip fee that then becomes a repipe, with no new approval, is not a general repair.</p>
      <p>Leave this page when the symptom changes the trade. No hot water is a <a href="/services/water-heater-repair/">heater</a>. Sewage at a floor drain is a <a href="/services/drain-cleaning/">drain</a> or a <a href="/services/sewer-line-repair/">service line</a>. A wet yard is <a href="/services/leak-detection/">leak detection</a>. A smell of gas is <a href="/services/gas-line-repair-installation/">gas</a>, and you leave the house first.</p>
      <h2>Keep the list short enough to price</h2>
      <p>Write down the room, the fixture, and whether the water is clean or sewage. That is enough for a general-repair visit. It is not enough for a remodel. Moving walls or adding a bathroom is <a href="/services/remodel-addition-plumbing/">remodel plumbing</a>. An inspection of the whole house with a written report, and no repair that day, is <a href="/services/plumbing-inspection/">a plumbing inspection</a>.</p>
      <p>In Aurora, small fixture repairs often stay repairs. Changing drains, opening walls, or replacing a water heater can need a permit. The <a href="/guides/aurora-water-heater-permits/">heater permit guide</a> is only for the heater. Ask the building department about the rest rather than assuming the faucet list covers a bathroom gut.</p>
      """ + qas([
        ("I have a drip and a running toilet. Is that one job?", "Yes, if that is really all. Put both on the list so the quote names each one. It stops being general repair if the plumber finds sewage backing up, a leaking tank shell, or a pipe in the wall. Those have their own pages and their own scope."),
        ("Can this visit include the water heater?", "Only as a look, unless the quote says repair or replacement. A new tank in Aurora is permitted work, and same-day inspection is not guaranteed. Do not let a 'while we're here' become a heater swap you did not approve."),
        ("Is general repair the same as repiping?", "No. General repair fixes the fixtures you listed. Repiping replaces supply pipes through the house. One bad faucet is not that project. Ask for the failed part before you approve a whole-house number."),
        ("What if I smell gas during the visit?", "Stop. Leave if the odor is strong, and call the gas utility or emergency services. A general plumbing list does not include opening gas pipe. The gas page explains the boundary. It does not give installation steps."),
      ]) + """
    </article>
    """
    return _page("/services/general-plumbing-repair/", "General plumbing repair in Aurora | Aurora Plumbing Guide", "A visit for several ordinary fixture repairs, and the symptoms that belong on a different page.", "General plumbing repair in Aurora", "General repair", "general plumbing repairs Aurora CO", "service", body)


ALL = [bathtub, faucet, toilet, disposal, frozen, winterization, general]
