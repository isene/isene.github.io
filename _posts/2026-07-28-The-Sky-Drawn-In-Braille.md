---
layout: post
comments: true
title: The sky, drawn in braille
image: /assets/posts/astro-sky.png
tags: [Geekery, Technology]
---

![The sky chart in astro](/assets/posts/astro-sky.png)

I love our sky. I love the terminal. Now they fuse.

My [astro](https://github.com/isene/astro) app has always shown a star chart for the hour I pick. It fetched it from a website, as a picture, one per hour, converted through ImageMagick and cached on disk.

Now it draws its own... in braille.

## What it draws

9,096 stars from the Yale Bright Star Catalogue, and the constellation figures. The sun, moon and planets where they actually are for that hour. Zenith at the centre, horizon at the rim, north up and east to the left.

Every star wears its own colour, worked out from its B-V index. Braille cells carry a 2x4 dot matrix, and those dots come out close to square. So the sky is round without any fudging.

![The sky in the main pane](/assets/posts/astro-sky-pane.png)

It sits in the main pane and follows the hour selected on the left. Press `s` and it takes the whole screen, where `←` and `→` walk the night an hour at a time. The left pane follows along.

## Details

The faintest star it plots comes from the Bortle number in the config. Bortle 4 gives magnitude 6.4, Bortle 9 gives 4.0. A city sky draws a city sky.

The chart also scales to the room it has. Two thousand stars in a pane fifteen rows high is one solid block of braille. Star counts run about half a magnitude per factor of ten... invert that, fill a tenth of the dots, and the pattern comes back.

The moon covers 13 degrees of sky in a day. Positions had to move to the hour, not the day, or it lands a handful of moon widths off.

## Summary

Built with [Claude](https://claude.com/claude-code) in a couple of hours. The sky drawn in astro needs no network, no image protocol, no cache. Just arithmetic over two tables in the binary. One frame takes 2 ms, and between keypresses it does nothing at all.

Public Domain, like [everything I make](/2026/04/MyTools.html).

- [astro](https://github.com/isene/astro)

---

Link to this post: https://isene.org/2026/07/The-Sky-Drawn-In-Braille.html
