"""Sewer, drain, and camera pages for Aurora, Colorado."""

from markup import INSPECT, SERVICE_LINE, WASTE, ext, qas


def sewer_repair(site: dict) -> dict:
    del site
    body = f"""
    <article class="sheet">
      <p class="eyebrow">Sewer service line · Aurora, Colorado</p>
      <h1>Sewer line repair in Aurora</h1>
      <p class="lede">A backup, a soggy yard, or a camera still of a broken pipe is a different job from a slow bathroom sink. In Aurora the first split is simple and expensive: the city main is Aurora Water's, and the service line from that main to the building is yours, including the connection and the street repair.</p>
      <h2>Which pipe is actually failing</h2>
      <p>Inside the house, a single slow fixture is often a branch clog. <a href="/services/drain-cleaning/">Drain cleaning</a> is the page for that. When several fixtures drain together, a lower-level shower or floor drain fills, or sewage comes back only at the bottom of the house, the problem may be the service line that leaves the building. Aurora Water's <a href="{WASTE}" rel="noopener noreferrer">wastewater page</a> says that lateral, from the sewer tap to the service address, is the owner's to maintain, along with the plumbing inside the building.</p>
      <p>The same page says Aurora Water maintains the city main and the manholes, in streets, alleys, and easements. It also says a common misconception is that the utility will make the repair and pay the damage. It will not, when the break is on the owner's service line or at the tap. The owner's list includes the tee or saddle where the service meets the main, and the street or property repair if that work disturbs them. Call 811 to locate the service line and tap. Aurora Water locates the city main.</p>
      <figure>
        <img class="diagram" src="/img/lateral.svg" alt="Diagram: the service line and tap belong to the owner; the city main belongs to Aurora Water.">
        <figcaption class="caption">The split on Aurora Water's wastewater page. Not a photograph of a job.</figcaption>
      </figure>
      <h2>What should be known before anyone names a method</h2>
      <p>Spot repair, a liner, a burst, or a full replacement are not interchangeable. A liner needs a pipe that can hold it. A collapse, a bad belly, or an offset joint can rule a method out. Clay pipe, which the City says is possible on homes built before 1985, fails differently from the PVC it says is typical later. That year is a hint, not a diagnosis. The <a href="{SERVICE_LINE}" rel="noopener noreferrer">service-line page</a> says the useful step is a video of the actual line. Start with <a href="/services/sewer-camera-inspection/">what the video needs to show</a>, then decide.</p>
      <p><a href="/services/hydro-jetting/">Hydro-jetting</a> can clear roots and grease. It is a cleaning method. On a cracked clay line it can also open the crack. Ask for the video before you accept jetting as the repair, and do not treat a city jet truck working the main in the street as proof that your service line was cleaned. The wastewater page describes gurgling in toilets while the city jets its own main. That can be normal pressure in the main. A backup that stays after the truck leaves is a different problem.</p>
      <h2>What changes the price without inventing one</h2>
      <p>This guide does not estimate dollars. The scope items that move an Aurora quote are concrete. Depth and length of the run. Whether the break is under a slab, a yard, or the public street. Whether the tap itself is being replaced. Who patches asphalt, curb, and sidewalk. Whether a cleanout has to be added so the next cleaning does not mean another dig. Access for the machine. Restoration of landscaping. And whether the quote is to clean a blockage, to repair a joint, or to replace the run.</p>
      <p>If sewage is backing up now, Aurora Water says to call a plumber and to call Aurora Water at 303-326-8645, and to call your insurance company for direction. That city number is Aurora Water's, not a line for this website, and it is not a click-to-call link here. Insurance may or may not cover a service line. The City says coverage varies and tells owners to read the policy. This page does not tell you that a plan will pay.</p>
      <p>After a plumber videos the line, Aurora residents can ask the City for a free second look. That offer, and what to hand over, is on the <a href="/guides/aurora-sewer-camera-second-opinion/">camera second-opinion guide</a>. We do not submit footage and we are not the City.</p>
      <h2>Questions that keep the quote honest</h2>
      <p>Ask where the defect sits relative to the building, the cleanout, and the tap. Ask who owns that segment under Aurora Water's description, not under a rule from another city. Ask which method the video supports, and which methods it rules out. Ask whether street restoration is included. Ask for a copy of the video you can forward. The full ownership write-up is the <a href="/guides/aurora-sewer-line-responsibility/">sewer responsibility guide</a>. A pressurized water leak in the yard is a <a href="/services/water-line-repair/">water service line</a>, not this pipe.</p>
      {qas([
        (
            "Does Aurora Water repair the line from the house to the main?",
            "No. The City's wastewater page says the owner maintains the service line from the sewer tap to the building, including the tee or saddle and related street or property damage. Aurora Water maintains the city main and manholes. A backup at a floor drain can still be on your line. Confirm the location on video before you treat the bill as the City's.",
        ),
        (
            "Should I approve trenchless work from a description alone?",
            "No. A liner or a burst depends on the pipe that is already in the ground. Clay, a collapse, or a separated joint can make a method a bad fit. Ask for the video, the distance and depth, and a sentence on why that method matches this pipe. The City's free footage review is a second opinion, not a substitute for the recording itself.",
        ),
        (
            "The city truck was on my street. Is my backup their problem?",
            "Not by itself. Aurora Water jets and cameras its own mains, and it warns that a jet in the main can gurgle household traps. That is not a repair of your service line. If sewage remains after the main is clear, the service line is still the owner's. Ask whether the main was inspected and where your tap connects.",
        ),
        (
            "Who pays if the repair cuts the street?",
            "If the cut is for your service line or tap, the wastewater page assigns the associated street and property damage to the owner. Ask the quote to name patching, curb, sidewalk, and landscape, and to say what is excluded. 811 locates the service. Aurora Water locates the city main. Do not dig from a guess.",
        ),
        (
            "Is a house built before 1985 automatically a clay-pipe replacement?",
            "No. The City says older homes can have clay and later homes generally have PVC, and that the line still has to be seen. A year of construction is a reason to video the pipe, not a reason to replace it. Get the material and the defects from the recording, then compare repair and replacement on that evidence.",
        ),
      ])}
    </article>
    """
    return _meta(
        "/services/sewer-line-repair/",
        "Sewer line repair in Aurora, Colorado | Aurora Plumbing Guide",
        "How Aurora assigns the sewer service line, the tap, and street repair, and what a quote should show before trenchless work or replacement.",
        "Sewer line repair in Aurora",
        "Sewer repair",
        "sewer line repair Aurora CO",
        "service",
        body,
    )


