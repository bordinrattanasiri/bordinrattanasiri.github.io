#!/usr/bin/env python3
"""
Reproduces every number quoted on the page.

    python3 verify.py

Run it in the folder holding lesson-1.html and lesson-2.html.
No dependencies. Python 3.8+.

What it measures
----------------
Each lesson page keeps its teaching in two places.

  1. The main line - the <article class="step"> blocks. This is what a
     reader sees by scrolling, without pressing anything.
  2. The answer registry - a JavaScript object called ANSWERS. This content
     appears only when a button is pressed, and every entry in it was
     written in reply to a question.

Lesson 1 is the chat explanation kept verbatim and cut into steps, so its
main-line total is a measurement of the chat answer rather than of the page.

Three answer windows in lesson 1 were added by Claude on its own initiative
rather than asked for. They are listed below and excluded from the count of
questions asked. Claude says it added them in the chat message that delivers
the first version of the page.
"""

import re
import statistics
import sys
from pathlib import Path

PRE_PLACED = ["1.2", "5.2", "6.1"]  # windows Claude added unprompted


# ---------------------------------------------------------------------------
# A small scanner for the ANSWERS literal. It is not a JavaScript engine; it
# understands exactly the shape these pages use: nested objects and arrays,
# double-quoted strings with backslash escapes, and strings joined with +.
# Keeping it explicit means you can read it and see it hides nothing.
# ---------------------------------------------------------------------------

def scan(src):
    """Return a flat list of ("key"|"value", depth, key, text) events."""
    i, n = 0, len(src)
    stack, keys, out = [], [None], []

    def read_string(i):
        i += 1
        buf = []
        while i < n:
            c = src[i]
            if c == "\\":
                buf.append(src[i + 1])
                i += 2
                continue
            if c == '"':
                return "".join(buf), i + 1
            buf.append(c)
            i += 1
        raise ValueError("unterminated string")

    while i < n:
        c = src[i]
        if c in "{[":
            stack.append(c)
            keys.append(None)
            i += 1
        elif c in "}]":
            if stack:
                stack.pop()
                keys.pop()
            i += 1
        elif c == '"':
            s, j = read_string(i)
            k = j
            while k < n and src[k] in " \t\r\n":
                k += 1
            if k < n and src[k] == ":":     # a quoted key
                keys[-1] = s
                out.append(("key", len(stack), s, ""))
                i = k + 1
            else:                            # a value
                out.append(("value", len(stack), keys[-1], s))
                i = j
        elif c.isalpha() or c == "_":
            m = re.match(r"[A-Za-z_]\w*\s*:", src[i:])
            if m:
                keys[-1] = m.group(0).rstrip(": \t\r\n")
                out.append(("key", len(stack), keys[-1], ""))
                i += m.end()
            else:
                i += 1
        else:
            i += 1
    return out


def registry(src):
    """Return {step: [{q, a, thread:[{q, a}]}]} for one lesson page."""
    m = re.search(r"var ANSWERS = (\{[\s\S]*?\n\});", src)
    if not m:
        return {}

    steps, step_id = {}, None
    for kind, depth, key, value in scan(m.group(1)):
        # A step id is a quoted key sitting directly inside ANSWERS.
        if kind == "key" and depth == 1 and re.fullmatch(r"\d+\.\d+", key):
            step_id = key
            steps.setdefault(step_id, [])
            continue
        if kind != "value" or step_id is None:
            continue
        if depth == 3:                       # { "2.1": [ { HERE } ] }
            if key == "q":
                steps[step_id].append({"q": value, "a": "", "thread": []})
            elif key == "a" and steps[step_id]:
                steps[step_id][-1]["a"] += value
        elif depth == 5:                     # ... { thread: [ { HERE } ] }
            if not steps.get(step_id):
                continue
            win = steps[step_id][-1]
            if key == "q":
                win["thread"].append({"q": value, "a": ""})
            elif key == "a" and win["thread"]:
                win["thread"][-1]["a"] += value
    return steps


def text_len(html):
    """Visible characters: drop figures, drop tags, collapse whitespace."""
    html = re.sub(r"<svg[\s\S]*?</svg>", "", html)
    html = re.sub(r"<[^>]+>", "", html)
    return len(re.sub(r"\s+", " ", html).strip())


def report(path):
    src = Path(path).read_text(encoding="utf-8")
    blocks = re.findall(r'<article class="step"[\s\S]*?</article>', src)
    lengths = [text_len(b) for b in blocks]
    reg = registry(src)

    windows = sum(len(v) for v in reg.values())
    follow_ups = sum(len(w["thread"]) for v in reg.values() for w in v)
    unprompted = sum(len(v) for k, v in reg.items() if k in PRE_PLACED)
    asked = windows - unprompted + follow_ups
    per_step = {k: len(v) + sum(len(w["thread"]) for w in v)
                for k, v in reg.items() if k not in PRE_PLACED}
    reply_chars = sum(text_len(w["a"]) + sum(text_len(t["a"]) for t in w["thread"])
                      for v in reg.values() for w in v)

    print(f"\n{path}")
    print("=" * len(path))
    print(f"  steps on the main line           {len(blocks)}")
    print(f"  main-line characters             {sum(lengths):,}")
    print(f"  median characters per step       {statistics.median(lengths):,.0f}")
    print(f"  steps under 600 characters       {sum(1 for x in lengths if x < 600)}")
    print(f"  answer windows                   {windows}  ({unprompted} unprompted)")
    print(f"  follow-up questions in threads   {follow_ups}")
    print(f"  questions the learner asked      {asked}")
    print(f"  characters written in reply      {reply_chars:,}")
    if asked:
        top, count = max(per_step.items(), key=lambda kv: kv[1])
        print(f"  busiest step                     {top} - {count} of {asked} "
              f"({100 * count / asked:.0f}%)")
        print("  questions by step                "
              + ", ".join(f"{k} = {v}" for k, v in sorted(per_step.items())))


if __name__ == "__main__":
    files = sys.argv[1:] or ["lesson-1.html", "lesson-2.html"]
    missing = [f for f in files if not Path(f).exists()]
    if missing:
        sys.exit(f"Not found: {', '.join(missing)}. "
                 "Run this in the folder with the lesson files.")
    for f in files:
        report(f)
    print()
