---
layout: post
comments: true
title: An audience of one - by the numbers
image: /assets/posts/audience-of-one-numbers.png
tags: [Geekery, Technology]
---

![An audience of one - by the numbers](/assets/posts/audience-of-one-numbers.png)

The [previous post](/2026/05/Audience-of-One.html) made a case for building your own desktop. The argument was philosophical: removing multi-user accommodation eliminates substantial complexity. This post is the tally.

The bottom line, before the details: **+3.5 hours of battery time** on my Dell XPS 14, a fan that is mostly silent, and a terminal stack that fits in 691 KB instead of 109 MB.

All numbers below come from the actual binaries on my XPS 14 today, measured against the upstream tools they replaced. Every CHasm binary is pure x86_64 NASM with zero shared libraries and every Fe₂O₃ binary is Rust on top of a small shared library called `crust`.

## Binary size

The terminal stack — shell, terminal emulator, window manager, status bar, pager — is the part of the desktop that runs all the time. Here is what that costs in CHasm versus what it cost before.

<table style="border-collapse: collapse; width: 100%; margin: 1em 0;">
  <tr>
    <th style="border: 1px solid #555; padding: 8px; text-align: left;">Layer</th>
    <th style="border: 1px solid #555; padding: 8px; text-align: left;">Before</th>
    <th style="border: 1px solid #555; padding: 8px; text-align: right;">Bytes</th>
    <th style="border: 1px solid #555; padding: 8px; text-align: left;">After (CHasm)</th>
    <th style="border: 1px solid #555; padding: 8px; text-align: right;">Bytes</th>
  </tr>
  <tr><td style="border: 1px solid #555; padding: 8px;">Shell</td><td style="border: 1px solid #555; padding: 8px;">bash</td><td style="border: 1px solid #555; padding: 8px; text-align: right;">1,540,520</td><td style="border: 1px solid #555; padding: 8px;">bare</td><td style="border: 1px solid #555; padding: 8px; text-align: right;">168,232</td></tr>
  <tr><td style="border: 1px solid #555; padding: 8px;">Terminal</td><td style="border: 1px solid #555; padding: 8px;">kitty (binary)</td><td style="border: 1px solid #555; padding: 8px; text-align: right;">207,496</td><td style="border: 1px solid #555; padding: 8px;">glass</td><td style="border: 1px solid #555; padding: 8px; text-align: right;">191,208</td></tr>
  <tr><td style="border: 1px solid #555; padding: 8px;">Terminal (full)</td><td style="border: 1px solid #555; padding: 8px;">kitty.app bundle</td><td style="border: 1px solid #555; padding: 8px; text-align: right;">109,270,888</td><td style="border: 1px solid #555; padding: 8px;">glass</td><td style="border: 1px solid #555; padding: 8px; text-align: right;">191,208</td></tr>
  <tr><td style="border: 1px solid #555; padding: 8px;">Window manager</td><td style="border: 1px solid #555; padding: 8px;">i3</td><td style="border: 1px solid #555; padding: 8px; text-align: right;">580,800</td><td style="border: 1px solid #555; padding: 8px;">tile</td><td style="border: 1px solid #555; padding: 8px; text-align: right;">82,616</td></tr>
  <tr><td style="border: 1px solid #555; padding: 8px;">Status bar</td><td style="border: 1px solid #555; padding: 8px;">i3bar</td><td style="border: 1px solid #555; padding: 8px; text-align: right;">122,160</td><td style="border: 1px solid #555; padding: 8px;">strip</td><td style="border: 1px solid #555; padding: 8px; text-align: right;">34,744</td></tr>
  <tr><td style="border: 1px solid #555; padding: 8px;">Bar content</td><td style="border: 1px solid #555; padding: 8px;">conky</td><td style="border: 1px solid #555; padding: 8px; text-align: right;">1,019,056</td><td style="border: 1px solid #555; padding: 8px;">asmites (×16)</td><td style="border: 1px solid #555; padding: 8px; text-align: right;">159,488</td></tr>
  <tr><td style="border: 1px solid #555; padding: 8px;">Screen locker</td><td style="border: 1px solid #555; padding: 8px;">i3lock</td><td style="border: 1px solid #555; padding: 8px; text-align: right;">59,864</td><td style="border: 1px solid #555; padding: 8px;">bolt</td><td style="border: 1px solid #555; padding: 8px; text-align: right;">30,528</td></tr>
  <tr><td style="border: 1px solid #555; padding: 8px;">Pager</td><td style="border: 1px solid #555; padding: 8px;">less</td><td style="border: 1px solid #555; padding: 8px; text-align: right;">245,256</td><td style="border: 1px solid #555; padding: 8px;">show</td><td style="border: 1px solid #555; padding: 8px; text-align: right;">41,144</td></tr>
