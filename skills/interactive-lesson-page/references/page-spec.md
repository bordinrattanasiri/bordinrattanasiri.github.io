# Page specification

One self-contained HTML file. No build step, no external JS. Web fonts from Google Fonts are
fine; everything else is inline.

## Layout

Top to bottom, this is the order of the page:

```
sticky progress rail   ── understood count, progress bar, reset button
masthead               ── eyebrow, title, one-line orientation
how-to-use             ── collapsible <details>, closed by default
series rail            ── series only: position, ordered list of all lessons, short overview
lesson map             ── collapsible <details>, open by default, one line per section
prerequisites panel    ── optional
two-column grid        ── main column (sections and steps) | sticky sidebar reference panel
post-lesson panel      ── discussion box first, then the next-direction buttons
                          (in a series that is not the last lesson: one next-lesson button
                           instead of the directions)
two modals             ── ask modal, answer modal (markup at the end of the body)
```

There is no separate next-steps panel: the direction buttons inside the post-lesson panel are
that mechanism, and they carry its gate.

At ≤900px the grid collapses to one column and the sidebar becomes a collapsible bar pinned
under the rail.

## How-to-use block

The page works differently from anything the learner has used, and this block is the only place
that says so. It is a `<details>` under the masthead, closed by default so a learner who already
knows can ignore it, and its contents are fixed. Translate the nine lines below into the language
of the lesson; do not rewrite them, reorder them, add to them, or turn them into prose.

> **How to use this page**
>
> 1. This page can be read anywhere, but every button on it works by copying a message to your
>    clipboard for you to paste into the Claude chat that built it, so the two are used together.
> 2. Read the steps in order, and when a step has landed press **Understood** at the foot of it
>    and move on to the next one.
> 3. When you have a question, press **Ask** on that step, type it in, press **Copy question**
>    and paste it into the chat — the answer appears in a new window on that step, and you can
>    ask more than once.
> 4. When a step did not land but you cannot yet turn the problem into a question, press
>    **Explain more** and choose from ⟨the sub-options this lesson offers⟩ — the step is written
>    again from a different direction, and you can press it again if it still does not land.
> 5. The small buttons inside the prose open side notes — in this lesson ⟨what they actually
>    hold⟩ — which you can read or skip without it affecting your grasp of the main line, and you
>    can ask inside them too.
> 6. Some steps hold a question to try: write your answer in the box and copy it into the chat,
>    and the verdict appears in that box together with a button that opens the full solution.
> 7. At the foot of the page there is a box for saying what you think about what you have just
>    learned — a disagreement, a half-formed connection, anything it brought to mind — and the
>    reply appears in the page underneath what you wrote.
> 8. Below that are the directions this lesson can lead to next, which unlock once every step is
>    marked understood, and pressing none of them is a perfectly good way to finish here.
> 9. When you have worked through the lesson, download this page and keep it for review —
>    everything asked and answered along the way is in the file.
>
> **Note.** Each chat holds a limited amount of work, and once a page has been built and worked
> over for a while the answers get less sharp. When that happens, type "write me a handoff" in
> the chat and you will get back a short summary file; download it together with this page, open
> a new chat, drop both files in and press enter to carry straight on.

Four things about filling it in:

- **Three slots are filled from the page you actually built** — the button names exactly as they
  read on the page, the sub-options of the *explain more* menu, and what the side windows in this
  lesson genuinely hold, named concretely rather than as "extra material".
- **Drop line 5 or line 6 entirely** when the lesson has no side windows or no check questions,
  and renumber what remains.
- **In a series, line 8 is replaced** by: *Below that is the button for the next lesson in this
  series, which unlocks once every step is marked understood.* The last lesson of a series keeps
  the ordinary line 8.
- **The quoted phrase in the note is an example, not a command.** Translate it naturally and keep
  the quotation marks; any wording the learner uses to ask for a handoff is honoured.

