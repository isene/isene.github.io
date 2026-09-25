---
layout: post
comments: true
title: The Watt quest
image: /assets/posts/watt-quest.png
tags: [Geekery, Technology]
---

![Where the watts go at idle](/assets/posts/watt-quest.png)

In May I wrote up [Watt](/2026/05/Watt.html), the lean desktop. 3.6 watts at idle. I called that lean. But I kept chasing.

It sits near 2.4 now.

## Where the watts go

The picture is the whole cost when at idle. Two blocks: the bare machine and the screen. The programs I run are that thin band.

Magnify that band and it shows the software details: `Claude Code` is most of it. The two suites I built to chase the battery drains, CHasm and Fe₂O₃, draw 26 milliwatts together. Less than one idle Claude session. The screen alone costs more than every program put together.

## What actually drained it

Chasing watts is mostly finding unnecessary drain:
- A graphics library woke up the GPU. I didn't ask for that.
- A chat tab, open and animating, held 2 watts on one core. With my new browser, "gaze" it throttles itself to nothing when not active on the screen.
- The disk lost interrupts and froze the whole machine. Intel's VMD, switched off in the BIOS.

None of them my code. I built tools to capture every drain. You cannot cut what you cannot see.

Every number here comes off the battery gauge, sampled over five minutes. A single reading is noise; a watt swings minute to minute.

## Still chasing

The screen is the wall now. Everything I write is noise against it. That is the sign the software side is done, and the quest turns to the panel and the radios.

Still chasing.

---

Link to this post: https://isene.org/2026/09/The-Watt-Quest.html
