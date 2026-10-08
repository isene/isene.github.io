---
layout: post
comments: true
title: "Raid, Vector and Marble"
image: /assets/posts/raid-play.png
tags: [Geekery, Technology, Personal, Games]
---

![A gunship over a lake, a flak gun in its sights](/assets/posts/raid-play.png)

It's madness, but not just Marble Madness. With my own software throughout, it's now silly easy to create something new. The funkey game engine makes for easy game creations.

After [Gems](/2026/09/Gems.html), [Salvo](/2026/09/Salvo.html), [the Eliminator](/2026/09/Eliminator.html) and [Stack](/2026/09/Stack.html), I asked Claude for three more games in one message. A helicopter game, then Tempest, then Marble Madness.

## Raid

A gunship over fractal mountains, in the spirit of Comanche.

- Six missions, from a radar post at dawn to a fortress at night.
- A gun, rockets and guided missiles. Trucks, tanks, flak, gunboats, missile sites and other gunships.
- The gunship follows the ground at the height you set.
- The hills are cover. A missile site cannot see what flies low behind one.
- Hover over the pad to rearm and repair.
- After the sixth mission it all begins again. Harder.

## Vector

A tribute to Tempest. Play it in [your browser](https://isene.org/fe2o3/try/funkeys/play.html?g=vector).

![A heart-shaped web, the claw on its rim](/assets/posts/vector-play.png)

- Glowing lines on black. Sixteen webs seen down their length, a claw on the rim.
- Flippers flip from lane to lane. Tankers split in two. Spikers leave spikes.
- Fuseballs ride the edges. Pulsars charge their lane.
- The superzapper clears the web. Once.
- The lines add their light where they cross, and fade as on a vector tube.
- Leave the title alone and it plays itself.

## Marble

A tribute to Marble Madness. Play it right here:

<div class="fk-game">
<canvas id="marble-game" data-wasm="/assets/play/marble.wasm?v=1.0" aria-label="marble, a tribute to Marble Madness"></canvas>
<div class="fk-pad" id="marble-pad" hidden></div>
<p class="fk-bar"><button type="button" id="marble-full">Full screen</button> <button type="button" id="marble-keys">Keys on screen</button></p>
</div>

<script src="/assets/play/funkey.js?v=4"></script>
<script src="/assets/play/marble.js?v=1"></script>

Click the game, then `Space`. On a phone the keys show under it.

![The marble on ice, with acid ahead and a spring behind](/assets/posts/marble-ice.png)

- Six courses, each against the clock. You take with you the seconds you have left over to the next course.
- The arrows roll the marble along the tiles. `Right` is down to the right, `Down` is down to the left.
- Roll off the edge, drop too far, get eaten or melt: it costs seconds. A new marble rolls in.
- Steel balls charge and knock you off. Knock one off yourself for 1000 points.
- Green springs hop around and eat marbles. Acid slides across the track.
- On ice the arrows do little. Aim before you get there.
- Two courses have a hole to jump. Take the slope before it at full speed.

![The six courses](/assets/posts/marble-courses.png)

## Tributes

Copies would need the makers' own programs. So everything here is new: the land, the webs, the courses, the foes, the sounds.

Tempest had a knob to spin. Marble Madness had a trackball. Here the arrow keys do the work.

Raid paints the land on every core, so it stays in the terminal. The other two are the same Rust code in the terminal and in the browser.

## Summary

Built with [Claude](https://claude.com/claude-code) on [funkey](https://isene.org/funkey/) in one go. Raid took an hour, vector 35 minutes, marble 45. 5 minutes of my time. Public Domain, like [everything I make](/2026/04/MyTools.html).

- [raid](https://github.com/isene/funkey/blob/master/examples/raid.rs)
- [vector](https://github.com/isene/funkey/blob/master/examples/vector.rs)
- [marble](https://github.com/isene/funkey/blob/master/examples/marble.rs)

---

Link to this post: https://isene.org/2026/10/Raid-Vector-Marble.html
