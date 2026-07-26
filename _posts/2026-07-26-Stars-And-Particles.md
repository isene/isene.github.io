---
layout: post
comments: true
title: Stars and particles
image: /assets/posts/fe2o3-science.png
tags: [Geekery, Technology]
---

![Stars and particles](/assets/posts/fe2o3-science.png)

Yesterday I posted [five new tools](/2026/07/Five-New-Rust-Tools.html). Today there are two more, and they are both science.

My mother got me going when I was 8. She pointed to the sky just above the apartment building where we lived (Tveita, Oslo) and said, "Do you see those three stars up there? That's the belt of Orion". I was hooked. Four years later I was hanging out at Oslo University bugging professors in astrophysics with questions about the cosmos. Then I got into particle physics and started pestering professors at the physics campus as well.

Together the two new apps cover about 36 orders of magnitude. Betelgeuse is 500 light-years out. A quark is smaller than an attometre. Both fit in a terminal.

<img src="/assets/posts/fe2o3-logo-stars.svg" align="left" width="150">

## stars

The Hertzsprung-Russell diagram. Temperature across, luminosity up. Stars land where their physics puts them, and the shape that falls out of that is the main sequence, running diagonally from the hot blue stars down to the cool red dwarfs.

<br clear="all"/>

![stars](/assets/posts/fe2o3-stars.png)

461 named stars from the HYG catalog. Walk the diagram cell by cell with the arrow keys. Several stars often share one cell, so `Tab` cycles them and `Enter` lists them all. Each one brings its numbers and its full Wikipedia article, cached locally.

Press `t` and a schematic evolutionary track is laid over the plot: 1, 5 or 15 solar masses, with every stage named below. Up the giant branch, back across the top at constant brightness while the core burns out, then down and left onto the white dwarf cooling track. The one solar mass track is the Sun's future.

Measured values come from Wikidata. The rest are derived from spectral type and absolute magnitude, and one color mode paints the diagram by which is which.

<img src="/assets/posts/fe2o3-logo-particles.svg" align="right" width="150">

## particles

The Standard Model. Seventeen fundamental particles, three generations of quarks and leptons, the four force carriers, the Higgs, plus the proton and neutron they build.

<br clear="all"/>

![particles](/assets/posts/fe2o3-particles.png)

Mass, charge, spin, color charge, which of the four forces it feels, its antiparticle, the year it was found. The neutrinos only have upper limits.

Then press `Tab` and it takes a carbon atom apart. Four levels, each labelled with its real size. The atom, almost entirely empty. The nucleus, six protons and six neutrons. One proton. One quark.

![a proton](/assets/posts/fe2o3-particles-proton.png)

That is a proton: three valence quarks, red, green and blue, held by gluon flux tubes, in a haze of virtual pairs. The quarks account for about 1% of its mass. The rest is the energy of the field itself.

One level down you try to pull a quark out. The string stretches, stores energy, and snaps into a new quark-antiquark pair. You end up holding two mesons. You never get a free quark.

It rotates with the arrow keys. There is no animation loop, so a still model costs nothing. Drawn in braille, eight sub-pixels per character cell.

## Summary

Two apps, both built today with [Claude](https://claude.com/claude-code). "particles" was an Opus 5 one-shot from a rather slim prompt (but with knowledge drawn from "stars" and "elements"). Same rules as the rest of the suite: a single static binary, instant start, zero cost when idle.

Both fetch once and then work offline. Press `c` and ask Claude about whatever is on screen, with the data and the article as context.

Public Domain, like [everything I make](/2026/04/MyTools.html).

- [stars](https://github.com/isene/stars)
- [particles](https://github.com/isene/particles)

---

Link to this post: https://isene.org/2026/07/Stars-And-Particles.html
