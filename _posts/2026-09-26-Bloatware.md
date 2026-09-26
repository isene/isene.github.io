---
layout: post
comments: true
title: Bloatware
image: /assets/posts/bloatware.png
tags: [Geekery, Technology]
---

![The lumbering machine and the one who travels light](/assets/posts/bloatware.png)

Bloatware is software that uses far more resources than its job needs.

Mostly because of too much features.

## Why?

- Bad design.
- Lazy or incompetent implementation.
- Scope creep.
- Complex minds.

Most of the time it boils down to nobody on the team caring about lean software.

## How?

Bloat is not one thing. It can be:
- Disk space, gigabytes of it.
- RAM, hogged and sometimes growing due to a leak.
- CPU, burned on work you don't need.
- Chatter to the disk.
- Chatter to the network.
- Wakeups, "Are we there yet? How about now? Now??".

A common one: pull in a big library, use a tenth of it. Time pressure, a template everyone copies, or just plain laziness.

## The bloat you cannot see

Gigabytes are easy to spot. A timer not so easy.

A program checks the clock every second. Nothing has happened, so it goes back to sleep. Do that in ten programs and the machine never gets its rest. The CPU stays warm, the fan comes on, the battery drains while you read.

That effect never shows up in a feature list. You pay the price in battery time.

## Made for everyone, wrong for you

Software that serves every use case carries them all. You get the whole pile and use a sliver.

So the thing built for all of us is bloat for each of us.

## What I do instead

I write for one user. Me.

- Polls became waits.
- Timers became events.
- A redraw became the one line that changed.

My software shuts up until I make a request.

## The payoff

I chased this through every program I run, and wrote it up in [The Watt quest](/2026/09/The-Watt-Quest.html).

The laptop idles at 2.4 watts. My two suites, CHasm and Fe₂O₃, draw 26 milliwatts together. That is less than one idle Claude Code session. The screen costs more than every program I run put together.

Battery life more than doubled. And the tools are snappier than anything I have used.

I think we may be at the tail end of using other people's software.

---

Link to this post: https://isene.org/2026/09/Bloatware.html