## Progress state and the storage key

Understood/ask state is stored per step under a single key. Declare it once, as a literal
constant at the top of the script, derived from the page filename:

```js
var STORE_KEY = "lesson-<slug>-v1";   /* must match the page filename; never changed later */
```

This is what carries the learner's marked steps across every rebuild of the file. The page is
rewritten on almost every turn, and if a rebuild invents a different key the new file reads an
empty box and the learner's progress silently resets. Copy the existing key forward on every
edit. It changes in exactly two cases: a lesson rebuilt from scratch rather than extended, and
the next lesson of a series, which is a different file with its own key.

Use `window.storage` when present and degrade silently to in-memory state when it is not, so the
page never throws in an environment that does not provide it:

```js
var hasStore = (typeof window.storage !== "undefined" && window.storage);
```

Never use `localStorage` or `sessionStorage` — they fail in this environment.

The reset button clears the stored state for this key and returns every step to neutral. Confirm
before doing it; it is the one control on the page that destroys something.

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

**The last step of the lesson has nothing after it**, so its third line changes job rather than
being filled with something invented. It states what the learner can now do that they could not
do when the lesson began, or names what the lesson deliberately left outside its boundary. It is
never a teaser for further study, and in a lesson belonging to a series it names what the next
lesson takes up — by content, never by lesson number.

When a step is rewritten in response to an *explain more* request, the crux block is rewritten
with it and stays last before `.extras`. The step's `data-id`, its number and its position never
change.

Aside buttons — see *Side windows* below — may appear anywhere in the step's prose, at the
sentence they attach to, but never inside `.crux`, `.extras` or `.acts`.

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

## Clipboard tags

Every copy action emits a tagged first line so the next chat message identifies itself. Keep
these exact shapes; the routing in the main SKILL.md depends on them.

```
[<lesson name> — step §3.1 <step heading>]                        ← ask on a step
[<lesson name> — follow-up in answer window §3.1 · <window title>] ← follow-up inside a window
[<lesson name> — follow-up in side window §3.1 · <aside title>]    ← follow-up inside a side window
[<lesson name> — explain more §3.1 <step heading>]\nkind: <category>
[<lesson name> — check answer §3.1]                                ← answer to a check question
[<lesson name> — follow-up in check solution §3.1]                 ← follow-up in a solution window
[<lesson name> — post-lesson discussion]                           ← discussion box
[<lesson name> — end-of-lesson handoff]                            ← direction button
[<lesson name> — end-of-lesson handoff (series)]                   ← next-lesson button in a series
```

Translate the tag wording to the lesson's language, but keep the section marker and step id
literal so they stay machine-identifiable. Where a step carries more than one window, the title
after the `·` is what tells them apart, so window titles on the same step must be distinct.

Implement copy with `navigator.clipboard.writeText` and a hidden-textarea + `execCommand`
fallback, then show a short confirmation message next to the button.

## Content registries

All injected content lives in object literals at the top of the script. This is the only place
later turns add content, apart from rewriting the inside of a step's markup directly.

Three of them are **keyed by step id**, and every key must correspond to a step that exists in
the page: `ANSWERS`, `CHECKS`, and `ASIDES` — whose keys carry a suffix, so the step id is the
part before `-a`. Two of them are **not keyed by step id** and must be exempted from that check:
`DISCUSS` is a flat list with no keys at all, and `KIND_LABEL` is keyed by category name. Any
registry added later declares which of the two groups it belongs to.

