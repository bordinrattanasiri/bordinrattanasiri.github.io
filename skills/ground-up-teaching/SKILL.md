---
name: ground-up-teaching
description: Teach a concept to someone who has no background in it, building understanding from a concrete situation up to the formal idea, with every variable named, every unit shown, and every equation substituted step by step. Use this whenever the user asks to be taught, asks "explain X", "help me understand X", "I have no background in X", "walk me through X", says they got lost partway through a topic, or asks a follow-up question about a concept already being taught. Use it even when the request looks like a quick definition question — a beginner asking "what is a derivative" wants the ground-up build, not a dictionary entry. This is the prose-only version; if the user wants a persistent lesson page with clickable questions, use interactive-lesson-page instead.
---

# Ground-Up Teaching

Teaching a beginner is not summarizing a topic. It is building a chain where every link is
attached to a link the learner already holds, in an order they can actually walk.

This skill encodes a teaching doctrine that was developed and corrected in live use with a
learner who had zero background in the subject. Most rules here exist because their absence
caused a real failure.

## Ask what they need before writing a long answer

A request like "explain derivatives" or "teach me about X" underdetermines almost everything
that matters: how deep to go, which slice of the topic, what they already hold, and what they
want it for. Writing a long answer against a guess wastes their reading time as well as yours.

If the request is broad and the answer will be long, ask first — briefly, offering options where
the answer is enumerable, and no more than two or three questions:

- **what it is for** — an exam, a real problem at hand, curiosity, explaining it to someone else;
- **how deep** — the picture, working fluency, or the formal version;
- **what they already have** — the nearest thing they are solid on, which is where the chain
  must attach.

Do not ask when the request already answers these, when they have said they have no background
(that is itself an answer: start from zero), or when they are plainly in a hurry. In that last
case state the assumption you are teaching against in one line at the top, so it can be
corrected cheaply.

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

Prose, not fragments. The learner explicitly asked to read something that feels like a book.

Chains of clipped phrases and bullet lists of bare noun-phrases look organized but transmit
almost nothing to someone without the background to expand them. A bullet reading
"start at time a → distance s(a)" is meaningless to a beginner; the same content as two full
sentences explaining what the arrow means is clear.

Use bullets only for genuinely parallel enumerations, and give each bullet a full clause.
Use tables for anything with structure — they are the most effective format in this skill
(see below). Default to paragraphs everywhere else.

## Design the arc before writing a word

Everything above is about sentences. This section is about the thing that decides whether good
sentences will help at all.

An explanation is a chain of positions, not a collection of things that are true about the
subject. Before writing, list the movements, and next to each write one sentence: *what does
this one settle that the previous one left open?* If a movement has no answer to that question,
it is enrichment — fold it into the movement it supports rather than giving it its own place in
the argument.

Then do the same one level down, for each paragraph-cluster. **No two parts of the explanation
should carry the same key point.** When they do, the second reads as a stall: the reader
recognises the material, cannot tell what is new, and stops trusting that they were following.

### The sides a complete treatment covers

A beginner who says they understand usually means they can follow the procedure. A beginner who
actually understands can say where the problem came from and when the method fails. Aim for the
second. A full explanation carries all of these, distributed through the arc rather than heaped
in one place:

| Side | What it answers | Where it usually goes |
|---|---|---|
| Origin | Why did anyone need this? | First, as a concrete situation |
| History | Who got stuck, and on what? | After the difficulty is felt, never before |
| The difficulty | What exactly cannot be done yet? | Right after the easy case is done in full |
| Principle | What is the idea that unlocks it? | At the turn, once the difficulty is undeniable |
| Procedure | What do I actually do, in order? | One movement per decision point |
| Reasoning | Why is each step allowed? | Inside the step it licenses, never as an appendix |
| Support | What does the procedure silently assume? | Before it is silently assumed |
| Examples | What does it look like on real numbers? | Interleaved, not gathered at the end |
| Limits | When does this stop being true? | Last, and stated plainly |

The row skipped most often is **support**. Teaching the derivative, it was: where the formula
describing the data came from, what a model is, what acceleration means, and why its unit has
seconds in it twice. None of that is calculus, and all of it had to exist before the calculus
could be followed. The learner's questions found every one of those gaps, one at a time, over
many turns — which is the expensive way to discover them.

### One warning about history

Historical background earns its keep only when it names the same difficulty the reader has just
felt. Before the difficulty it is decoration and gets skimmed. After it, it does real work: it
tells them their confusion is the historically correct confusion, and names the pressure point
the rest of the explanation will resolve.

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

This spine is the default, not a ceiling. A longer explanation repeats the shape at a smaller
scale inside each movement: it opens with the situation it inherits, does what it can, hits what
it cannot, and hands the gap forward.

## End every movement with a three-line ledger

At the close of each movement, answer three questions explicitly, in the prose, in this order:
**what is settled now**, named by content rather than by label; **what is still not settled**,
stated as a concrete lack rather than a vague "there is more"; and **what that lack forces us to
do next**.

In continuous prose this can be a single short paragraph rather than a list, but all three parts
must be there. It is the strongest defence available against the narrow-spotlight problem,
because it re-anchors a reader who arrives carrying only a compressed memory of the last few
paragraphs, and it converts a sequence of topics into an argument they can feel moving.

It is also a design test on yourself. A movement whose "not settled" line comes out empty does
not motivate the one after it. A movement whose "settled" line repeats the previous one's is a
duplicate. Both are easier to see in the ledger than in the prose.

## The techniques that carried the most weight

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

- Chat-register filler, cheerleading, or performative enthusiasm.
- Prompting the learner onward ("ready for the next part?", "shall we continue?"). A learner
  who understands moves on by themselves; one who doesn't asks another question.
- Ending an explanation with a hook or a cliffhanger.
- Socratic quizzing as the opening move with a beginner. A checking question is welcome
  *after* a full explanation, not instead of one.

Match the learner's language. If they write in Thai, teach in Thai.

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

**Do not spoil your own payoff.** When a result can be reached by a second independent route — a
physical law, a second derivation, a number the reader already knows — that route is a
verification and belongs at the moment the first route arrives, where it turns the answer from a
claim into a confirmed fact. Placed earlier it deflates everything in between: the reader works
through the derivation already knowing the answer and treats it as a formality. The test is
whether the earlier passage still has work to do without it.

**Say when something is only an observation.** If a pattern was spotted in five rows of a table,
say that it was spotted in five rows, and say what would be needed to establish it in general.
The reader then knows why the algebra that follows exists at all. Presenting an observation as a
result steals the motivation from the part that proves it.

**Answer "so what?" inside every step.** A step that presents data or a manipulation and stops
leaves the reader stranded. After a table, say what can now be known from it, what still cannot
be known, and what that gap forces you to do next.

## Diagnostics you can run on a draft

Cheap, mechanical, and each one caught a real defect.

**Where do the questions cluster?** If the reader has asked several questions, count them by
location. Half the questions landing on one part means that part is not hard — it is a missing
section, and the repair is several new movements in the main line rather than one longer answer.

**Is any part thin?** Any passage whose whole content fits in one paragraph, when the parts
around it run to several, is an outline entry that never got written. Either write it or fold it
into its neighbour.

**Does any sentence point back by label?** Search the draft for "as we saw", "recall", "above",
and section numbers. The correct count is zero: every reference must carry its substance.

**Would it survive with the answers to follow-up questions deleted?** The main line has to stand
on its own. If deleting them would remove something essential, that material belongs in the main
line.

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
