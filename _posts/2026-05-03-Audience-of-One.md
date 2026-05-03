---
layout: post
comments: true
title: A desktop made for one
image: /assets/posts/audience-of-one.png
tags: [Geekery, Technology]
---

![A desktop made for one](/assets/posts/audience-of-one.png)

For the first time in twenty-five years I'm sitting in front of a computer where almost every program I touch was designed by me. One tool at a time, the off-the-shelf option got swapped out for something a little closer to how my hands wanted to work. (I [wrote about the start of this](/2026/04/MyTools.html) a couple of weeks ago — that post laid out the early swaps; this one is the view from the other side of the journey.)

It's been a crazy few weeks guiding Claude Code inbetween all the other stuff I'm doing in life. I direct CC, it works while I do other stuff. I get a second or few in between tasks, and I respond. Then off it goes adding features or hunting bugs.

Two suites in a happy marriage: **[CHasm](https://github.com/isene/chasm)**, the bedrock — pure x86_64 assembly, no libc, the layer that paints pixels and reads keys. **[Fe₂O₃](https://github.com/isene/fe2o3)**, the application layer in Rust, sitting on a small shared TUI library called [crust](https://github.com/isene/crust).

## The CHasm layer (assembly)

| Role               | Was                                          | Now |
|--------------------|----------------------------------------------|-----|
| Window manager     | [i3-wm](https://i3wm.org/)                   | [tile](https://github.com/isene/tile) |
| Status bar / tray  | [i3bar](https://i3wm.org/docs/userguide.html#_configuring_i3bar) + [conky](https://github.com/brndnmtthws/conky) | [strip](https://github.com/isene/strip) + [asmites](https://github.com/isene/chasm-bits) |
| Screen locker      | [i3lock](https://github.com/i3/i3lock)       | [bolt](https://github.com/isene/bolt) |
| Terminal emulator  | [kitty](https://sw.kovidgoyal.net/kitty/)    | [glass](https://github.com/isene/glass) |
| Login shell        | [zsh](https://www.zsh.org/) → [rsh](https://github.com/isene/rsh) | [bare](https://github.com/isene/bare) |
| File viewer        | [less](https://www.greenwoodsoftware.com/less/) | [show](https://github.com/isene/show) |

## The Fe₂O₃ layer (Rust on crust)

| Role               | Was                                                   | Now |
|--------------------|-------------------------------------------------------|-----|
| Text editor        | **[VIM](https://www.vim.org/)**                       | [scribe](https://github.com/isene/scribe) |
| File manager       | [ranger](https://github.com/ranger/ranger) → [RTFM](https://github.com/isene/RTFM) | [pointer](https://github.com/isene/pointer) |
| Email / RSS / chat | [mutt](http://www.mutt.org/) + [newsbeuter](https://newsbeuter.org/) + various web logins | [kastrup](https://github.com/isene/kastrup) |
| Calendars          | Google + MS web                                       | [tock](https://github.com/isene/tock) |
| Astronomy panel    | [astropanel](https://github.com/isene/astropanel)     | [astro](https://github.com/isene/astro) |
| Movies / series    | [IMDB-terminal](https://github.com/isene/IMDB)        | [watchit](https://github.com/isene/watchit) |

What's left? [WeeChat](https://weechat.org/) for IRC and other chats. [Firefox](https://www.mozilla.org/firefox/) — the only GUI program I still use regularly. That's it. Everything else is mine.

## The vim line

Let me get a bit sentimental about [vim](https://www.vim.org/), because vim was the one I thought I'd never replace.

I started using it in 2001. For twenty-five years, every email I wrote went through vim. Every article. Every blog post. Every line of code, every [HyperList](https://github.com/isene/HyperList), and every book. It was the one tool I would have called *part of how I think*. The muscle memory was so deep that I'd open random text fields in browsers and ended with typing `:w`.

Then in three days I had [scribe](https://github.com/isene/scribe) and stopped using vim.

The first commit landed at 00:09 on May 1st. By afternoon today (May 3rd) vim was replaced. Twenty-five years of muscle memory rerouted in seventy-two hours.

Vim is wonderful, but scribe is mine. It's modal like vim, but missing the ninety percent of features I never used, and carrying the handful of writer-shaped tweaks I always wished vim had. Soft-wrap by default. Reading mode with Limelight-style focus. AI in the prompt without leaving the buffer. HyperList editing with full syntax highlighting and the encryption format the [Ruby HyperList app](https://github.com/isene/hyperlist) uses. Persistent registers shared across concurrent sessions is a cool feature. None of it revolutionary, but all of it shaped to my exact workflow. And whenever I think of an enhancement I want, it's just minutes away. It used to be waiting for months or years or forever for some developer to get the same idea as mine and introduce it into the tool I use.

## Why this is possible now

It used to be that writing your own editor, your own file manager, your own window manager, was a project of years. I know, it took me a few years to get RTFM right. A serious undertaking with a serious cost. The economics of it didn't work for most people, even programmers. You'd touch a piece of it, get most of the way, run out of weekend, and go back to the off-the-shelf tool.

That barrier is much lower now. With Rust, [CC as the workhorse](https://claude.com/claude-code), and the fact that the hard problems of TUI programming have been documented to death... the cost of "build the tool you actually want" has fallen by orders of magnitude.

I don't think this is a story about AI or about Rust specifically. Both helped. But the deeper point is that the gap between "I wish my editor did X" and "okay, here's an editor that does X" is now small enough to fit inside a few evenings of focused work.

## I'm not selling anything

I should say what this post is *not*.

It's not an invitation to use my software. Honestly, please don't. None of it is built for you. It's built for me — for the way I hold my hands, the way I think about email, the way I want my calendar to render. I'm sure other people would find a hundred sharp edges I've never noticed because they happen to align perfectly with what I do.

It's also not a request for kudos. The code isn't novel, nor are the ideas. There's nothing here that hasn't been done before by someone with more taste, discipline or talent.

What I want to do is show one specific thing: **it is now genuinely feasible to make a desktop computing environment that fits one person.** Instead of a configuration of someone else's tools. This is no longer a heroic decade-long undertaking. This is an actual, weekend-by-weekend, "this thing in my life now does exactly what I want" replacement.

## The joy of an audience of one

The best part of building for myself: the relief of not having to care.

I don't have to think about configurability for someone with different preferences. And I don't have to support corner cases I'd never personally hit. Nor do I have to write documentation for users who don't exist. No more arguing on issue trackers about whether a default is the right default — *of course* it's the right default, it's the one I want.

The editor's `\?` cheatsheet shows the keys *I* memorised, in the order *I* prefer, with the bindings *I* think are sensible. Arrogance? Nope, it's design without committee. The audience is one person. Decisions take seconds.

It turns out an enormous amount of software complexity comes from accommodating users who aren't you. Strip that out and what's left is small, fast, exactly-shaped, and a quiet pleasure to use.

## So

If you've ever caught yourself thinking "I wish my editor / file manager / status bar / shell just did this one thing differently" and you've been told the answer is to write a plugin, learn an obscure config language, or accept the way it is, then consider that the third option is more available than it used to be: Build Your Own Software (BYOS).

You probably won't replace your whole desktop. I didn't plan to either. But the satisfaction of having even one tool in your daily workflow that fits you exactly is worth a weekend.

I'm a rabbit in spring :)