```js
/* keyed by step id — expandable windows created from questions asked on a step. */
var ANSWERS = {
  "3.1": [
    { q: "Button label — the learner's question, condensed",
      a: "<p>…full answer HTML…</p>",
      thread: [                                   // optional, grows over time
        { q: "follow-up asked inside this window", a: "<p>…</p>" }
      ] }
  ]
};

/* keyed by step id (before the -a suffix) — enrichment windows, opened by a named
   button placed inline in a step's prose. */
var ASIDES = {
  "3.1-a1": { title: "Button label — also the heading of the window",
              body:  "<p>…the aside, a few paragraphs…</p>",
              thread: []                       // grows exactly like an ANSWERS thread
            }
};

/* keyed by step id — check questions posed by the teacher, rendered as a highlighted
   box in the step. */
var CHECKS = {
  "2.1": [
    { body:   "<p>…the question…</p>",
      note:   "…the verdict on the learner's answer, one or two sentences, optional…",
      answer: null,        // null → no solution button yet; HTML string → button appears
      thread: []           // follow-ups asked inside the solution window
    }
  ]
};

/* NOT keyed by step id — a flat list. The post-lesson discussion, rendered straight
   into the panel at the foot of the page. */
var DISCUSS = [
  { q: "…the learner's message, condensed to a line…",
    a: "<p>…the reply, in full…</p>" }
];

/* NOT keyed by step id — category labels for the explain-more menu. Rename per subject. */
var KIND_LABEL = {
  "principle": "Principle / reasoning / origin",
  "solve":     "How to substitute and solve",
  "example":   "More worked examples"
};
```

`EXPAND` is deliberately **not** a registry. Deeper-explanation requests are satisfied by editing
the step's markup directly, because a separate sub-panel breaks the continuous read.

## Rendering rules

- Each `ANSWERS[id]` entry renders as a pill button in `.extras`; clicking opens the answer modal
  with the answer, its thread, and a compose box for the next follow-up.
- Each `ASIDES[id]` entry is bound to the button already sitting in the prose — nothing is
  injected and nothing moves. Clicking opens the answer modal.
- Each `CHECKS[id]` entry renders as a bordered box inserted after `.extras`, holding the
  question, a textarea and a submit button. See *Check boxes* below for what happens next.
- `DISCUSS` renders as a plain transcript inside the post-lesson panel, above the box: each
  entry's message then its reply, in order, always visible. No button, no modal.
- The answer modal contains **no understood button**. Commitment controls exist only on the main
  page.
- Steps get a visual state: neutral, understood, or asked.

## Check boxes

A check question behaves like everything else on the page: the learner answers, the answer goes
back through the chat, and what returns is a window they can keep asking inside.

1. **Before it is answered.** The box shows the question, a textarea, and a *submit answer*
   button. The button copies the tagged message with the learner's text below the tag; it does
   not judge anything locally.
2. **Once the reply comes back.** `note` is filled with the verdict — plainly whether it was
   right, right in part, or wrong, and exactly which part was off — and renders inside the box
   under the question. `answer` is filled with the full solution, which makes a *show solution*
   button appear beside the submit button.
3. **The solution opens in the answer modal**, exactly as an answer window does: the solution,
   the thread beneath it, and a compose box at the foot. Follow-ups asked there append to that
   check's `thread` and render inside the same window, in order. This is the same control and the
   same behaviour as the other two window types; only the clipboard tag differs.

A check never blocks anything and never enters the progress count.

## Side windows

An aside is a `<button class="aside">` standing inside the step's prose, at the sentence it
attaches to:

```html
<p>…Huygens spent the winter of 1656 on the problem, and
<button class="aside" data-aside="3.1-a1">why a pendulum clock changed the world</button>
is a detour worth taking…</p>
```

The id convention is `<step id>-a<n>`. It keeps every aside attached to a step for validation and
for the handoff without constraining where in the step the button may sit.

- The button's visible text and the registry `title` are the same string. If the markup button is
  left empty the script fills it from `title`; if the registry entry is missing the script removes
  the button rather than leaving a dead control on the page.
- Clicking opens the **answer modal** — the same modal, the same thread rendering, the same
  compose box at the foot.
- Asides carry no understood/ask state, never enter the progress count, and never gate anything.
- Style the button as inline text — a marked underline or a small pill. Visibly a control, not
  loud enough to compete with the sentence it stands in. `.trivia` stays what it was: a short
  aside that remains in the flow instead of opening a window.

