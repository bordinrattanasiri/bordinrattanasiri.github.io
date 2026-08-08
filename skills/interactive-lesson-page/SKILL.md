---
name: interactive-lesson-page
description: Build a self-contained HTML lesson page for teaching a topic from scratch, where the learner marks each step understood, asks questions on any step, requests deeper explanation, and receives answers back as new expandable windows and merged rewrites in the same page across many turns. Use this whenever the user asks for a lesson page, study page, interactive lesson, "หน้าเรียน", or a teaching artifact they can keep and work through; whenever they want to learn a topic over multiple sessions rather than in one chat answer, including subjects large enough that they must be planned as a series of lessons; for every follow-up in an ongoing lesson thread, including messages that arrive tagged with a step number from a page you built earlier; and for a session that opens with nothing but a handoff document that names this skill. For teaching in chat without a page, use ground-up-teaching instead.
---

# Interactive Lesson Page

Build one HTML page that teaches a topic from zero, and then keep growing it as the learner
works through it. The page is the whole classroom: the learner reads there, asks there, and gets
every answer there. Chat carries only a short note about what changed.

**The first delivery decides everything.** The learner reads the main line and may never press a
single button, so the page has to be complete before anyone sees it. Questions arrive afterwards
and are answered in windows; they never restructure what was already built. Every rule in this
skill exists to make that first build as good as it can be made, and the largest part of making
it good happens before a word of prose is written: the lesson is a chain in which every link
attaches to a link the learner already holds, and designing that chain is the job.

## Two files to read first

1. `references/pedagogy.md` — how the lesson is designed and written: the shape of the arc, the
   rules for the prose, the side windows, the check questions, the diagnostics to run on a
   draft. This is the larger half of the job. Read it before planning anything.
2. `references/page-spec.md` — the required behaviour of the page, the content registries, and
   the markup contract. Read it before writing any HTML.

`references/build-notes.md` is the build and validation procedure. Read it when you start
producing or editing the file.

This file answers *what happens when, and in what order*. It does not restate the writing rules;
where a decision depends on them it points at `pedagogy.md`.

## How a session can start

Three ways, and the first thing to do is work out which one this is.

1. **A new request** — the learner asks to be taught something. Go to *Scoping the lesson*.
2. **A handoff document** — a file from an earlier session, often dropped in with no message at
   all. That is the intended way to continue, so read it and begin from it rather than asking
   what they would like to do.
3. **A page file with no handoff** — a finished lesson uploaded back, with a question about it
   or a request to carry on. Go to *Continuing from a page file*.

### Resuming from a handoff document

The document carries two lines that decide what happens, because the session that wrote it knew.
They answer separate questions and must both be read:

```
page: new                       ← or: continue the attached file
subject: next part of <series name> — lesson 3 of 5
```

**`page: new` + `subject: next part`.** The subject was split into parts when the series was
agreed, and the learner has already spent a session inside it. Do not re-scope it. Open with a
short message that recaps what the previous lesson settled, names what this one covers, and
places it in the planned sequence — which lesson this is, with the rest listed in order. Close
by asking whether there is anything to add or change before the page is built, name the language
the page will be written in, and wait. **Build only after they confirm.**

**`page: new` + `subject: new topic`.** The direction came from the buttons at the foot of the
last page, which makes this a new subject that happens to have a neighbour. Run the scoping
below in full. What the handoff records about the learner is context for asking better questions,
not a substitute for asking them — someone who wanted a working grasp of the last subject may
want the formal treatment of this one.

**`page: continue the attached file`.** The previous session ran out of room while the lesson was
still being worked on. The page file should have arrived with the document; take it and carry on
in the working loop from where the record says they stopped. Nothing is rebuilt and nothing is
re-scoped, whichever subject line accompanies it. If the file did not come with it, ask for it —
that is a technical matter and belongs in chat.

Either way the handoff is context, not a script. Where it reports that questions piled up on one
step, weigh that while planning; it does not decide what this lesson contains.

### Continuing from a page file

A session may open with a finished page and no handoff document, because the learner had the page
built and came back to it later. That is a reasonable way to use this and it works: a finished
page states its own scope — the lesson map, the section ledes and the crux blocks say what it
covers, in what order, and where it stops — and the rules for answering already require every
addition to agree with what is on the page.

Read the file in full: the step ids, the registries, and every answer already given, so that what
you add agrees with what the learner has already read. Then continue the working loop on that
file. Do not rebuild it and do not re-scope it — the scope was settled when it was built, and
rebuilding would destroy every window and every answer already in it.

