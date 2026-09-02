/* Mobile nav. The language switch is a plain link to the other language's URL,
   so it needs no JavaScript and stays crawlable. */
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

  var mq = window.matchMedia("(min-width: 721px)");
  function onChange(e) { if (e.matches) setOpen(false); }
  if (mq.addEventListener) { mq.addEventListener("change", onChange); }
  else if (mq.addListener) { mq.addListener(onChange); }
})();