</table>

CHasm core total (bare + glass + tile + strip + asmites + bolt + show): **707,960 bytes = 691 KB**.

The kitty comparison is the headline number. The kitty *binary* is small because it is a launcher; the real workhorse is `~/.local/kitty.app`, which contains a bundled Python 3.14 runtime, HarfBuzz, pixman, GLib, SQLite, and 107 shared objects. **109 MB total.** glass replaces it at 191 KB with zero shared objects, including a TrueType / OpenType rasterizer (glyph), color emoji via CBDT, variable fonts, synthetic italic/bold, and full Unicode beyond the BMP.

That is a factor of 571× smaller for the user-visible terminal feature set I actually use.

## Dynamic linking

<table style="border-collapse: collapse; width: 100%; margin: 1em 0;">
  <tr>
    <th style="border: 1px solid #555; padding: 8px; text-align: left;">Tool</th>
    <th style="border: 1px solid #555; padding: 8px; text-align: right;"><code>.so</code> dependencies</th>
  </tr>
  <tr><td style="border: 1px solid #555; padding: 8px;">bare</td><td style="border: 1px solid #555; padding: 8px; text-align: right;"><strong>0</strong></td></tr>
  <tr><td style="border: 1px solid #555; padding: 8px;">glass</td><td style="border: 1px solid #555; padding: 8px; text-align: right;"><strong>0</strong></td></tr>
  <tr><td style="border: 1px solid #555; padding: 8px;">tile</td><td style="border: 1px solid #555; padding: 8px; text-align: right;"><strong>0</strong></td></tr>
  <tr><td style="border: 1px solid #555; padding: 8px;">strip</td><td style="border: 1px solid #555; padding: 8px; text-align: right;"><strong>0</strong></td></tr>
  <tr><td style="border: 1px solid #555; padding: 8px;">bolt</td><td style="border: 1px solid #555; padding: 8px; text-align: right;"><strong>0</strong></td></tr>
  <tr><td style="border: 1px solid #555; padding: 8px;">show</td><td style="border: 1px solid #555; padding: 8px; text-align: right;"><strong>0</strong></td></tr>
  <tr><td style="border: 1px solid #555; padding: 8px;">chasm-bits (each)</td><td style="border: 1px solid #555; padding: 8px; text-align: right;"><strong>0</strong></td></tr>
  <tr><td style="border: 1px solid #555; padding: 8px; background: #2a2a2a;" colspan="2"></td></tr>
  <tr><td style="border: 1px solid #555; padding: 8px;">bash</td><td style="border: 1px solid #555; padding: 8px; text-align: right;">2</td></tr>
  <tr><td style="border: 1px solid #555; padding: 8px;">kitty (launcher)</td><td style="border: 1px solid #555; padding: 8px; text-align: right;">6</td></tr>
  <tr><td style="border: 1px solid #555; padding: 8px;">kitty (bundle)</td><td style="border: 1px solid #555; padding: 8px; text-align: right;">107</td></tr>
  <tr><td style="border: 1px solid #555; padding: 8px;">i3</td><td style="border: 1px solid #555; padding: 8px; text-align: right;">55</td></tr>
  <tr><td style="border: 1px solid #555; padding: 8px;">i3bar</td><td style="border: 1px solid #555; padding: 8px; text-align: right;">46</td></tr>
  <tr><td style="border: 1px solid #555; padding: 8px;">i3lock</td><td style="border: 1px solid #555; padding: 8px; text-align: right;">32</td></tr>
  <tr><td style="border: 1px solid #555; padding: 8px;">conky</td><td style="border: 1px solid #555; padding: 8px; text-align: right;">51</td></tr>
  <tr><td style="border: 1px solid #555; padding: 8px;">urxvt</td><td style="border: 1px solid #555; padding: 8px; text-align: right;">43</td></tr>
  <tr><td style="border: 1px solid #555; padding: 8px;">gnome-terminal</td><td style="border: 1px solid #555; padding: 8px; text-align: right;">80</td></tr>
  <tr><td style="border: 1px solid #555; padding: 8px;">vim</td><td style="border: 1px solid #555; padding: 8px; text-align: right;">86</td></tr>
