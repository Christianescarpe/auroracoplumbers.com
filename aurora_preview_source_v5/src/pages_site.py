"""Home, indexes, permit guide, checklist, and legal pages."""

from markup import INSPECT, PERMIT, esc, qas


def home(site: dict) -> dict:
    del site
    body = """
    <section class="landing-band" aria-labelledby="hero-title">
      <div class="hero-split">
        <div class="hero-copy-col">
          <p class="eyebrow">Aurora, Colorado &middot; Consumer Plumbing Guide</p>
          <h1 id="hero-title">Plumber Aurora CO</h1>
          <p class="hero-subheadline">Name the pipe &amp; permit scope before you hire</p>
          <p class="lede">A slow sink, a wet tank, and sewage in the basement are different jobs, and in Aurora they are not the same pipe. Compare local scopes, utility boundaries, and inspection rules before requesting a contractor quote.</p>
          <div class="btn-row">
            <a class="btn-primary" href="/services/">Which repair &rarr;</a>
            <a class="btn-outline" href="/guides/plumbing-quote-checklist/">Quote checklist &rarr;</a>
          </div>
        </div>
        <div class="hero-photo-frame">
          <img src="/img/hero-plumber-inspection.jpg" alt="Plumber inspecting residential pipe fittings and water supply lines" width="800" height="600" loading="eager" decoding="async">
        </div>
      </div>
      <div class="hero-bento">
        <div class="bento-stat-card">
          <div>
            <div class="bento-stat-num">37<span>+</span></div>
            <div class="bento-stat-label">Service Scopes &amp; Decision Guides</div>
          </div>
          <a class="circle-arrow" href="/services/" aria-label="Browse all plumbing repair scopes">&rarr;</a>
        </div>
        <div class="bento-thumb">
          <img src="/img/copper-pipes-wrench-repair.jpg" alt="Copper supply lines and wrench fitting in mechanical space" width="400" height="300" loading="lazy" decoding="async">
        </div>
        <div class="bento-info-card">
          <p>Aurora Plumbing Guide shows homeowners what to ask an independent licensed contractor. It does not employ crews, pull permits, or dispatch a truck.</p>
          <a class="inline-arrow-link" href="/about/">How This Guide Is Verified &rarr;</a>
        </div>
      </div>
    </section>

    <section class="landing-band" aria-labelledby="showcase-heading">
      <div class="band-header-center">
        <p class="eyebrow">Scope Clarity First</p>
        <h2 id="showcase-heading">Built Around Local Rules</h2>
        <p class="band-sub">Separate indoor fixture repairs from permitted tank swaps and lateral excavation before signing any estimate across Aurora and the Front Range.</p>
      </div>
      <div class="showcase-banner-wrap">
        <img src="/img/hero-construction-pipes.jpg" alt="Residential plumbing piping and main supply installation" width="1200" height="525" loading="lazy" decoding="async">
      </div>
      <div class="stats-strip">
        <div class="stat-item"><div class="stat-figure">37</div><div class="stat-caption">Distinct Residential<br>Plumbing Scopes</div></div>
        <div class="stat-item"><div class="stat-figure">45</div><div class="stat-caption">Front Range Cities<br>&amp; Towns Documented</div></div>
        <div class="stat-item"><div class="stat-figure">15</div><div class="stat-caption">Permit &amp; Utility<br>Decision Guides</div></div>
        <div class="stat-item"><div class="stat-figure">100<span>%</span></div><div class="stat-caption">Private Browser-Only<br>Quote Checklist</div></div>
      </div>
    </section>

    <section class="landing-band" aria-labelledby="problems-heading">
      <div class="asymmetric-top">
        <div>
          <p class="eyebrow">What Kind of Problem Is It</p>
          <h2 id="problems-heading">Core Plumbing Repair Scopes</h2>
          <p class="band-sub">Start with the symptom on your property. Each page separates repair vs. replacement paths and flags what needs a city permit or utility check.</p>
        </div>
        <a class="icon-card" href="/services/water-heater-repair/">
          <div>
            <span class="icon-badge" aria-hidden="true">&#9881;</span>
            <h3>No Hot Water or Wet Tank</h3>
            <p>A wet fitting or failed valve can still be repairable. A full tank swap requires a permit and inspection request.</p>
          </div>
          <span class="inline-arrow-link">Learn More &rarr;</span>
        </a>
      </div>
      <div class="icon-card-grid">
        <a class="icon-card" href="/services/tankless-water-heater-installation/"><div><span class="icon-badge" aria-hidden="true">&#9889;</span><h3>Switching to Tankless</h3><p>Changing to tankless means new venting, condensate drainage, and gas-load or electrical capacity checks—not a thinner tank.</p></div><span class="inline-arrow-link">Learn More &rarr;</span></a>
        <a class="icon-card" href="/services/drain-cleaning/"><div><span class="icon-badge" aria-hidden="true">+</span><h3>One Slow Sink or Drain</h3><p>Start with a localized clog. If the lowest floor drain backs up with sewage, the issue may extend to your main lateral.</p></div><span class="inline-arrow-link">Learn More &rarr;</span></a>
        <a class="icon-card" href="/services/sewer-line-repair/"><div><span class="icon-badge" aria-hidden="true">&harr;</span><h3>Sewer Backup or Broken Line</h3><p>Aurora Water maintains the main. Property owners keep the line from the building through the tap, including street patching.</p></div><span class="inline-arrow-link">Learn More &rarr;</span></a>
      </div>
    </section>

    <section class="landing-band" aria-labelledby="categories-heading">
      <div class="band-header-center">
        <p class="eyebrow">System Categories</p>
        <h2 id="categories-heading">Solutions for Your Home</h2>
        <p class="band-sub">Explore dedicated repair and replacement pages across heating, supply piping, drainage, and fixture assemblies.</p>
      </div>
      <div class="photo-card-grid">
        <a class="photo-card" href="/services/water-heater-replacement/"><div><h3>Water Heaters</h3><p>Permit expectations, same-day inspection limits, and tank swap quote items.</p></div><div class="photo-card-media"><img src="/img/water-filtration-system-install.jpg" alt="Residential utility room water heater and filtration setup" width="600" height="450" loading="lazy" decoding="async"></div></a>
        <a class="photo-card" href="/services/leak-detection/"><div><h3>Leak Detection</h3><p>A sewer camera cannot see a pressurized supply line. Isolate leaks before slab cuts.</p></div><div class="photo-card-media"><img src="/img/pipe-leak-pliers-under-sink.jpg" alt="Plumber isolating pipe joint leak under residential sink" width="600" height="450" loading="lazy" decoding="async"></div></a>
        <a class="photo-card" href="/services/faucet-sink-fixture-repair/"><div><h3>Fixtures &amp; Valves</h3><p>Separate simple faucet, toilet, or disposal repairs from concealed wall piping damage.</p></div><div class="photo-card-media"><img src="/img/bathroom-sink-faucet-plumbing.jpg" alt="Bathroom sink faucet and chrome supply plumbing assembly" width="600" height="450" loading="lazy" decoding="async"></div></a>
        <a class="photo-card" href="/services/whole-house-repiping/"><div><h3>Supply Repiping</h3><p>Compare spot pipe repair against full-house supply replacement when pressure drops.</p></div><div class="photo-card-media"><img src="/img/plumbing-equipment-fittings-layout.jpg" alt="Plumbing shutoff valves, fittings, and manifold equipment layout" width="600" height="450" loading="lazy" decoding="async"></div></a>
      </div>
    </section>

    <section class="landing-band" aria-labelledby="facts-heading">
      <div class="split-rules">
        <div>
          <p class="eyebrow">City &amp; Utility Rules</p>
          <h2 id="facts-heading">Three Aurora Facts That Move the Price</h2>
          <p class="band-sub">Before accepting an open-ended quote, verify who owns the pipe outside your foundation and what Aurora Water or the Building Division actually provides.</p>
          <div class="rule-stack">
            <details class="rule-accordion" open><summary>Sewer Ownership Runs to the Tap</summary><div class="rule-body"><p>Aurora Water keeps the sewer main and manholes. You keep the service line from the tap to the building, including the tee or saddle and street repair if work disturbs it.</p><a class="inline-arrow-link" href="/guides/aurora-sewer-line-responsibility/">Who Owns the Line &rarr;</a></div></details>
            <details class="rule-accordion"><summary>Free City Sewer Video Second Look</summary><div class="rule-body"><p>If a plumber cameras your lateral, Aurora residents can ask the City for a free second look at the recording. This site does not upload video files for you.</p><a class="inline-arrow-link" href="/guides/aurora-sewer-camera-second-opinion/">Camera Review Guide &rarr;</a></div></details>
            <details class="rule-accordion"><summary>Same-Day Water Heater Inspection Limits</summary><div class="rule-body"><p>A licensed contractor can request a same-day inspection on a replacement tank when you and the contractor are both present, though the City may still arrive another day.</p><a class="inline-arrow-link" href="/guides/aurora-water-heater-permits/">Permit &amp; Inspection Guide &rarr;</a></div></details>
          </div>
        </div>
        <div class="stacked-photos">
          <div class="stacked-photo-box"><img src="/img/industrial-utility-pipe-service.jpg" alt="Commercial and residential utility pipe servicing equipment" width="800" height="450" loading="lazy" decoding="async"></div>
          <div class="stacked-photo-box"><img src="/img/pipe-adjustment-wrench-service.jpg" alt="Plumber adjusting water and gas pipe fittings with wrench" width="800" height="450" loading="lazy" decoding="async"></div>
        </div>
      </div>
    </section>

    <section class="landing-band" aria-labelledby="jurisdiction-heading">
      <div class="band-header-center">
        <p class="eyebrow">Outside Aurora City Limits</p>
        <h2 id="jurisdiction-heading">If the House Is Not in Aurora</h2>
        <p class="band-sub">Aurora rules stop at the city line. A mailing city is not a permit jurisdiction—check the rules and quote prep checklist for your actual parcel.</p>
      </div>
      <div class="workflow-split">
        <div class="workflow-tabs" role="tablist" aria-label="Jurisdictions and homeowner tools">
          <button type="button" class="workflow-tab is-active" role="tab" aria-selected="true" data-title="Compare Scopes With the Quote Checklist" data-body="When you are ready to compare written quotes, use the checklist. It stays in your browser, asks for no name or address, and outputs no guessed pricing." data-href="/guides/plumbing-quote-checklist/" data-cta="Open Quote Checklist &rarr;" data-img="/img/kitchen-sink-plumbing-tools.jpg" data-alt="Kitchen sink drain and plumbing service tools"><span class="workflow-tab-main"><span class="icon-badge" aria-hidden="true">&#10003;</span><span><span class="workflow-tab-title">Quote Checklist</span><span class="workflow-tab-desc">Browser-only scope questions before hiring.</span></span></span><span class="workflow-tab-arrow" aria-hidden="true">&rarr;</span></button>
          <button type="button" class="workflow-tab" role="tab" aria-selected="false" data-title="Centennial Permit &amp; District Split" data-body="Centennial does not supply water or sewer directly. Special districts handle utilities while city permitting follows its own published review tiers." data-href="/areas/centennial/" data-cta="Read Centennial Guide &rarr;" data-img="/img/tiled-bathroom-sink-repair.jpg" data-alt="Residential bathroom plumbing fixture and tiled wall"><span class="workflow-tab-main"><span class="icon-badge" aria-hidden="true">&#9678;</span><span><span class="workflow-tab-title">Centennial Rules</span><span class="workflow-tab-desc">Special water/sewer districts, separate city permits.</span></span></span><span class="workflow-tab-arrow" aria-hidden="true">&rarr;</span></button>
          <button type="button" class="workflow-tab" role="tab" aria-selected="false" data-title="Parker &amp; Highlands Ranch Boundaries" data-body="Parker handles permitting inside the town while Highlands Ranch is unincorporated Douglas County. Confirm district service boundaries for your parcel." data-href="/areas/parker/" data-cta="Read Parker &amp; Area Rules &rarr;" data-img="/img/shower-valve-repair-bathroom.jpg" data-alt="Bathroom shower mixing valve and pipe trim installation"><span class="workflow-tab-main"><span class="icon-badge" aria-hidden="true">&#9635;</span><span><span class="workflow-tab-title">Parker &amp; Highlands Ranch</span><span class="workflow-tab-desc">Town vs. unincorporated Douglas County permits.</span></span></span><span class="workflow-tab-arrow" aria-hidden="true">&rarr;</span></button>
          <button type="button" class="workflow-tab" role="tab" aria-selected="false" data-title="Castle Rock Tankless &amp; Gas Math" data-body="Castle Rock may skip plan review on standard tank swaps but adds review and gas-load sizing math when converting to a tankless water heater." data-href="/areas/castle-rock/" data-cta="Read Castle Rock Guide &rarr;" data-img="/img/under-sink-modern-bathroom.jpg" data-alt="Clean under-sink water supply lines and shutoff valves"><span class="workflow-tab-main"><span class="icon-badge" aria-hidden="true">&#9728;</span><span><span class="workflow-tab-title">Castle Rock Permitting</span><span class="workflow-tab-desc">Tankless gas-load calculations and plan review.</span></span></span><span class="workflow-tab-arrow" aria-hidden="true">&rarr;</span></button>
        </div>
        <div id="workflow-panel" class="workflow-panel">
          <div><h3 data-wf-title>Compare Scopes With the Quote Checklist</h3><p data-wf-body>When you are ready to compare written quotes, use the checklist. It stays in your browser, asks for no name or address, and outputs no guessed pricing.</p></div>
          <div class="workflow-panel-media"><img data-wf-img src="/img/kitchen-sink-plumbing-tools.jpg" alt="Kitchen sink drain and plumbing service tools" width="800" height="400" loading="lazy" decoding="async"></div>
          <div><a class="btn-outline" data-wf-link href="/guides/plumbing-quote-checklist/">Open Quote Checklist &rarr;</a><div class="workflow-quick-links"><a href="/areas/centennial/">Centennial</a><a href="/areas/parker/">Parker</a><a href="/areas/highlands-ranch/">Highlands Ranch</a><a href="/areas/castle-rock/">Castle Rock</a><a href="/areas/">All 45 Areas</a></div></div>
        </div>
      </div>
    </section>

    <section class="landing-band" aria-labelledby="guides-spotlight-heading">
      <div class="band-header-center">
        <p class="eyebrow">Essential Reading</p>
        <h2 id="guides-spotlight-heading">Questions &amp; Guides Across the Front Range</h2>
        <p class="band-sub">Understand how referrals work, how to request a City camera second opinion, and which neighboring cities have verified permit pages.</p>
      </div>
      <div class="spotlight-grid">
        <div class="spotlight-main">
          <div><div class="spotlight-num">01</div><h3>How a Plumbing Referral Works Here</h3><p>This website is an independent consumer plumbing guide. It does not hold a plumbing license, employ crews, or accept web forms. Learn how scope preparation works before live call routing is connected.</p><a class="btn-primary" href="/how-it-works/">Read How It Works &rarr;</a></div>
          <div class="spotlight-photo"><img src="/img/repairman-fixing-pipes-wrench.jpg" alt="Plumber working with wrench on residential water piping" width="600" height="450" loading="lazy" decoding="async"></div>
        </div>
        <a class="spotlight-side" href="/guides/aurora-sewer-camera-second-opinion/"><div><div class="spotlight-side-num">02</div><div class="spotlight-side-label">Camera Review</div></div><div class="spotlight-side-photo"><img src="/img/home-bathroom-sink-drain.jpg" alt="Drain assembly inspection inside home bathroom" width="360" height="480" loading="lazy" decoding="async"></div></a>
        <a class="spotlight-side" href="/areas/"><div><div class="spotlight-side-num">03</div><div class="spotlight-side-label">Nearby Cities</div></div><div class="spotlight-side-photo"><img src="/img/modern-bathroom-sink-plumbing.jpg" alt="Finished bathroom plumbing fixtures and drain setup" width="360" height="480" loading="lazy" decoding="async"></div></a>
      </div>
    </section>

    <section class="landing-band qa-list" aria-labelledby="qa-heading">
      <p class="eyebrow">Key Clarifications</p>
      <h2 id="qa-heading">Questions to Settle First</h2>
      <div class="qa-grid">
        <article class="qa-item"><h3 class="qa-q">Are you the plumber?</h3><p class="qa-a">No. This is a referral-style guide. It does not hold a plumbing license, employ a crew, or dispatch a truck. The pages tell you what to ask an independent contractor. Calls, email, and forms are turned off until a real destination exists. Nothing you read here books a visit.</p></article>
        <article class="qa-item"><h3 class="qa-q">Does Aurora Water own the sewer from the house to the main?</h3><p class="qa-a">No. The City's wastewater page says you maintain the service line from the sewer tap to the building, including the connection and related street damage. Aurora Water maintains the city main and the manholes. A backup in a floor drain can still be yours. Get a camera before you assign the bill.</p></article>
        <article class="qa-item"><h3 class="qa-q">Will the City inspect a new water heater today?</h3><p class="qa-a">Not as a promise. A licensed contractor may request a same-day inspection when you can both be there. The City says it may inspect on another day if the schedule is full. Ask the contractor to make the request. Do not sign a quote that treats same-day approval as guaranteed.</p></article>
        <article class="qa-item"><h3 class="qa-q">Does Aurora's sewer rule apply in the next town?</h3><p class="qa-a">No. Denver keeps the lateral through the tap on the owner and uses its own quick permit. Lakewood's sewer drawing is only the city's north-side customers. A mailing city is not the permit office. Use the nearby-cities list for the parcel you actually have, and do not carry Aurora's tap rule across the line.</p></article>
        <article class="qa-item"><h3 class="qa-q">Can I send you the sewer video?</h3><p class="qa-a">No. Aurora Water accepts resident video at the address on the City's wastewater page. This website has no upload and no inbox. The second-opinion guide lists what the recording should show so the City's review is useful. We are not the City.</p></article>
      </div>
    </section>
    """
    return _page(
        "/",
        "Plumber Aurora CO | Aurora Plumbing Guide",
        "Decide the plumbing job in Aurora, Colorado, before you hire. Referral guide. Compare plumbing scopes, permit rules, and utility boundaries before hiring.",
        "Plumber Aurora CO",
        "Home",
        "plumber Aurora CO",
        "primary",
        body,
    )


