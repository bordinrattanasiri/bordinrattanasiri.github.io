# Pedagogy: how to write the lesson content

Teaching a beginner is not summarizing a topic. It is building a chain where every link is
attached to a link the learner already holds, in an order they can actually walk.

This document is the writing half of the `interactive-lesson-page` skill. It governs the text
of the main steps, the expandable answer windows, the threads inside them, and the check
solutions. The doctrine below was developed and corrected in live use with a learner who had
zero background in the subject; most rules exist because their absence caused a real failure.

## The prime directive: write for a narrow, moving spotlight

The single most important fact about your reader: **their working memory is not yours.**

You hold the entire conversation at uniform clarity. They do not. Their attention is a narrow
bright spot with blur falling off in all directions. Details they processed three paragraphs
ago have already evaporated — what survives is a compressed *understanding*, not the words,
not the numbers, and definitely not the section numbers.

Everything below follows from this.

**Never refer to earlier material by label alone.** Not "the four pieces from §3.1", not "as
we saw above", not "recall the formula". Carry the content with you every time:

- Bad: "This is the second of the four pieces we assembled earlier."
- Good: "This is the distance at the far end of the interval — one of the two quantities we
  are going to subtract from each other."

**Name every intermediate object by what it *is*, every time you mention it.** A learner deep
in algebra loses track of what they are computing and why.

- Bad: "The new form we got is 2 + h."
- Good: "The new form of the average-rate expression, now that we have cancelled, is 2 + h."

**Keep the reader oriented.** In any explanation longer than a few paragraphs, keep answering
three questions in the prose itself: what are we doing right now, why does it need doing, and
where does its result go next.

**Assume nothing is still on screen.** If a rewrite or expansion is long, the reader will not
scroll back up to reconcile it with what was there before. Merge new material into the
existing text so it reads as one continuous piece, rather than appending a block that assumes
the reader still remembers the top.

## Write in complete sentences

Prose, not fragments. The standard is a book: something a reader can move through without
having to reconstruct what the writer left out.

Chains of clipped phrases and bullet lists of bare noun-phrases look organized but transmit
almost nothing to someone without the background to expand them. A bullet reading
"start at time a → distance s(a)" is meaningless to a beginner; the same content as two full
sentences explaining what the arrow means is clear.

Use bullets only for genuinely parallel enumerations, and give each bullet a full clause.
Use tables for anything with structure — they are the most effective format in this skill
(see below). Default to paragraphs everywhere else.

### The register is written, not spoken

Complete sentences are not enough by themselves — a transcript of someone talking is made of
complete sentences too. The page is a book, so it is written in the voice of a book: composed
expository prose that holds together when read straight through, rather than the voice of someone
improvising aloud in front of a class.

What this rules out is conversational scaffolding, not warmth. No greeting or sign-off inside a
step, no "okay, so", no "right?", no "let us see", no exclamation mark doing the work of
enthusiasm, no rhetorical question asked only to fill the gap before its own answer. Address the
reader where the address does work — "notice that the leftover term is still sitting there" — and
never as filler.

The rule is sharper in languages that carry the difference in the words themselves, and Thai is
the clearest case, so it is worked out here as the example of what the rule means anywhere. A Thai
lesson is written in written Thai: no ครับ or ค่ะ, no sentence-final particles used for tone (นะ, สิ,
ล่ะ, เลย), none of the connectives that belong to speech rather than to writing. Every language the
page might be written in draws this line somewhere in its own vocabulary; find where, and stay on
the written side of it.

The test is to read a paragraph aloud. It should sound like a well-made book being read, which is
unhurried and put together in advance — not like a person thinking out loud, which is where the
fillers come from.

## Design the arc before writing a word

Everything above is about sentences. This section is about the thing that decides whether good
sentences will help at all.

A lesson is a chain of positions, not a collection of things that are true about the subject.
Before writing, list the sections, and next to each write one sentence: *what does this section
settle that the previous one left open?* If a section has no answer to that question it is not a
section — it is enrichment, and it belongs inside a step.

