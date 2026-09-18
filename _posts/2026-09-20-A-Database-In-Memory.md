---
layout: post
comments: true
title: A database in memory
image: /assets/posts/ferrite.png
tags: [Geekery, Technology]
---

![ferrite: a plane of core memory with one bit set](/assets/posts/ferrite.png)

It's been one hell-of-a-chase for performance and optimizations. It was time for optimizing the SQL layer for my apps.

I know, the world doesn't need another database. SQLite is in every phone and every browser, and it's very good. But it keeps its rows on disk in pages and decodes a page on every read. My tools have small databases. A calendar. A few hundred events. Those fit in memory with room to spare.

So I decided to create a db in memory that beats SQLite at small reads and writes. Rust, no dependencies, part of [Fe₂O₃](https://isene.github.io/fe2o3/). Done in a day.

[ferrite](https://github.com/isene/ferrite) is the result. It speaks SQL. Tables, indexes, joins, foreign keys, transactions. The rows live in memory, with a log and a snapshot on disk.

## The numbers

Every step had to beat SQLite before I was satisfied. The bench runs SQLite and ferrite on the same disk, in the same mode, a table of 100,000 rows.

![Operations a second, SQLite and ferrite side by side](/assets/posts/ferrite-speed.png)

Reads: 1.9 million a second against 419 thousand. A mix of reads and updates: 709 thousand against 112 thousand. Loading the table: 1.9 million rows a second against 1.3 million.

The FULL columns sit close together. There every commit waits for the disk, and the disk is the bottleneck, not db.

A lookup through an index takes 53 microseconds against 123. The whole comparison, speed and features side by side, is one page: [isene.org/ferrite](https://isene.org/ferrite/).

## Trust

A database that answers fast and wrong is worse than a db that crashes. So a machine makes up SQL, tens of thousands of statements, and runs every one on SQLite and on ferrite. Every answer is compared. Where they differ, ferrite is wrong until shown otherwise.

Then the power cut test. A program inserts rows and is killed mid-write, 10,000 times in each mode. Nothing committed was lost, and no file was left that would not open.

## In memory, on disk

The default is NORMAL. A commit is written at once, so a program that crashes loses nothing. A power cut can lose the last few. FULL waits for the disk on every commit and costs ten times as much on writes. That's my choice to gain performance. The README says so at the top.

## The first user

[tock](https://github.com/isene/tock), my calendar, runs on it now. One line in its config, and the first start copies the SQLite file in. My eight calendars and 503 events came across in 31 milliseconds and read back the same. Much fater than with SQLite.

## What it is not

A server. A database shared between programs. A home for more data than the machine has memory. For those, SQLite.

## Summary

Built with [Claude](https://claude.com/claude-code), from the plan to the calendar running on it, in one day. 7,900 lines of Rust, bench and tests included. No dependencies. 

Ferrite is iron oxide, like Fe₂O₃. Ferrite cores were the memory of the early computers. That's the logo: a plane of cores with one bit set.

Public Domain, like [everything I make](/2026/04/MyTools.html).

- [ferrite](https://github.com/isene/ferrite)
- [isene.org/ferrite](https://isene.org/ferrite/)

---

Link to this post: https://isene.org/2026/09/A-Database-In-Memory.html