What the page does not carry is what was said around it: what scoping deliberately excluded, what
the learner said about their background, and the reasoning behind answers already written. Where
an answer would turn on one of those, ask rather than assume. Progress marks live in the browser
under the page's storage key, so the same browser still shows them and any other starts clean.

## Scoping the lesson

The first build is the expensive one, and it is the one that decides whether the lesson works. So
do not start writing from a one-line request. Find out what is actually wanted first.

Take as many turns as it takes. Some learners answer everything in one message; others want to
discuss the boundary, push back, and think aloud about what they are really after. Both are the
process working. There is no turn budget and no question limit — the only thing that ends this
phase is having enough to build against.

| What to establish | Why it changes the page |
|---|---|
| **Purpose** — exam, work problem, curiosity, teaching someone else | Decides whether procedure or intuition leads, and how many worked examples are needed |
| **Boundary** — which slice of the topic, and explicitly what to leave out | A topic named in three words can mean a two-hour lesson or a twenty-hour one |
| **Depth** — conceptual picture, working fluency, or formal rigour | Decides whether proofs, edge cases and formal definitions appear at all |
| **Background** — what the learner already holds that the chain can attach to | Every link must attach to a link they already have; guessing this wrong wastes the entire build |
| **Presentation** — worked numbers, diagrams, history, real-world applications | These are the enrichment axes; learners usually have a preference and it is cheap to ask |
| **Language** — the language the page itself will be written in | It is normally the language they are writing to you in, but not always; it decides the prose, the sidebar, and the wording of every button |

**Ask in whatever form fits the question.** Where the answers are enumerable, offering a few
options is far less work to answer than open prose and gives sharper information; if the
environment can show them as something to tap or click, use it. Where the options would not mean
anything yet, say what the choice is about in two or three sentences first, then ask. Where the
answer is genuinely open, ask an open question. And where one answer would narrow the field
usefully, ask that one and let the rest follow from it. Keep each turn short enough to answer in
a moment.

When the answers come back, restate the plan: the arc, what it covers, what is deliberately
excluded, the language it will be written in, and the division into lessons if the subject needs
more than one. A few lines is enough. The point is that a misunderstanding is caught before an
hour of work goes into it rather than after. Then ask in plain words whether there is anything
else they want to say before the page is built — a constraint, a specific confusion to target, a
textbook to align with.

**Build only after they confirm.** A partial answer is not consent to start.

Two exceptions. If the learner says to just build it, or is plainly impatient, ask nothing more
and build — but write the assumptions you made into the page's opening lines so they are visible
and correctable. And if this is a further lesson in a series whose scope is already settled, do
not re-scope it; see *Resuming from a handoff document* above.

### One lesson or a series

Scoping has a second output besides the boundary of this lesson: whether one page can hold the
subject at all. Two different situations force the question, and they are answered differently.

**The subject is too large for one page.** The signs appear while you are still sketching the
arc: the honest step list keeps growing, or the boundary can only be drawn by cutting something
the learner has said they want. Do not solve this by compressing — a compressed lesson is a
summary, and a summary teaches nobody from zero. Propose a division instead: a numbered list of
lessons, each with a title and one clause saying what it settles, in the order they have to be
walked, plus a sentence on what the whole set adds up to.

**The subject is one node in a network.** The requested topic leans on a neighbouring one, or a
neighbouring one is what makes it obvious. Here the requested topic need not be lesson one — you
may propose that something else comes first, provided you say plainly what that lesson supplies
and what the requested lesson would otherwise have to smuggle in through a prerequisites panel.
A series of this kind is a claim that the topics hold each other up, so make the claim, one
sentence per link, rather than listing related subjects.

In both cases the proposal belongs in the same restatement of the plan, and the learner confirms,
reorders, cuts, or refuses it. **A series exists only once they say so.** A learner is entitled
to want exactly the one thing they asked for; then teach the one thing and let the prerequisites
panel carry what the dropped lesson would have supplied.

**Propose a series only when the subject forces one.** Two conditions justify one and nothing
else does: the topics hold each other up so tightly that teaching one alone means smuggling in
half of another, or the honest treatment of a single topic genuinely will not fit on one page.
Breadth is not a third condition. Almost any subject *could* be divided, and a list of related
things is not a chain.

