# One Sentence for a Traveler from 1800

[![make.fun · u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)
[![rank](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/RieryBuild/makefun-u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/rank.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)
[![reward](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/RieryBuild/makefun-u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/reward.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)

Entry for [One Sentence for a Traveler from 1800](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb): a program that writes one sentence explaining the modern internet to someone arriving from the year 1800, using only words and pictures a person from 1800 would already know.

## The sentence

> It is a road joining the post offices and libraries of many towns, so a letter you send can reach a friend across the sea and fetch a book from a far town in a breath.

167 characters, one sentence. The road is the picture: post offices for messages, libraries for knowledge, joined so a letter can cross the sea and a book can be fetched, all in a breath. Nothing in it was coined after 1800 — no internet, computer, screen, or wire — and it claims only what is true: many towns, not every town; a letter and a book, not everything at once.

## Run it

Python 3, standard library only, no network, deterministic (the same sentence every run — the program writes one fixed sentence, so both grading runs produce identical bytes):

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## Files

- `main.py` — the entry program; writes the sentence to `$MAKEFUN_OUTPUT_DIR/entry.txt`
- `LICENSE` — MIT
- `.makefun/owner.json` — claim wallet
