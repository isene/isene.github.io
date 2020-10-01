---
layout: post
comments: true
title: Linux Porn
image: /assets/posts/LinuxPorn.jpg
tags: [Geekery, Technology]
---

In search of Nerdvana, I turned another corner. I got around to tackle the full
range of colors in my Linux setup.

I am running Ubuntu 20.04 on my Dell XPS 15 laptop. No desktop manager, just
the [i3 Window Manager](https://i3wm.org/) straight on X. Most of my work is
done in the terminal
([urxvt](http://software.schmorp.de/pkg/rxvt-unicode.html)). I write 95% of
all text in [VIM](https://www.vim.org/), [mutt](http://www.mutt.org/) is my
email client, I use [weechat](https://weechat.org/) for IRC, Twitter, Slack
and Discord chats, [newsbeuter](https://newsbeuter.org/) is my rss reader,
etc. 

I use very few programs outside the terminal with
[qutebrowser](https://qutebrowser.org/) being the main exception. I enjoy the
consistent user interface of text based programs.  Working on the command line
also gives a lot more power than in the confines of a graphical user
interface.

In the past few days I have had the pleasure of massaging my perfectionism by
finally working out a complete color scheme for `ls` and for the file manager
[ranger](https://ranger.github.io/). The result is pure Linux porn (click to
enlarge):

<a href="/assets/posts/LinuxPorn.png" target="_blank"><img src="/assets/posts/LinuxPorn.png" /></a>

You may notice the comprehensive information bar at the top of my screen. I
have added every bit of info I need and displayed it via
[conky](https://github.com/brndnmtthws/conky) - time, weather, air quality,
moon phase, cpu and system load, cpu temperature, memory, IP address and wifi
connection, ping, unread mails and blog comments, laptop volume, light and
battery. Ask if you wonder about the information therein.

The color scheme for `ls` covers more than 500 file types across 15 categories
with certain file types having shades of the category's color. The color
scheme for ranger cover the main categories. In this way colors are harmonized
between the terminal and inside ranger. I also reworked my colors in
`.Xresources` itself to have a pleasant experience across all terminal
applications.

You can find the [LS_COLORS and ranger color scheme on
GitHub](https://github.com/isene/LS_COLORS) with easy installation. May the
colors be with you.

---
Link to this post: <https://isene.org/2020/10/LinuxPorn.html>