Four signs that you are about to propose one for the wrong reason: the lessons after the first
exist to teach material the learner never asked about; the division falls where the page got long
rather than at a joint in the argument; you cannot say in one clause what each lesson settles
that the one before it left open; or the first lesson would not be a whole lesson if they stopped
there. Any of these means it is one page — possibly a long one, which is fine.

The cost of not proposing is small and the cost of proposing wrongly is not. If a second lesson
turns out to be wanted, the direction buttons at the foot of the finished page produce it anyway,
scoped by what actually happened rather than by what you guessed before building. So when the
case is not obvious, build the one page. One page is the default and most topics fit on one page.

Each lesson of a confirmed series is its own page file, with its own storage key and its own step
numbering starting at §1.1. Nothing is ever appended to the previous lesson's page.

## Check the facts before you plan

The arc is built out of specifics — dates, names, numbers, versions, the exact form of a rule,
the syntax that actually compiles — and a lesson that gets one wrong teaches it wrong to someone
with no way of catching it. Before designing the arc, look up whatever you could not state
precisely from memory, and anything in the subject that moves: current versions, current
practice, anything you would be guessing at. Do the same for the material that will become side
windows, which is where half-remembered stories collect.

This costs a few minutes and it belongs before the plan rather than after, because a fact
discovered late can force the arc to be rebuilt around it.

## Design the whole arc before writing

The largest single determinant of whether the page works is the shape of the lesson, and that is
decided before a word of prose exists. Design the whole arc first — the sections, what each one
settles that the previous one left open, and the sub-steps inside them with the single key point
each one carries. Only then write.

`pedagogy.md` holds the rules for doing this: how to cut the arc, how to test it for collisions
and gaps, what a complete treatment has to cover, and what makes a step a step rather than an
outline entry. It is not repeated here. Nothing about the arc is decided by counting: the subject
decides how many sections it has and how far each step has to go, and a step is right when it
carries one idea completely, not when it reaches a length.

## Adapting the page to the subject

The mechanics are fixed; the labels are not. Nothing in this skill is specific to mathematics —
the same machinery carries history, law, music, engineering and programming, and the adaptation
is always a translation of vocabulary rather than a loosening of the doctrine.

- The *explain more* sub-options were "principle / reasoning / origin", "how to substitute and
  solve", and "more worked examples" for a mathematics lesson. Rename them for the subject —
  a history lesson might offer "context and causes", "sources and evidence", "another case".
  Two to four of them; three is a good default.
- Add check questions where self-testing helps and none where it does not. Where they go matters
  more than how many there are — see *Where a check question belongs* in `pedagogy.md`.
- The sidebar was a variable reference for a mathematics lesson. It should hold whatever the
  learner will need to look up repeatedly: a glossary, a timeline, a cast of actors, a formula
  card. Keep the same sticky/collapsible behaviour.
- In a programming lesson the worked numbers become a real input traced through a real
  implementation: show the code, then walk it in prose, then show what it produces for one
  concrete input before generalising. A snippet the learner can paste and run is the equivalent
  of a substituted equation, and the same rule applies to both — it is shown *and* explained,
  never dropped in as self-evident. The *explain more* labels for such a lesson might be
  "why it is written this way", "line by line", "another case it has to handle".
- A custom diagram or data visualisation is worth building where it genuinely shows something
  prose cannot. Do not decorate.
- Some subjects want a **prerequisites panel above the first section** — a short refresher of the
  knowledge the chain is about to attach to, or a few questions that let the learner find out for
  themselves whether they hold it. Use it when the lesson depends on specific prior machinery a
  learner may or may not have, and when starting without it would strand them three steps in.
  Skip it when the lesson genuinely starts from zero. It is a panel, not a gate: never lock the
  lesson behind it.

## The third window: the aside you open yourself

Two of the page's three windows are reactive — the learner presses something and the page
answers. The third one is yours: material that research turns up which is genuinely good and
genuinely optional, placed in the prose as a named button at the sentence it attaches to.

It exists because a page built strictly to the chain reads flat. The chain is what makes the
subject teachable; the asides are what make the page somewhere worth spending two hours in. They
also let a lesson admit that the subject is larger than the slice being taught without the slice
losing its shape.

**One test decides whether something may be an aside: delete every aside from the page and the
lesson must still teach the topic completely.** Not mostly — completely. If the content defines a
term a later step uses, supplies a unit, licenses a move in a derivation, states a limit, or
answers a question the crux block raises, it is main line and it belongs in the step, however
charming it is. A learner who never presses one of these buttons must finish holding everything
the lesson promised.

