(function () {
  var tool = document.getElementById("quote-tool");
  if (!tool) return;

  var briefing = document.getElementById("briefing");
  var status = document.getElementById("tool-status");

  function selected(name) {
    return Array.prototype.map.call(
      tool.querySelectorAll('input[name="' + name + '"]:checked'),
      function (node) { return node.value; }
    );
  }

  function one(name) {
    var node = tool.querySelector('input[name="' + name + '"]:checked');
    return node ? node.value : "";
  }

  function labelFor(input) {
    var label = input.closest("label");
    if (!label) return input.value;
    return label.textContent.replace(/\s+/g, " ").trim();
  }

  function addParagraph(parent, text) {
    var p = document.createElement("p");
    p.textContent = text;
    parent.appendChild(p);
  }

  function addList(parent, items) {
    var ul = document.createElement("ul");
    items.forEach(function (item) {
      var li = document.createElement("li");
      li.textContent = item;
      ul.appendChild(li);
    });
    parent.appendChild(ul);
  }

  function addHeading(parent, level, text) {
    var heading = document.createElement(level);
    heading.textContent = text;
    parent.appendChild(heading);
  }

  document.getElementById("build-briefing").addEventListener("click", function () {
    var symptoms = selected("symptom");
    briefing.replaceChildren();
    if (!symptoms.length) {
      addParagraph(briefing, "Select at least one problem. Nothing is sent either way.");
      status.textContent = "No briefing yet. Nothing was sent.";
      briefing.focus();
      return;
    }

    addHeading(briefing, "h2", "Briefing for a contractor you contact yourself");
    addParagraph(briefing, "This text was built in your browser. It was not submitted, priced, or saved by the site.");
    addHeading(briefing, "h3", "What you marked");
    var marked = [];
    tool.querySelectorAll("input:checked").forEach(function (input) {
      marked.push(labelFor(input));
    });
    addList(briefing, marked);

    var questions = [
      "Which building department permits this exact parcel, and who will pull the permit?",
      "What is included, and what is excluded, before any work starts?"
    ];

    if (symptoms.indexOf("no-hot-water") !== -1 || symptoms.indexOf("not-enough-hot") !== -1 || symptoms.indexOf("heater-leaking") !== -1) {
      questions.push("Is the next step a repair diagnosis of the existing heater, or a permitted replacement?");
      questions.push("If it is a replacement, is it like-for-like in type, fuel, and input, or will gas sizing and energy-code paperwork be required?");
    }
    if (symptoms.indexOf("want-tankless") !== -1 || one("change") === "change") {
      questions.push("Can the existing gas supply, vent, condensate path, and electrical circuit support a tankless unit? That is a different project from swapping a like tank.");
    }
    if (symptoms.indexOf("tankless-problem") !== -1 || one("style") === "tankless") {
      questions.push("For an existing tankless unit, what did the error or the scale condition show, and would parts be replaced or the whole unit?");
    }
    if (one("place") === "garage") {
      questions.push("The heater is in a garage. Does the quote include elevation and vehicle protection when the city handout requires them?");
    }
    if (one("place") === "attic") {
      questions.push("The heater is in an attic, closet, or above living space. Does the quote include the pan, drain, access, and combustion-air items the permit handout triggers?");
    }
    if (one("fuel") === "gas") {
      questions.push("A gas heater needs the contractor to handle venting, combustion air, the connector, and any sizing calculation. Those are not homeowner steps.");
    }
    if (symptoms.indexOf("one-fixture") !== -1) {
      questions.push("Is one slow fixture a local blockage, or is there a reason to inspect the building drain before cleaning?");
    }
    if (symptoms.indexOf("multi-drain") !== -1) {
      questions.push("Where does a camera show the defect, relative to the cleanout and the right-of-way?");
      questions.push("Is the quote for cleaning, a spot repair, or replacement, and who maintains that segment: the city, another agency, or the owner?");
    }
    if (one("camera") === "camera-no" && (symptoms.indexOf("multi-drain") !== -1 || symptoms.indexOf("one-fixture") !== -1)) {
      questions.push("What has to be seen on camera before trenchless work or hydro-jetting is recommended? Jetting is not appropriate for every pipe.");
    }
    if (symptoms.indexOf("wet-spot") !== -1 || symptoms.indexOf("low-pressure") !== -1) {
      questions.push("How will the leak be located before walls, a slab, or the yard are opened?");
    }
    if (symptoms.indexOf("supply-pipe") !== -1) {
      questions.push("Is this one water-service or branch repair, or is the evidence actually strong enough for whole-house repiping?");
    }
    if (one("where") === "outside" || one("where") === "where-unknown") {
      questions.push("Is this parcel inside city limits? A city mailing address is not enough to choose the city permit handout or the city sewer rules.");
    }

    addHeading(briefing, "h3", "Questions to ask");
    addList(briefing, questions);
    addParagraph(briefing, "No dollar figure belongs on this briefing. A real quote has to come from someone who has seen the property and checked the current code.");
    addParagraph(briefing, "Explore our published plumbing guides for permit and lateral rules, and check our areas directory for municipal coverage.");

    var links = document.createElement("p");
    var notes = document.createElement("a");
    notes.href = "/guides/";
    notes.textContent = "Plumbing guides";
    var area = document.createElement("a");
    area.href = "/areas/";
    area.textContent = "Service area limits";
    links.appendChild(notes);
    links.appendChild(document.createTextNode(" · "));
    links.appendChild(area);
    briefing.appendChild(links);

    status.textContent = "Briefing ready on this page. It was not sent.";
    briefing.focus();
  });

  document.getElementById("reset-briefing").addEventListener("click", function () {
    tool.querySelectorAll("input").forEach(function (input) {
      input.checked = false;
    });
    briefing.replaceChildren();
    status.textContent = "Selections cleared. Nothing was stored.";
  });

  document.getElementById("copy-briefing").addEventListener("click", function () {
    var text = briefing.innerText.trim();
    if (!text) {
      status.textContent = "Build a briefing before copying. Nothing was sent.";
      return;
    }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(function () {
        status.textContent = "Copied on this device. Nothing was sent.";
      }, function () {
        status.textContent = "Clipboard copy was blocked. Select the briefing and copy it yourself. Nothing was sent.";
      });
    } else {
      status.textContent = "Select the briefing and copy it yourself. Nothing was sent.";
    }
  });

  document.getElementById("print-briefing").addEventListener("click", function () {
    if (!briefing.innerText.trim()) {
      status.textContent = "Build a briefing before printing. Nothing was sent.";
      return;
    }
    window.print();
    status.textContent = "Print dialog opened on this device. Nothing was sent.";
  });
})();
