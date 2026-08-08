# Teaching skills: `interactive-lesson-page` and `ground-up-teaching`

Two skills that change how a language model teaches — from producing correct explanations to
building lessons a beginner can actually walk through.

They were not designed in the abstract. They were written, and repeatedly corrected, while
using them to learn real subjects from zero.

📄 [Read this as a page](https://bordinrattanasiri.github.io) ·
🔎 [Where these skills came from](https://bordinrattanasiri.github.io/origin.html) — one lesson,
cut into 25 steps, and the eighteen questions that produced most of the rules below.

---

## Why they exist

Ask a capable model to explain something and you get a competent summary: accurate, dense,
ordered by topic, and close to useless if you are starting from nothing. It states results
without their origins. It defines terms before those terms do any work. It refers to things you
have not met yet. It leaves the connective tissue for you to infer. You read it, feel that you
understood, and find later that you cannot use any of it.

The failure is not one of knowledge. The model knows the subject. The failure is that
**explaining and teaching are different activities**, and nothing in a plain chat request asks
for the second one.

For most people the available response to this is nothing. You cannot fine-tune the model. You
cannot design the interface. You can only ask better questions, one at a time, and start over
tomorrow. A skill is the one lever that is actually within reach: a reusable specification of
*how* to teach, so that the next subject arrives in a form that has already been shown to work,
instead of depending on how well you happened to phrase the request.

That is the wider claim behind this repository. Using a general-purpose chat model to study
something seriously is still much harder than it should be, and the missing piece is rarely
capability — it is method and workflow. What is needed looks less like a conversation and more
like an application built for the shape of the subject being learned.

---

## The observation that shaped the design

The design rests on an asymmetry between how a model holds a problem and how a person does.

A model holds the whole block at once, evenly and sharply. It can see everything it has said and
everything it is about to say, and it can pull all of it into a single act of reasoning.

A person cannot. Human working memory has one narrow point of sharp focus, surrounded by
material that fades outward — present, but blurred to different degrees, and decaying as
attention moves on. Read a section and understand it, and what survives into the next section is
a *concept*, not the wording, not the details, and often not the thread. In a genuinely difficult
subject you can be following the procedure correctly and simultaneously lose track of what step
you are on, why this step exists, and where you are in the whole arc.

Almost every rule in these skills is a consequence of taking that seriously:

- **Write for a narrow, moving spotlight.** Whatever a sentence depends on must be inside the
  reader's focus at the moment they read it, not four paragraphs back.
- **Never reference by number.** "As we saw in §3.2" is worthless to someone who does not
  remember section numbers — and nobody remembers section numbers. Earlier material is
  referenced by carrying its substance forward in a clause.
- **State the position constantly.** What is settled, what is still open, what this part is for.
  A reader who knows where they are can follow much harder material than one who does not.
- **One thread.** Every part is tied into a single line of argument, so the shape of the whole
  stays visible from any point inside it.
- **Assume nothing is still on screen.** Not the definition, not the variable, not the reason
  this quantity mattered.

---

## Architecture before prose

The largest determinant of whether a lesson works is fixed before a word of it is written.

Both skills therefore force the arc to be designed first: every step, what it settles, what it
needs from earlier steps, what it hands to the next. A lesson planned one step at a time drifts —
the third step arrives needing something the first should have established, and by then the first
cannot be repaired.

The rule that keeps the arc honest: **a section exists because the previous section left
something undone.** If nothing forces it, it is enrichment rather than structure, and it either
becomes optional material or it goes. Each step carries one clear key point, and the points do
not overlap, so that working through the lesson is stepwise and a question asked in one step gets
answered within that step's scope instead of bleeding across the others.

---

## Completeness is not deferred to questions

A tempting design is to teach lightly and let the learner ask for the rest. It does not work.
Anything a learner had to ask for was usually a paragraph that should have been written, and
material that accumulates in follow-up answers is invisible to everyone who does not ask.

So the first delivery has to be complete. In `interactive-lesson-page` this becomes a hard
invariant: **the page as first built is the lesson.** It is what the learner works inside for the
whole session, and questions only surface gradually as they read — which is precisely why the
initial build has to be made with real care rather than sketched and patched. Once delivered, its
main line does not change in response to questions. Answers live in their own windows attached to
the step they belong to; the main line changes only through an explicit *explain this further*
request on a specific step.

---

## The artefact is the classroom

In the page skill, everything lives in the HTML file: the teaching, the answers to questions, the
corrections, the check questions, and even the discussion at the end of the lesson. Nothing is
taught in chat. Chat carries a two-line note saying what changed and where it now sits.

The reason is simple. The file is the only thing the learner keeps. A brilliant explanation that
exists only in a chat log is gone the moment the conversation scrolls, and a learner who saves the
page should find in it the complete lesson and every conversation that happened around it.

In the chat skill the conversation *is* the artefact, which is why the explanation is delivered
one movement per message rather than as a single long answer. A carefully built explanation
dumped into one message defeats itself: the reader loses the thread somewhere in the middle, and
by the time they think to ask, the place where they lost it has scrolled away.

---

## The two skills

### `interactive-lesson-page`

Builds one self-contained HTML page that teaches a topic from zero, then grows it across many
turns as the learner works through it.

The workflow: scope the lesson with a few questions and confirm → design the whole arc → build
the page → then a working loop, where the learner marks steps understood, asks questions on
individual steps, or requests deeper explanation, and each of those routes to a different kind of
edit. The page carries a progress rail, a map of the argument, a per-step signpost of what was
settled and what was not, a sidebar of terms and symbols, optional enrichment windows, check
questions, and a closing panel that ends the session with a handoff document for the next one.

Files: `SKILL.md` (orchestration and routing), `references/pedagogy.md` (how to write the
teaching — the larger half of the job), `references/page-spec.md` (functional and markup
contract), `references/build-notes.md` (build procedure and validation).

### `ground-up-teaching`

The same doctrine with no page, for subjects that do not need the page's apparatus.

The workflow: a few scoping questions → a posted map of the entire planned explanation → then one
movement per message, continuing as the learner responds, with questions answered where they
arise and the thread returned to afterwards → a closing offer → a handoff document.

File: `SKILL.md`.

The two are siblings on purpose. Where a rule exists in both, it says the same thing in the
vocabulary of its medium.

---

## Design invariants

These are settled decisions, most of them made after something went wrong without them.

1. The delivered page is fixed. Questions never restructure it; only an explicit request to
   expand a step rewrites that step.
2. Nothing is taught in chat.
3. Scope is agreed before building; the build waits for confirmation.
4. A multi-lesson series is proposed only when the subject forces one, and only exists once the
   learner agrees. Breadth alone is not a reason.
5. Enrichment is optional by construction: delete every optional window and the lesson must still
   teach the topic completely.
6. Prose, not fragments — written register rather than spoken, complete sentences, concrete
   example before symbol, always.
7. Teaching happens in the learner's language, with the English term given at first appearance
   for anything the argument is built on, then one form held consistently.
8. Claims carry their status when they are not plain verified fact: illustrative reconstruction,
   simplification made for teaching, or genuinely contested ground.
9. Facts are checked before the arc is planned, and arithmetic and code output are verified before
   they are published.
10. Each skill carries its own handoff, so a session can be closed and resumed by dropping one
    file into a fresh conversation.
11. Nothing is subject-specific. The rules are written in the vocabulary of quantitative subjects
    because they are hardest to satisfy there, and translated explicitly for subjects without
    equations — code, law, history, music.

---

## Using them

Each skill is a folder: a `SKILL.md` and, for the page skill, a `references/` directory. Install
them the way your Claude surface installs skills — the zipped folder in each release is already
in the expected shape. Consult Anthropic's current documentation for where skills are uploaded,
since that has moved more than once.

Then simply ask to be taught something. The skill takes over from there: it will ask what you
want the subject for, how deep to go, and what you already hold, and then build.

---

## Status

Both skills are in active use and still changing. They encode a particular view of what teaching
is, tested against real attempts to learn real subjects — which means the rules that look
arbitrary usually are not, and the ones that look obvious were usually learned the hard way.

Contributions, disagreements, and reports of where the doctrine breaks are all welcome.
