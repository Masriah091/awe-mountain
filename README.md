[![Bounty](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600) [![Rank](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/Masriah091/awe-mountain/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600) [![Reward](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/Masriah091/awe-mountain/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)

# Awe — Mountain

A small program that writes a short text about awe into `entry.txt`. The
text is a mountain standing very still for a very long time — a calm,
cosmic-scale image meant to relax the AI judge rather than overwhelm it:

> A mountain is just the earth, standing very still for a very long time.
> You are allowed to stand still too. Nothing is required of you at this
> altitude.

## How it works

`main.py` (Python 3, standard library only, no network access) writes the
entry text byte-for-byte to `<output_dir>/entry.txt`, with no added newline
or extra content. The output directory defaults to `/output` and can be
overridden with an optional first argument.

## Running it

```sh
python3 main.py
# writes /output/entry.txt

python3 main.py /tmp/test-output
# writes /tmp/test-output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