def camera(site: dict) -> dict:
    del site
    body = f"""
    <article class="sheet">
      <p class="eyebrow">Diagnosis, not the repair</p>
      <h1>Sewer camera inspection in Aurora</h1>
      <p class="lede">A camera inspection is how you find out whether you need a cleaning, a spot repair, or a new service line. It is also the recording Aurora Water will look at, for free, if you are an Aurora resident and you are unsure what the plumber recommended.</p>
      <h2>What you are buying</h2>
      <p>You are buying a look inside the pipe, from a known point, with a copy you can keep. A useful visit names the access point, usually a cleanout, and records distance so a defect can be found again. It should show material, cracks, offsets, bellies, roots, and grease, and it should say where the camera stopped. A verbal summary without the file is a weak basis for opening a street.</p>
      <p>The City's <a href="{SERVICE_LINE}" rel="noopener noreferrer">service-line page</a> says a video is the practical way to learn what the sewer line is made of and what condition it is in. It also says water service lines cannot be videotaped the same way. A camera quote for a yard water leak is the wrong tool. That decision lives on <a href="/services/leak-detection/">leak detection</a> and <a href="/services/water-line-repair/">water line repair</a>.</p>
      <h2>Real estate, backups, and "while we're here"</h2>
      <p>A sale inspection and an emergency backup are different assignments. For a sale, you want the whole service line to the tap if the camera can reach it, because the owner is responsible for that run under Aurora's wastewater rules. For a backup, you want to know whether the line is blocked, broken, or both, and whether the city main is even involved. <a href="/services/sewer-line-repair/">Sewer line repair</a> should follow the recording, not the other way around.</p>
      <p>If the company offers to jet before anyone has seen the pipe, read <a href="/services/hydro-jetting/">hydro-jetting</a> first. Jetting is sometimes the right cleaning. It is not how you discover a collapse.</p>
      <h2>The City's second look</h2>
      <p>Aurora's wastewater page offers residents a free review of plumber video of the lateral or private service line. Staff will comment on suggestions and next steps. The page says customers usually get a YouTube link or an email file they can forward. Use the address published on that City page. This website does not take the file, and it is not Aurora Water. Details are on the <a href="/guides/aurora-sewer-camera-second-opinion/">second-opinion guide</a>.</p>
      <p>Ask the plumber, before the truck leaves, for the file format the City can actually open, the direction of travel, and a still or a timestamp at the tap if they reached it. A recording that never leaves the company van cannot be reviewed by anyone else.</p>
      {qas([
        (
            "What should the video include?",
            "A copy you keep, the access point, distances, pipe material, and the defects in view: cracks, offsets, bellies, roots, or grease. It should say where the camera stopped and whether it reached the tap. A spoken summary without the file is not enough to open a street or to send to Aurora Water.",
        ),
        (
            "Can Aurora Water review the footage?",
            "Yes, for Aurora residents, as a free second opinion on the wastewater page. You forward the plumber's video to the address that page publishes. Staff comment on the line. They are not hiring the plumber and this website does not upload anything for you. Read the second-opinion guide before you send a file.",
        ),
        (
            "Will a camera see a water-line leak?",
            "Not the pressurized water service. The City says water service lines cannot be videotaped. A sewer camera belongs in the drain line. A wet yard or a hissing meter question needs a different location method, described on the leak-detection page, before anyone cuts the street.",
        ),
        (
            "Is the camera visit the repair?",
            "No. The recording sorts cleaning, a spot repair, and replacement. Approving a liner or a dig from a sales sentence skips that sort. Keep the file, compare it with the written scope, and use the City review if you are unsure what you were told.",
        ),
      ])}
    </article>
    """
    return _meta(
        "/services/sewer-camera-inspection/",
        "Sewer camera inspection in Aurora | Aurora Plumbing Guide",
        "What an Aurora sewer camera visit should hand you, and how the City's free footage review fits after the recording.",
        "Sewer camera inspection in Aurora",
        "Camera inspection",
        "sewer camera inspection Aurora CO",
        "service",
        body,
    )


