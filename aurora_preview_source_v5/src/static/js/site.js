(function () {
  var button = document.querySelector(".nav-toggle");
  var nav = document.getElementById("site-nav");
  if (!button || !nav) return;

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
})();
