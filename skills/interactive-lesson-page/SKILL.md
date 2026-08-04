---
name: interactive-lesson-page
description: Build a self-contained HTML lesson page for teaching a topic from scratch, where the learner marks each step understood, asks questions on any step, requests deeper explanation, and receives answers back as new expandable windows and merged rewrites in the same page across many turns. Use this whenever the user asks for a lesson page, study page, interactive lesson, "หน้าเรียน", or a teaching artifact they can keep and work through; whenever they want to learn a topic over multiple sessions rather than in one chat answer; and for every follow-up in an ongoing lesson thread — including messages that arrive tagged with a step number from a page you built earlier. For teaching in chat without a page, use ground-up-teaching instead.
---

# Interactive Lesson Page

Build one HTML page that teaches a topic from zero, and then keep growing it as the learner
works through it. The page is the whole classroom: the learner reads there, asks there, and
gets every answer there. Chat carries only a two- or three-line note about what changed.

## Two things to read first

1. `references/pedagogy.md` — how to write the teaching content. This is the larger half of
   the job and the part that determines whether the lesson works. Read it before writing any
   lesson text.
2. `references/page-spec.md` — the required functional behaviour of the page, the content
   registries, and the CSS/markup contract. Read it before writing any HTML.

`references/build-notes.md` has the build and validation procedure. Read it when you start
producing or editing the file.

## Turn 0 — scope the lesson before building anything

The first build is the expensive one, and it is also the one that decides whether the lesson
works, because the learner reads the main line and may never press a single button. So do not
start writing from a one-line request. Spend one or two short turns finding out what is
actually wanted.

Ask by offering options the learner can pick from rather than open prose questions wherever the
answer is enumerable — it is far less work to answer and it gives sharper information. One
question per turn where possible, three at the very most, two to four options each.

| What to establish | Why it changes the page |
|---|---|
| **Purpose** — exam, work problem, curiosity, teaching someone else | Decides whether procedure or intuition leads, and how many worked examples are needed |
| **Boundary** — which slice of the topic, and explicitly what to leave out | A topic named in three words can mean a two-hour lesson or a twenty-hour one |
| **Depth** — conceptual picture, working fluency, or formal rigour | Decides whether proofs, edge cases and formal definitions appear at all |
| **Background** — what the learner already holds that the chain can attach to | Every link must attach to a link they already have; guessing this wrong wastes the entire build |
| **Presentation** — worked numbers, diagrams, history, real-world applications | These are the enrichment axes; learners usually have a preference and it is cheap to ask |

When the answers come back, restate the plan in three or four lines — the arc, roughly how many
sections, what is deliberately excluded — so a misunderstanding is caught before an hour of work
goes into it rather than after. Then ask once more, in plain words, whether there is anything
else they want to say before the page is built: a constraint, a specific confusion to target, a
textbook to align with, the language to teach in.

**Build only after they confirm.** A partial answer is not consent to start.

Two exceptions. If the learner says to just build it, or is plainly impatient, ask nothing more
and build — but write the assumptions you made into the page's opening lines so they are
visible and correctable. And if this is a further lesson in a series whose scope is already
settled, skip straight to building.

## The working loop

**Turn 1 — build the page** (only once the scoping above is confirmed)**.** Design the full arc of the lesson, break it into numbered
sub-steps, write every step properly, and ship the file. The lesson skeleton created here is
permanent: later turns add to it and rewrite individual steps, but never renumber or restructure.

**Every later turn — the learner sends one of four things:**

| What arrives | What it means | What you do |
|---|---|---|
| A question tagged with a step number | They pressed *ask* on that step | Add an entry to `ANSWERS[step]` — a new expandable window on that step |
| A question tagged as a follow-up inside an expand window | They asked again inside a window | Append to that window's `thread` array — the window becomes a running conversation |
| A request tagged as wanting deeper explanation of a type | They pressed *explain more* and chose a category | **Rewrite the step itself** in the main page, merging old and new into one continuous read |
| An answer to a check question | They pressed *submit answer* on a check box | Mark the check correct/partial, fill in its `answer` so a *show solution* button appears |
| A message tagged as post-lesson discussion | They typed in the discussion box at the foot of the page | Reply conversationally in chat — the one place discussion belongs in chat rather than in the page |
| A request tagged as an end-of-lesson handoff | They chose a next direction | Run the `handoff` skill, tailored to that direction — see *Ending a lesson* below |

