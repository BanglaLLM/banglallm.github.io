/* Language toggle */
(function () {
  var KEY = "banglallm_lang";
  var html = document.documentElement;
  var btn = document.getElementById("lang-toggle");

  var saved = null;
  try { saved = localStorage.getItem(KEY); } catch (e) {}
  if (saved === "bn" || saved === "en") setLang(saved);

  if (btn) {
    btn.addEventListener("click", function () {
      var next = html.getAttribute("data-lang") === "bn" ? "en" : "bn";
      setLang(next);
      try { localStorage.setItem(KEY, next); } catch (e) {}
    });
  }

  function setLang(lang) {
    html.setAttribute("data-lang", lang);
    html.setAttribute("lang", lang);
  }
})();

/* Mobile nav */
(function () {
  var toggle = document.getElementById("nav-toggle");
  var nav = document.getElementById("site-nav");
  if (!toggle || !nav) return;

  function setOpen(open) {
    nav.classList.toggle("is-open", open);
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
  }

  toggle.addEventListener("click", function () {
    setOpen(toggle.getAttribute("aria-expanded") !== "true");
  });

  nav.addEventListener("click", function (e) {
    if (e.target.closest("a")) setOpen(false);
  });

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && toggle.getAttribute("aria-expanded") === "true") {
      setOpen(false);
      toggle.focus();
    }
  });

  // Widening past the breakpoint must not strand the panel in its open state
  var mq = window.matchMedia("(min-width: 721px)");
  function onChange(e) { if (e.matches) setOpen(false); }
  if (mq.addEventListener) { mq.addEventListener("change", onChange); }
  else if (mq.addListener) { mq.addListener(onChange); }
})();
