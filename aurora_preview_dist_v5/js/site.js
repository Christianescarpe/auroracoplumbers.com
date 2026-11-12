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

  // Hero full-width background image crossfade slider
  var heroSections = document.querySelectorAll(".hero-has-slider");
  if (heroSections.length) {
    var reduceMotionQuery = window.matchMedia ? window.matchMedia("(prefers-reduced-motion: reduce)") : null;
    heroSections.forEach(function (hero) {
      var slides = Array.prototype.slice.call(hero.querySelectorAll(".hero-bg-slide"));
      if (slides.length < 2) return;
      var dots = Array.prototype.slice.call(hero.querySelectorAll(".hero-slider-dot"));
      var prevBtn = hero.querySelector("[data-hero-prev]");
      var nextBtn = hero.querySelector("[data-hero-next]");
      var index = 0;
      var timerId = null;
      var hovered = false;
      var focused = false;

      function loadSlide(i) {
        var slide = slides[(i + slides.length) % slides.length];
        if (!slide) return;
        var src = slide.getAttribute("data-bg");
        if (src && !slide.dataset.loaded) {
          slide.dataset.loaded = "true";
          var preloader = new Image();
          preloader.onload = function () {
            slide.style.backgroundImage = "url('" + src + "')";
          };
          preloader.src = src;
          slide.style.backgroundImage = "url('" + src + "')";
        }
      }

      function goTo(nextIndex) {
        var target = (nextIndex + slides.length) % slides.length;
        loadSlide(target);
        loadSlide(target + 1);
        slides.forEach(function (s, idx) {
          s.classList.toggle("is-active", idx === target);
        });
        dots.forEach(function (d, idx) {
          var active = idx === target;
          d.classList.toggle("is-active", active);
          d.setAttribute("aria-pressed", active ? "true" : "false");
        });
        index = target;
      }

      function stopTimer() {
        if (timerId) {
          clearInterval(timerId);
          timerId = null;
        }
      }

      function startTimer() {
        stopTimer();
        if (reduceMotionQuery && reduceMotionQuery.matches) return;
        if (document.hidden || hovered || focused) return;
        timerId = setInterval(function () {
          goTo(index + 1);
        }, 5500);
      }

      // Lazy-preload slide 2 shortly after first paint so initial crossfade is seamless
      setTimeout(function () {
        loadSlide(1);
      }, 1500);

      dots.forEach(function (dot, idx) {
        dot.addEventListener("click", function () {
          goTo(idx);
          startTimer();
        });
      });

      if (prevBtn) {
        prevBtn.addEventListener("click", function () {
          goTo(index - 1);
          startTimer();
        });
      }

      if (nextBtn) {
        nextBtn.addEventListener("click", function () {
          goTo(index + 1);
          startTimer();
        });
      }

      hero.addEventListener("mouseenter", function () {
        hovered = true;
        stopTimer();
      });
      hero.addEventListener("mouseleave", function () {
        hovered = false;
        startTimer();
      });
      hero.addEventListener("focusin", function () {
        focused = true;
        stopTimer();
      });
      hero.addEventListener("focusout", function () {
        focused = false;
        startTimer();
      });

      document.addEventListener("visibilitychange", function () {
        if (document.hidden) stopTimer();
        else startTimer();
      });

      if (reduceMotionQuery && typeof reduceMotionQuery.addEventListener === "function") {
        reduceMotionQuery.addEventListener("change", function () {
          if (reduceMotionQuery.matches) stopTimer();
          else startTimer();
        });
      }

      startTimer();
    });
  }
})();
