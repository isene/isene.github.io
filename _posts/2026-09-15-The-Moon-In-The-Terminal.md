---
layout: post
comments: true
title: The Moon in the terminal
image: /assets/posts/moon.png
tags: [Geekery, Technology]
---

![moon: tonight's Moon and the days around it](/assets/posts/moon.png)

I really like our moon. I like that it's big and the exact right size and distance to make for great solar eclipses. If I ever went to Mars, I would miss our moon

[moon](https://github.com/isene/moon) shows the Moon as it looks tonight. Craters and seas, the lit part bright, the night side dark gray. Along the bottom sit the phases of the three days before and the days ahead, to the edge of the window. `←` and `→` step a day. `t` brings you back to today.

## The map

`Tab` opens a map of the near side, drawn in braille, with labels. Seas in blue, craters in yellow, mountains and valleys in tan.

![The map, with the naked-eye craters named](/assets/posts/moon-map.png)

`+` and `-` zoom, the arrows pan. Zoom in and more names show up, biggest first, wherever there is room. Over a thousand of them, from the International Astronomical Union's list.

`/` finds one. Type "tycho", hit `Enter`, and the map jumps there and marks it.

![Tycho, found and zoomed in](/assets/posts/moon-tycho.png)

## The real Moon

`Tab` once more and the real Moon shows up. NASA's photo, lit for the day on screen, drawn as a true picture in the terminal through [glow](https://github.com/isene/glow). It needs a terminal that shows pictures, like glass or kitty.

![The real Moon, as a picture in the terminal](/assets/posts/moon-photo.png)

## At the eyepiece

A telescope shows the Moon upside down. A star diagonal mirrors it. `f` steps from the naked eye to the telescope to the diagonal... so the screen matches the eyepiece. The photo, the phase strip and the map follow along.

![The telescope view, south up](/assets/posts/moon-telescope.png)

## Details

The picture is NASA's photo map from the Lunar Reconnaissance Orbiter. It was shot with the Sun high, so the craters had no shadows. I mixed in the Moon's measured heights, lit from the north-west, and the rims came back.

A braille cell holds eight dots. Here the cell's background carries the shade, and a dot goes only where part of the cell is brighter. Flat ground stays clean. Crater rims get their dots.

Tycho didn't show on the whole disk at first. It is small on a map, but bright to the naked eye. So the craters you can see without a telescope are always named.

## Summary

Built with [Claude](https://claude.com/claude-code) in an hour. One binary with the maps and the names inside. No network, no cache, no waiting. Between keypresses it does nothing at all.

Public Domain, like [everything I make](/2026/04/MyTools.html).

- [moon](https://github.com/isene/moon)

---

Link to this post: https://isene.org/2026/09/The-Moon-In-The-Terminal.html
