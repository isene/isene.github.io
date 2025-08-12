---
layout: post
comments: true
title: HyperList Ruby TUI - Because Lists Should Be Hyper
image: /assets/posts/hyperlist-logo.svg
tags: [Geekery, Technology, Ruby, HyperList]
---

After 14 years of HyperList evolution and thousands of users leveraging the VIM plugin, it's time for HyperList to break free from VIM and become a standalone terminal application. 

Enter [HyperList Ruby TUI](https://github.com/isene/HyperList) - a full-featured terminal interface for creating and managing HyperLists that runs anywhere Ruby runs.

![](https://isene.org/assets/posts/hyperlist-screenshot.png)

## What the hell is HyperList?

HyperList is my brainchild for describing literally *anything* - states, processes, plans, thoughts, systems, you name it. It's a structured, hierarchical markup language that's powerful enough to model complex systems yet simple enough to jot down your shopping list. Think of it as Markdown's more organized cousin who went to engineering school.

I've been using HyperList for everything from project management to philosophical explorations, from system documentation to creative writing outlines. The [VIM plugin](https://github.com/isene/hyperlist.vim) has been downloaded tens of thousands of times. But not everyone uses VIM (their loss), so here's HyperList for the masses.

## Built on rcurses - Because curses sucks

Just like with RTFM v5, this new HyperList TUI is built on my [rcurses library](https://github.com/isene/rcurses) - a complete rewrite of the ancient curses library in pure Ruby. Why? Because the original curses is about as pleasant to work with as a angry hedgehog in a balloon factory.

The result? A blazing fast, rock-solid terminal application with proper color support across all terminals (yes, even gnome-terminal - that was a fun bug to squash).

## Features that'll make you smile

This isn't just a text editor with syntax highlighting. It's a purpose-built HyperList machine:

* **Full HyperList syntax support** - Every element properly colored and highlighted
* **Advanced folding** - Collapse and expand sections with multiple fold levels (0-9 and beyond)
* **Vim-style navigation** - Because good ideas are worth stealing
* **Smart checkboxes** - Multiple types with timestamp tracking
* **Template system** - Jump to fill-in markers with N
* **Presentation mode** - Focus on one item at a time with P
* **Export everything** - HTML, Markdown, plain text, even PNG graphs
* **References and links** - Jump between items, open files, follow URLs
* **Powerful editing** - Move items and entire trees, indent/unindent, yank and paste
* **Search and marks** - Find anything, mark positions, jump around
* **Split views** - Work with multiple sections simultaneously
* **Autosave** - Never lose your work

## Installation is dead simple

```bash
gem install hyperlist
```

That's it. You're done. Run it with:

```bash
hyperlist                  # New document
hyperlist myfile.hl       # Open existing
```

## The technical bits

Written in pure Ruby with rcurses handling the terminal magic. No external dependencies beyond the rcurses gem. Works on Linux, macOS, and anywhere else Ruby runs. The entire application is a single file you can hack on if you're so inclined.

The code is clean, well-commented, and follows the HyperList philosophy: structured, hierarchical, and powerful. It handles massive files without breaking a sweat thanks to intelligent caching and lazy rendering.

## Why this matters

HyperList isn't just another outliner or todo app. It's a methodology for thinking in hierarchies, for breaking down complexity into manageable, structured components. And now it's accessible to anyone who can open a terminal.

The Ruby TUI brings HyperList into the modern era while keeping the terminal-first philosophy that makes it so damn efficient. No mouse needed, no GUI overhead, just you and your structured thoughts flying across the screen.

## Get it now

* **Install**: `gem install hyperlist`
* **Source**: [github.com/isene/HyperList](https://github.com/isene/HyperList)
* **RubyGems**: [rubygems.org/gems/hyperlist](https://rubygems.org/gems/hyperlist)
* **HyperList specs**: [isene.org/hyperlist](https://isene.org/hyperlist)

Try it. Break it. Fork it. Make it yours. And let me know what you build with it.

The terminal is where real work happens. HyperList just made it hyper.