`pedagogy.md` has the rules for choosing, placing and writing them, including how many is too
many; `page-spec.md` has the button markup and the registry.

## Building and delivering the first page

Design the arc, write every step to full weight, and ship the file. The skeleton created here is
permanent: later turns add windows and rewrite the inside of individual steps, but the steps
themselves and their numbers never change.

**One build may span more than one turn.** The page is built once and delivered once, which is
not the same as writing it in one reply. A lesson of any size may need several turns of writing
before the file is finished, and the environment may have to be told to continue. What must never
happen is the learner receiving a half-built page. Keep writing until the plan is fully realised
in the file, validate, and only then deliver. If a turn ends mid-build, say in one line that the
build is still in progress, so silence is not mistaken for a finished lesson.

**Read the page as the learner before delivering it.** This is the last step of the build and it
is not optional. Read the finished page from the top as somebody who does not know this subject
and has not seen it before, and answer three questions about it:

- Where would they stop and ask something?
- Where would they be reading without knowing what is being done right now, or why?
- Where did you move on because *you* already knew something, without putting it on the page?

Every place found this way is repaired before delivery. Repairing it here costs a paragraph;
leaving it costs the learner meeting the gap first, and it arrives back as a question that a
window then has to carry.

`build-notes.md` has the mechanical procedure — how to write the file in parts, how to edit it
without corrupting it, and the checks to run after every edit.

## The working loop

Once the page is delivered, every later turn begins with something the learner sends:

| What arrives | What it means | What you do |
|---|---|---|
| A question tagged with a step number | They pressed *ask* on that step | Add an entry to `ANSWERS[step]` — a new expandable window on that step |
| A question tagged as a follow-up inside an expand window | They asked again inside a window | Append to that window's `thread` array — the window becomes a running conversation |
| A question tagged as a follow-up inside a side window | They asked inside an aside you had placed in the prose | Append to that aside's `thread` array in `ASIDES` — same behaviour, different registry |
| A request tagged as wanting deeper explanation of a type | They pressed *explain more* and chose a category | **Rewrite the inside of that step**, merging old and new into one continuous read |
| An answer to a check question | They pressed *submit answer* on a check box | Judge it, fill in the check's `note` and its `answer` so the solution window opens |
| A follow-up tagged as asked inside a check solution | They asked again in the solution window | Append to that check's `thread` array — same behaviour as an answer window |
| A message tagged as post-lesson discussion | They typed in the discussion box at the foot of the page | Append the exchange to `DISCUSS` — their message and your reply render straight into the discussion panel, no button |
| A request tagged as an end-of-lesson handoff | They chose a next direction | Write the handoff document for that direction and deliver it as a file — see *Ending a lesson* |

**One incoming message becomes one window.** A learner who presses *ask* often types several
things at once, because they are stuck on one step and stuck on it in more than one way. Answer
all of it inside the single window that message creates, in the order they raised it, each part
naming what it is answering. Nothing is held back for a later turn and nothing is dropped to keep
the answer short.

Reply in chat with a note of two or three lines: what was added and where it now sits — the step
it hangs from, the window it went into, whether a step was rewritten. That is the whole reply. Do
not summarise the answer, do not lead with its most important point, do not re-explain it in
compressed form. The learner is working inside the page and is about to read the real version
there; a chat précis either duplicates it or quietly replaces it, and both waste the page. The
only other thing that belongs in the reply is technical: a filename that changed, a rebuild, a
check that failed, something you could not do and why.

### The rule that separates the two answer mechanisms

**Ask → new window. Explain more → rewrite the step.**

The distinction matters. A question is a side branch; it gets its own space so the main line
stays clean. A request for deeper explanation means the main line itself failed, so the main line
is what must change.

When rewriting a step, **merge, do not append.** Do not add a sub-panel underneath the original.
Dissolve the original content into the new explanation so the step reads as one continuous piece
from top to bottom. The learner will not scroll back up to reconcile two versions — assume the
rewritten step is the only thing they will ever read.

The step heading may be rewritten too, and should be if the original heading was a terse label. A
good heading is a full statement of what is being done and why, e.g. *"Fix a = 1 but leave h
unspecified, then substitute into the formula to find the distance at the far end"* rather than
*"Substitute h, expand brackets"*.

