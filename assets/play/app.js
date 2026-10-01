// A Fe₂O₃ terminal app inside a blog post. In the post:
//
//   <div class="fe-app" data-app="moon" data-wasm="/fe2o3/try/apps/moon.wasm?v=0.1.12"
//        data-keys="← → step a day">
//     <img src="/assets/posts/try-moon.png" alt="The Moon tonight">
//   </div>
//   <script src="/assets/play/app.js?v=1"></script>
//
// The picture shows until the reader clicks it. Only then do the terminal
// (xterm.js) and the app load, from the try page at /fe2o3/try/, and the
// app starts where the picture was. A reader who only reads loads nothing.
(function () {
  "use strict";
  if (window.__feApps) return;
  window.__feApps = true;
  const TERM = "/fe2o3/try/term/";
  const SCRIPTS = ["xterm.js?v=6.0.0", "addon-fit.js?v=0.11.0", "addon-webgl.js?v=0.19.0", "addon-image.js?v=0.9.0", "term.js?v=4"];

  const style = document.createElement("style");
  style.textContent = `
.fe-app { position: relative; margin: 1rem 0 1.4rem; }
.fe-app > img { display: block; width: 100%; margin: 0; cursor: pointer; }
.fe-app .fe-start { position: absolute; left: 0; right: 0; top: 42%; margin: 0; padding: 0.9rem 0; border: 0; cursor: pointer;
  background: rgba(0, 0, 0, 0.65); color: #ffd040; font: bold 1.1rem ui-monospace, Menlo, Consolas, monospace; }
.fe-app .fe-screen { background: #0a0910; box-shadow: 0 0 0 1px #26263a; border-radius: 8px; }
.fe-app .fe-screen .xterm { padding: 6px; }
.fe-app .fe-screen.on { box-shadow: 0 0 0 2px #ffd040; }
.fe-app .fe-bar { margin: 0.4rem 0 0; }
.fe-app .fe-bar button, .fe-app .fe-bar a { font: inherit; font-size: 0.9rem; color: #eee; background: #2a2d3a; border: 1px solid #4a5068;
  border-radius: 5px; padding: 0.2rem 0.7rem; margin-right: 0.4rem; cursor: pointer; text-decoration: none; }
.fe-app .fe-keys { font-size: 0.85rem; opacity: 0.75; }
.fe-app .fe-screen:fullscreen { box-sizing: border-box; padding: 0.5rem; border-radius: 0; }`;
  document.head.append(style);

  // The terminal's files, loaded once for all the apps on the page.
  let ready = null;
  const load = () => ready || (ready = (async () => {
    const css = document.createElement("link");
    css.rel = "stylesheet";
    css.href = TERM + "xterm.css";
    document.head.append(css);
    for (const s of SCRIPTS) {
      await new Promise((ok, fail) => {
        const el = document.createElement("script");
        el.src = TERM + s;
        el.onload = ok;
        el.onerror = fail;
        document.head.append(el);
      });
    }
  })());

  for (const box of document.querySelectorAll(".fe-app")) {
    const name = box.dataset.app, img = box.querySelector("img");
    const start = document.createElement("button");
    start.type = "button";
    start.className = "fe-start";
    start.textContent = "CLICK TO RUN " + name.toUpperCase() + " HERE";
    box.append(start);
    const run = async () => {
      start.textContent = "LOADING…";
      start.disabled = true;
      const h = Math.max(img ? img.clientHeight : 0, 360);
      try { await load(); } catch (e) { start.textContent = "COULD NOT LOAD"; return; }
      const screen = document.createElement("div");
      screen.className = "fe-screen";
      screen.style.height = h + "px";
      const bar = document.createElement("p");
      bar.className = "fe-bar";
      if (document.fullscreenEnabled) {
        const full = document.createElement("button");
        full.type = "button";
        full.textContent = "Full screen";
        full.addEventListener("click", () => screen.requestFullscreen().catch(() => {}));
        bar.append(full);
      }
      const page = document.createElement("a");
      page.href = "/fe2o3/try/app.html?a=" + encodeURIComponent(name);
      page.textContent = "On its own page";
      bar.append(page);
      if (box.dataset.keys) {
        const keys = document.createElement("span");
        keys.className = "fe-keys";
        keys.textContent = box.dataset.keys;
        bar.append(keys);
      }
      box.replaceChildren(screen, bar);
      crustterm.run(screen, box.dataset.wasm, { name });
    };
    start.addEventListener("click", run);
    if (img) img.addEventListener("click", run);
  }
})();
