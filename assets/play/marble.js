// marble in a blog post: the game, keys on the screen for phones, and full
// screen. The game is funkey's marble built for the web; funkey.js plays it.
(async function () {
  "use strict";
  // The tiles run corner to corner, so a button rolls the way its arrow points.
  const MOVE = [["ArrowLeft", "↖", ""], ["ArrowLeft|ArrowUp", "↑", ""], ["ArrowUp", "↗", ""],
    ["ArrowLeft|ArrowDown", "←", ""], ["", "", ""], ["ArrowRight|ArrowUp", "→", ""],
    ["ArrowDown", "↙", ""], ["ArrowRight|ArrowDown", "↓", ""], ["ArrowRight", "↘", ""]];
  const KEYS = [[" ", "Space", "start"], ["p", "P", "pause"], ["q", "Q", "quit"]];
  const style = document.createElement("style");
  style.textContent = `
.fk-game { margin: 1rem 0 1.4rem; }
.fk-game canvas { display: block; width: 100%; aspect-ratio: 16 / 10; background: #000; }
.fk-game .fk.on canvas { outline: 2px solid #ffd040; outline-offset: 2px; }
.fk-bar { margin: 0.5rem 0 0; }
.fk-bar button, .fk-pad button { font: inherit; color: #eee; background: #2a2d3a; border: 1px solid #4a5068;
  border-radius: 5px; cursor: pointer; }
.fk-bar button { font-size: 0.9rem; padding: 0.2rem 0.7rem; margin-right: 0.4rem; }
.fk-pad { display: flex; flex-wrap: wrap; justify-content: space-between; gap: 0.8rem; margin: 0.6rem 0 0;
  user-select: none; -webkit-user-select: none; }
.fk-pad[hidden] { display: none; }
.fk-pad .move, .fk-pad .keys { display: grid; gap: 0.3rem; }
.fk-pad .move { grid-template-columns: repeat(3, 3.4rem); grid-auto-rows: 3.2rem; }
.fk-pad .keys { grid-template-columns: 4.6rem; grid-auto-rows: 3.2rem; }
.fk-pad button { padding: 0; font-weight: 600; font-size: 1.1rem; line-height: 1.05; touch-action: none;
  -webkit-touch-callout: none; }
.fk-pad button small { display: block; font-size: 0.6rem; font-weight: 400; opacity: 0.7; }
.fk-pad button.down { background: #ffd040; color: #000; }
.fk-pad button.gap { visibility: hidden; }
.fk-game:fullscreen { background: #000; box-sizing: border-box; padding: 0.5rem; margin: 0; display: grid; gap: 0.5rem;
  grid-template: "screen" 1fr "pad" auto / 1fr; }
.fk-game:fullscreen .fk { grid-area: screen; min-height: 0; }
.fk-game:fullscreen .fk, .fk-game:fullscreen canvas { width: 100%; height: 100%; }
.fk-game:fullscreen canvas { aspect-ratio: auto; object-fit: contain; }
.fk-game:fullscreen .fk.on canvas { outline: none; }
.fk-game:fullscreen .fk-pad { grid-area: pad; margin: 0; }
.fk-game:fullscreen .fk-bar { display: none; }
@media (orientation: landscape) {
  .fk-game:fullscreen { grid-template: "move screen keys" 1fr / auto 1fr auto; align-items: center; }
  .fk-game:fullscreen .fk-pad:not([hidden]) { display: contents; }
  .fk-game:fullscreen .move { grid-area: move; }
  .fk-game:fullscreen .keys { grid-area: keys; }
}`;
  document.head.append(style);

  const box = document.querySelector(".fk-game");
  const pad = document.getElementById("marble-pad");
  const button = ([k, label, small]) => {
    const b = document.createElement("button");
    b.type = "button";
    if (!k) { b.className = "gap"; b.tabIndex = -1; return b; }
    b.dataset.key = k;
    b.textContent = label;
    if (small) { const s = document.createElement("small"); s.textContent = small; b.append(s); }
    return b;
  };
  const group = (cls, list) => {
    const g = document.createElement("div");
    g.className = cls;
    g.append(...list.map(button));
    return g;
  };
  pad.append(group("move", MOVE), group("keys", KEYS));
  pad.hidden = !(window.matchMedia && matchMedia("(pointer: coarse)").matches);
  document.getElementById("marble-keys").addEventListener("click", () => { pad.hidden = !pad.hidden; });
  const full = document.getElementById("marble-full");
  if (!document.fullscreenEnabled) full.hidden = true;
  full.addEventListener("click", () => box.requestFullscreen().catch(() => {}));

  const canvas = document.getElementById("marble-game");
  const game = await funkey.play(canvas, canvas.dataset.wasm);
  funkey.pad(pad, game);
})();