Then do the same one level down. Write the key point of every sub-step as a single sentence,
and read the whole list for collisions. **Two sub-steps must never have the same key point.**
When they do, the second one reads as a stall: the learner recognises the material, cannot tell
what is new, and loses confidence that they were following properly. Merge them, or re-cut the
boundary between them.

### How finely to cut it

A sub-step is one idea that a learner could plausibly get stuck on by itself. That is the whole
criterion, and it is what makes a per-step *understood* or *ask* button mean anything: a learner
can say "this one" and be pointed at exactly the thing that did not land.

Nothing here is decided by counting. The subject decides how many sections it has, how many steps
each one needs, and how far each step has to go; a step is right when it carries its one idea
completely, not when it reaches a length. What can be said without counting anything is where the
cut has gone wrong. A step is too coarse when you cannot state its key point in one sentence
without an "and". It is too fine when its whole content would fit in a single paragraph, which
means it is an outline entry that was never written — either write it properly or fold it into
its neighbour. And two shapes are always wrong however they are cut: a step that presents
something and stops, leaving the reader with a table and no reading of it, and a step whose only
job is to declare terminology that a later step will actually use.

### Make the connections visible instead of leaving them to be inferred

Three devices carry the through-line, and all three are cheap:

- A **lesson map** near the top — one line per section saying what it settles, so the learner can
  place themselves at any moment.
- A **section lede** — two or three sentences at the head of each section saying where the story
  is, what this section adds, and what it hands to the next.
- A **crux block** at the foot of every sub-step — what is settled now, what is still missing, and
  what that gap forces next. This is the most useful structural element in the whole page, because
  it keeps the thread visible at the scale the learner actually reads at, and because writing it
  exposes any step that does not advance the argument.

### Scope discipline, and why it starts here

Because each step owns exactly one key point, a question asked on a step can be answered inside
that step's remit and stopped at its boundary. If answering properly seems to require material
belonging to a later step, that is evidence the arc is wrong — not a licence to spill forward. Say
what can be said here, name the boundary in one clause, and let the later step do its job.

### The sides a complete treatment covers

A beginner who says they understand a topic usually means they can follow a procedure. A
beginner who *actually* understands it can say where the problem came from and when the method
fails. Aim for the second. In practice a full lesson carries all of these, distributed across
the arc rather than heaped in one place:

| Side | What it answers | Where it usually goes |
|---|---|---|
| Origin | Why did anyone need this? | First, as a concrete situation |
| History | Who got stuck, and on what? | After the difficulty is felt, never before |
| The difficulty | What exactly cannot be done yet? | Immediately after the easy case is done in full |
| Principle | What is the idea that unlocks it? | At the turn, once the difficulty is undeniable |
| Procedure | What do I actually do, in order? | Broken into one step per decision point |
| Reasoning | Why is each step allowed? | Inside the step it licenses, never as an appendix |
| Support | What does the procedure silently assume? | Before it is silently assumed |
| Examples | What does it look like on real numbers? | Interleaved, not gathered at the end |
| Limits | When does this stop being true? | Last, and stated plainly |

The row that gets skipped most often is **support**. In the derivative lesson it was: where the
formula for the data came from, what a model is, what acceleration means, and why its units have
seconds in them twice. None of that is calculus, and all of it had to exist before the calculus
could be followed. The learner's questions found every one of those gaps.

### One warning about history

History is enrichment that earns its keep only when it names the same difficulty the learner has
just felt. Placed before the difficulty it is decoration and the learner skims it. Placed after,
it does real work: it tells them their confusion is the historically correct confusion, and it
names the pressure point the rest of the lesson is going to resolve.

### Enrichment the learner may skip: the side window

Some of what research turns up is too good to drop and wrong to put in the chain. It is adjacent
rather than load-bearing: the life behind a name, the same idea working in a field this lesson
never mentions, the topic at a different scope or layer or case from the one being held in focus,
a sub-topic that would distort the arc if it were promoted to a step, the wrong answer that stood
for a century. The page carries this as a named button inside the prose that opens a window.

