---
layout: post
title: My digital artwork
permalink: /art/
images:
  - image_path: /assets/art/Call.jpg
    title: The Call
  - image_path: /assets/art/SoftEntanglement.jpg
    title: Soft Entanglement
  - image_path: /assets/art/ThroughTheFog.jpg
    title: Through the fog
  - image_path: /assets/art/Prison.jpg
    title: Prison
  - image_path: /assets/art/Droplets.jpg
    title: Droplets
  - image_path: /assets/art/GoldSlabFromTheTempleOfCarnea.jpg
    title: Gold slab from the Temple of Carnea
  - image_path: /assets/art/dream.jpg
    title: Dream
  - image_path: /assets/art/lighthouse_o.jpg
    title: Lighthouse
  - image_path: /assets/art/snowscape.jpg
    title: Snowscape
  - image_path: /assets/art/flare.jpg
    title: Flare
  - image_path: /assets/art/seasons.jpg
    title: Seasons
  - image_path: /assets/art/starsets.jpg
    title: Our star sets
  - image_path: /assets/art/bloodred.jpg
    title: Blood red
  - image_path: /assets/art/blue.jpg
    title: The blue hour
  - image_path: /assets/art/astronomy.jpg
    title: My passion
  - image_path: /assets/art/coincident.jpg
    title: Coincident
  - image_path: /assets/art/lighthouse.jpg
    title: Lighthouse
  - image_path: /assets/art/thinking.jpg
    title: Thinking
  - image_path: /assets/art/random.jpg
    title: Random
  - image_path: /assets/art/birth.jpg
    title: Then what?
  - image_path: /assets/art/details.jpg
    title: Attention to detail
  - image_path: /assets/art/humanfactor.jpg
    title: The human factor
---
<p align="center">
{% for image in page.images %}
<a href="{{ image.image_path }}" target="_blank"><img src="{{ image.image_path }}" alt="{{ image.title}}" width="700" /></a>
{% endfor %}
</p>
{% include youtube.html id='SmC8ekwl6Gw' %}