def drains(site: dict) -> dict:
    del site
    body = f"""
    <article class="sheet">
      <p class="eyebrow">A clog is not yet a broken line</p>
      <h1>Drain cleaning in Aurora</h1>
      <p class="lede">Drain cleaning removes a blockage. It does not rebuild a service line. In Aurora that difference decides whether you are buying an hour with a cable or a project that can include the tap and the street.</p>
      <h2>One fixture, or the whole house</h2>
      <p>A single slow lavatory, with other fixtures behaving, is usually a branch line inside the building. A cable or a small machine from the trap or a nearby cleanout is the ordinary scope. When a tub, a shower, and a toilet on the same level all lag, the blockage may be a shared branch. When the lowest drain in the house backs up, or more than one floor is affected, stop treating it as a local clog and read <a href="/services/sewer-line-repair/">sewer line repair</a>.</p>
      <p>Aurora Water names the usual contents of a blockage: tree roots, fats, oils and grease, baby wipes, and other paper products. The service-line page adds hair, kitty litter, and so-called flushable wipes, and it says wipes do not break down the way toilet paper does. None of that advice is a repair. It is how a clear pipe gets closed again. Scraping grease into the trash is the City's suggestion. It will not seal a crack.</p>
      <h2>When cleaning is the wrong product</h2>
      <p>If a line is cleared and the backup returns in days, the pipe may be holding roots in a crack, sitting in a belly, or offset at a joint. Cleaning it again without a camera repeats the visit. <a href="/services/sewer-camera-inspection/">Camera inspection</a> is the step that shows whether <a href="/services/hydro-jetting/">jetting</a> is even safe. Jetting is still cleaning. It is not a patch.</p>
      <p>Sewage and stormwater are separate systems in Aurora. A yard that floods in a cloudburst is not, by that fact alone, a sanitary drain cleaning. Ask which system is involved before you approve work on the service line.</p>
      <p>Inside the building, the wastewater page still assigns the pipes to the owner. A cleaning quote should say which fixture, which cleanout, and what happens if the cable cannot pass. It should not quietly become a dig. If the technician says the city main is the problem, ask them to show why, and call Aurora Water at the number on the wastewater page, 303-326-8645. That is the City's line, not ours.</p>
      {qas([
        (
            "Is a slow kitchen sink a sewer replacement?",
            "Usually no. One lazy fixture, with the rest of the house draining, points to a branch clog. Start with cleaning from that fixture or the nearest cleanout. Replacement of the service line is a different scope, and it should wait on a backup that involves more of the building or on a camera that shows a broken pipe.",
        ),
        (
            "The clog came back. Now what?",
            "A second cleaning without a look inside the pipe often misses a crack, a belly, or roots in a joint. Ask for a camera from a cleanout toward the tap, and keep the recording. Then decide among another cleaning, jetting if the pipe can take it, or a repair. Do not approve a street cut from the repeat visit alone.",
        ),
        (
            "Are wipes and grease an Aurora issue or a generic tip?",
            "Aurora Water names them. The wastewater page lists fats, oils, grease, and wipes as ordinary causes of blockage, and the service-line page says wipes do not break down like toilet paper. Keeping them out of the line protects a sound pipe. It does not fix a separated joint.",
        ),
        (
            "Who do I call if sewage is coming up?",
            "The City says to call a plumber so the repair can start, and to call Aurora Water at 303-326-8645 to report it, plus your insurer for direction. This website cannot take that call. If more than one fixture or a lower-level drain is involved, treat it as a service-line question until a camera shows otherwise.",
        ),
      ])}
    </article>
    """
    return _meta(
        "/services/drain-cleaning/",
        "Drain cleaning in Aurora, Colorado | Aurora Plumbing Guide",
        "When an Aurora clog is a branch-line cleaning and when it is the start of a service-line repair.",
        "Drain cleaning in Aurora",
        "Drain cleaning",
        "drain cleaning Aurora CO",
        "service",
        body,
    )