def services_index(site: dict) -> dict:
    del site
    body = """
    <article class="sheet">
      <p class="eyebrow">Pick the job</p>
      <h1>Which plumbing repair is it</h1>
      <p class="lede">Each link is a different job. Floor drains sit with drain cleaning or sewer repair, depending on whether the pipe is blocked or broken. Nothing here places a phone call.</p>
      <h2>Hot water</h2>
      <ul class="link-list">
        <li><a href="/services/water-heater-repair/">Storage tank repair</a></li>
        <li><a href="/services/water-heater-replacement/">Storage tank replacement</a></li>
        <li><a href="/services/tankless-water-heater-installation/">Tankless installation</a></li>
        <li><a href="/services/tankless-water-heater-repair/">Tankless repair</a></li>
      </ul>
      <h2>Fixtures</h2>
      <ul class="link-list">
        <li><a href="/services/faucet-sink-fixture-repair/">Faucets and fixtures</a></li>
        <li><a href="/services/toilet-repair-installation/">Toilets</a></li>
        <li><a href="/services/bathtub-shower-installation/">Tubs and showers</a></li>
        <li><a href="/services/garbage-disposal-repair/">Garbage disposals</a></li>
        <li><a href="/services/general-plumbing-repair/">Several small repairs, one visit</a></li>
      </ul>
      <h2>Drains and sewers</h2>
      <ul class="link-list">
        <li><a href="/services/drain-cleaning/">Drain cleaning</a></li>
        <li><a href="/services/sewer-camera-inspection/">Camera inspection</a></li>
        <li><a href="/services/hydro-jetting/">Hydro-jetting</a></li>
        <li><a href="/services/sewer-line-repair/">Sewer line repair</a></li>
        <li><a href="/services/trenchless-sewer-repair/">Trenchless sewer repair</a></li>
        <li><a href="/services/sewer-ejector-pumps/">Sewer ejector pumps</a></li>
        <li><a href="/services/backwater-valve-installation/">Backwater valves</a></li>
        <li><a href="/services/sump-pump-repair-installation/">Sump pumps</a></li>
      </ul>
      <h2>Supply, pressure, and treatment</h2>
      <ul class="link-list">
        <li><a href="/services/leak-detection/">Leak detection</a></li>
        <li><a href="/services/water-line-repair/">Water service line</a></li>
        <li><a href="/services/pipe-repair-replacement/">Pipe repair</a></li>
        <li><a href="/services/whole-house-repiping/">Whole-house repiping</a></li>
        <li><a href="/services/water-pressure-problems/">Water pressure</a></li>
        <li><a href="/services/water-treatment-installation/">Treatment installation</a></li>
        <li><a href="/services/water-treatment-repair/">Treatment repair</a></li>
        <li><a href="/services/backflow-preventers/">Backflow preventers</a></li>
        <li><a href="/services/well-pump-installation/">Well pump installation</a></li>
        <li><a href="/services/well-pump-repair/">Well pump repair</a></li>
      </ul>
      <h2>Building, gas, and cold weather</h2>
      <ul class="link-list">
        <li><a href="/services/remodel-addition-plumbing/">Remodels and additions</a></li>
        <li><a href="/services/commercial-plumbing/">Commercial plumbing</a></li>
        <li><a href="/services/plumbing-inspection/">Plumbing inspections</a></li>
        <li><a href="/services/gas-line-repair-installation/">Gas lines</a></li>
        <li><a href="/services/frozen-pipe-repair/">Frozen pipes</a></li>
        <li><a href="/services/plumbing-winterization/">Winterization</a></li>
        <li><a href="/services/mobile-home-plumbing/">Mobile homes</a></li>
        <li><a href="/services/pool-spa-plumbing/">Pools and spas</a></li>
        <li><a href="/services/radiant-floor-heating-installation/">Radiant floor installation</a></li>
        <li><a href="/services/radiant-floor-heating-repair/">Radiant floor repair</a></li>
      </ul>
      <p>Gas, wells, pools, and radiant pages say what they will not do. They are explanations, not a crew on call. Paperwork is in the <a href="/guides/">guides</a>. Cities with a source behind them are on <a href="/areas/">nearby cities</a>.</p>
    </article>
    """
    return _page(
        "/services/",
        "Plumbing repairs explained | Aurora Plumbing Guide",
        "Choose the Aurora plumbing page that matches the job: heater, drain, sewer, or water line.",
        "Which plumbing repair is it",
        "Which repair",
        "",
        "support",
        body,
    )