Reply in chat with a short note: what was added, where it is, and the one or two most
important points. Never teach in chat — the learner asked for everything to live in the page.

## The rule that separates the two answer mechanisms

**Ask → new window. Explain more → rewrite the step.**

The distinction matters. A question is a side branch; it gets its own space so the main line
stays clean. A request for deeper explanation means the main line itself failed, so the main
line is what must change.

When rewriting a step, **merge, do not append.** Do not add a sub-panel underneath the
original. Dissolve the original content into the new explanation so the step reads as one
continuous piece from top to bottom. The learner will not scroll back up to reconcile two
versions — assume the rewritten step is the only thing they will ever read.

The step heading may be rewritten too, and should be if the original heading was a terse label.
A good heading is a full statement of what is being done and why, e.g. *"Fix a = 1 but leave h
unspecified, then substitute into the formula to find the distance at the far end"* rather than
*"Substitute h, expand brackets"*.

## Designing the step breakdown

Aim for 20–30 sub-steps grouped into 6–9 sections. Each sub-step should be one idea that a
learner could plausibly get stuck on independently — that granularity is what makes per-step
understood/ask buttons meaningful.

Two failure modes to avoid, both observed in practice:

- **A step that presents something and stops.** A data table with no interpretation left the
  learner asking "so what?". Every step must answer: what can be known from this now, what
  still cannot, and what that forces next.
- **A step that only declares terminology before it is used.** Such a step is made redundant by
  the step that actually uses the terminology. Fold the definitions into the step where they
  do work.

## The content architecture is the job

The largest single determinant of whether the page works is the shape of the lesson, and that is
decided before a word of prose exists. Design the whole arc first as a list of section titles
with a one-line statement of what each section settles. Only then write.

**One key point per sub-step, and no key point twice.** Write the key point of every sub-step as
a single sentence before writing any of them, and read the list for collisions. If two sentences
overlap, merge the steps or re-cut them. Overlap is not harmless duplication — it makes the
learner feel they have lost their place, and it empties the per-step buttons of meaning, since a
step whose substance already appeared elsewhere cannot be marked understood as a unit.

**Every section exists because the previous one left something undone.** The lesson is a chain,
not a list of topics about the subject. Before adding a section, name the unfinished business
that forces it. If nothing forces it, it is enrichment: it belongs inside a step, not as a
section of its own.

**Cover the subject from every side that supports understanding.** A complete lesson usually
carries all of: where the problem came from, its history where it has one, the difficulty stated
plainly, the principle, the procedure step by step, the reasoning under each step, the
supporting knowledge the procedure silently assumes, worked examples, and an honest statement of
the limits. Thin coverage on any of these surfaces later as a question — and a question the
learner had to ask is usually a paragraph that should have been written.

**Make the connections visible instead of leaving them to be inferred.** Three devices carry
this and all three are cheap:

- A **lesson map** near the top — one line per section saying what it settles, so the learner
  can place themselves at any moment.
- A **section lede** — two or three sentences at the head of each section saying where the story
  is, what this section adds, and what it hands to the next.
- A **crux block** at the foot of every sub-step — what is settled now, what is still missing,
  and what that gap forces next. This is the most useful structural element in the whole page,
  because it keeps the thread visible at the scale the learner actually reads at, and because
  writing it exposes any step that does not actually advance the argument.

**Scope discipline, and why it starts here.** Because each step owns exactly one key point, a
question asked on a step can be answered inside that step's remit and stopped at its boundary.
If answering properly seems to require material belonging to a later step, that is evidence the
arc is wrong — not a licence to spill forward. Say what can be said here, name the boundary in
one clause, and let the later step do its job.

## Evidence from rebuilding a lesson from scratch

The same lesson was built twice: once by writing a chat answer and cutting it into steps, and
once by designing the arc first and writing every step to full weight. Measuring visible text
per sub-step:

| | sub-steps | under 600 characters | median |
|---|---|---|---|
| Cut up from a chat answer | 25 | 21 | 223 |
| Built architecture-first | 30 | 0 | 1903 |

In the first version the only steps written to full weight were the four the learner had
happened to ask about, and the material that actually made the lesson land had accumulated in
answer windows — invisible to anyone who did not press a button.

Two diagnostics follow, both worth running on your own draft:

