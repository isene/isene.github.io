---
layout: post
comments: true
title: Chess in the terminal
image: /assets/posts/gambit.png
tags: [Geekery, Technology]
---

![gambit: a game against claude, with the model named in the corner](/assets/posts/gambit.png)

I started playing chess for real about a decade ago. I used it to overcome my annoyance when I lost in life. Losses would have an impact, so I decided to play chess until loss didn't have that impact. It took 3 years and some 30K blitz games (1 minute games, 1+0) for that irritation of losing to subside. I deliberately didn't try to get better, and so I lost around 50% of the games and stayed pretty stable at 1500 elo rating. At the tail end of those three years, the feeling of loss dissipated within 14 days. And the rating popped to 1600. And it stayed like that for a few years. I played on to see if I could get to the point where I would enjoy a loss and not merely have no annoyance. And I got there. Now my rating is around 1750 with a peak above 1800.

Running out of ideas for what to make these days, I decided to make a dig at a new fe2o3 app called gambit. Chess in the terminal. Claude went to work while I enjoyed Crystal Palace win their Europa League game 4-0.

[gambit](https://github.com/isene/gambit) plays chess in the terminal, against an LLM. Or on Lichess. You move with the arrows, or type the moves the way you write them: `e4`, `Nf3`, `O-O`.

## The rules

The rules were 95% of the job. Castling, en passant, a pawn becoming a queen, stalemate, the fifty move rule, the same position three times.

## The opponent

The model is told the position, the moves so far and every legal move, and answers with one of them. An answer that is not legal is asked again, twice. After that gambit plays a plain move itself, and reports that.

`o` picks what model to play against.

![Four ways to reach a model](/assets/posts/gambit-opponents.png)

The first needs no key: it runs `claude -p`. With a key it can be Anthropic's API, OpenAI's, anything that uses that type of API, or a command of your own. The corner names the model that actually answered, and the panel keeps the running cost. Not relevant when you play on a subscription but interesting as a reference.

A move through `claude -p` runs a few cents, since the command carries its own tools and instructions into every call. The API with the same model is far cheaper.

## How strong

The LLM opponents are slow and weak. It plays the opening from memory, drifts, and hangs pieces like the rest of us. Two leaderboards ([ChessBench](https://chessbench-ai.github.io/) and [dubesor's](https://dubesor.de/chess/chess-leaderboard)) rate models at chess, and their numbers sit a thousand points apart, so take them with a grain of salt.

The models will evolve, so it will be interesting to see the development.

If you want to be beaten properly, play Stockfish, play on Lichess.

## Lichess

`L` plays on [lichess](https://lichess.org) instead: their computer at any of its eight levels, or a real opponent over ten minutes. gambit becomes the board. It follows the game, shows both clocks, and sends your moves.

Lichess forbids engine help on an ordinary account, so the model plays no part in a lichess game.

## Details

![The keys, in the corner](/assets/posts/gambit-help.png)

Every piece has the proper symbol with its letter under it, capitals for White and small letters for Black. The pieces taken are shown beside the board, with the point lead next to whoever is ahead.

While you think, gambit does nothing. It waits for a key, and wakes once a second to move the clock on.

## Summary

Built with [Claude](https://claude.com/claude-code) during one football match. One binary. No network, unless you ask it to reach one.

Public Domain, like [everything I make](/2026/04/MyTools.html).

- [gambit](https://github.com/isene/gambit)

---

Link to this post: https://isene.org/2026/09/Chess-In-The-Terminal.html