def areas_index(site: dict) -> dict:
    del site
    body = """
    <article class="sheet">
      <p class="eyebrow">Only cities that were checked</p>
      <h1>Nearby cities, when the rules differ</h1>
      <p class="lede">Aurora's sewer tap rule does not follow you across a city limit. These cities were written from their own permit or utility pages. A town that is only a point on a map is not given Aurora's sentences.</p>
      <ul class="link-list">
        <li><a href="/areas/centennial/">Centennial</a> does not provide water or sewer. A house water heater is one-stop. An addition is not. See also <a href="/areas/centennial/water-heater-replacement/">Centennial water heater replacement</a>.</li>
        <li><a href="/areas/parker/">Parker</a> permits inside the town. The district's service-line boundary is not settled on that page.</li>
        <li><a href="/areas/highlands-ranch/">Highlands Ranch</a> uses Douglas County, not a city building department.</li>
        <li><a href="/areas/castle-rock/">Castle Rock</a> reviews tankless heaters with a gas-load sheet. See <a href="/areas/castle-rock/tankless-water-heater-installation/">Castle Rock tankless installation</a>.</li>
        <li><a href="/areas/lakewood/">Lakewood</a> has many districts. The city sewer graphic is only the north-side utility.</li>
        <li><a href="/areas/arvada/">Arvada</a> says you maintain the service line on your property, and stops there.</li>
        <li><a href="/areas/englewood/">Englewood</a> permits water heaters and water-line changes. A 2024 ownership proposal was not treated as current law.</li>
        <li><a href="/areas/littleton/">Littleton</a> owners keep the sewer line including the tap. Denver Water supplies drinking water.</li>
        <li><a href="/areas/westminster/">Westminster</a> owners keep the lateral to the main, including under a driveway.</li>
        <li><a href="/areas/denver/">Denver</a> keeps a house water heater on a quick permit and the sewer lateral, including the tap, on the owner.</li>
        <li><a href="/areas/thornton/">Thornton</a> uses a different permit when a service repair enters the right of way.</li>
        <li><a href="/areas/northglenn/">Northglenn</a> lists water heaters and sewers as one-stop permits.</li>
        <li><a href="/areas/commerce-city/">Commerce City</a> splits building permits from right-of-way permits.</li>
        <li><a href="/areas/brighton/">Brighton</a> allows an emergency heater or service repair only if you permit it the next business day and leave it open.</li>
        <li><a href="/areas/federal-heights/">Federal Heights</a> sends electrical permits to the state.</li>
        <li><a href="/areas/wheat-ridge/">Wheat Ridge</a> permits water heater replacement in OpenGov.</li>
        <li><a href="/areas/broomfield/">Broomfield</a> permits every water heater, and it will not issue a new tap license before the building permit.</li>
        <li><a href="/areas/louisville/">Louisville</a> can review a water heater the same day. An addition takes weeks.</li>
        <li><a href="/areas/longmont/">Longmont</a> uses different phones for taps inside and outside the building.</li>
        <li><a href="/areas/greenwood-village/">Greenwood Village</a> makes you find the district on a map before the permit.</li>
        <li><a href="/areas/lone-tree/">Lone Tree</a> does not sell water. Southgate, Parker Water, and Northern Douglas County Water can each apply. The bill controls. The building permit stays with the city.</li>
        <li><a href="/areas/castle-pines/">Castle Pines</a> has its own building department. The water district is whoever bills the house.</li>
        <li><a href="/areas/edgewater/">Edgewater</a> runs its water utility and splits sewer with East Jefferson Sanitation District.</li>
        <li><a href="/areas/sheridan/">Sheridan</a> requires a water-heater permit visible from the street.</li>
        <li><a href="/areas/foxfield/">Foxfield</a> is its own town, with water heaters on a one-stop list.</li>
        <li><a href="/areas/bow-mar/">Bow Mar</a> files building permits through Columbine Valley.</li>
        <li><a href="/areas/columbine-valley/">Columbine Valley</a> is the building counter Bow Mar uses.</li>
        <li><a href="/areas/cherry-hills-village/">Cherry Hills Village</a> has a sanitation district, and some taps are also inspected by Englewood.</li>
        <li><a href="/areas/watkins/">Watkins</a> is a census place in both Adams County and Arapahoe County. The ZIP code is not the permit office.</li>
        <li><a href="/areas/bennett/">Bennett</a> is a town in both Adams County and Arapahoe County. Mail can fall outside the town.</li>
        <li><a href="/areas/strasburg/">Strasburg</a> is a census place in both Adams County and Arapahoe County, not a city.</li>
        <li><a href="/areas/byers/">Byers</a> is a census place in Arapahoe County, not Adams County. A Byers ZIP still needs a parcel check.</li>
        <li><a href="/areas/elizabeth/">Elizabeth</a> permits only inside town. Many Elizabeth addresses are Elbert County.</li>
        <li><a href="/areas/cherry-creek/">Cherry Creek CDP</a> is Arapahoe County, not Denver's Cherry Creek neighborhood.</li>
        <li><a href="/areas/four-square-mile/">Four Square Mile</a> is an Arapahoe County census area, not Aurora.</li>
        <li><a href="/areas/franktown/">Franktown</a> is Douglas County, and it is not on Pinery Water's community list.</li>
        <li><a href="/areas/sedalia/">Sedalia</a> has a water district whose primary published service is water, not a census-wide sewer.</li>
        <li><a href="/areas/the-pinery/">The Pinery</a> is Pinery Water's community, not a stand-in for the other Douglas places.</li>
        <li><a href="/areas/stonegate/">Stonegate</a> is Stonegate Village Metropolitan District where the bill says so, not the Town of Parker.</li>
        <li><a href="/areas/meridian/">Meridian</a> is Meridian Metropolitan District for its customers, not the City of Lone Tree.</li>
        <li><a href="/areas/roxborough-park/">Roxborough Park</a> is Douglas County. Roxborough Water's central, east, and west areas are not the same service.</li>
        <li><a href="/areas/evergreen/">Evergreen</a> uses Jefferson County, with a well or a district proved on Form 1001.</li>
        <li><a href="/areas/golden/">Golden</a> permits water heaters and water or sewer utility repairs, after an address check that the municipal status is Golden.</li>
        <li><a href="/areas/morrison/">Morrison</a> contracts inspections to Charles Abbott Associates. Confirm the utility on the bill before street work.</li>
        <li><a href="/areas/erie/">Erie</a> reviews a water heater in one to two business days.</li>
        <li><a href="/areas/lafayette/">Lafayette</a> distinguishes a water-heater repair from a replacement.</li>
        <li><a href="/areas/superior/">Superior</a> takes permits only through CommunityCore. SAFEbuilt inspects.</li>
        <li><a href="/areas/boulder/">Boulder</a> treats water heaters as mechanical permits and can exempt a simple stoppage.</li>
      </ul>
      <p>A Census point within 50 straight-line miles is not a promise that a plumber will come, and it is not drive time. Denver's lead program is a <a href="/guides/denver-water-lead-service-line/">guide</a>, not a city hub, because eligibility is an address search. If your mail says Aurora and the parcel is not, confirm the city before you use <a href="/guides/aurora-sewer-line-responsibility/">Aurora's sewer page</a>.</p>
    </article>
    """
    return _page(
        "/areas/",
        "Cities near Aurora | Aurora Plumbing Guide",
        "Centennial, Parker, Highlands Ranch, and Castle Rock, where the permit or the utility changes the plumbing job.",
        "Nearby cities, when the rules differ",
        "Nearby cities",
        "",
        "support",
        body,
    )