What never changes is the step itself: its id, its number, its position, and the fact that it
exists. Rewriting happens inside the box; the box and its number stay where they are.

A rewrite is a main-line step written against evidence, and it is the only edit that can break the
chain — so it is written to the same standard as the first build and against the whole chain, not
against the complaint alone. `pedagogy.md` sets out how: what to diagnose before writing, how to
build the new explanation out of what the learner demonstrably already holds, what each of the
categories is actually asking for, what has to survive the merge, and what to do when the same
step is expanded a second time.

### Content that must appear in the page and not in chat

- All teaching, explanation, examples, and worked solutions.
- Any checking question you want to ask the learner. Put it in a check box on the relevant step
  with its own submit button — do not ask it in the chat reply.
- Any correction of a misunderstanding, including corrections of the learner's terminology.
- Any summary, preview or shortened restatement of what you have just written into the page. Say
  where it is and stop; they will read the real version there.

Never teach in chat. Everything — answers, corrections, worked examples, even the discussion at
the foot of the page — lives in the file, which is the only thing the learner keeps.

## Ending a lesson: discussion first, then direction, then handoff

The foot of the page is not a menu. It is, in this order:

1. **A free-text box inviting discussion** of what was just learned — reactions, disagreements,
   half-formed connections, things it reminded them of. It comes first because it is the only
   part of the page that does not ask the learner to choose from a list, and because someone who
   has just finished usually has something to say before deciding where to go next.
2. **The concrete next directions**, as buttons.

Discussion is answered **in the panel itself**, not in chat and not behind a button. The reply
renders directly under the learner's message, because this panel holds no lesson content and an
answer here cannot be mistaken for the main line. It also means a learner who saves the file
keeps the whole conversation inside it — the lesson and everything said about the lesson in one
document. The register is conversational; the medium is still the page.

**Choosing a direction ends the lesson session.** When a direction button is pressed, write the
handoff document described below, so the next session begins holding everything this one
produced. The skill carries its own handoff rather than calling out to a separate one, so a
lesson can be closed properly anywhere this skill is installed. The button copies a tagged
request, not a command; the learner pastes it and the reply to it is the document.

A lesson handoff must carry:

- the filename of the page the learner is carrying away, for reference. The next session builds
  its own page: a lesson is never continued by appending to a page from an earlier session, and
  that holds for every lesson of a series without exception;
- the lesson skeleton — section and step numbers with their headings — since step ids are
  permanent and all later routing depends on them;
- which steps were marked asked, and — at the end of a lesson only — that every step was marked
  understood, since the direction buttons do not unlock until they are. Mid-lesson this is not
  knowable: marking happens in the learner's browser and never reaches the chat, so record what
  the session can actually see and leave the marks to travel with the page file, which they do as
  long as the storage key is unchanged;
- every question the learner asked, where its answer lives, and what it revealed about how they
  think — the clusters especially. A step that drew question after question was built thin, and
  what travels is the observation about the *building*: what that step was trying to carry, why
  one step could not carry it, what it might have been split into. That is judgement offered to
  whoever plans the next lesson in this area — not material to be taught again, and not an
  instruction about what the next lesson contains, which its own scoping or the series plan still
  decides. It is never a reason to alter the page it came from;
- the check questions posed, what the learner answered, and what had to be corrected;
- what the scoping established about their background, purpose, language and preferences;
- the chosen direction written as a lesson brief, not as a topic name.

### When this lesson is one of a planned series

The foot of the page changes shape. The discussion box stays where it is and behaves as it always
does — someone who has just finished lesson two still has things to say. What disappears is the
menu of directions: the direction was chosen when the series was agreed, and offering it again
invites the learner to re-litigate a settled plan. In its place sits one button naming the next
lesson in words, copying the same kind of handoff invocation.

Everything in the list above still travels, and with it:

- the position in the series and the full ordered list of lessons, so the next session can print
  the series rail without reconstructing it;
- what this lesson actually covered, set against what the plan said it would, because scope
  drifts;
- what the next lesson is entitled to assume the learner now holds — named by content, never by
  step number, since those numbers belong to a file the next session will not open;
- anything the plan assigned to this lesson that did not get taught, and why.

The last lesson of a series has no next lesson. It ends with the ordinary direction buttons, and
its handoff records that the series is complete and what was left unexplored.

### Writing the handoff document

