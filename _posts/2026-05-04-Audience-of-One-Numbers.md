---
layout: post
comments: true
title: An audience of one - by the numbers
image: /assets/posts/audience-of-one-numbers.png
tags: [Geekery, Technology]
---

![An audience of one - by the numbers](/assets/posts/audience-of-one-numbers.png)

The [previous post](/2026/05/Audience-of-One.html) made a case for building your own desktop. The argument was philosophical: removing multi-user accommodation eliminates substantial complexity. This post is the tally.

All numbers below come from the actual binaries on my XPS 14 today, measured against the upstream tools they replaced. Every CHasm binary is pure x86_64 NASM with zero shared libraries and every Fe₂O₃ binary is Rust on top of a small shared library called `crust`.

The bottom line of all of this is +3.5h of battery time on my Dell XPS14 laptop.

## Binary size

The terminal stack — shell, terminal emulator, window manager, status bar, pager — is the part of the desktop that runs all the time. Here is what that costs in CHasm versus what it cost before.

| Layer            | Before               | Bytes       | After (CHasm)   | Bytes      |
|------------------|----------------------|-------------|------------------|------------|
| Shell            | bash                 | 1,540,520   | bare             | 168,232    |
| Terminal         | kitty (binary)       | 207,496     | glass            | 191,208    |
| Terminal (full)  | kitty.app bundle     | 109,270,888 | glass            | 191,208    |
| Window manager   | i3                   | 580,800     | tile             | 82,616     |
| Status bar       | i3bar                | 122,160     | strip            | 34,744     |
| Bar content      | conky                | 1,019,056   | asmites (×16)    | 159,488    |
| Screen locker    | i3lock               | 59,864      | bolt             | 30,528     |
| Pager            | less                 | 245,256     | show             | 41,144     |

CHasm core total (bare + glass + tile + strip + asmites + bolt + show): **707,960 bytes = 691 KB**.

The kitty comparison is the headline number. The kitty *binary* is small because it is a launcher; the real workhorse is `~/.local/kitty.app`, which contains a bundled Python 3.14 runtime, HarfBuzz, pixman, GLib, SQLite, and 107 shared objects. **109 MB total.** glass replaces it at 191 KB with zero shared objects, including a TrueType / OpenType rasterizer (glyph), color emoji via CBDT, variable fonts, synthetic italic/bold, and full Unicode beyond the BMP.

That is a factor of 571× smaller for the user-visible terminal feature set I actually use.

## Dynamic linking

| Tool              | `.so` dependencies |
|-------------------|--------------------|
| bare              | **0**              |
| glass             | **0**              |
| tile              | **0**              |
| strip             | **0**              |
| bolt              | **0**              |
| show              | **0**              |
| chasm-bits (each) | **0**              |
| —                 | —                  |
| bash              | 2                  |
| kitty (launcher)  | 6                  |
| kitty (bundle)    | 107                |
| i3                | 55                 |
| i3bar             | 46                 |
| i3lock            | 32                 |
| conky             | 51                 |
| urxvt             | 43                 |
| gnome-terminal    | 80                 |
| vim               | 86                 |

Every CHasm binary is statically linked. Nothing in `/usr/lib` can break my terminal at boot. Distribution upgrade churn no longer reaches the desktop.

## The Fe₂O₃ side

The Rust tools are not micro-optimised for size in the same way. They opt into a shared `crust` TUI library and link `libc` like any normal Linux program. They are still small.

| Fe₂O₃ tool | Bytes      | Replaces       | Predecessor bytes |
|------------|-----------:|----------------|------------------:|
| scribe     |  2,939,560 | vim            |         5,609,800 |
| pointer    |  4,240,680 | ranger         |         4,866,877 |

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

| shell | `echo true \| shell` | `echo ls \| shell` | syscalls/invocation |
|-------|---------------------:|-------------------:|--------------------:|
| bash  | 2.5 s                | 4.5 s              | 26                  |
| bare  | **2.1 s**            | 4.5 s              | **14**              |

bare wins the minimal benchmark (~17% faster) and ties on the realistic one where the spawned command's own work dominates. Half the syscalls per invocation, no dynamic linker, no `.bashrc` parse. Same binary in both rows; bare detects `isatty(0)` at startup and gates history, PATH exec-cache, and prompt-state init behind it.

None of that matters if you only ever start a shell once a day; all of it matters if you fork shells from inside a status bar refreshing every 4 seconds, because that is **86,400 forks/day per segment** at 1 Hz, the reason CHasm's status bar segments are tiny static asm binaries ("asmites") rather than shell helpers.

## Resident memory

Captured from `/usr/bin/time -v` on cold runs of `<shell> -c exit`:

| Shell | RSS      |
|-------|---------:|
| bare  |   392 KB |
| bash  | 3,700 KB |
| zsh   | 4,200 KB |

bash and zsh sit at roughly ten times the resident-set size of bare on a no-op invocation. Again: irrelevant for one shell, decisive for hundreds of helper invocations per minute.

## What this buys

I did not set out to make small binaries. I set out to make a desktop that fits the way I work. Small binaries are what falls out of the process when the design rules are:

1. **No wasted CPU cycles.** Every feature has a config flag and an early-return fast path. A "for some users" feature that runs unconditionally for everyone is waste.
2. **Lightning fast.** No interpreters in the hot path. No `awk`, `sed`, `perl`, or `python` in shell helpers, just builtins or asm.
3. **More battery life.** Anything that polls, wakes, or spawns a subprocess on a timer is suspect. Prefer `inotify` to `sleep 1; check`. Prefer `stat()` to `fork()`.

A stack that is **691 KB total** with **zero shared libraries** is what those rules look like applied to the terminal layer. A 109 MB Python-bundling terminal is what they look like ignored.

## Caveats

- Feature parity is not 1:1. kitty has graphics protocol, ligatures via HarfBuzz, and a configuration language. glass has none of those. glass has variable fonts, CBDT color emoji, and a 191 KB binary. But the fonts render just as nice with the assembly glyph engine doing the font job.
- vim has 35 years of plugins. scribe has 72 hours of me. The comparison is "the editor I use" against "the editor I used to use", not feature counts.
- I do not recommend any of this for anybody else. The whole premise of the previous post was that **the audience is one**.

## The small print

All binary sizes from `stat -c%s` on 2026-05-03. Shared-object counts from `ldd | grep -c '=>'`. Startup measurements from 1000-iteration loops on the 2026 Dell XPS 14 (the model that shipped in early January this year). Measurements that risked perturbing my running session, interactive terminal startup and live RSS of foreground processes, were skipped. The CHasm sources are at [github.com/isene/chasm](https://github.com/isene/chasm); the Fe₂O₃ sources at [github.com/isene/fe2o3](https://github.com/isene/fe2o3).