def guides_index(site: dict) -> dict:
    del site
    body = """
    <article class="sheet">
      <p class="eyebrow">Paperwork and boundaries</p>
      <h1>Aurora plumbing guides</h1>
      <p class="lede">These guides answer a single question the service pages keep pointing at. They are not a second copy of the hiring pitch.</p>
      <ul class="link-list">
        <li><a href="/guides/aurora-water-heater-permits/">Aurora water heater permits</a></li>
        <li><a href="/guides/aurora-sewer-line-responsibility/">Who owns an Aurora sewer line</a></li>
        <li><a href="/guides/aurora-sewer-camera-second-opinion/">Aurora's free camera review</a></li>
        <li><a href="/guides/plumbing-quote-checklist/">Quote checklist</a> you keep on this device</li>
        <li><a href="/guides/tankless-conversion-quote-checklist/">Tankless quote checklist</a></li>
        <li><a href="/guides/drain-cleaning-vs-sewer-repair/">Drain cleaning versus sewer repair</a></li>
        <li><a href="/guides/trenchless-vs-open-cut/">Trenchless versus open cut</a></li>
        <li><a href="/guides/water-line-vs-sewer-line/">Water line versus sewer line</a></li>
        <li><a href="/guides/city-county-utility-jurisdiction/">Which office controls the address</a></li>
        <li><a href="/guides/centennial-heater-vs-remodel-permit/">Centennial heater versus remodel</a></li>
        <li><a href="/guides/castle-rock-tankless-permit/">Castle Rock tankless papers</a></li>
        <li><a href="/guides/denver-water-lead-service-line/">Denver Water lead lines</a></li>
        <li><a href="/guides/lakewood-water-sewer-provider/">Lakewood providers</a></li>
        <li><a href="/guides/frozen-pipe-vs-winterization/">Frozen pipes versus winterization</a></li>
        <li><a href="/guides/well-pump-vs-city-water/">Well versus city water</a></li>
      </ul>
      <p>Hiring pages stay under repairs. These answer one paperwork or boundary question and link back.</p>
    </article>
    """
    return _page(
        "/guides/",
        "Plumbing guides | Aurora Plumbing Guide",
        "Aurora permit, sewer ownership, camera review, and a quote checklist that does not submit anything.",
        "Aurora plumbing guides",
        "Guides",
        "",
        "support",
        body,
    )