**What may go in one.** Side stories and the world around the topic; trivia in the literal sense,
things worth knowing that nothing depends on; the same subject seen at another scope, layer or
case; the sub-topic the boundary deliberately left out. **What may not:** anything a later step
reads back. If deleting the window would make a later step limp, it was never an aside — it was
main line wearing a costume, and it goes into the step.

**Where it goes.** At the sentence it attaches to, mid-paragraph if that is where the connection
lives, so the learner meets it at the moment it is interesting. Not gathered at the foot of the
step, which turns asides into a reading list nobody opens. Never inside the crux block, which
carries the argument and stays pure signposting.

**How it is written.** Full sentences like everything else, and lighter in pitch — this is the
one place in the page where being entertaining is the point — but not lighter in register: still
written prose, still the voice of a book, only a book enjoying itself. A few paragraphs, shorter than a
step. Self-contained, because the learner opens it out of the reading order: restate what it
attaches to in its own words instead of pointing at the prose around it. And bound by the same
sequencing rules as everything else, which asides break more often than any other content type:
it may not use machinery the learner has not met, and it may not reveal a result that a later
step — or a later lesson in the series — exists in order to arrive at. A fun fact that gives away
the ending costs more than it adds.

**How many.** Few. Most steps carry none, and a subject whose surroundings are thin is entitled
to have none at all; a page with one on every step is decorating rather than teaching. The
question before building one is not "is this related?" but "will they be glad they pressed it?" —
if that needs an argument, cut it.

A remark of one or two sentences that genuinely belongs in the flow stays in the flow, as a
`.trivia` line. The window is for material with enough body that leaving it inline would
interrupt the chain.

## Structure of a lesson

This shape worked; use it as the default spine.

1. **A concrete situation first.** Not a definition. A ball rolling down a ramp with four
   measurements written in a table. Something the learner can picture and that already
   contains the problem the concept solves.
2. **The easy question, answered in full.** Do the thing they already know how to do, with
   real numbers, so the machinery is familiar before it gets abstract.
3. **The hard question, stated plainly, and left unanswered for now.** This is what creates
   the need for everything that follows.
4. **Name the variables, in a table, with units and with the value they take in this example.**
5. **Assemble the formula piece by piece,** explaining what each piece means and where it came
   from, rather than presenting it finished.
6. **Substitute real numbers, several rounds,** showing every arithmetic step.
7. **Confront the breaking point** — the place where the naive approach fails — and explain
   *why* it fails in terms of what the operation means, not by citing a rule.
8. **Generalize with algebra,** then verify the general result against the numbers already
   computed.
9. **State the answer and give it its name.**
10. **Say what should be carried away** — the one conceptual reframing, not a recap.

This spine is the default, not a ceiling. A longer lesson repeats the shape at a smaller scale
inside each section: a section also opens with the situation it inherits, does the thing it can
do, hits what it cannot, and hands the gap forward.

### Translating the spine to a subject without equations

The spine is written in the vocabulary of a quantitative subject because that is where it is
hardest to satisfy. Every item has a counterpart everywhere else, and the work is to translate
it rather than to drop it.

**Real numbers** become the one concrete case the lesson follows all the way through: a specific
input traced through a specific implementation in a programming lesson, one statute applied to
one set of facts in a law lesson, one passage analysed bar by bar in a music lesson. The
requirement is not arithmetic, it is that something particular is carried from the beginning to
the end instead of a general description.

**Units** become what each object *is* — its type, its scope, what it is a count or an instance
of. In code that is types and shapes; in an argument it is what a claim is a claim about. The
purpose is the same in both: a result whose kind is wrong is wrong regardless of how it was
produced, and the learner should be able to see that without checking the details.

**Substituting several rounds** becomes running the same procedure on a second and a third case,
including one where the obvious move fails. **Generalising with algebra** becomes stating the
general rule only after the concrete case has been walked — the ordering is what matters, not
the notation. **The breaking point** always exists somewhere: the input the code does not handle,
the case the doctrine was not written for, the passage the rule does not describe.

A lesson that has no numbers in it should still be recognisable as this spine. A lesson that
skips these items because the subject "isn't mathematical" has skipped the parts that do the
teaching.

