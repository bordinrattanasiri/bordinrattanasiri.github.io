# One lesson, measured

**[bordinrattanasiri.github.io](https://bordinrattanasiri.github.io)**

I teach music theory in Thailand. My own maths stopped in secondary school.
In July 2026 I asked Claude to teach me derivatives, a topic I had never
studied, and then asked for its chat explanation back word for word as a web
page — with two buttons on every sub-step: one to mark it understood, and one
that opens a box to type a question. Answers came back attached to the step
they were asked from.

Same words. Same model. Same session, minutes apart. The only new thing was
somewhere to point.

I asked 18 questions. Eleven landed on one step out of 25. Answering all of
them took three times more writing than the entire original explanation
contained.

|                                | Lesson 1 | Lesson 2 |
| ------------------------------ | -------: | -------: |
| Steps on the main line         |       25 |       30 |
| Characters on the main line    |   13,889 |   60,580 |
| Median characters per step     |      223 |    1,856 |
| Steps under 600 characters     |       21 |        0 |
| Questions asked                |       18 |        — |
| Characters written in reply    |   42,220 |        0 |
| Questions on the busiest step  |  11 / 18 |        — |

Lesson 1 is the chat explanation, cut into steps. So the first column is a
measurement of the chat answer, not of the page.

## Check it

```
python3 verify.py
```

No dependencies, Python 3.8 or newer. It prints every figure above and names
the three answer windows that Claude added unprompted, which are excluded
from the count of 18.

## What's here

| | |
| --- | --- |
| `index.html` | The page, with the full index of all 18 questions |
| `lesson-1.html` | The chat explanation cut into 25 steps, with the replies still inside |
| `lesson-2.html` | The same topic rebuilt after the first pass was diagnosed |
| `verify.py` | Reproduces every number |
| `skills/` | Two skill files and three reference documents |

Both lessons are single HTML files in Thai, with no server and no
dependencies. Save either and it works offline.

## Transcripts

- [Session 1 — learning derivatives, and building lesson 1](https://claude.ai/share/a9ce90b1-004f-497b-be87-658c9d3e8af8)
- [Session 2 — writing the method down, and lesson 2](https://claude.ai/share/b5642d3e-54cc-4d52-aff2-718a3fe5ec74)

Unedited, including the turns that went wrong.

## The rule worth keeping

A cluster of questions on one step means a section is missing, not that the
step is hard. The repair is never a longer answer. It is new steps on the
main line.

---

MIT licensed. Use it, adapt it, or ignore it.
Bordin Rattanasiri · bordin.rattanasiri@gmail.com
