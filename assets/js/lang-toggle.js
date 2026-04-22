(function () {
  var KEY = "banglallm_lang";
  var html = document.documentElement;
  var btn = document.getElementById("lang-toggle");
  if (!btn) return;

  var saved = null;
  try { saved = localStorage.getItem(KEY); } catch (e) {}
  if (saved === "bn" || saved === "en") setLang(saved);

  btn.addEventListener("click", function () {
    var next = html.getAttribute("data-lang") === "bn" ? "en" : "bn";
    setLang(next);
    try { localStorage.setItem(KEY, next); } catch (e) {}
  });

  function setLang(lang) {
    html.setAttribute("data-lang", lang);
    html.setAttribute("lang", lang);
  }
})();
