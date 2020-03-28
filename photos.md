---
layout: post
title: My photo gallery
permalink: /photos/
images:
  - image_path: /assets/photos/swan_fall.jpg
    title: Autumn swan
  - image_path: /assets/photos/bogstad.jpg
    title: Reflection at Bogstadvannet
  - image_path: /assets/photos/swan.jpg
    title: Swan portrait
  - image_path: /assets/photos/fuglen.jpg
    title: Niklas and Geir in Tokyo
  - image_path: /assets/photos/tokyo1.jpg
    title: Tokyo from the Mitsubishi club
  - image_path: /assets/photos/poseidon.jpg
    title: The tranquile Poseidon temple on Poros
  - image_path: /assets/photos/sailingsunset.jpg
    title: Sunset while sailing
  - image_path: /assets/photos/oslofjordsunset.jpg
    title: Sunset from the Oslo fjord
  - image_path: /assets/photos/oramasunset.jpg
    title: Sunset from Orama
  - image_path: /assets/photos/tokyo2.jpg
    title: Sunset from Tokyo Station
  - image_path: /assets/photos/tokyo3.jpg
    title: Storm is brewing in Tokyo
  - image_path: /assets/photos/tromsdalstinden.jpg
    title: After ascending Tromsdalstinden
  - image_path: /assets/photos/solartelescope.jpg
    title: The solar telescope building at NAOJ
  - image_path: /assets/photos/tokyostation.jpg
    title: Tokyo Station from above
  - image_path: /assets/photos/molde.jpg
    title: A bright day in Molde
  - image_path: /assets/photos/roros.jpg
    title: Røros
  - image_path: /assets/photos/fuckoffee.jpg
    title: Fuckoffee
  - image_path: /assets/photos/tanzania.jpg
    title: Giraffes in Tanzania
  - image_path: /assets/photos/sunsetspectacle.jpg
    title: Atmospheric phenomenon at sunset in Oslo
  - image_path: /assets/photos/barbaigwarrior.jpg
    title: The Barbaig warrior
---
<p align="center">
{% for image in page.images %}
<a href="{{ image.image_path }}" target="_blank"><img src="{{ image.image_path }}" alt="{{ image.title}}" width="700" /></a>
{% endfor %}
</p>