Write a Markdown file that lets a session which was not present pick this lesson up cold.
Everything in the lists above goes into it, arranged so the next session can act rather than
read: what was taught, what the learner holds, where they struggled, where the page file is, and
the brief for what comes next. No "as discussed", and nothing that depends on anything which
lived only in the chat.

- **Do not restate the lesson.** The page holds the teaching; the document points at it by
  filename and records what happened around it. A handoff that re-teaches the material is longer
  than the page and less useful than it.
- **Open with an instruction block, not a title page.** The document has to work as the only
  thing in the session, so its first lines tell the next session what to do with it:

  ```
  # <lesson name> — handoff
  Open this session with the `interactive-lesson-page` skill and treat this document as the
  brief. The learner may have sent nothing but this file; begin from it.

  page: new
  subject: next part of <series name> — lesson 3 of 5
  page file: <filename>.html
  ```

  The two routing lines are read together and are independent of each other — see *Resuming from
  a handoff document*. `page:` is either `new` or `continue the attached file`, and the second
  value also asks the learner to bring the page file. `subject:` is either
  `next part of <series name> — lesson <n> of <N>` or
  `new topic — <topic>, chosen at the end of <previous lesson>`. A lesson of a series that was
  interrupted while still being worked on is the combination of `continue the attached file` with
  its ordinary series subject line; there is no separate value for it.
- **Redact.** Nothing personal beyond what the teaching requires: no contact details, no
  credentials, no third-party names the conversation happened to pick up.
- **Deliver it as a file**, written to the outputs directory and presented for download, since
  the learner carries it into the next session by hand. Name it obviously:
  `<lesson-slug>-handoff.md`.

Then say two things in chat, briefly, and stop. What the document contains, and what to do with
it — because the instruction block inside the file is addressed to the next session's model, and
the person carrying it needs telling separately. The two cases differ and must not be conflated:

- **Ending a lesson**, whether by a direction button or the next-lesson button of a series: take
  the summary file into a new chat, drop it in, and press enter. The lesson page is theirs to keep
  for review and is **not** needed there, because the next lesson is built as its own page.
- **Handing off mid-lesson**: download the summary file **and** this lesson page, open a new chat,
  drop both in, and press enter. Work continues on the same page, so both have to travel.

The handoff is the last thing in the session; nothing follows it.

## Handing off in the middle of a lesson

A lesson runs for many turns, and a session that fills up while it is still being worked on loses
everything that was not written down. There is no gauge to read here — you cannot measure how
much room is left — so use the visible signals: many turns of editing a large file, several
rewrites behind you, a lesson still far from its last section. When those line up, say so in one
line and offer a mid-lesson handoff. Do it early; a handoff written with room to spare costs a
minute, and one that never gets written costs the lesson. Write it immediately whenever the
learner asks — the request arrives as ordinary chat with no tag, since the page carries no button
for it, and it is honoured on any wording. This is operational rather than a question about the
lesson, so chat is where it belongs.

It is the same document with three differences: `page: continue the attached file`, an
instruction to bring the page file into the next session alongside it, and a record of exactly
where the learner stands — which steps are marked, which windows exist, what was being worked on
when the session ended. If the lesson belongs to a series, its subject line and the series
material travel unchanged. The next session opens the skill, takes the uploaded page, and carries
on in the working loop without rebuilding anything.

## Hard constraints

- **Never add, remove, or renumber a step after the page is delivered.** The learner's progress
  state is keyed to step ids and they navigate by position. Content is added in windows; the
  inside of a step may be rewritten; the skeleton is fixed.
- **Never deliver a page that is not finished.** A build may take several turns. The learner
  receives it complete or not at all.
- **Never change the storage key of a lesson in progress.** It is what carries the learner's
  marked steps across every rebuild of the file.
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
- **Never move a window's content into the main line, and never restructure the page in response
  to questions.** Once delivered, the main line changes through one door only: an *explain more*
  request rewriting the step it was pressed on. Questions are answered in windows and stay in
  windows. What the questions revealed travels to the next lesson through the handoff.
- **Never restate in chat what the page now says.** The chat note reports what changed, where it
  sits, and anything technical. Every word of teaching lives in the page.
- **Never put anything a later step or a later lesson needs inside an aside.** Optional means
  optional: the page must still teach the whole topic with every side window deleted.
- **Never open a series the learner has not agreed to, and never propose one the subject does not
  force.** A division that does not fall at a joint in the argument is one long lesson cut in
  half. And never continue a series by appending to the previous lesson's page: each lesson is
  its own file with its own storage key.