### The same shape one level up: a series

A series is the same chain with whole lessons as its links. Each lesson settles something the
previous one left open, and if you cannot say in one clause what a lesson settles that its
predecessor did not, it is not a lesson — it is a section of the one before it.

That test is also how you decide whether a series should exist at all, so run it on the proposed
division before offering it to anyone. If two of the lessons settle the same kind of thing, or if
one of them exists only because the material was getting long, there is no chain there and it is
one lesson. And each link has to be whole on its own: someone who stops after lesson two should
be holding a complete idea, not two thirds of one. A division made where the page got long cuts
through the middle of an argument and leaves both halves unable to stand.

Three things change once a lesson has a lesson behind it.

**The gap is days, not paragraphs.** The narrow-spotlight problem stops being about the previous
page and becomes about the previous week. Whatever the earlier lesson established, this one
re-establishes in its own words at the point where it is used — briefly, as a statement of the
position rather than a recap. Never "as we established in lesson one": they do not have lesson
one open, and they may not have it in memory either.

**The opening is not a fresh start.** Lesson one opens with a concrete situation. Lesson four
opens with the concrete situation that the previous lesson could not handle — the same move one
level up, and the reason the learner is here at all.

**The limits belong to the series as well as to the lesson.** Close by saying, in words, what
this lesson leaves to the next one. That is the series' version of *what is still not settled*,
and without it a lesson that stops mid-subject reads as an unfinished lesson rather than a link.

## End every movement with a three-line ledger

At the close of each sub-step — and at the close of each movement in prose teaching — answer
three questions explicitly, in the text, in this order:

- **what is settled now**, named by content rather than by label;
- **what is still not settled**, stated as a concrete lack rather than a vague "there is more";
- **what that lack forces us to do next.**

This is worth its space three times over. It is the strongest available defence against the
narrow-spotlight problem, because it re-anchors a reader who arrives with only a compressed
memory of the last few paragraphs. It converts a sequence of topics into an argument the reader
can feel moving. And writing it is a design test on yourself: a step whose "what is still not
settled" line is empty does not motivate the next step, and a step whose "what is settled" line
repeats the previous step's is a duplicate that should be merged.

Keep each line to one clause. This is a signpost, not a summary — a summary invites the reader
to skip the step.

## The techniques that do the most work

### Substitute into a real situation; do not explain in the abstract

When the learner did not understand why acceleration has units of metres per second per
second, the layered prose explanation failed. What worked was a table of a car pulling away
from a traffic light — a stopwatch column and a speedometer column — and then pointing at
which column each "second" came from.

**Rule: when an idea won't land, stop rephrasing it and build a scenario where the reader can
see the parts sitting in separate cells of a table.**

### Tables that show where each thing lives

Three table shapes did most of the work:

- **Variable tables**: symbol, what it means (a full clause), value in this example, unit.
- **Situation tables**: the real-world scenario broken into columns so an abstract distinction
  becomes a visible difference between two columns.
- **Verification tables**: the new general result recomputed against numbers derived earlier
  the long way, one row per case, so the reader can see the two columns agree.

Verification tables are especially valuable. They convert "trust me" into "check it yourself"
and they re-anchor the reader who has lost the thread during the algebra.

### Always show units, and unpack the strange ones

Attach units to every quantity, including intermediate ones. When a unit is composite,
explain what it is a record of — "seconds squared" is not a thing that exists in nature, it is
a fossil of having divided by time twice. Show the division chain that produces it.

Then show that units can be used as a self-check: if the units of a result come out as the
wrong kind of thing, the calculation is wrong regardless of the arithmetic.

Where a subject has no units, the same discipline applies to what each thing *is*: the type a
function returns, the scope a rule governs, what a number is a count of. Name it every time it
appears, and use the mismatch the same way — a result of the wrong kind is wrong before anyone
checks the details.

### Two-sided sanity checks

Where a result can be reached by a second independent route, show that route and show the
answers agree. Deriving a formula from data and then finding it matches a law from another
field is powerful evidence to a learner, and it converts a formula from an assertion into
something that fits into the world they already know.