def permit_guide(site: dict) -> dict:
    del site
    body = f"""
    <article class="sheet">
      <p class="eyebrow">City of Aurora Building Division</p>
      <h1>Aurora water heater permits</h1>
      <p class="lede">Yes, plan on a permit and an inspection for a water heater replacement in Aurora. No, the City does not promise the inspector will come the same day. Here is the scheduling language that was actually published, and the piece that was not retrieved.</p>
      <h2>What the inspections page says</h2>
      <p>The <a href="{INSPECT}" rel="noopener noreferrer">inspections and certificate page</a> says work proceeds after required permits, and that the permit card and approved plans must be on the job. For replacement water heaters and furnaces, a licensed plumbing or HVAC contractor may contact the Building Division and ask for a same-day inspection when both the contractor and the homeowner will be present. The City says it will try, and it reserves the right to inspect another day based on volume and staff. Put that sentence next to any quote that says "we'll close it today."</p>
      <p>Other same-day inspections, the page says, go through field supervisors and depend on justification and staffing. Weekend and overtime inspections, when granted, are billed at hourly rates the page does not spell out here. Do not invent the fee. Emergency structural repairs from fire, water, wind, or a vehicle can start before the permit, with a same-day inspection if you call 303-739-7420, and the contractor must still get the permit on the next working business day to meet the code the City cites. That path is for structural damage. It is not a water-heater exemption.</p>
      <h2>How a request gets on the board</h2>
      <p>Contractors who are registered and licensed with Aurora can request, cancel, and read inspections online, up to 5:45 a.m. the day of the inspection. Everyone else may view results. Phone requests use 303-739-7420, Monday, Tuesday, Thursday, and Friday, 7:30 a.m. to 4:30 p.m., and Wednesday 8:30 a.m. to 4:30 p.m. After 4:30 p.m. the request is not added to the next day. The page also lists an email cutoff at 4:30 p.m. Use the address printed there. It is not a contact for this website, and it is not linked as a send button.</p>
      <p>The <a href="{PERMIT}" rel="noopener noreferrer">permitting page</a> is the front door for building permits and contractor licensing. A city handbook that search results describe as asking for heater capacity and fuel type was not opened as a PDF. The file request was refused. Confirm those fields on the live application. Do not treat this paragraph as the form.</p>
      <h2>What to ask the contractor</h2>
      <p>Who pulls the permit. Whether they are licensed with the City so they can request the inspection. Whether you must be home. Which inspection they expect, given that the City's list includes plumbing and gas-pipe inspections for some work. What happens if the inspector comes tomorrow instead of today. If the heater is tankless, leave this guide and use <a href="/services/tankless-water-heater-installation/">tankless installation</a>, and if the house is in Castle Rock, use that town's gas-load rule. The hiring decision for a tank stays on <a href="/services/water-heater-replacement/">replacement</a>.</p>
      {qas([
        (
            "Is same-day inspection guaranteed?",
            "No. Aurora says a licensed contractor can request it for a replacement water heater when the homeowner and the contractor are both available. The same paragraph reserves another day when volume or staffing does not allow it. A quote may not convert that try into a promise. Ask them to request it, and ask what the backup day does to the schedule.",
        ),
        (
            "Can a homeowner put the inspection on the calendar?",
            "The online request tool, as described, is for contractors registered and licensed with the City. Others can view results. Phone and email paths are published for the permit center. This guide will not walk you through pulling a permit as a project. If you are acting as owner-builder, ask the counter what they require before you schedule work.",
        ),
        (
            "Where are the hours and the phone?",
            "Permit center phone 303-739-7420. Weekdays 7:30 a.m. to 4:30 p.m., except Wednesday, which starts at 8:30 a.m. After 4:30 p.m. a request waits. Online requests by eligible contractors run until 5:45 a.m. the day of the inspection. Those are City hours, printed so you can check a contractor's story. They are not a hotline for this site.",
        ),
      ])}
    </article>
    """
    return _page(
        "/guides/aurora-water-heater-permits/",
        "Aurora water heater permits | Aurora Plumbing Guide",
        "Aurora's published inspection rules for water heater replacements, including the same-day request the City does not guarantee.",
        "Aurora water heater permits",
        "Heater permits",
        "Aurora water heater permit",
        "guide",
        body,
    )


