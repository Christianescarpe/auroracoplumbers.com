(function () {
  var button = document.querySelector(".nav-toggle");
  var nav = document.getElementById("site-nav");
  if (button && nav) {
    var desktop = window.matchMedia("(min-width: 860px)");

    function setOpen(open) {
      button.setAttribute("aria-expanded", open ? "true" : "false");
      nav.classList.toggle("is-open", open);
    }

    function sync() {
      if (desktop.matches) {
        nav.classList.remove("is-open");
        button.setAttribute("aria-expanded", "true");
      } else if (!nav.classList.contains("is-open")) {
        button.setAttribute("aria-expanded", "false");
      }
    }

    button.addEventListener("click", function () {
      if (desktop.matches) return;
      setOpen(button.getAttribute("aria-expanded") !== "true");
    });

    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape" && !desktop.matches) setOpen(false);
    });

    nav.addEventListener("click", function (event) {
      if (event.target.closest("a") && !desktop.matches) setOpen(false);
    });

    if (typeof desktop.addEventListener === "function") {
      desktop.addEventListener("change", sync);
    }
    sync();
  }

  // Homepage interactive jurisdiction / guide tabs
  var tabs = document.querySelectorAll(".workflow-tab");
  var panel = document.getElementById("workflow-panel");
  if (tabs.length && panel) {
    var titleEl = panel.querySelector("[data-wf-title]");
    var bodyEl = panel.querySelector("[data-wf-body]");
    var linkEl = panel.querySelector("[data-wf-link]");
    var imgEl = panel.querySelector("[data-wf-img]");

    tabs.forEach(function (tab) {
      tab.addEventListener("click", function () {
        tabs.forEach(function (item) {
          item.classList.remove("is-active");
          item.setAttribute("aria-selected", "false");
        });
        tab.classList.add("is-active");
        tab.setAttribute("aria-selected", "true");

        if (titleEl && tab.dataset.title) titleEl.textContent = tab.dataset.title;
        if (bodyEl && tab.dataset.body) bodyEl.textContent = tab.dataset.body;
        if (linkEl && tab.dataset.href) {
          linkEl.setAttribute("href", tab.dataset.href);
          if (tab.dataset.cta) linkEl.textContent = tab.dataset.cta;
        }
        if (imgEl && tab.dataset.img) {
          imgEl.setAttribute("src", tab.dataset.img);
          if (tab.dataset.alt) imgEl.setAttribute("alt", tab.dataset.alt);
        }
      });
    });
  }
})();