def jetting(site: dict) -> dict:
    del site
    body = f"""
    <article class="sheet">
      <p class="eyebrow">Cleaning with pressure · after the pipe is seen</p>
      <h1>Hydro-jetting in Aurora</h1>
      <p class="lede">Hydro-jetting uses water at high pressure to cut roots and grease. It can be the right cleaning for a service line. It can also be the wrong tool in a pipe that is already cracked. Aurora gives you a second, unrelated meaning of "jetting": the city truck flushing its own main in the street.</p>
      <h2>Your line is not the city main</h2>
      <p>Aurora Water's <a href="{WASTE}" rel="noopener noreferrer">wastewater page</a> describes a large jet truck working the city sewer. You may hear the engine, and you may hear gurgling in toilets and sinks. The City says the nozzle's pressure in the main can pull water from traps and that the water returns when the pass is done. It also says sewage from the main is not being pushed into the house by that work. Keep traps full so sewer gas stays out.</p>
      <p>That operation does not jet your service line, and it does not mean you hired hydro-jetting. If a backup continues after the city main is flowing, the next question is the owner-maintained line from the tap to the house. Read <a href="/services/sewer-line-repair/">sewer line repair</a> for who pays, and <a href="/services/sewer-camera-inspection/">camera inspection</a> for how you see the pipe.</p>
      <h2>When a hired jet makes sense</h2>
      <p>A cable punches a hole in a clog. A jet washes the wall of the pipe, which is why it is used on grease and on fine roots. It belongs after a camera, or at least after the operator can say the pipe is intact enough to take the pressure. The City's note that pre-1985 homes can have clay is a reason to look, because a fractured clay pipe does not need more force. PVC is not automatically safe either. Offsets and bellies still matter.</p>
      <p>A jetting quote should name the access cleanout, the length to be washed, and what is excluded. It should not promise the line is repaired. Roots return to moisture at a crack. The service-line page says an intact pipe is less inviting to roots and suggests cleaning a problem line, but cleaning on a schedule is not a patch. If the video shows a break, go back to repair or replacement.</p>
      <p><a href="/services/drain-cleaning/">Drain cleaning</a> with a small cable is still the better first step for one indoor fixture. Jetting a kitchen branch from a roof vent, without knowing where the nozzle will go, is how fixtures get flooded. Ask where the hose enters and where it stops.</p>
      {qas([
        (
            "Is the city jet truck cleaning my service line?",
            "No. The truck described on Aurora's wastewater page is flushing the city main. Gurgling in your toilet can be that work. It is not a visit you scheduled, and it does not restore a broken lateral. If the backup remains, the service line from the tap to the house is still the owner's problem.",
        ),
        (
            "Should the line be jetted before it is camera'd?",
            "Usually no. Jetting is a strong cleaning, and a cracked or offset pipe can be made worse. Ask for a camera unless the operator can already show a recent recording of this run. Roots in an otherwise round pipe are a better candidate than a collapse.",
        ),
        (
            "Will jetting stop roots for good?",
            "It removes the roots it can reach. The City notes that roots follow moisture into a crack or a separated joint. If the video shows that opening, jetting is maintenance until the joint is repaired. A quote that calls jetting a permanent fix, without a repair, is overselling the hose.",
        ),
        (
            "How is this different from cabling a drain?",
            "A cable opens a path through a clog and is the usual tool for one slow fixture. A jet washes the pipe wall and is aimed at grease and roots in a larger line. Neither one replaces a crushed section. Pick the tool after you know whether the pipe is blocked, broken, or both.",
        ),
      ])}
    </article>
    """
    return _meta(
        "/services/hydro-jetting/",
        "Hydro-jetting in Aurora, Colorado | Aurora Plumbing Guide",
        "When jetting an Aurora service line is a cleaning, and how that differs from the city truck jetting the main.",
        "Hydro-jetting in Aurora",
        "Hydro-jetting",
        "hydro jetting Aurora CO",
        "service",
        body,
    )