### Name the limits honestly

Say what a result does *not* cover. The model fits the four measured points but is not proven
by them; the formula holds while acceleration is constant and breaks when air resistance
enters. Naming the boundary makes the valid region trustworthy rather than making the whole
thing feel shaky.

## Handling the learner's own contributions

### When they are right, say so first, then extend

Confirm plainly before adding anything. Then use their answer as the launch point for the next
insight rather than restating it. When the learner observed that the constant-speed case needs
no limit at all, the right move was to agree and then name the underlying pattern: the leftover
`h` term in the average is the fingerprint of acceleration, and the limit exists to remove it.

### When they are partly wrong, correct the specific word

Do not soften a factual error into vagueness, and do not rewrite the whole thing. Identify the
exact term that is off, correct it, and confirm everything around it that was right. When the
learner called `g` a force, the correction was one sentence — `g` is an acceleration, weight is
the force — followed by confirming that their "g-force" association was otherwise correct.

### When you misread them, say so plainly

If they point out that you answered a question they did not ask, acknowledge it directly and
move on. Do not over-apologize and do not silently pivot.

### Read what they typed, not what you expected

The learner wrote "15 m/s" and was told about the first division — which was already sitting in
the "/s" they had written. Check whether the units or notation in their message already
contain the step you are about to explain.

### Verify their numbers before responding

If the learner submits a derived result, actually compute it before answering. Run the
arithmetic. Do not eyeball algebra and declare it correct.

## Tone

Informational, warm, unhurried. Enrichment is wanted: historical background, adjacent
phenomena, why the units are shaped that way, what happens in the extreme cases. Those
tangents were explicitly appreciated.

What is not wanted:

- Chat-register filler, cheerleading, or performative enthusiasm. The voice stays written rather
  than spoken throughout — see *the register is written, not spoken* above.
- Prompting the learner onward ("ready for the next part?", "shall we continue?"). A learner
  who understands moves on by themselves; one who doesn't asks another question.
- Ending an explanation with a hook or a cliffhanger.
- Socratic quizzing as the opening move with a beginner. A checking question is welcome
  *after* a full explanation, not instead of one.

Match the learner's language. If they write in Thai, teach in Thai.

### Terms keep their English

A lesson taught in another language carries one extra duty, because the words a field actually
uses are not always the words a translation produces, and because the learner will eventually
read about this subject in English.

Every term the argument is built on — the load-bearing vocabulary, not every noun in the lesson —
gets its full identity at its first appearance: the formal term in the learner's language, the
transliterated form if the field uses one, any other name it commonly goes by, and the English in
brackets. The example has to be shown in some language other than English for it to show anything;
in Thai it reads as *ค่าคงตัวของการสลายตัว หรือที่มักเรียกทับศัพท์ว่า ดีเคย์คอนสแตนต์ (decay constant)*, and the shape
is the same in any language: full identity once, then one form held.

After that first appearance, pick one of those forms and hold it for the rest of the lesson.
Which one is a question about the field rather than about purity: where practitioners speak in
transliteration, the transliteration is the honest choice and a formal translation reads as
invented; where the formal term is what people actually say, use that. What is never acceptable
is drifting between forms, because a learner has no way of knowing that two words are the same
thing, and the lesson silently doubles its vocabulary.

Every term treated this way also goes into the sidebar reference panel, in both languages — see
`page-spec.md`. The panel is where a reader looks when a word has evaporated, and a term that
exists only in the paragraph that introduced it will evaporate.

## Sequencing rules

**Never cite material the learner has not reached yet.** If a later result would help, either
derive it inline right there or leave it out. Citing forward is worse than useless — it makes
the learner feel they missed something.

**Do not do the next step's job.** An expansion of one step should stop at the boundary where
the following step takes over. Overlap makes the next step feel redundant and confuses the
sense of progression.

**Do not introduce a concept before the point where it is used.** A step whose only purpose is
to declare terminology in advance will be redundant by the time the terminology gets used.
Fold the explanation into the step where the thing does work. Meaning is clearest at the moment
of use.

