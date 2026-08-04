# Page specification

One self-contained HTML file. No build step, no external JS. Web fonts from Google Fonts are
fine; everything else is inline.

## Layout

```
sticky progress rail  ── understood count, progress bar, reset button
masthead              ── eyebrow, title, one-line orientation
how-to-use            ── collapsible <details>, closed by default
two-column grid       ── main column (sections and steps) | sticky sidebar
next-steps panel      ── locked until every step is marked understood
two modals            ── ask modal, answer modal
lesson map            ── collapsible <details>, open by default, one line per section
prerequisites panel   ── optional, above the first section
post-lesson panel     ── discussion box first, then the next-direction buttons
```

At ≤900px the grid collapses to one column and the sidebar becomes a collapsible bar pinned
under the rail.

## The step

Every sub-step is one `<article class="step" data-id="N.M">` containing, in order:

```html
<article class="step" data-id="3.1">
  <span class="step-no">§3.1</span>
  <h3>Full-sentence heading stating what is being done and why</h3>

  <!-- lesson prose, equations, tables -->

  <div class="crux">           <!-- what this step settled, what it did not, what comes next -->
    <div><b>settled</b><span>…</span></div>
    <div><b>not yet</b><span>…</span></div>
    <div><b>next</b><span>…</span></div>
  </div>

  <div class="extras"></div>   <!-- expand buttons + check boxes are injected here -->
  <div class="acts"></div>     <!-- action buttons are injected here -->
</article>
```

The `.crux` block is required on every step and is written by hand, not injected. Its three
labels are fixed within a lesson and translated to the lesson's language. Keep each line to a
single clause; the block is a signpost, not a summary. Mark the operative words with `<em>`,
which is styled as emphasis rather than italics.

When a step is rewritten in response to a *explain more* request, the crux block is rewritten
with it and stays last before `.extras`.

`data-id` is permanent. `.extras` and `.acts` must always be present and always last — the
script injects into them and inserts the *explain more* menu after `.acts`.

## The three action buttons

Injected into `.acts` for every step:

| Button | Behaviour |
|---|---|
| **Understood** | Toggles state to `ok`, updates the progress rail, persists |
| **Not understood / ask** | Opens the ask modal; on copy, marks the step `ask` and copies a tagged question |
| **Explain more** | Toggles an inline menu of 2–4 category buttons; each copies a tagged request |

A badge at the right of the row shows the current state in words.

Understood/ask state is stored per step. Use `window.storage` when present and degrade
silently to in-memory state when it is not:

```js
var hasStore = (typeof window.storage !== "undefined" && window.storage);
```

Never use `localStorage` or `sessionStorage` — they fail in this environment.

## Clipboard tags

Every copy action emits a tagged first line so the next chat message identifies itself. Keep
these exact shapes; the routing in the main SKILL.md depends on them.

```
[<lesson name> — ขั้น §3.1 <step heading>]        ← ask on a step
[<lesson name> — ถามต่อในกล่องขยายความ §3.1 · <window title>]   ← follow-up inside a window
[<lesson name> — ขอคำอธิบายเพิ่ม §3.1 <step heading>]\nประเภทที่ต้องการ: <category>
[<lesson name> — ตอบคำถามทวน §3.1]                ← answer to a check question
```

Translate the tag wording to the lesson's language, but keep the section marker and step id
literal so they are machine-identifiable.

Implement copy with `navigator.clipboard.writeText` and a hidden-textarea + `execCommand`
fallback, then show a short confirmation message next to the button.

## Content registries

All injected content lives in three object literals at the top of the script. This is the only
place later turns add content, apart from rewriting step markup directly.

```js
/* Expandable windows created from questions asked on a step. */
var ANSWERS = {
  "3.1": [
    { q: "Button label — the learner's question, condensed",
      a: "<p>…full answer HTML…</p>",
      thread: [                                   // optional, grows over time
        { q: "follow-up asked inside this window", a: "<p>…</p>" }
      ] }
  ]
};

/* Check questions posed by the teacher, rendered as a highlighted box in the step. */
var CHECKS = {
  "2.1": [
    { body: "<p>…the question…</p>",
      note: "…inline verdict shown once answered, optional…",
      answer: null,        // null → no solution button yet; HTML string → button appears
      thread: []           // optional follow-ups on the solution
    }
  ]
};

/* Category labels for the explain-more menu. Rename per subject. */
var KIND_LABEL = {
  "principle": "Principle / reasoning / origin",
  "solve":     "How to substitute and solve",
  "example":   "More worked examples"
};
```