def responsibility(site: dict) -> dict:
    del site
    body = f"""
    <article class="sheet">
      <p class="eyebrow">Aurora Water · not another city's rule</p>
      <h1>Who owns the sewer line in Aurora</h1>
      <p class="lede">Aurora does not split the service line into a private half and a city-maintained half out to the main. The owner's duty runs from the building to the tap on the city main, and it includes that connection.</p>
      <h2>The City's own list</h2>
      <p>On the <a href="{WASTE}" rel="noopener noreferrer">wastewater page</a>, property owners are responsible for maintenance and repair of the wastewater service line from the sewer tap to the service address, and for plumbing inside the building. They are responsible for the connection to the city main, including the tee or saddle. They are responsible for street and property damage if work on that service line or tap affects those areas. They locate the service line and tap by calling 811.</p>
      <p>Aurora Water is responsible for the city main and the manholes, and for street or property damage associated with that city work. It responds to blockage calls by cleaning or inspecting the city main. It locates the city mains. It maintains more than 1,200 miles of sanitary sewer, cleans hundreds of miles a year, and cameras a smaller share of the main. Those figures describe the public system, not a promise to camera your lateral for free. The free offer is a review of video you already have.</p>
      <figure>
        <img class="diagram" src="/img/lateral.svg" alt="Diagram showing the owner service line meeting the city main at the tap.">
        <figcaption class="caption">Owner's line and tap in copper. City main in green. Based on Aurora Water's description.</figcaption>
      </figure>
      <h2>What this changes in a quote</h2>
      <p>A company that says "the city owns it past the sidewalk" is using some other town's habit. In Aurora, ask them to mark the tap and to say whether the price includes the saddle and the pavement. If they are only cleaning a clog, the <a href="/services/drain-cleaning/">drain cleaning</a> page is the better fit. If they want to replace pipe, the scope belongs on <a href="/services/sewer-line-repair/">sewer line repair</a>, after a <a href="/services/sewer-camera-inspection/">camera</a>.</p>
      <p>The service-line page adds a materials caution. Homes from before 1985 can have clay laterals. Later homes generally have PVC. Water services are generally copper and cannot be videoed. "Generally" is the City's word. The pipe in the ground decides. Storm drains are a separate system and are not this lateral.</p>
      <p>Neighboring cities are not covered by this page. A Denver, Centennial, or county address can sit on a different utility even when the mailing city says Aurora. Confirm the jurisdiction before you borrow this split. This guide does not publish those other rules.</p>
      {qas([
        (
            "Does the city maintain the lower lateral to the main?",
            "Not under Aurora's wastewater page. The owner keeps the service line from the tap to the building and the tee or saddle itself. Aurora Water keeps the main and the manholes. A rule from another city that gives the sidewalk-to-main piece to the city does not apply here. Ask the locator marks and the video where this tap actually is.",
        ),
        (
            "What does 811 cover?",
            "The City tells owners to call 811 to locate their sewer service line and tap. Aurora Water locates the city mains. Those are different marks. A quote that starts digging without them is guessing at a pipe the owner will pay to hit, including the street if the tap is in it.",
        ),
        (
            "Who reviews a video if I doubt the repair?",
            "Aurora residents can send the plumber's footage to the City for a free second opinion. The wastewater page describes that review. This website is not the intake. Use the camera second-opinion guide so the file shows the tap, the distances, and the defects.",
        ),
      ])}
    </article>
    """
    return _meta(
        "/guides/aurora-sewer-line-responsibility/",
        "Who owns the sewer line in Aurora | Aurora Plumbing Guide",
        "Aurora Water's split: the owner keeps the service line and the tap; the city keeps the main and the manholes.",
        "Who owns the sewer line in Aurora",
        "Sewer responsibility",
        "Aurora sewer line responsibility",
        "guide",
        body,
    )


