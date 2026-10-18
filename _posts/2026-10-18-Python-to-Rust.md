---
layout: post
comments: true
title: "From Python to Rust"
image: /assets/posts/python-to-rust.png
tags: [Geekery, Technology, Rust, AI]
---

![The Rust crab walks away from a shed python skin](/assets/posts/python-to-rust.png)

As you may know I have a lot of software projects. I used to program Ruby by hand, now I do all in Claude Code and most of it in Rust or Assembly. Apart from the latest passion for games I have a solution that gathers my mail, chats, documents and feeds in one place. It answers my questions about all of it. It incorporates much of what I did in my messaging hub [kastrup](https://github.com/isene/kastrup), and in many of my other software solutions.

I wondered what benefits it would have if I took this whole 50K LOC Python software and ported it to Rust.

With my meticulously crafted Claude Code setup I put it to the task. It ran for more than 100 hours over a week, without my intervention. I never had to press "Yes" or "Accept" once.

## The verdict

- 83K LOC of Rust (plus 14K of unit tests)
- One executable of 50 MB versus Python with 190 packages. Upgrade = swap one file
- Docker image 1.8 GB versus 5.3 GB with all the AI models. 0.8 GB without the photo captioner
- Starts 42x faster: 0.05 s versus 2.11 s
- Answers 7-11x faster, and serves 11-50x more requests a second
- 10x less memory at rest: 92 MB versus 893 MB (without the AI models)
- 5-9x less CPU per answer. Less power for the same work
- Like C/C++, no garbage collector. Unlike C/C++, the compiler blocks memory bugs
- Type errors are caught when it compiles, not when it runs
- 2,696 tests run on both apps side by side, all green
- On a copy of my real data: 528 of 560 answers identical. The rest come from one add-on left out on purpose, and a plug-in connector

The whole comparison on one page (click to enlarge):

<a href="/assets/posts/python-to-rust-compared.png" target="_blank"><img src="/assets/posts/python-to-rust-compared.png" /></a>

## The biggest win

The porting found 358 faults in the Python. 355 are now fixed in both.

And that is not because we didn't have a solid and secure Python solution. We did plenty of rounds with audits for bugs and security issues. But this round went deeper: both apps got the same questions, and every difference was a bug in one of them.

A few of them:

- A feed's key followed a redirect to any site. Now it goes only to the site the admin named.
- Thirteen routes crashed on an id that was no id.
- A session's times came from two different clocks.
- The upgrade read every item on every run.

## The cost

72% more lines, and a 5-minute build from scratch - but I'd hardly call that a cost.

The Python stays on disk. The Rust runs.

---

Link to this post: https://isene.org/2026/10/Python-to-Rust.html
