---
layout: post
comments: true
title: "More games in the browser"
image: /assets/posts/raid-web.png
tags: [Geekery, Technology, Personal, Games]
---

![A gunship over a green hill at dusk, a flak gun firing at it](/assets/posts/raid-web.png)

I'm having a renaissance of my young years as a gamer here, and since funkey engine got faster lately... I added more of the games in the browser.

## Raid

The gunship over fractal mountains from [the last batch](/2026/10/Raid-Vector-Marble.html). Play it right here:

<div class="fk-game">
<canvas id="raid-game" data-wasm="/assets/play/raid.wasm?v=1.2" aria-label="raid, a gunship over fractal mountains"></canvas>
<div class="fk-pad" id="raid-pad" hidden></div>
<p class="fk-bar"><button type="button" id="raid-full">Full screen</button> <button type="button" id="raid-keys">Keys on screen</button></p>
</div>

<script src="/assets/play/funkey.js?v=4"></script>
<script src="/assets/play/raid.js?v=1"></script>

Click the game, then `Space`. On a phone the keys show under it.

- `Left` and `Right` turn. `Up` and `Down` set the speed.
- `W` and `S` set the height over the ground. `A` and `D` slide sideways.
- `Space` fires the gun, `F` a rocket, `E` a guided missile at the boxed target.
- Six missions. The hills are cover.
- A top ten with initials, shared by everyone who plays here or on the [try page](https://isene.org/fe2o3/try/funkeys/play.html?g=raid).

## Soar

The original basis for Raid: flight over fractal mountains, water and clouds. Fly it in [your browser](https://isene.org/fe2o3/try/funkeys/play.html?g=soar).

![Rocky peaks around a bay, the sun low over the haze](/assets/posts/soar-web.png)

Let the autopilot fly, or take the stick. Nothing to win here.

## Castle

The walk from the hills to a castle and in through its gate. Walk it in [your browser](https://isene.org/fe2o3/try/funkeys/play.html?g=castle).

![A path across the grass to a stone castle, mountains behind](/assets/posts/castle-web.png)

Nothing to win here either.

## One core

A browser gives a game one core. In the terminal games get a lot more umpf. On one core Raid and Soar were a bit too slow. Castle was twice too slow.

- Raid and Soar now work out the ground for every other column of pixels. Each column is drawn twice as wide.
- Castle draws a picture half as wide and half as high.

Now a frame takes about 22 milliseconds. 30 pictures a second.

The terminal versions are untouched. Same pictures, pixel for pixel. Same speed.

The 18th game is Doom. That needs the data file of the original game, and that is many megabytes. Doom stays in the terminal.

## Summary

Built with [Claude](https://claude.com/claude-code) on [funkey](https://isene.org/funkey/). One message, 22 minutes. Public Domain, like [everything I make](/2026/04/MyTools.html).

- [raid](https://github.com/isene/funkey/blob/master/examples/raid.rs), [soar](https://github.com/isene/funkey/blob/master/examples/soar.rs) and [castle](https://github.com/isene/funkey/blob/master/examples/castle.rs)
- [All 17 games on the try page](https://isene.org/fe2o3/try/funkeys/)

---

Link to this post: https://isene.org/2026/10/More-Browser-Games.html