def second_opinion(site: dict) -> dict:
    del site
    body = f"""
    <article class="sheet">
      <p class="eyebrow">City review · you send the file</p>
      <h1>Aurora's free sewer-camera review</h1>
      <p class="lede">If you live in Aurora and a plumber has video of your service line, the City will look at it and talk through what it shows. The review is free. It is a second opinion. It is not a work order, and this website is not the office that receives the file.</p>
      <h2>What the City says it will do</h2>
      <p>The <a href="{WASTE}" rel="noopener noreferrer">wastewater page</a> offers the review to Aurora residents who have a backup or a question about their lateral or private service line. A staff member looks at the video and comments on suggestions, next steps, and possible resolutions. The page says a plumber or other vendor usually provides the video as a YouTube link or an email attachment that you forward. Use the contact published on that page. Do not send the file here. We cannot forward it, and we are not affiliated with Aurora Water.</p>
      <h2>What to ask the plumber to capture</h2>
      <p>A review is only as clear as the recording. Before the truck leaves, ask for a file you can forward, the cleanout they entered, and distances. Ask them to note pipe material, the worst defects, and whether the camera reached the tap or stopped short. A clip of one root, with no location, is hard for anyone to judge. The checklist for the visit itself is <a href="/services/sewer-camera-inspection/">sewer camera inspection</a>.</p>
      <p>Use the review when you are being asked to replace a long run, to open the street, or to buy a liner, and the explanation does not match what you see. It is also reasonable when two companies describe the same video differently. It is not a reason to leave an active sewage backup unattended. The City still says to call a plumber and Aurora Water at 303-326-8645 when sewage is backing up.</p>
      <h2>What the review is not</h2>
      <p>It does not mean the City will pay for the service line. Ownership stays as described in the <a href="/guides/aurora-sewer-line-responsibility/">responsibility guide</a>. It does not choose a contractor. It does not guarantee a same-week repair. If the video shows a cleaning rather than a break, <a href="/services/drain-cleaning/">drain cleaning</a> or <a href="/services/hydro-jetting/">jetting</a> may be the scope, and the review can help you see that before you fund a replacement.</p>
      {qas([
        (
            "How do I request the review?",
            "Follow the wastewater page on auroragov.org. Residents forward the plumber's video to the address that page gives, often a link or a file the company already sent you. This guide does not collect the video and does not submit it. If you cannot find the address, use the phone number printed on that City page rather than guessing an inbox.",
        ),
        (
            "Will the City send a crew to dig?",
            "The offer is a review of footage and advice on next steps. It is not a promise that Aurora Water will excavate an owner service line. If the defect is on your line or at your tap, the repair and the street patch remain the owner's under the City's own list. The review helps you test the recommendation.",
        ),
        (
            "What if sewage is in the house right now?",
            "Call a plumber and call Aurora Water at 303-326-8645, which is the number on the wastewater page, and call your insurer. The free review is for understanding a recording. It is not the emergency response, and this website cannot take the report. Keep people away from the overflow until the line is handled.",
        ),
      ])}
    </article>
    """
    return _meta(
        "/guides/aurora-sewer-camera-second-opinion/",
        "Free sewer camera review in Aurora | Aurora Plumbing Guide",
        "How Aurora residents can ask the City to review a plumber's sewer video, and what that review does not do.",
        "Aurora's free sewer-camera review",
        "Camera review",
        "Aurora sewer camera second opinion",
        "guide",
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
        "keyword_status": "Topic of this page. No volume or difficulty study. Preview only.",
        "kind": kind,
        "body": body,
    }
