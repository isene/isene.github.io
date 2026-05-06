---
layout: post
comments: true
title: The agency stack
image: /assets/posts/agency-stack.png
tags: [Geekery, Philosophy, Technology]
---

![The agency stack](/assets/posts/agency-stack.png)

It's been an interesting few days with insightful comments related to my latest developments.

The sharpest pushback on [my desktop post](/2026/05/Audience-of-One.html) — the one about replacing my desktop with software I'd built — was a single line in the lobste.rs thread:

> How is this OSS/FS promise if you have just hard locked yourself into using an insanely big subscription-based closed source software (claude)? You sure that it's liberating?

It's a fair charge and I want to answer it properly, because the off-the-cuff response I gave in the thread was true but incomplete.

## The argument, in full

The Free and Open Source Software movement has always been about **agency over the artifacts I depend on**... the right to read, modify, share, and replace any program in my life. I've been an [OSS/FS advocate since 1999](/2026/04/MyTools.html), board member of EFN (FSF's sister org in Norway) for 10 years, one of those people who organised the nerd protest march against OOXML.

So here I am, having spent the last five weeks building my desktop with [Claude Code](https://claude.com/claude-code), a proprietary product from a single American company on a subscription that could change price or terms tomorrow. Have I just bought my agency back from one set of vendors and rented it from another?

I want to grant the critic their point. **Yes**, I have a new dependency. **Yes**, it's closed. **Yes**, if Anthropic disappears or goes hostile or just gets boring, my flow of new tools stops. That's a real cost.

But I think the framing of "agency or no agency" misses how agency actually stacks.

## The stack was never clean

Pull on any thread of "I'm using free software" and you find proprietary fibres a few layers down. The Linux kernel runs on a CPU whose microcode is not free. The keyboard firmware in your laptop is not free. The display panel's scaler is not free. The fab process that made the silicon is locked behind a forest of trade secrets. Even Stallman's GCC was, for years, bootstrapped with whatever compiler was at hand on the host system — sometimes proprietary.

OSS/FS has never delivered a fully free stack. What it has delivered, consistently, is **more agency than you had before**, in the layers where agency was reachable. The question was never "is this entirely free?" — it was "is this freer than the alternative?"

By that test, my desktop today has *more* of my agency in it than it did six months ago, not less. The window manager, terminal, editor, file manager, mail client, calendar, RSS reader, music tool — every one of them is something I can read end to end, modify in an afternoon, and redistribute under the Unlicense if anyone wants. They live in two sister suites: [Fe₂O₃](https://isene.org/fe2o3/) (the Rust half: editor, file manager, browser, mail, calendar, astronomy, and so on) and [CHasm](https://isene.org/chasm/) (the x86_64 assembly half: shell, terminal, window manager, status bar, screen locker, font rasterizer). Claude is a single new layer in the stack, and it's the layer **furthest from my final artifact**.

If Anthropic vanishes tomorrow, I lose the ability to **generate new** code as fast as I'm generating it now. I do not lose:

- The code itself, all of which is mine.
- The right to modify it by hand, the way I would have anyway in a pre-LLM world.
- The patterns I've learned by walking through these designs.
- The ability to switch to whatever LLM tooling comes next — open-weight or otherwise.

The artifact is the thing. The artifact is mine. The toolchain that produced it is rentable, and I'm renting it.

## The compiler argument

I frame it like this: **an LLM is a compiler**.

When I write Rust, I don't write the machine code. I write Rust, and a compiler turns it into instructions the CPU can run. The compiler is a trust layer — I trust it to translate my intent faithfully. Most of human software development has lived inside this trust assumption, and most programmers do not write their own compilers.

When I write a prompt to Claude Code, I trust it to translate my intent into Rust. It's a higher-level compiler. The trust surface is bigger, the failure modes are weirder, and the licence is proprietary. But the *shape* of the dependency ("I trust this tool to translate") is one we've always had with our toolchains.

If LLMs were on a public-domain compute substrate tomorrow, I'd switch. Until then, the same calculation that lets us run gcc-on-Intel applies: use the freest tool that gets the job done, and don't pretend the stack is purer than it is.

## What's actually at risk

The honest answer to "what do I lose if this goes wrong?" is this: I lose **velocity**, not **possession**.

If Anthropic decides scribe should not exist, they cannot un-publish the source from my disk. They cannot make my running editor stop running. They cannot revoke my understanding of how the code works. What they *can* do is stop being a useful collaborator, at which point I revert to writing code at human speed, the way I did from 1978 to 2025.

Velocity is real. Five weeks of LLM-paired work is years at solo human speed (my speed). If the rate goes back to solo-human, I will ship less new stuff per unit time. But the *existing* stuff doesn't move; my tools keep working; my muscle memory keeps applying.

This is a different trade than, say, depending on a closed cloud service whose servers hold the only copy of my data, or a SaaS app whose contents disappear when the subscription lapses. The proprietary tool is *upstream* of my work, not *containing* it.

## Why I'm OK with the trade

A purist position is available: refuse to use any closed tool, build everything on free-software foundations, accept the slower pace as the price of consistency. I respect that position. I've taken something like it for most of my life.

I think it's the wrong choice for *me, today*, because:

- The agency I gain at the artifact layer is enormous and immediate.
- The agency I cede at the toolchain layer is bounded — I keep what I produce, and the worst case is "develop slower again", not "lose my desktop".
- Open-weight LLMs are improving fast; if Anthropic gets unbearable, the alternatives will likely be ready.
- The asymmetry is in my favour: a few weeks of subscribed compute bought me decades of compounding personal-fit improvements.

The alternative — wait for the perfect free-software stack before using anything imperfect — is the same logic that kept Linux desktops perpetually "almost ready" for thirty years. At some point you have to build with what's in the room.

## The bigger point

OSS/FS was never a destination. It's a direction. **More agency, more often, in more layers than yesterday.**

By that measure, my desktop has more freedom in it now than it did before I started talking to a closed model. While the model is closed, the the result is. And the result is what I live inside.

If the model becomes free too, even better. If it doesn't, I still own the desktop.

I think that's the right way to keep score.
