---
layout: post
comments: true
title: "Chomp and Blocks"
image: /assets/posts/blocks-cats.png
tags: [Geekery, Technology, Personal, Games]
---

![Two cats on the grass above a blue bay](/assets/posts/blocks-cats.png)

A good old favorite had to come next. And Alexander's favorite as well.

Both are now games on [funkey](https://isene.org/funkey/). Both play in your browser.

## Chomp

A tribute to Pac-Man. Play it right here:

<div class="fk-game">
<canvas id="chomp-game" data-wasm="/assets/play/chomp.wasm?v=1.0" aria-label="chomp, a tribute to Pac-Man"></canvas>
<div class="fk-pad" id="chomp-pad" hidden></div>
<p class="fk-bar"><button type="button" id="chomp-full">Full screen</button> <button type="button" id="chomp-keys">Keys on screen</button></p>
</div>

<script src="/assets/play/funkey.js?v=4"></script>
<script src="/assets/play/chomp.js?v=1"></script>

Click the game, then `Space`. On a phone the keys show under it.

- A maze of dots, a muncher and four chasers.
- The chasers hunt by the arcade's rules....
- You get it. It's Pac Man.
- Each level is faster, and the scared seconds get fewer.
- The maze, the art and the sounds are new.
- A top ten with initials, shared by everyone who plays here or on the [try page](https://isene.org/fe2o3/try/funkeys/play.html?g=chomp).

28 minutes after my message it was there.

## Blocks

In the spirit of Minecraft. Play it in [your browser](https://isene.org/fe2o3/try/funkeys/play.html?g=blocks).

- A world of blocks grown from a seed: hills, a sea, tunnels through the stone and groves of trees.
- One great mountain with snow on top. Clouds drift over it all.
- Walk it, swim in it, dig into it and build on it with ten kinds of block.
- What you dig goes in your pockets. From them you make planks, glass, brick and a pickaxe for the stone.
- Water runs into a hole dug beside it.
- Cats come to see who is there, and sit by you.
- `W` and `S` walk, `A` and `D` sidestep, the arrows look round. `Space` jumps and swims.
- `F` digs, `E` builds, `C` lists the things to make.
- There is nothing to win.

## Three iterations

Three messages from me. Three successive versions.

## One: the basics

"build the basics first, then add blocks to the launcher for me to try"

23 minutes later I walked among hills and groves. Digging. Building.

![Version 0.1: groves on the hills, a wall of brick and a block of glass](/assets/posts/blocks-0.1.png)

## Two: the wish list

"blocks: Water, Mountains, Clouds, Crafting, Some cute animals, starting with cats"

51 minutes. A sea with shores to swim from. A mountain with snow on top. Clouds. Pockets, and a list of things to make. Eight cats.

![Version 0.2: a mountain with snow above the trees](/assets/posts/blocks-peak.png)

## Three: the browser

"It crazy good. Can we somehow speed it up to fit in a browser?"

A browser gives a game one core. A frame of blocks took 60 milliseconds there. 57 minutes later it took 25. It looks the same.

- The sky is painted only where no land is.
- The nearest land goes first.
- The sides of the blocks that face away are never sent to the painter.

In the terminal a frame went from 13 to 9 milliseconds.

## Summary

Built with [Claude](https://claude.com/claude-code) on [funkey](https://isene.org/funkey/). Chomp in one go: 28 minutes. Blocks in three: 23, 51 and 57 minutes. Each game is one file of Rust. Public Domain, like [everything I make](/2026/04/MyTools.html).

- [chomp](https://github.com/isene/funkey/blob/master/examples/chomp.rs)
- [blocks](https://github.com/isene/funkey/blob/master/examples/blocks.rs)

---

Link to this post: https://isene.org/2026/10/Chomp-and-Blocks.html