**Do not spoil your own payoff.** When a result can be reached by a second independent route —
a physical law, a second derivation, a known answer — that route is a verification and belongs
at the moment the first route arrives, where it converts the answer from a claim into a
confirmed fact. Placed earlier it deflates everything between: the learner reads the derivation
knowing the answer already and treats it as a formality. The test is whether the earlier step
still has work to do without it.

**Say when something is only an observation.** If a pattern has been spotted in five rows of a
table, say that it is a pattern spotted in five rows, and say what would be needed to establish
it. The learner then knows why the algebra that follows exists. Presenting an observation as a
result steals the motivation from the step that proves it.

**Mark the status of anything that is not plain verified fact.** The page is the only source the
learner has — nothing in this skill sends them to a book or a website — so a claim they cannot
check has to arrive carrying its own status, in one clause, without hedging every sentence into
mush. Three kinds need it.

*Illustrative reconstruction.* The apple, the flash of insight in the bath, the conversation that
supposedly settled it. Most of these are stories told about the work rather than records of it,
and they are worth telling for what they make visible — but told as *the story that gets told*,
not as something documented. Where the record does exist and is specific, say that instead: a
dated letter is stronger material than a legend and costs the same words.

*Simplification made for teaching.* Frictionless, ideal, infinitely divisible, "assume the input
is well formed", "the compiler does more than this". A learner who is not told will believe the
simplified thing is how the world works, and will meet the correction later as a contradiction
rather than as a refinement. One clause naming what was idealised is enough, placed where the
simplification is made and not in a footnote at the end.

*Genuinely unsettled ground.* Where more than one account is held by people who know the field,
say so and give the shape of the disagreement in a sentence. Manufacturing a consensus is the
worse error: it teaches the subject as smaller and more finished than it is, and the learner is
defenceless the first time they meet the argument in the wild.

The bar is not universal hedging — that would be its own dishonesty, since most of a lesson is
settled and should be stated flatly. It is that where you would not be able to show your working
if challenged, the sentence says so.

**Answer "so what?" inside every step.** A step that presents data or a manipulation and stops
leaves the reader stranded. After a table, say what can now be known from it, what still cannot
be known, and what that gap forces you to do next.

## Where a check question belongs

A check is not a quiz sprinkled over the lesson. It goes where getting it wrong would be
expensive, and it earns its place in three situations.

**At a convergence.** Several things that were introduced separately have just come together and
the learner has to hold the relationship correctly to go on: the point where the pieces of an
equation are assembled, where two values have to be seen as related rather than merely both
present, where a mechanism finally has all its parts. These are the moments where a
misunderstanding does not stay local — it corrupts everything after it — and they are the single
best place to ask.

**Where a result has to be produced, not recognised.** The learner should be able to compute the
value, apply the rule to a case they have not seen, predict what the code prints, name which of
two forces is doing the work. Recognition is not the same skill and does not show what this
question is asking about.

**Where the point of the thing can be caught wrongly.** A law, a definition or a principle that
has an obvious misreading standing next to it: the check exists to catch that misreading here,
where it can still be corrected cheaply.

Two rules constrain all three. A check must be answerable from the step it sits on and what came
before it, never from material still ahead — a check that requires the next section is a
sequencing error dressed as a question. And a check never introduces content: if the only way to
answer is to learn something the lesson never taught, the teaching is missing and the question is
hiding it.

None of this is subject-specific. In mathematics the convergence is usually where a formula is
assembled or a value first has to be found; in physics it is where a law's point can be caught
wrongly; in programming it is where the trace has to be predicted rather than read; in law or
history it is where a rule or a cause has to be applied to a case that is not the worked one.

## Diagnostics you can run on a finished draft

These are cheap, mechanical, and each one caught a real defect.

**Where would the questions cluster?** Ask it of the draft before anyone sees it: which step is
carrying so much that it would draw question after question? That step is not a hard step, it is
a missing section, and while you are still drafting the repair is to make it three or four
main-line steps instead of one. The same count is worth taking after delivery, but not as a
repair — the page stands as it was built, and what the cluster showed travels in the handoff as
an observation for whoever plans the next lesson.

