---
layout: post
comments: true
title: Five new Rust tools
image: /assets/posts/fe2o3-new.png
tags: [Geekery, Technology]
---

![Five new Fe2O3 tools](/assets/posts/fe2o3-new.png)

I keep building the tools I use. I know, the world doesn't need another calculator, but I do. My [Fe₂O₃ suite](https://isene.org/fe2o3/) of Rust terminal tools has swallowed almost everything I run in a day. Over the last five weeks it got five new members.

I have an itch. I scratch. Or I get an urge, and by evening it was a binary in `~/bin`.

<img src="/assets/posts/fe2o3-logo-elements.svg" align="left" width="150">

## elements

The periodic table in the terminal. All 118 of them, plus the hypothesized ones out to 126 that nobody has made yet. Move with the arrow keys. Every element brings its full Wikipedia article, cached locally. No browser, no network, snappy.

<br clear="all"/>

![elements](/assets/posts/fe2o3-elements.png)

The colors are the fun part. Eight modes recolor the whole table: category, phase, block, electronegativity, melting point, density. My favourite is cosmic origin, which paints each element by how it came into existence. Hydrogen and helium from the Big Bang. Carbon and lead from dying stars. Gold and platinum from neutron stars colliding. The heavy end made by us. You can see the history of the universe in one screen of colored squares.

Press `c` and you get [Claude](https://claude.com/claude-code) in the pane, with that element's data and article as context. I asked why Osmium is so dense and got lanthanide contraction, relativistic orbitals and hexagonal packing... a better answer than I would have found on my own.

<img src="/assets/posts/fe2o3-logo-rpnx.svg" align="right" width="150">

## rpnx

The HP-41 grabbed me when I was a young teen and just wouldn't let go. Reverse Polish Notation has no `=` and no parentheses. You push values on a stack and the operators act on what is there. Once that is in your fingers, everything else feels like extra typing... no parenthesis and you see every intermediate result.

<br clear="all"/>

![rpnx](/assets/posts/fe2o3-rpnx.png)

The X/Y/Z/T stack, Last X, the full math, trig, log, stats and base-conversion set. It also runs [XRPN](https://github.com/isene/xrpn) programs, so my old HP-41 FOCAL code still executes. The calculation engine is a shared crate. The terminal version and the one on my phone give identical answers.

<img src="/assets/posts/fe2o3-logo-typo.svg" align="left" width="150">

## typo

A touch typing tutor. It's idiotic that I still can't touch type at the age of 59. This app is long overdue for me. Eight lessons, home row to full sentences. Strict mode, live WPM and accuracy, personal bests. It knows the US and Norwegian layouts. Here æ, ø and å get their own drills.

<br clear="all"/>

![typo](/assets/posts/fe2o3-typo.png)

Strict means the drill does not move until you hit the right key. No skipping ahead, no fudging the numbers. Typing is the one interface I use for everything, so it needs sharpening.

<img src="/assets/posts/fe2o3-logo-melody.svg" align="right" width="150">

## melody

A piano roll in the terminal. Put notes down, jam freely on the keyboard, or record against a metronome. What you play is quantized to the grid. Then tweak each note's pitch, length and strength until the line sits right.

<br clear="all"/>

![melody](/assets/posts/fe2o3-melody.png)

It exports a clean WAV, which is the whole point. I sketch a melody here and hand it to something bigger to build a real track around. No audio library. Notes are synthesised to raw PCM and streamed to whatever player is on the system. The WAV file is written by hand. The sound device only wakes when something actually plays.

<img src="/assets/posts/fe2o3-logo-fonts.svg" align="left" width="150">

## fonts

A font picker that shows you the actual font, in your terminal. Every family on the system, rendered in its own typeface as you move down the list.

<br clear="all"/>

![fonts](/assets/posts/fe2o3-fonts.png)

It exists because I was tired of running xfontsel or guessing from names. It hands back the family and point size. My editor [scribe](https://github.com/isene/scribe) calls it as a picker, the way it calls [prism](https://github.com/isene/prism) for colors. The preview in that screenshot is the [Amar font](/2026/07/A-Font-For-Amar.html) Claude made for my role-playing world.

## Summary

Five tools, five weeks, all built with [Claude](https://claude.com/claude-code) in the evenings. Each is a single static binary. It starts instantly and burns nothing while it waits. That is the rule the whole suite obeys: when idle, it does NOTHING. No timers, no polling, no wakeups.

All of it is Public Domain, like [everything I make](/2026/04/MyTools.html). Take it, fork it, or ignore it.

Software built for everyone fits everyone a little. This fits one person exactly. That person can be you too, if you build your own.

---

Link to this post: https://isene.org/2026/07/Five-New-Rust-Tools.html
