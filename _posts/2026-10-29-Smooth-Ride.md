---
layout: post
comments: true
title: "A smooth ride for Claude Code"
image: /assets/posts/smooth.jpg
tags: [Technology, AI, Geekery]
---

![A hooded figure hands a lantern to a young sailor, while small boats with screens glide over a fjord](/assets/posts/smooth.jpg)

I love helping others. I've [coached](/coaching/) hundreds of people and the software I make is almost entirely public domain.

So this time I hand over my whole way of working with [Claude Code](https://www.claude.com/product/claude-code). In one plugin.

## Count the prompts

In early October I counted what I type into my sessions. 1,496 prompts in two weeks. More than 100 of them were a bare "yes" or "go".

Each of those was a prompt Claude shouldn't need.

And so I wrote the rules down. Claude does local work that can be undone without asking. It asks before anything leaves the machine: a mail, a push, a post. Every question gets a number, so I answer "3 yes" and move on.

The only thing I'm truly good at is simplifying stuff.

## What is in the plugin

- A guard on shell commands. It refuses five types, like `pkill` and a bare `git stash`, and it asks before `sudo` (obviously... except for what's already in sudoers).
- A check on what Claude writes to a `.md` or `.txt` file. No em-dashes, no long sentences, no jargon from a phrasebook you edit yourself.
- An output style called `plain`. The verdict first, at most 12 lines, numbered questions, an ETA (as a clock time).
- A check on every answer. An answer that breaks the style goes back for a rewrite before I read it.
- The hooks for [fleet](/2026/10/Fleet.html), so sessions get their messages and keep their open questions in a list.
- A starter `CLAUDE.md` with my rules for simplicity, privacy and for checking the work.

The answer check at work. The first answer breaks two rules, goes back, and comes out right:

<a href="/assets/posts/smooth-session.png" target="_blank"><img src="/assets/posts/smooth-session.png" alt="The answer check sends an answer back, and Claude rewrites it" /></a>

All of it together costs a fraction of a second per answer.

## I know, I know...

In the [deck post](/2026/10/Deck.html) I told you to build your own. I still mean it. So take this apart. Keep what fits, throw out the rest, make it yours.

My own screen: [fleet](/2026/10/Fleet.html) on top, [deck](/2026/10/Deck.html) below.

<a href="/assets/posts/smooth-tools.png" target="_blank"><img src="/assets/posts/smooth-tools.png" alt="fleet lists sixteen sessions, and deck shows one session" /></a>

## Get it

In Claude Code:

```
/plugin marketplace add isene/cc-smooth
/plugin install cc-smooth@cc-smooth
```

Then `/output-style cc-smooth:plain`. For the screen that shows all your sessions, add [fleet](https://github.com/isene/fleet). Linux and macOS.

Everything is at [github.com/isene/cc-smooth](https://github.com/isene/cc-smooth). Public domain.

---

Link to this post: https://isene.org/2026/10/Smooth-Ride.html