def checklist(site: dict) -> dict:
    city = esc(site["cityName"])
    body = f"""
    <article class="sheet">
      <p class="eyebrow">Stays in this browser</p>
      <h1>Plumbing quote checklist</h1>
      <p class="lede">Tick what is going on. The page writes questions you can read to a contractor. It does not price the job, store the answers, or send them.</p>
      <div class="callout" role="note">
        <p>There is no approved place for a lead. Do not type your name, phone, email, or street address. This checklist does not ask for them.</p>
      </div>
      <div id="quote-tool" class="quote-tool" data-city="{city}">
        <fieldset>
          <legend>What is going wrong?</legend>
          <p class="hint">Choose every item that fits.</p>
          <label><input type="checkbox" name="symptom" value="no-hot-water"> No hot water</label>
          <label><input type="checkbox" name="symptom" value="not-enough-hot"> Hot water runs out quickly</label>
          <label><input type="checkbox" name="symptom" value="heater-leaking"> Water at or under the heater</label>
          <label><input type="checkbox" name="symptom" value="tankless-problem"> An existing tankless unit is failing</label>
          <label><input type="checkbox" name="symptom" value="one-fixture"> One fixture drains slowly</label>
          <label><input type="checkbox" name="symptom" value="multi-drain"> Several fixtures are slow, or sewage is backing up</label>
          <label><input type="checkbox" name="symptom" value="wet-spot"> Wet spot, or water running when fixtures are off</label>
          <label><input type="checkbox" name="symptom" value="low-pressure"> Low pressure through the house</label>
          <label><input type="checkbox" name="symptom" value="supply-pipe"> A known supply-pipe failure</label>
          <label><input type="checkbox" name="symptom" value="want-tankless"> Thinking about switching a tank to tankless</label>
        </fieldset>
        <fieldset>
          <legend>Heater, if you know it</legend>
          <p class="choice-label" id="fuel-label">Fuel</p>
          <div class="choices" role="radiogroup" aria-labelledby="fuel-label">
            <label><input type="radio" name="fuel" value="gas"> Gas</label>
            <label><input type="radio" name="fuel" value="electric"> Electric</label>
            <label><input type="radio" name="fuel" value="fuel-unknown"> Not sure</label>
          </div>
          <p class="choice-label" id="style-label">Type</p>
          <div class="choices" role="radiogroup" aria-labelledby="style-label">
            <label><input type="radio" name="style" value="tank"> Storage tank</label>
            <label><input type="radio" name="style" value="tankless"> Tankless</label>
            <label><input type="radio" name="style" value="heat-pump"> Heat pump</label>
            <label><input type="radio" name="style" value="style-unknown"> Not sure</label>
          </div>
          <p class="choice-label" id="place-label">Where it sits</p>
          <div class="choices" role="radiogroup" aria-labelledby="place-label">
            <label><input type="radio" name="place" value="garage"> Garage</label>
            <label><input type="radio" name="place" value="attic"> Attic, closet, or above living space</label>
            <label><input type="radio" name="place" value="outdoor"> Outdoors</label>
            <label><input type="radio" name="place" value="place-unknown"> Not sure</label>
          </div>
          <p class="choice-label" id="change-label">Next heater</p>
          <div class="choices" role="radiogroup" aria-labelledby="change-label">
            <label><input type="radio" name="change" value="like"> Same type and fuel</label>
            <label><input type="radio" name="change" value="change"> Changing type or fuel</label>
            <label><input type="radio" name="change" value="change-unknown"> Not sure</label>
          </div>
        </fieldset>
        <fieldset>
          <legend>Where and what you already know</legend>
          <p class="choice-label" id="where-label">Jurisdiction</p>
          <div class="choices" role="radiogroup" aria-labelledby="where-label">
            <label><input type="radio" name="where" value="inside"> Inside Aurora city limits</label>
            <label><input type="radio" name="where" value="outside"> Another city, or an Aurora mailing address that may be outside the city</label>
            <label><input type="radio" name="where" value="where-unknown"> Not sure</label>
          </div>
          <p class="choice-label" id="camera-label">Sewer camera</p>
          <div class="choices" role="radiogroup" aria-labelledby="camera-label">
            <label><input type="radio" name="camera" value="camera-yes"> Already done</label>
            <label><input type="radio" name="camera" value="camera-no"> Not yet</label>
            <label><input type="radio" name="camera" value="camera-na"> Not a sewer problem</label>
          </div>
        </fieldset>
        <div class="tool-actions">
          <button type="button" id="build-briefing">Build my briefing</button>
          <button type="button" id="reset-briefing">Clear selections</button>
        </div>
        <div id="briefing" class="briefing" aria-live="polite" tabindex="-1"></div>
        <div class="tool-actions">
          <button type="button" id="copy-briefing">Copy briefing</button>
          <button type="button" id="print-briefing">Print briefing</button>
        </div>
        <p id="tool-status" class="tool-status" role="status"></p>
      </div>
      <h2>What the briefing is for</h2>
      <p>It reminds you to name the city, the permit, the pipe, and the exclusions. It does not size a gas line or bless jetting. Read <a href="/guides/aurora-water-heater-permits/">heater permits</a> or <a href="/guides/aurora-sewer-line-responsibility/">sewer ownership</a> when those are the open questions. The <a href="/services/">repair list</a> is where the hiring pages live.</p>
      <section class="qa-list">
        <h2>Questions to settle first</h2>
        <h3 class="qa-q">Does this checklist send my information?</h3>
        <p class="qa-a">No. The buttons build, copy, or print text on this device. There is no form and no address field. If a browser asks to use the clipboard, that copy still stays local. Do not add your name or phone to the printout if you are worried about where the paper goes.</p>
        <h3 class="qa-q">Why is there no price?</h3>
        <p class="qa-a">A number without the city, the pipe, the permit, and the exclusions is not a quote you can compare. This page lists the questions that change scope. The contractor who sees the property is the one who prices it. Nothing here is a bid from Aurora Plumbing Guide.</p>
        <h3 class="qa-q">What if I do not know whether I am inside Aurora?</h3>
        <p class="qa-a">Choose "not sure" and make that the first question you ask. An Aurora mailing address can sit outside the city, and Centennial, Parker, Douglas County, and Castle Rock do not share one sewer rule. The briefing will tell you to confirm the permit office before you compare scopes.</p>
      </section>
    </article>
    """
    page = _page(
        "/guides/plumbing-quote-checklist/",
        "Plumbing quote checklist | Aurora Plumbing Guide",
        "A browser-only checklist for an Aurora plumbing quote. No price and no submission.",
        "Plumbing quote checklist",
        "Quote checklist",
        "plumbing quote checklist",
        "guide",
        body,
    )
    page["extra_scripts"] = '<script src="/js/quote.js"></script>'
    return page


