---
layout: post
comments: true
title: Programming - what I've been up to lately
image: /assets/posts/rubycode.png
tags: [Geekery, Personal]
---
  
Few things gets me going like programming. After a rush of coding in the
beginning of the year, I found myself missing the creative intellectual
challange that programming poses. Then I found a missing application and my
geek life got new zest.

With three telescopes and a bunch of eyepieces, there are lots of calculations
that I want done. An eyepiece is that optical piece you put in at the end of a
telescope that determines the magnification and field of view you get.

There is a set of interesting properties that can be calculated for a given
telescope. And telescope/eyepiece combinations also yield a set of interesting
properties.

Having already made a program for the HP-41 that calculates all this, I
thought it would be cool to recreate this type of program as a
terminal/console application (for Linux, MacOS, Windows).

Three evenings later and "Telescope" was up on
[Github](https://github.com/isene/telescope) and
[Rubygems.org](https://rubygems.org/gems/telescope-term).

![](/assets/posts/telescopescreenshot.png)

I also did a bunch of improvements to the RTFM filemanager.

To make for easier installations, I started making Ruby "gems" out of my
applications. This makes it silly easy to install my set of (useful)
solutions, simply do this in a terminal:

* For [Telescope](https://github.com/isene/telescope): `gem install telescope-term`
* For [Astropanel](https://github.com/isene/astropanel): `gem install astropanel`
* For the [RTFM filemanager](https://github.com/isene/RTFM): `gem install rtfm-filemanager`
* For [T-REX](https://github.com/isene/t-rex) (the RPN calculator): `gem install t-rex`

In less than 2 months, there's now more than 8500 downloads of my RubyGems.
All free with no restrictive licenses. I like that people find them useful.