### One modal, three kinds of window

The answer modal is reused by answer windows, side windows and check solutions. The script must
therefore keep, alongside the open window's id and index, **which kind it is**, because that is
what decides the tag the compose box copies and which registry the follow-up will be appended to.
Set it when the modal is opened and read it when the compose box is used; never infer it from the
id, since a step id alone does not distinguish an answer from a check.

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

## Series rail (only when the lesson belongs to a confirmed series)

A block between the how-to-use box and the lesson map, answering three questions at a glance: is
this part of something, which part, and what are the others.

```html
<section class="series">
  <p class="series-pos">Part of a series · lesson 2 of 5</p>
  <p class="series-intro">…one short paragraph on how the five hold together…</p>
  <ol class="series-list">
    <li class="done"><b>…lesson title…</b><span>…one clause on what it settled…</span></li>
    <li class="here"><b>…this lesson…</b><span>…what it settles…</span></li>
    <li><b>…</b><span>…</span></li>
  </ol>
</section>
```

The list is to the series what the lesson map is to the lesson: never a bare list of titles,
always the title plus what that lesson does in the argument. Mark the current lesson `here` and
earlier ones `done`; both are visual only. Nothing is clickable and there is no cross-file state —
each lesson is a separate file with its own storage key.

## Sidebar reference panel

The sticky column beside the main text. It is a reference, not a summary: every line in it is
something the reader may need to look up mid-sentence, and nothing in it teaches. A learner who
read only the sidebar would learn nothing; a learner who has lost a symbol finds it there in one
glance.

It holds, in labelled groups:

- **terms** — the load-bearing vocabulary of the lesson. In a lesson taught in a language other
  than English every entry carries both forms, the term as the lesson says it and the English.
  That pairing is what lets the learner read English sources afterwards, and it is the main
  reason the panel exists in a translated lesson.
- **symbols and abbreviations**, each with a gloss of one clause.
- **variables** — symbol, what it stands for, its unit, and the value it takes in the running
  example.
- **the formulas and equations the lesson keeps returning to**, in the same styled markup the
  body uses, so they are recognisably the same objects and not a second notation.

```html
<aside class="side">
  <div class="sidegroup"><h4>terms</h4>
    <div class="sideitem"><b>…term as the lesson says it…</b>
      <span class="term-en">…English…</span></div>
  </div>
  <div class="sidegroup"><h4>symbols</h4>
    <div class="sideitem"><b><span class="v">h</span></b><span>…one clause, with unit…</span></div>
  </div>
</aside>
```

An entry appears only once the lesson has introduced the thing: the panel never previews and
never holds a term the body has not defined. One line per entry. The groups are the structure and
are never dissolved into one merged list — terms sit with terms, symbols with symbols — and
within each group the order is the order of introduction rather than the alphabet, so the panel
reads as a trace of the lesson. At ≤900px it collapses into the bar pinned under the rail, which
is why every entry must stay legible on a single line.

## Prerequisites panel (optional)

When a lesson depends on prior machinery, put a panel above the first section holding either a
compact refresher or a few self-check questions with revealable answers. Same visual language as
a section, but marked `<section class="sec prereq">` so it is visually distinct.

Its steps are **not** `<article class="step">` and carry no understood/ask buttons, so they do
not enter the progress count and cannot block the post-lesson panel.

Whether a piece of prior machinery gets a real section or a line in this panel is decided during
scoping, from what the learner said about their background, and the page is built on that answer.
If a gap surfaces later, it is handled the way every other gap is handled — answered in a window,
or through an *explain more* request on the step where it bit — and noted in the handoff as an
observation about how this page was scoped: the panel was carrying more than a panel can carry.
That is a remark for whoever plans the next lesson in this area to weigh, not a commitment about
what the next lesson contains. This lesson's sections are not restructured mid-lesson.