def _is_preview(site: dict) -> bool:
    return bool(site.get("noindex", True))


def _phone_button(site: dict, label_prefix: str = "Call ") -> str:
    phone = site.get("referralPhone") or {}
    if not (site.get("callsEnabled") and phone.get("live") and phone.get("e164") and phone.get("display")):
        return ""
    e164 = esc(phone["e164"])
    display = esc(phone["display"])
    return f'<a class="btn-call" href="tel:{e164}" aria-label="Call {display}">{esc(label_prefix)}{display}</a>'


def about(site: dict) -> dict:
    brand = esc(site["brandName"])
    preview = _is_preview(site)
    intro_note = (
        "Those facts are not established for this preview, so they are not written."
        if preview
        else "Any licensed work is performed strictly by independent contractors you choose to hire."
    )
    referral_note = (
        'A future referral, if one is approved, would introduce you to an independent company under rules that are not set. Read <a href="/how-it-works/">how it works</a>. The <a href="/contact/">contact page</a> explains why there is nothing to submit.'
        if preview
        else 'Read <a href="/how-it-works/">how it works</a> or visit the <a href="/contact/">contact page</a> for referral call details.'
    )
    desc = (
        "Aurora Plumbing Guide is a referral publication, not a plumbing contractor. Contact is not open."
        if preview
        else "Aurora Plumbing Guide is a consumer plumbing guide for Aurora, Colorado homeowners."
    )
    body = f"""
    <article class="sheet">
      <p class="eyebrow">Who publishes this</p>
      <h1>About this guide</h1>
      <p class="lede">{brand} is a referral-style publication about plumbing decisions in Aurora, Colorado. It is not a plumbing contractor.</p>
      <p>The pages name City and Town rules that were read, and they say when a rule was not retrieved or when two documents disagree. They do not invent a crew, a shop, a license number, an insurance certificate, a review score, or years in business. {intro_note}</p>
      <p>A contractor you hire is the one who diagnoses, pulls the permit, and does the work. This site does not supervise that contractor. {referral_note}</p>
      <p>Content was checked against city pages on {esc(site["contentDateLabel"])}. Codes move. The official page and the inspector outrank this summary.</p>
    </article>
    """
    return _page(
        "/about/",
        "About | Aurora Plumbing Guide",
        desc,
        "About this guide",
        "About",
        "",
        "support",
        body,
    )


def how(site: dict) -> dict:
    preview = _is_preview(site)
    cta = _phone_button(site)
    phone = site.get("referralPhone") or {}
    if preview or not cta:
        eyebrow = "Not switched on"
        h1 = "How a referral would work"
        title = "How referral would work | Aurora Plumbing Guide"
        desc = "What a plumbing referral is, and why this preview does not connect you to a contractor."
        lede = "You read the decision, then you call. There is no request form. A phone number is the only way a referral would be placed, and that number is not published until routing is confirmed."
        step3 = "When a number is connected, you would call it. An independent contractor may call you back about that conversation. This preview has no number on the page, no tap-to-call link, and no form to fill out. Geography and hours are not stated because they are not confirmed."
        cta_block = ""
    else:
        eyebrow = "Phone-only referral"
        h1 = "How a referral works"
        title = "How a referral works | Aurora Plumbing Guide"
        desc = "How to connect by phone with an independent plumbing contractor in Aurora, Colorado."
        lede = "You review the scope and permit rules first, then place a direct phone call. There is no lead form."
        step3 = f'Call {esc(phone.get("display", ""))} directly to speak with an independent plumbing routing line. There is no web form or email inbox to fill out.'
        cta_block = f'<div class="call-panel"><h2>Ready to call</h2><p>Speak with the referral routing line directly:</p>{cta}</div>'

    body = f"""
    <article class="sheet">
      <p class="eyebrow">{eyebrow}</p>
      <h1>{h1}</h1>
      <p class="lede">{lede}</p>
      {cta_block}
      <ol class="steps">
        <li>
          <h2>You name the scope</h2>
          <p>The <a href="/services/">repair list</a> separates a clog from a broken sewer, a tank repair from a tankless conversion, and a water leak from a drain. The <a href="/guides/plumbing-quote-checklist/">checklist</a> is notes for you. It does not call anyone and it does not send a message.</p>
        </li>
        <li>
          <h2>A contractor does the work</h2>
          <p>Permits, gas, cameras, and excavation belong to the person allowed to perform them where the property sits. This website does not pull the permit and does not stand behind the work.</p>
        </li>
        <li>
          <h2>The call is the referral</h2>
          <p>{step3}</p>
        </li>
      </ol>
      <p>Verify the license of anyone you hire with the Colorado agency that issues plumbing licenses. This page does not link a guessed lookup URL. If the property is in <a href="/areas/centennial/">Centennial</a>, <a href="/areas/parker/">Parker</a>, <a href="/areas/highlands-ranch/">Highlands Ranch</a>, or <a href="/areas/castle-rock/">Castle Rock</a>, the permit office changes with the parcel.</p>
    </article>
    """
    return _page(
        "/how-it-works/",
        title,
        desc,
        h1,
        "How it works",
        "",
        "support",
        body,
    )


