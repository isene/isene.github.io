---
layout: post
comments: true
title: A rusty front door
image: /assets/posts/fe2o3-launcher.png
tags: [Geekery, Technology]
---

![The fe2o3 launcher](/assets/posts/fe2o3-launcher.png)

Two days ago I posted [five new tools](/2026/07/Five-New-Rust-Tools.html). Yesterday [two more](/2026/07/Stars-And-Particles.html). That puts 27 apps in the [Fe₂O₃ suite](https://isene.org/fe2o3/), and I am starting to lose sight of all the wonderful apps. So the suite got a front door, simply called `fe2o3`.

## The grid

Every app as a card: its logo, what it is, one line on why. Arrow keys move. `Enter` runs it in the same terminal, and when you quit you are back on the grid. `?` pops up that app's own help, `w` opens its repo, `/` filters.

Six groups, each with its own tint; daily drivers, desk, science, media, play, system. Plus the retired shelf, where rush and crush now sit.

## It installs, too

Grab this one binary and it fetches the rest.

`i` downloads the app under the cursor from its latest release. `I` downloads every missing one on screen. Solid frame and a green tick means you have it. Dashed frame and an amber down-arrow means it's one keypress away.

You can take the launcher, walk the grid, and pick up only what you fancy.

Binaries land in `~/bin`, or `~/.local/bin` if you have no `~/bin`.

## Summary

Built with [Claude](https://claude.com/claude-code) in an evening. One static binary, logos baked in. It does one blocking read on stdin and nothing else while it waits, like the rest of the suite.

```
curl -L "https://github.com/isene/fe2o3/releases/latest/download/fe2o3-linux-x86_64" \
  -o ~/bin/fe2o3 && chmod +x ~/bin/fe2o3
fe2o3
```

Then press `I` for all of it, or `i` for the one you want.

Public Domain, like [everything I make](/2026/04/MyTools.html).

- [fe2o3](https://github.com/isene/fe2o3)

---

Link to this post: https://isene.org/2026/07/A-Rusty-Front-Door.html