**Is any step thin?** Read the steps for weight rather than measuring them. A step whose whole
content fits in one paragraph, sitting among steps that run to several, is an outline entry that
never got written. Write it or fold it into its neighbour.

**Does any sentence refer to a step by number?** Search for the section marker in the body text.
The correct count is zero. Every reference must carry the substance instead.

**Would the lesson survive with every side window deleted?** It has to. Side windows exist from
the moment the page is built and the learner may open none of them, so anything essential that
has drifted into one is invisible to most readers. If deleting a side window would remove
something the lesson needs, that content is main line and it goes into the step.

This test is about side windows only. The answer windows are a different thing entirely: they do
not exist when the page is built, they are created by one learner's own questions afterwards, and
they are never deleted. The main line does not depend on them because it was finished before they
existed. The rule that keeps content out of them is a drafting rule, not a test — never ship a
step you could only explain properly if asked.

**Does every step's key point appear exactly once?** Read the list of key-point sentences alone,
without the prose. Collisions are visible in seconds this way and nearly invisible inside the
text.

**Read the whole page as the learner.** The last diagnostic, and the one that catches what the
others cannot, is described as the closing step of the build in `SKILL.md`: read the finished page
from the top as somebody who does not know the subject, and repair every place where they would
stop and ask, would not know what was being done or why, or would meet something you skipped
because you already knew it.

## Answering follow-up questions

A follow-up is not a standalone mini-essay. It has a location in the lesson.

Before writing, work out three things: which already-covered idea this attaches to, what the
answer adds that the main line does not already contain, and where it hands back to the main
line. Then write it so that it reads as part of the same continuous story.

Restate the anchor idea in the answer itself rather than pointing at it, for the same reason as
the prime directive: the learner no longer has the earlier wording.

When a question exposes that the original explanation was inadequate, the fix is to explain it
properly here in full — merged and continuous — not to patch it with a paragraph that assumes
the flawed original is still fresh.

## Rewriting a step when the learner asks for more

*Explain more* is the only door into the main line after delivery, and what comes out of it is a
main-line step. Everything in this file applies to it unchanged: written to the standard of the
first build, one key point, concrete before abstract, closing on a crux block that hands forward.
The one difference is that this time you are writing against evidence, because the learner has
told you the first attempt did not work.

**Hold the whole chain while writing it.** A rewritten step is not a self-contained answer to a
complaint; it is one link in a chain that already exists, and the chain has more in it now than it
did at the build. Before writing, have in view every step before this one, every step after it,
and every answer already given in a window anywhere in the lesson. All of that is what the learner
is carrying. The rewrite has to read continuously with all of it — the same story told better at
this point in it, not a better paragraph dropped into a story it no longer fits.

The answers already given are part of that material and are treated like taught content: do not
contradict them, do not teach the same ground again from zero, and do not move them. The window
stays where it is and keeps its own text. What changes is that the step is now written so that a
learner holding both the step and the window reads one continuous account rather than two
overlapping ones.

**Diagnose before writing.** The failure mode here is saying the same thing at greater length —
more words, more restatement, more hedging around the same route. That is the one thing already
known not to work. Find the actual break first: a jump taken in one sentence that needed three, a
term used before it was earned, a step of a derivation performed silently, an assumption about
what the reader was already holding. Where the step has answer windows on it, the questions inside
them are the sharpest available map of where it broke, so read them as diagnosis. Then enter from
somewhere else. **A rewrite changes the route, not the volume.**

**Build it out of what they already hold.** The learner reached this step and pressed the button
here, which means the steps before it landed. That is unusually good information and it is worth
using deliberately: you know which pieces they are carrying. Reach back into those pieces and
assemble the explanation out of them — show how the thing being taught here stands in relation to
what the earlier steps established, make that relation explicit rather than leaving it to be
noticed, and look for a vantage point from which the whole run is visible at once. Often the
better second attempt is not a deeper account of this step at all: it is a clearer account of how
this step sits among the ones around it, or the same route broken into more and smaller moves.