</table>

Every CHasm binary is statically linked. Nothing in `/usr/lib` can break my terminal at boot. Distribution upgrade churn no longer reaches the desktop.

## The Fe₂O₃ side

The Rust tools are not micro-optimised for size in the same way. They opt into a shared `crust` TUI library and link `libc` like any normal Linux program. They are still small.

<table style="border-collapse: collapse; width: 100%; margin: 1em 0;">
  <tr>
    <th style="border: 1px solid #555; padding: 8px; text-align: left;">Fe₂O₃ tool</th>
    <th style="border: 1px solid #555; padding: 8px; text-align: right;">Bytes</th>
    <th style="border: 1px solid #555; padding: 8px; text-align: left;">Replaces</th>
    <th style="border: 1px solid #555; padding: 8px; text-align: right;">Predecessor bytes</th>
  </tr>
  <tr><td style="border: 1px solid #555; padding: 8px;">scribe</td><td style="border: 1px solid #555; padding: 8px; text-align: right;">2,939,560</td><td style="border: 1px solid #555; padding: 8px;">vim</td><td style="border: 1px solid #555; padding: 8px; text-align: right;">5,609,800</td></tr>
  <tr><td style="border: 1px solid #555; padding: 8px;">pointer</td><td style="border: 1px solid #555; padding: 8px; text-align: right;">4,240,680</td><td style="border: 1px solid #555; padding: 8px;">ranger</td><td style="border: 1px solid #555; padding: 8px; text-align: right;">4,866,877</td></tr>
</table>