`EXPAND` is deliberately **not** a registry. Deeper-explanation requests are satisfied by
editing the step's markup directly, because a separate sub-panel breaks the continuous read.

## Rendering rules

- Each `ANSWERS[id]` entry renders as a pill button in `.extras`; clicking opens the answer
  modal with the answer, its thread, and a compose box for the next follow-up.
- Each `CHECKS[id]` entry renders as a bordered box inserted after `.extras`, with a submit
  button and, once `answer` is filled, a show-solution button.
- The answer modal contains **no understood button**. Commitment controls exist only on the
  main page.
- Steps get a visual state: neutral, understood, or asked.

## Lesson map and section ledes

Two elements carry the through-line and both are plain markup.

The **lesson map** sits under the masthead as a `<details open>` block: a short intro line, then
one row per section giving the section number and a single clause naming what that section
settles. It is not a table of contents — never reuse the section headings verbatim; write what
each section *does* in the argument.

```html
<details class="map" open>
  <summary>the thread of this lesson</summary>
  <div class="mb">
    <p class="mintro">…why the sections are in this order…</p>
    <div class="mrow2"><b>§1</b><span><i>set the problem</i> — …</span></div>
  </div>
</details>
```

The **section lede** is a `<p class="sec-lede">` immediately after each `.sec-head`: two or three
sentences saying where the story is, what this section adds, and what it hands to the next. Bold
the one phrase that is the section's contribution.

## Prerequisites panel (optional)

When a lesson depends on prior machinery, put a panel above the first section holding either a
compact refresher or a few self-check questions with revealable answers. Same visual language as
a section, but marked `<section class="sec prereq">` so it is visually distinct.

Its steps are **not** `<article class="step">` and carry no understood/ask buttons, so they do
not enter the progress count and cannot block the next-steps panel. If the learner reports that
a prerequisite is missing, that is a signal to add a real section at the front of the lesson —
not to expand the panel.

## Post-lesson panel

The foot of the page, after the last section, in this order:

```
post-lesson panel
├── discussion box     ── free-text, always enabled, no gate
└── direction buttons  ── 3–5 concrete directions + a free-text option
```

**Discussion box first.** A textarea with a copy button, inviting the learner to say what they
think about what they have just learned rather than to choose something. It is never locked
behind the progress count — someone may want to argue with step four. Its copy payload is
tagged as post-lesson discussion so the reply happens in chat.

**Direction buttons second**, keeping the existing next-steps behaviour: disabled until every
step is marked understood, remaining count shown while locked, each direction described in words
rather than by section number.

A direction button ends the lesson session, so its payload is not a question but a **handoff
invocation**. The first line must be the literal slash command so that pasting it runs the
skill; the tag lines follow as its argument:

```
/handoff <lesson name> finished — next session will cover <direction in words>
[<lesson name> — end-of-lesson handoff]
direction: <direction in words>
page file: <filename>.html
```

## Clipboard tags added for the post-lesson panel

```
[<lesson name> — พูดคุยหลังบทเรียน]                ← discussion box
[<lesson name> — สรุปส่งต่อท้ายบทเรียน]              ← direction button, on the line after /handoff
```

Same rule as the other tags: translate the wording, keep the shape machine-identifiable.

## Next-steps panel

Disabled until every step is marked understood. Shows the remaining count while locked. Offers
3–5 concrete directions plus a free-text option; each copies a request describing the direction
in words. Do not label directions by section number.

## Visual design

Use CSS custom properties for the palette and honour `prefers-color-scheme: dark`. A restrained
paper-and-ink scheme reads well for long study sessions. Three type roles: a serif or display
face for headings, a humanist sans for body, a monospace for numbers, units, and labels. A
distinct colour for variables so symbols are identifiable mid-sentence.

Support `prefers-reduced-motion` and give focus states a visible outline.

## Equations and tables

Render maths as styled HTML, not images and not a LaTeX dependency:

```html
<div class="eq">
  <span class="frac"><span class="num">s(a+h) − s(a)</span><span class="den">h</span></span>
</div>
```

Classes added by the elements above, all plain CSS with no new dependencies: `.map`, `.mintro`
and `.mrow2` for the lesson map; `.sec-lede` for section ledes; `.crux` for the per-step
signpost; `.prereq` for the prerequisites panel; `.postbox` and `.discuss` for the post-lesson
panel; `.fig` and `.figcap` for hand-built diagrams; `.trivia` for enrichment asides that must
read as lighter than body text.

`.eq.plain` for an unboxed intermediate line. `<span class="v">` for variables. Tables use one
`table.data` class with a header row; keep them narrow enough to read on a phone and drop
font-size a step when a table needs six or more columns.
