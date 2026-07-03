---
layout: post
comments: true
title: The Selection Gap
image: /assets/posts/petrinets.png
tags: [Geekery, Philosophy, Technology]
---

![The Selection Gap](/assets/posts/petrinets.png)

Back in my consulting days I toyed with [Petri nets](https://en.wikipedia.org/wiki/Petri_net) to map business processes. Circles hold tokens, bars fire, tokens move. It could be used for finding bottlenecks. I never could find any serious application for them, filed them under useful engineering and moved on.

For years I have worked on [the Freedom Proof](https://isene.com/freewill/), a mathematical argument that free will grounds existence. Recently I got the hunch that there could be a connection here to explore.

![Petri Nets](/assets/posts/petri.png)

A Petri net is a lawful system. The firing rule is completely formal. Without any randomness. There are no hidden knobs and no observer obscuring the clean machine. A transition fires when every input place holds a token. It eats one token per input arc and drops one on each output:

![The firing rule](/assets/posts/petri-firing.png)

But put one token in front of two transitions and both are ready to fire. Firing one kills the other. Net theory calls this a conflict. The theory refuses to pick. Both continuations are lawful. The math maps the choice point with full rigor and leaves the choosing open. It cannot be closed from inside. The choosing must lie outside the system.

That gives a clean result: lawful does not necessarily mean determined. A fully law-governed system can have a branching, undetermined future. Determinism was always an extra, hidden assumption on top of the laws.

![The unfolding: every lawful run, one actual history](/assets/posts/petri-unfolding.png)

All the lawful runs of a net form one branching tree. The actual history is one path through it. The math describes the whole tree and stays silent on which path gets to be real.

[Gödel](/2026/04/TEG.html) shows the laws cannot ground themselves. Petri shows the laws cannot select the history. Two gaps, and the Freedom Proof fills both with the same answer: choice.

I searched the literature, fanning out a bunch of AI agents, and found nobody who has made this argument before. So I wrote it up, with proper figures and also a section on what it does NOT prove. The paper is on [PhilPapers](https://philpapers.org/rec/ISETSG) and as a [PDF on my site](https://isene.com/freewill/TEG-PetriNets.pdf).

## And of course there is an app

I could not write about token games without building one. [petri](https://github.com/isene/petri) is a terminal Petri net player, part of my [Fe₂O₃ suite](https://isene.org/fe2o3/) of Rust tools. Describe a net in a few lines of plain text. Fire transitions by hand, or let a random run resolve the conflicts while a trace shows the path you got. It hunts deadlocks for you too. Conflicts are marked with ‼. That is the exact spot where the system hands you the choice.

---

Link to this post: https://isene.org/2026/07/The-Selection-Gap.html