Knowing what they hold changes the route, not the reference rules. Earlier material is still
carried into the sentence by its substance and never pointed at by number — having understood
something when they read it is not the same as having its wording available now.

**The category names which rewrite is being asked for.** The buttons are three different jobs and
produce three different steps.

- *Principle, reasoning, origin* means the step stated something without earning it. Rebuild it
  from where the thing comes from: the problem it was invented to solve, what goes wrong without
  it, why it takes the form it takes.
- *How to substitute and solve*, or whatever the procedural category is called in this subject,
  means they can follow the object but not the operation. Slow the mechanics to one move per
  sentence, perform every substitution in view, and say what each move is for.
- *More worked examples* means the idea landed but is not theirs yet. Add instances that vary the
  thing that matters — a case where the quantity is negative, a case at the boundary, a case where
  the rule nearly fails — and say what varies and what stays fixed. A second example identical in
  shape to the first teaches nothing.

**What must survive the rewrite.** The step keeps its key point; a rewrite that arrives somewhere
else has moved the lesson rather than repaired it. It does not take over the next step's job,
however naturally the expanded explanation runs on — the boundary is where it always was. Nothing
the original established may quietly disappear in the merge, because later steps read back into
it. And the crux block still hands forward to the same place, since the step after this one has
not changed.

**When the same step is expanded twice.** The second request says the rewrite failed too, so it is
not extended. Abandon the route entirely and start lower: one concrete instance, worked all the
way through with nothing left implicit, before any general statement is made at all. Generality
after the instance, never before it.

**Then read it back into the chain.** A rewritten step is checked the way the first build is
checked, and against the run of steps around it rather than alone: the story is still continuous
through it, nothing now appears twice, every answer window on the surrounding steps still agrees
with what the main line says, and the step still does the job the lesson map promised it does.

## Applying this inside the page's content slots

**Main steps.** Full book-style prose as described above. This is what the learner reads on
first pass and the only thing many steps will ever be judged on.

**Expandable answer windows.** Same voice, same completeness, but scoped to the question. The
window must state the anchor idea in its own words rather than pointing back at the step, since
the learner opened it precisely because the step did not land. End at the natural boundary of
the question — do not drift into territory that a later step is responsible for.

**Threads inside a window.** Each follow-up is answered in place, in order, so the window reads
as a conversation that stays informational. Confirm what the learner got right before adding
anything new. Keep entries shorter than the parent answer unless the question opens genuinely
new ground.

**Side windows.** The one slot where the register may lighten. Same completeness inside its own
small scope and the same duty to restate its anchor, but it is allowed to be a story rather than
an argument. It answers no question the lesson raised, so it owes the chain nothing — and for
exactly that reason it may take nothing from it: no definition, no unit, no step of a derivation,
nothing a later step or a later lesson reads back. Its thread behaves like any other thread.

**Check solutions.** Show the full derivation step by step, then verify it against numbers the
learner has already seen, then draw out the pattern the exercise was designed to reveal. A
solution that only says "correct" wastes the strongest teaching moment available.

**A step rewritten after *explain more*.** A main step in every respect, written under the extra
constraints in *Rewriting a step when the learner asks for more* above — diagnose the break, build
it from what the learner already holds, keep the key point and the boundary, and read it back into
the chain when it is done.

**The crux block on each step.** Three clauses, written in the same voice but compressed to the
bone: settled, not settled, forced next. Never a recap of the prose above it, and never a
teaser. If it can only be written vaguely, the step is doing more than one job.

**Post-lesson discussion, which is written into the panel at the foot of the page.** When the
learner writes in the discussion box they are no longer being taught — they are thinking out loud
about something they now partly own. Reply in that register, in the panel where they wrote: engage with what they actually said,
agree where they are right and say so first, disagree plainly where they are not, and follow
the tangent if it is a good one. Do not restate the lesson, do not quiz them, and do not steer
them back to the buttons. If the exchange turns into teaching — a real gap opens, or they ask
something the lesson should have covered — write that content into the page as a window on the
step it belongs to, and say in one line that you have done so.
