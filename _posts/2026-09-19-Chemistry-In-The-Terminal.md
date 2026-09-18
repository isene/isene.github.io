---
layout: post
comments: true
title: Chemistry in the terminal
image: /assets/posts/alchemy.png
tags: [Geekery, Technology]
---

![alchemy: golden rain, iodine on starch, and salt left in the bottom of a tube](/assets/posts/alchemy.png)

When I was 12 it was easyt for a boy to get his hands on interesting chemicals. Before I was 14 I had a full university grade lab beside my bed. The glassware came from the chemistry building at Blindern, where the students couldn't be bothered to wash their own flasks. I scrubbed them by hand in the bathroom for hours. The chemicals came from the pharmacies until they started shaking their heads, and then from the company Nerlien in the center of Oslo. Phosphorus. Caesium. Uranyl acetate. I could have made real havoc, but I was just curious.

The iodine clock went blue, clear, blue, clear. After a while that's just a colour. Fun, but after a while I wanted more action. I needed more bang.

New Year 1980. Rolf stirred the matchbox while I leaned over it and said "no, stir a bit more". Then it was very bright. I was blind for eighteen minutes. Rolf nearly lost a finger. My mom threw the whole laboratory out.

I asked Claude to build me the lab in the terminal.

[alchemy](https://github.com/isene/alchemy) is a chemistry bench in the terminal. Four glasses, a shelf of about seventy reagents, a burner. `SPACE` opens the shelf. Pour things together and watch.

## The colour

Iodine and starch. Blue black at once, and so strong that a trace of it shows. A drop of hypo and it's gone again.

Indicators do the other trick. The same water reads red in acid, green at neutral and purple in base. One drop colours the lot.

## Salt

Hydrochloric acid in the tube. Caustic soda after it. Both nasty, both gone.

Light the burner and wait. The water boils off. What's left in the bottom of the tube is dinner.

## The clock

![The clock has snapped: the hypo is gone and the beaker is blue black](/assets/posts/alchemy-clock.png)

Water, hydrogen peroxide, potassium iodide, sulfuric acid, starch, hypo. Nothing happens. Nothing keeps happening. Forty seconds of nothing.

Then blue.

Nowhere in the code does it say "now turn blue". There are three reactions. A slow one makes iodine. A fast one eats it. Starch holds whatever is left. While the hypo is in the beaker the iodine never builds up, and the moment it runs out, it does.

The other one swings. Iodous acid makes more of itself, malonic acid eats the iodine, round it comes again. Blue, clear, blue, clear, every fifteen seconds until the fuel runs out. The one I got bored of.

## The bang

![The bench goes black](/assets/posts/alchemy-bang.png)

Potassium chlorate is an oxidiser. Sulfur burns. Put them in a dry tube together and the tube goes to 1284 °C in a tenth of a second.

`s` puts the safety screen up. Mine was down back when I was 14.

## How it works

A glass holds so many millimoles of each substance. Each reaction has a speed: its rate constant times the concentration of every reactant multiplied together. Ten times a second, everything that can run runs a little further.

Then the picture is read off what's left. The colour is the dissolved substances mixed and deepened by how much there is. What won't dissolve falls to the bottom in its own colour. Gases leave, and that's the bubbles. Heat is shared over the water.

Nothing is a lookup. Mix two things nobody planned for and they still behave.

## Summary

Thirty minutes from `git init` to the tag, with two detours. The clocks needed two rounds of tuning before they would swing. And the precipitate hid behind the rim of the glass until I looked at a screenshot.

Built with [Claude](https://claude.com/claude-code). One binary. No network. A bench that has settled costs nothing: zero CPU ticks in twenty seconds.

Public Domain, like [everything I make](/2026/04/MyTools.html).

- [alchemy](https://github.com/isene/alchemy)

---

Link to this post: https://isene.org/2026/09/Chemistry-In-The-Terminal.html