def contact(site: dict) -> dict:
    preview = _is_preview(site)
    cta = _phone_button(site)
    phone = site.get("referralPhone") or {}
    if preview or not cta:
        eyebrow = "Nothing is accepted"
        h1 = "Call is not connected"
        title = "Contact not enabled | Aurora Plumbing Guide"
        desc = "No phone number is published. There is no request form. This preview does not place a call."
        lede = "A referral from this guide would be a phone call. There is no request form, and the call button is not on the site yet because the number has not been confirmed."
        panel = """
      <div class="disabled-panel">
        <h2>Phone only, not live</h2>
        <dl class="plain-dl">
          <dt>This guide's phone</dt>
          <dd>Not published. No tap-to-call link is on any page. An old campaign number is not being reused.</dd>
          <dt>Request form</dt>
          <dd>There isn't one. Do not look for a box to type your name or address. Nothing is waiting to be sent.</dd>
          <dt>City phones</dt>
          <dd>Numbers for Aurora Water or a building department are those offices' lines, printed so you can check a rule. They are not this guide, and they are not links.</dd>
        </dl>
      </div>"""
    else:
        eyebrow = "Phone-only referral"
        h1 = "Call for plumbing service"
        title = "Contact | Aurora Plumbing Guide"
        desc = f"Call {phone.get('display', '')} for Aurora plumbing service referrals. No web forms."
        lede = "Referrals are placed exclusively by phone. There is no web form or email submission."
        recipient = esc(site.get("callRecipientName") or "participating independent plumbing contractors")
        panel = f"""
      <div class="call-panel">
        <h2>Direct referral line</h2>
        <p>Tap below to call directly. Calls are routed to {recipient}.</p>
        {cta}
        <dl class="plain-dl">
          <dt>Phone number</dt>
          <dd>{esc(phone.get("display", ""))}</dd>
          <dt>Request form</dt>
          <dd>There is no request form. Nothing is collected or stored on this website.</dd>
          <dt>City phones</dt>
          <dd>Numbers for Aurora Water or a building department are those offices' lines, printed so you can verify a rule directly.</dd>
        </dl>
      </div>"""

    body = f"""
    <article class="sheet">
      <p class="eyebrow">{eyebrow}</p>
      <h1>{h1}</h1>
      <p class="lede">{lede}</p>
      {panel}
      <p>The <a href="/guides/plumbing-quote-checklist/">checklist</a> only helps you remember questions. It stays on your device.</p>
    </article>
    """
    return _page(
        "/contact/",
        title,
        desc,
        h1,
        "Contact",
        "",
        "support",
        body,
    )


def privacy(site: dict) -> dict:
    preview = _is_preview(site)
    phone = site.get("referralPhone") or {}
    recipient = esc(site.get("callRecipientName") or "participating independent plumbing contractors")
    if preview or not (site.get("callsEnabled") and phone.get("live")):
        eyebrow = f"Preview only · {esc(site['contentDateLabel'])}"
        lede = "This guide does not take a form, an upload, or an email. The only referral path intended later is a phone call, and that number is not on the site."
        desc = "No request form and no published phone number. The checklist stays in your browser."
        policy_tail = "A future live number would be shown in one place, the same on every page, and this policy would name who receives the call before that happens."
    else:
        eyebrow = f"Updated · {esc(site['contentDateLabel'])}"
        lede = "This guide does not collect web forms, uploads, or email addresses. The only contact method is a direct phone call."
        desc = "Privacy policy for Aurora Plumbing Guide. No request forms or browser tracking."
        policy_tail = f"Published phone calls to {esc(phone.get('display', ''))} are received and handled by {recipient}."

    body = f"""
    <article class="sheet">
      <p class="eyebrow">{eyebrow}</p>
      <h1>Privacy</h1>
      <p class="lede">{lede}</p>
      <p>Pages are static. There is no account and no analytics script. The checklist reads boxes in your browser and writes notes on the page. Those notes are not transmitted. Do not type your name, phone, or address into the checklist. If you call a published number, that call is between you and whoever answers. This website does not record it.</p>
      <p>City and town links leave this site and follow those governments' own practices. {policy_tail}</p>
    </article>
    """
    return _page(
        "/privacy/",
        "Privacy | Aurora Plumbing Guide",
        desc,
        "Privacy",
        "Privacy",
        "",
        "support",
        body,
    )


def terms(site: dict) -> dict:
    preview = _is_preview(site)
    if preview:
        eyebrow = f"Preview terms · {esc(site['contentDateLabel'])}"
        lede = "These terms cover an unpublished draft. They are not a contract for plumbing work and not an offer to refer you to a contractor."
        desc = "Terms for the Aurora Plumbing Guide preview. Not a bid and not a referral offer."
        tail = "No request is accepted. No result is guaranteed. No review is published because none are claimed. The local address in the footer of each page is only the preview canonical host. No production domain is attached."
    else:
        eyebrow = f"Terms of use · {esc(site['contentDateLabel'])}"
        lede = "These terms govern use of Aurora Plumbing Guide. This publication is not a plumbing contractor and does not guarantee contractor availability or pricing."
        desc = "Terms of use for Aurora Plumbing Guide."
        tail = "No online form request is accepted. No plumbing result or price is guaranteed. No customer review is published."

    body = f"""
    <article class="sheet">
      <p class="eyebrow">{eyebrow}</p>
      <h1>Terms</h1>
      <p class="lede">{lede}</p>
      <p>The articles are decision aids. They are not a diagnosis, a permit approval, or a price. Gas, electrical, and excavation hazards are real. Hire someone qualified, or use an owner-builder path only where that building department allows it. This site will not give gas or electrical steps.</p>
      <p>City pages can change after {esc(site["contentDateLabel"])}. If a summary and the official page disagree, follow the official page and the inspector. A mailing city is not a jurisdiction. Parker’s service-line documents are called out as unresolved on purpose.</p>
      <p>{tail}</p>
    </article>
    """
    return _page(
        "/terms/",
        "Terms | Aurora Plumbing Guide",
        desc,
        "Terms",
        "Terms",
        "",
        "support",
        body,
    )


def missing(site: dict) -> dict:
    preview = _is_preview(site)
    h1 = "That page is not in this preview" if preview else "Page not found"
    desc = (
        "That address is not a published page in this noindex preview."
        if preview
        else "That address does not match a published page on Aurora Plumbing Guide."
    )
    body = f"""
    <article class="sheet">
      <p class="eyebrow">404</p>
      <h1>{h1}</h1>
      <p class="lede">The address does not match a page that was published. Many city and specialty pages are intentionally absent until their own permit and utility sources are checked.</p>
      <p>Use the <a href="/">home page</a>, the <a href="/services/">repair list</a>, or the <a href="/areas/">cities that are written</a>. Reaching this page did not submit anything.</p>
    </article>
    """
    return _page(
        "/404.html",
        "Page not found | Aurora Plumbing Guide",
        desc,
        h1,
        "Page not found",
        "",
        "support",
        body,
        in_sitemap=False,
    )


def _page(path, title, description, h1, crumb, keyword, kind, body, in_sitemap=True) -> dict:
    return {
        "path": path,
        "title": title,
        "description": description,
        "h1": h1,
        "breadcrumb": crumb,
        "intended_keyword": keyword,
        "keyword_status": "Qualitative only. No volume or difficulty number.",
        "kind": kind,
        "in_sitemap": in_sitemap,
        "body": body,
    }