## Post-lesson panel

The foot of the page, after the last section, in this order:

```
post-lesson panel
├── discussion box     ── free-text, always enabled, no gate
└── direction buttons  ── 3–5 concrete directions + a free-text option,
                          disabled until every step is marked understood
```

**Discussion box first.** A textarea with a copy button, inviting the learner to say what they
think about what they have just learned rather than to choose something. It is never locked
behind the progress count — someone may want to argue with step four.

The reply comes back **into this panel**, not into chat and not behind a button: each exchange is
appended to `DISCUSS` and rendered as a transcript above the box, message then reply, in order.
Nothing here can be confused with the main line, because the panel sits below the last section
and holds no lesson content — which is exactly why the answer can be shown in the open. A learner
who saves the file then has the lesson and every conversation about it in one document.

**Direction buttons second.** Disabled until every step is marked understood, with the remaining
count shown while locked. Directly under the row of buttons sits one line of ordinary text saying
that pressing none of them is a complete way to end the lesson. It is not a caption on a disabled
control — it stays visible once the buttons unlock, because that is when it means something. A
series lesson does not carry it: there the single next-lesson button is the plan, not a menu.

Each direction is described in words rather than by section number, and the free-text option
copies the same payload with the learner's own wording in the `direction` line.

A direction button ends the lesson session, so its payload is not a question but a **handoff
request**. The skill writes the handoff itself, so the payload is an ordinary tagged message with
no command in it:

```
[<lesson name> — end-of-lesson handoff]
direction: <direction in words>
page file: <filename>.html
```

### Series variant

When the lesson belongs to a confirmed series and is not the last one, the direction buttons are
replaced by a single next-lesson button naming the next lesson in words. The discussion box above
it is untouched and still ungated. The button keeps the same gate the directions had and copies:

```
[<lesson name> — end-of-lesson handoff (series)]
series: <series name> — lesson <n> of <N>
next lesson: <next lesson name> — <what it settles>
remaining after that: <the rest, in order>
page file: <filename>.html
```

The last lesson of a series has no next lesson and uses the ordinary direction buttons.

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

## Code

Some subjects are taught in code, and code is content rather than decoration.

```html
<pre class="code"><code>…one runnable fragment…</code></pre>
```

Plain monospace styled by the page's own CSS. **No syntax highlighter**, because the file has to
work offline with no external script, and a highlighter that fails leaves an unreadable block.
If a line needs marking, mark it with a comment in the language itself.

A code block is shown and then walked in prose, exactly as an equation is: what this line does,
why it is written this way, what it produces for the one concrete input the step is following. A
block dropped in without the walk is the same failure as a bare formula. Keep fragments short
enough to read on a phone — the block scrolls horizontally rather than wrapping, so a line that
runs long is a line that will not be read.

## Class inventory

Classes added by the elements above, all plain CSS with no new dependencies: `.map`, `.mintro`
and `.mrow2` for the lesson map; `.sec-lede` for section ledes; `.crux` for the per-step
signpost; `.prereq` for the prerequisites panel; `.postbox` and `.discuss` for the post-lesson
panel, with `.dentry` for one exchange in its transcript; `.fig` and `.figcap` for hand-built
diagrams; `pre.code` for code blocks; `.trivia` for short enrichment asides that stay in the flow
and must read as lighter than body text; `.aside` for the inline button that opens a side window;
`.side`, `.sidegroup`, `.sideitem` and `.term-en` for the sidebar reference panel; `.series`,
`.series-pos`, `.series-intro` and `.series-list` for the series rail; `.nextlesson` for the
single next-lesson button that replaces the directions in a series.

`.eq.plain` for an unboxed intermediate line. `<span class="v">` for variables. Tables use one
`table.data` class with a header row; keep them narrow enough to read on a phone and drop
font-size a step when a table needs six or more columns.