- **Question clustering.** Twelve of the learner's twenty-one questions landed on one step. That
  is not a hard step, it is a missing section. On the rebuild that cluster became four main-line
  steps of its own, and the windows were emptied into the main line.
- **Density floor.** If a sub-step's prose would fit in a single paragraph, it is an outline
  entry rather than a step. Write it properly or fold it into its neighbour.

## Ending a lesson: discussion first, then direction, then handoff

The foot of the page is not a menu. It is, in this order:

1. **A free-text box inviting discussion** of what was just learned — reactions, disagreements,
   half-formed connections, things it reminded them of. It comes first because it is the only
   part of the page that does not ask the learner to choose from a list, and because someone who
   has just finished usually has something to say before deciding where to go next.
2. **The concrete next directions**, as buttons.

Discussion messages are answered in chat, conversationally. This is the one exception to the
rule that nothing is taught in chat — and it stops being an exception the moment the exchange
turns into teaching, at which point the material also goes into the page as a window on the step
it belongs to.

**Choosing a direction ends the lesson session.** When a direction button is pressed, run the
`handoff` skill with the chosen direction as its argument, so the next session begins holding
everything this one produced. Because `handoff` cannot be invoked by the model on its own, the
button copies a message that *is* the invocation; the learner pastes it and it runs.

Beyond whatever `handoff` normally includes, a lesson handoff must carry:

- the path of the page file, and the instruction to continue in that file rather than starting a
  new one unless the chosen direction is genuinely a separate lesson;
- the lesson skeleton — section and step numbers with their headings — since step ids are
  permanent and all later routing depends on them;
- which steps were marked understood and which were marked asked;
- every question the learner asked, where its answer lives, and what it revealed about how they
  think — the clusters especially, since a cluster marks a weak part of the main line;
- the check questions posed, what the learner answered, and what had to be corrected;
- what Turn 0 established about their background, purpose and preferences;
- the chosen direction written as a lesson brief, not as a topic name.

## Adapting the page to the subject

The mechanics are fixed; the labels are not.

- The *explain more* sub-options were "principle / reasoning / origin", "how to substitute and
  solve", and "more worked examples" for a mathematics lesson. Rename them for the subject —
  a history lesson might offer "context and causes", "sources and evidence", "another case".
  Use two to four; three is a good default.
- Add more check questions for subjects where self-testing helps, or none where it doesn't.
- The sidebar was a variable reference for a mathematics lesson. It should hold whatever the
  learner will need to look up repeatedly: a glossary, a timeline, a cast of actors, a formula
  card. Keep the same sticky/collapsible behaviour.
- One custom diagram or data visualisation per lesson, where it genuinely shows something
  prose cannot, is worth building. Do not decorate.
- Some subjects want a **prerequisites panel above the first section** — a short refresher of
  the knowledge the chain is about to attach to, or a few questions that let the learner find
  out for themselves whether they hold it. Use it when the lesson depends on specific prior
  machinery a learner may or may not have, and when starting without it would strand them three
  steps in. Skip it when the lesson genuinely starts from zero. It is a panel, not a gate: never
  lock the lesson behind it.

## Content that must appear in the page and not in chat

- All teaching, explanation, examples, and worked solutions.
- Any checking question you want to ask the learner. Put it in a check box on the relevant
  step with its own submit button — do not ask it in the chat reply.
- Any correction of a misunderstanding, including corrections of the learner's terminology.

## Hard constraints

- **Never renumber or delete existing steps.** The learner's progress state is keyed to step
  IDs, and they navigate by position.
- **Never cite a step the learner has not reached.** If a later result is needed, derive it
  inline. Referring forward makes the learner feel they have missed something.
- **Never cite any step by number as a substitute for content.** They do not remember the
  numbers. Carry the substance of the reference into the sentence.
- **Preserve every function already present in the page** when editing. Validate after every
  edit; a broken script silently destroys the entire lesson.
- **Never start building before the scope is confirmed.** The cost of a wrong first build is the
  whole build.
- **Never ship a step you could only explain properly if asked.** If you can already name the
  question a step will provoke, the answer belongs in the step.
- **Never let one step's key point reappear as another step's key point.** Carrying substance
  forward for orientation is required; re-teaching it is a structural error.
- **Never spoil a later step's payoff in an earlier one.** Where a result can be reached by a
  second independent route, that route belongs where the first route arrives, not before it.
