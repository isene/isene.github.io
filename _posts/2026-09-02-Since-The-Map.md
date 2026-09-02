---
layout: post
comments: true
title: Seven apps since the map
image: /assets/posts/since-the-map.jpg
tags: [Geekery, Technology]
---

[![A map with seven new towns drawn in fresh orange ink](/assets/posts/since-the-map.jpg)](/assets/posts/since-the-map.jpg)

A month ago I drew [a map of everything I have built](https://isene.org/2026/08/Map.html). It is already out of date. Seven apps have landed since. Six on the laptop, one on the phone.

I'm not standing still. Speed is crazy these days.

## fleet

I run several Claude Code sessions at once. Which one has finished and waits for me? Which workspace is it on? How much context has it burned? [fleet](https://github.com/isene/fleet) is my TUI app for that. `Enter` jumps to the session, and a new session opens on the workspace and with the background colour I set for it.

## hl2web

When writing a [HyperList](https://isene.org/hyperlist/) I used to distribute it as a PDF or a screenshot. [hl2web](https://github.com/isene/hl2web) turns it into one HTML file: folding, search and the colours from my original hyperlist.vim. No frameworks, nothing but the html file. The first one I made was [the TEG argument](https://isene.org/freewill).

## hl

I keep a lot of HyperLists. The question is often "where did I write that?". [hl](https://github.com/isene/hl) has every list I have into one solution. `hl --open` shows every unchecked box across all of them. `hl --tag teg`, `hl --ref "THEOREM"` and `hl --tree` get hits that grep can't get to. Monday morning in one screen.

## beam

With a workspace pinned to the projector, its active tab is what the room sees. [beam](https://github.com/isene/beam) shows thumbnails of the windows parked there. I pick one, `Enter`, and the room sees it... while I keep typing on the laptop, with the keyboard where it was.

## folio

I've used zathura for many years. I needed something even better. A PDF is two documents in one: the words, and the rendered page. Most readers show only the rendered page. [folio](https://github.com/isene/folio) shows either, or both side by side. `z` blows a scan up to the width of the terminal. `e` opens the `.md` or `.tex` beside the PDF, rebuilds on save and reloads the page. `s` searches every PDF I have indexed. `y` copies the text with file name and page number attached.

## yank

CopyQ hung a helper process every time it fought my terminal over the clipboard. Its process swarm ate my X server's (frame) selection slots. I wanted something simpler. [yank](https://github.com/isene/yank) records every copy and every mouse selection, woken only by frame when a selection changes. `Mod4+v` opens the history in a terminal window. `Enter` pastes the entry into the window I came from. No tray icon. No polling. Nothing running between copies.

## fresh

On the phone: [fresh](https://github.com/isene/nomad) lists the ten most recently installed apps, newest first. Tap to open, long-press to uninstall. I install a lot of apps to try them, and this is where I keep or ditch them easily.

## Under the hood

Two new libraries carry shared plumbing: [feed](https://github.com/isene/feed) parses RSS and Atom, [mail](https://github.com/isene/mail) does the pure-logic parts of email. The desktop [kastrup](https://github.com/isene/kastrup) and the phone kastrup now share one implementation instead of earning the same bugs twice.

## Summary

Seven apps in a month. The map keeps morphing.

---

Link to this post: https://isene.org/2026/09/Since-The-Map.html