scribe replaces vim at half the size and pointer replaces ranger with a lot more functionality, both on top of a `crust` runtime that several of these tools share.
scribe is much, much faster in handling [HyperLists](https://isene.org/hyperlist/) than vim+[hyperlist.vim](https://www.vim.org/scripts/script.php?script_id=4006) could ever be.

## Startup

"Shell startup" can mean two different things and the smaller number tells you nothing about the bigger one. Quoting both, from the bare README, both shells on the same machine:

**Interactive prologue** — `execve` to "ready for the first keystroke", with history, tab completion, and syntax-highlighted prompt initialised:

```
$ ./bare --bench
bare startup: 9 microseconds
```

**Non-interactive whole-process** — `echo cmd | shell > /dev/null`, i.e. spawn shell, parse one line, fork-exec the command, wait, exit. This is the right number for using a shell as a pipe target or script interpreter. 1000 iterations each:

<table style="border-collapse: collapse; width: 100%; margin: 1em 0;">
  <tr>
    <th style="border: 1px solid #555; padding: 8px; text-align: left;">shell</th>
    <th style="border: 1px solid #555; padding: 8px; text-align: right;"><code>echo true | shell</code></th>
    <th style="border: 1px solid #555; padding: 8px; text-align: right;"><code>echo ls | shell</code></th>
    <th style="border: 1px solid #555; padding: 8px; text-align: right;">syscalls/invocation</th>
  </tr>
  <tr><td style="border: 1px solid #555; padding: 8px;">bash</td><td style="border: 1px solid #555; padding: 8px; text-align: right;">2.5 s</td><td style="border: 1px solid #555; padding: 8px; text-align: right;">4.5 s</td><td style="border: 1px solid #555; padding: 8px; text-align: right;">26</td></tr>
  <tr><td style="border: 1px solid #555; padding: 8px;">bare</td><td style="border: 1px solid #555; padding: 8px; text-align: right;"><strong>2.1 s</strong></td><td style="border: 1px solid #555; padding: 8px; text-align: right;">4.5 s</td><td style="border: 1px solid #555; padding: 8px; text-align: right;"><strong>14</strong></td></tr>
</table>

bare wins the minimal benchmark (~17% faster) and ties on the realistic one where the spawned command's own work dominates. Half the syscalls per invocation, no dynamic linker, no `.bashrc` parse. Same binary in both rows; bare detects `isatty(0)` at startup and gates history, PATH exec-cache, and prompt-state init behind it.

None of that matters if you only ever start a shell once a day; all of it matters if you fork shells from inside a status bar refreshing every 4 seconds, because that is **86,400 forks/day per segment** at 1 Hz, the reason CHasm's status bar segments are tiny static asm binaries ("asmites") rather than shell helpers.

## Resident memory

Captured from `/usr/bin/time -v` on cold runs of `<shell> -c exit`:

<table style="border-collapse: collapse; width: 100%; margin: 1em 0;">
  <tr>
    <th style="border: 1px solid #555; padding: 8px; text-align: left;">Shell</th>
    <th style="border: 1px solid #555; padding: 8px; text-align: right;">RSS</th>
  </tr>
  <tr><td style="border: 1px solid #555; padding: 8px;">bare</td><td style="border: 1px solid #555; padding: 8px; text-align: right;">392 KB</td></tr>
  <tr><td style="border: 1px solid #555; padding: 8px;">bash</td><td style="border: 1px solid #555; padding: 8px; text-align: right;">3,700 KB</td></tr>
  <tr><td style="border: 1px solid #555; padding: 8px;">zsh</td><td style="border: 1px solid #555; padding: 8px; text-align: right;">4,200 KB</td></tr>
</table>

bash and zsh sit at roughly ten times the resident-set size of bare on a no-op invocation. Again: irrelevant for one shell, decisive for hundreds of helper invocations per minute.

## What this buys

I did not set out to make small binaries. I set out to make a desktop that fits the way I work. Small binaries are what falls out of the process when the design rules are:

1. **No wasted CPU cycles.** Every feature has a config flag and an early-return fast path. A "for some users" feature that runs unconditionally for everyone is waste.
2. **Lightning fast.** No interpreters in the hot path. No `awk`, `sed`, `perl`, or `python` in shell helpers, just builtins or asm.
3. **More battery life.** Anything that polls, wakes, or spawns a subprocess on a timer is suspect. Prefer `inotify` to `sleep 1; check`. Prefer `stat()` to `fork()`.

A stack that is **691 KB total** with **zero shared libraries** is what those rules look like applied to the terminal layer. A 109 MB Python-bundling terminal is what they look like ignored.

## Why assembly, then?

A fair reader question after seeing the previous post on Hacker News. Assembly is not chosen for purity or for the romance. The romance came after. Assembly fell out of the rules above the same way the small numbers did. There is no library tax. There is no runtime to warm up. Each instruction has a cost I can see and a behaviour I can predict. When the rule is *no wasted CPU cycles*, working at the level where every cycle is visible turns out to be the lowest-friction place to enforce that rule. Rust would also have worked for most of the stack. It is what powers the Fe₂O₃ side. Assembly was the right tool for the layer that runs all the time.

## Caveats

- Feature parity is not 1:1. kitty has graphics protocol, ligatures via HarfBuzz, and a configuration language. glass has none of those. glass has variable fonts, CBDT color emoji, and a 191 KB binary. But the fonts render just as nice with the assembly glyph engine doing the font job.
- vim has 35 years of plugins. scribe has 72 hours of me. The comparison is "the editor I use" against "the editor I used to use", not feature counts.
- I do not recommend any of this for anybody else. The whole premise of the previous post was that **the audience is one**. Building for one is not the same as not sharing. All the sources are public. Take what is useful, ignore the rest.

## The small print

All binary sizes from `stat -c%s` on 2026-05-03. Shared-object counts from `ldd | grep -c '=>'`. Startup measurements from 1000-iteration loops on the 2026 Dell XPS 14 (the model that shipped in early January this year). Measurements that risked perturbing my running session, interactive terminal startup and live RSS of foreground processes, were skipped. The CHasm sources are at [github.com/isene/chasm](https://github.com/isene/chasm); the Fe₂O₃ sources at [github.com/isene/fe2o3](https://github.com/isene/fe2o3).
