---
name: ground-up-teaching
description: Teach a concept to someone who has no background in it, building understanding from a concrete situation up to the formal idea, with every variable named, every unit shown, and every equation substituted step by step. Use this whenever the user asks to be taught, asks "explain X", "help me understand X", "I have no background in X", "walk me through X", says they got lost partway through a topic, or asks a follow-up question about a concept already being taught. Use it even when the request looks like a quick definition question — a beginner asking "what is a derivative" wants the ground-up build, not a dictionary entry. Teaching runs across turns rather than in one long answer: scope, then a map of the whole explanation, then one movement per message as the learner responds. Also use it when a session opens with nothing but a handoff document that names this skill. This is the prose-only version; if the user wants a persistent lesson page with clickable questions, use interactive-lesson-page instead.
---

# Ground-Up Teaching

Teaching a beginner is not summarizing a topic. It is building a chain where every link is
attached to a link the learner already holds, in an order they can actually walk.

This skill encodes a teaching doctrine that was developed and corrected in live use with a
learner who had zero background in the subject. Most rules here exist because their absence
caused a real failure.

The doctrine is the same one behind `interactive-lesson-page`, and so is the standard: an
explanation built with care, walked in an order that can actually be walked, where every result
has a visible origin and the parts are tied into one picture instead of listed. What differs is
the medium. There is no page here. The explanation is delivered into a conversation, a movement
at a time, and the conversation carries it — which suits subjects that do not need the page's
per-step apparatus, and which constrains how much may arrive at once.

**The explanation is never one long message.** A whole carefully built explanation delivered in a
single message defeats itself: the learner loses the thread somewhere in the middle, and by the
time they think to ask, the place where they lost it has scrolled away. They then read back and
forth trying to find where they were, which is the opposite of understanding. Delivered a
movement at a time, the same material has none of that problem — a question is asked where it
arose, answered there, and the conversation moves on with the thread still in the learner's hand.

This file is in four parts: how the prose is written, how the explanation is designed, how the
conversation is run from the first message to the handoff, and the checks to run before sending.
The first two are the standard; the third is the order of operations. Read all of it before
teaching anything, because the design work has to be finished before the first movement is sent.

---

**Writing: how every sentence is built.** This is the standard the prose is held to, and it
applies to the map, the movements, the
answers and the asides alike.

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
Use tables for anything with structure — they are the most effective format in this skill; the
three shapes that do the most work are set out under *the techniques that do the most work*.
Default to paragraphs everywhere else.

### The register is written, not spoken

Complete sentences are not enough by themselves — a transcript of someone talking is made of
complete sentences too. What the learner asked for reads like a book, and that means the voice of
a book: composed expository prose that holds together when read straight through, rather than the
voice of someone improvising aloud in front of a class. The pull the other way is strong here,
because the explanation arrives in a chat window where everything else is conversation. The
explanation is not conversation. It is written material that happens to be delivered there.

What this rules out is conversational scaffolding, not warmth. No greeting or sign-off wrapped
around the teaching, no "okay, so", no "right?", no "let us see", no exclamation mark doing the
work of enthusiasm, no rhetorical question asked only to fill the gap before its own answer.
Address the reader where the address does work — "notice that the leftover term is still sitting
there" — and never as filler.

The rule is sharper in languages that carry the difference in the words themselves, and Thai is
the clearest case, so it is worked out here as the example of what the rule means anywhere. A Thai
explanation is written in written Thai: no ครับ or ค่ะ, no sentence-final particles used for tone
(นะ, สิ, ล่ะ, เลย), none of the connectives that belong to speech rather than to writing. Every
language draws this line somewhere in its own vocabulary; find where, and stay on the written
side of it.

The test is to read a paragraph aloud. It should sound like a well-made book being read, unhurried
and put together in advance — not like a person thinking out loud, which is where the fillers come
from.

This governs the teaching itself. The short exchanges around it — the two or three clarifying
questions before you start, a one-line acknowledgement that you misread them — are naturally
briefer and more direct than the lesson prose, but they take the same view of filler.

## Tone

Informational, warm, unhurried. Enrichment is wanted: historical background, adjacent
phenomena, why the units are shaped that way, what happens in the extreme cases. Those
tangents were explicitly appreciated.

What is not wanted:

- Chat-register filler, cheerleading, or performative enthusiasm. The voice stays written rather
  than spoken throughout — see *the register is written, not spoken* above.
- Prompting the learner onward ("ready for the next part?", "shall we continue?"). A learner
  who understands moves on by themselves; one who doesn't asks another question. There are
  exactly two exceptions and both are named where they occur: the single steering line at the
  foot of the map, and the offer that follows the last movement.
- Ending an explanation with a hook or a cliffhanger.
- Socratic quizzing as the opening move with a beginner. A checking question is welcome
  *after* a full explanation, not instead of one.

Match the learner's language. If they write in Thai, teach in Thai.

### Terms keep their English

A lesson taught in another language carries one extra duty, because the words a field actually
uses are not always the words a translation produces, and because the learner will eventually
read about this subject in English.

Every term the argument is built on — the load-bearing vocabulary, not every noun — gets its full
identity at its first appearance: the formal term in the learner's language, the transliterated
form if the field uses one, any other name it commonly goes by, and the English in brackets. The
example has to be shown in some language other than English for it to show anything; in Thai it
reads as *ค่าคงตัวของการสลายตัว หรือที่มักเรียกทับศัพท์ว่า ดีเคย์คอนสแตนต์ (decay constant)*, and the shape is the
same in any language: full identity once, then one form held.

After that, pick one of those forms and hold it for the rest of the explanation. Which one is a
question about the field rather than about purity: where practitioners speak in transliteration,
the transliteration is the honest choice and a formal translation reads as invented; where the
formal term is what people actually say, use that. Drifting between forms is what is never
acceptable, because the learner has no way of knowing that two words are one thing, and the
vocabulary silently doubles.

There is no sidebar in this skill to park terms in, so the variable table carries the symbols and
their units, and terms carry their English inline at first use. When several arrive together,
a short two-column table of the terms with their English is worth the space — once, where they
arrive, not as a glossary at the end.

---

**Designing the explanation.** The largest determinant of whether an explanation works is
decided before a word of it is
written. This part is that work.

## Design the arc before writing a word

The prime directive and the sentence rules are about how to write. This section is about the
thing that decides whether good sentences will help at all, and it is the work that has to be
finished before the map is posted.

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

In delivery, each item of the spine is normally one movement and therefore one message. Two
adjacent items share a message only when neither could stand alone — naming the variables and
assembling the formula from them, for instance — and even then the pair must still settle one
thing and close with one ledger.

### Translating the spine to a subject without equations

The spine is written in the vocabulary of a quantitative subject because that is where it is
hardest to satisfy. Every item has a counterpart everywhere else, and the work is to translate
it rather than to drop it.

**Real numbers** become the one concrete case the explanation follows all the way through: a
specific input traced through a specific implementation in a programming lesson, one statute
applied to one set of facts in a law lesson, one passage analysed bar by bar in a music lesson.
The requirement is not arithmetic; it is that something particular is carried from the beginning
to the end instead of a general description.

**Units** become what each object *is* — its type, its scope, what it is a count or an instance
of. In code that is types and shapes; in an argument it is what a claim is a claim about. The
use is identical: a result of the wrong kind is wrong regardless of how it was produced, and the
learner should be able to see that without checking the details.

**Substituting several rounds** becomes running the same procedure on a second and a third case,
including one where the obvious move fails. **Generalising with algebra** becomes stating the
general rule only after the concrete case has been walked — the ordering is what matters, not
the notation. **The breaking point** always exists somewhere: the input the code does not handle,
the case the doctrine was not written for, the passage the rule does not describe.

An explanation with no numbers in it should still be recognisable as this spine. One that skips
these items because the subject "isn't mathematical" has skipped the parts that do the teaching.

In code, a fragment is shown and then walked in prose, line by line, and then run on the one
concrete input the explanation is following. A block pasted in without the walk is the same
failure as a bare formula.

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

## Sequencing rules

**Never cite material the learner has not reached yet.** If a later result would help, either
derive it inline right there or leave it out. Citing forward is worse than useless — it makes
the learner feel they missed something.

**Do not do the next movement's job.** An expansion of one movement should stop at the boundary
where the following one takes over. Overlap makes the next movement feel redundant and confuses
the sense of progression.

**Do not introduce a concept before the point where it is used.** A movement whose only purpose
is to declare terminology in advance will be redundant by the time the terminology gets used.
Fold the explanation into the movement where the thing does work. Meaning is clearest at the
moment of use.

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

**Mark the status of anything that is not plain verified fact.** This explanation is the only
source the learner has — nothing in this skill sends them to a book or a website — so a claim
they cannot check has to arrive carrying its own status, in one clause, without hedging every
sentence into mush. Three kinds need it.

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

The bar is not universal hedging — that would be its own dishonesty, since most of what is taught
is settled and should be stated flatly. It is that where you would not be able to show your
working if challenged, the sentence says so.

**Answer "so what?" inside every movement.** A movement that presents data or a manipulation and
stops leaves the reader stranded. After a table, say what can now be known from it, what still
cannot be known, and what that gap forces you to do next.

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

---

**Running the conversation.** What happens when, from the first message to the handoff.

## Ask what they need before planning anything

A request like "explain derivatives" or "teach me about X" underdetermines almost everything
that matters: how deep to go, which slice of the topic, what they already hold, and what they
want it for. Planning and then walking an entire explanation against a guess wastes much more
than one message of their reading time.

If the request is broad and the answer will be long, ask first. Ask in whatever form fits: where
the answers are enumerable, offering a few options is far less work to answer than open prose and
gives sharper information, and if the environment can show them as something to tap, use it;
where the options would mean nothing yet, say what the choice is about in a sentence or two
first; where the answer is genuinely open, ask openly. Keep each turn short enough to answer in a
moment, and take as many as the conversation needs — some learners answer everything at once,
others want to think aloud about what they are really after, and both are the process working.
What has to be settled:

- **what it is for** — an exam, a real problem at hand, curiosity, explaining it to someone else;
- **how deep** — the picture, working fluency, or the formal version;
- **what they already have** — the nearest thing they are solid on, which is where the chain
  must attach.

Do not ask when the request already answers these, when they have said they have no background
(that is itself an answer: start from zero), or when they are plainly in a hurry. In that last
case state the assumption you are teaching against in one line at the top, so it can be
corrected cheaply.

There is no confirmation gate. Once the answers are enough to scope the explanation, go straight
to the map — asking permission to begin turns a conversation into a form.

## Resuming from a handoff document

A session may open with nothing except a handoff file, dropped in and sent without a word. That
is the intended way to continue, so read it and begin rather than asking what they want.

The document carries two lines that decide what happens. They answer separate questions and must
both be read:

```
explanation: new                ← or: continue from where it stopped
subject: next part of <series name> — part 3 of 5
```

**`explanation: new` + `subject: next part`.** The subject was split into parts when the series
was agreed. Do not re-scope it. Open with one message that recaps what the last session settled,
says what this one covers and where it sits in the plan, and then posts the map for this part.
The learner replies — with a change, a question, or barely anything — and the first movement
follows.

**`explanation: new` + `subject: new topic`.** This is a new subject that happens to have a
neighbour, so ask the opening questions as usual: purpose, depth, what they already hold. What
the handoff records about them is context for asking better questions, not a reason to skip them
— someone who wanted a working grasp of the last subject may want the formal treatment of this
one.

**`explanation: continue from where it stopped`.** The last session ran out of room mid-arc,
whichever subject line accompanies it. Recap in two lines where it stopped, then continue at the
next movement of the plan the document carries. Do not re-plan and do not re-teach what was
delivered.

Either way the handoff is context, not a script. Where it reports that questions concentrated
somewhere, weigh that while planning; it does not decide what this session teaches.

## Plan the whole explanation, then post the map

Before anything is taught, plan the explanation to its end. Not a list of topics: the actual arc.
For every movement, know what it settles that the one before it left open, what it needs the
learner to already hold, which concrete situation, case or numbers it will use, and what it
hands forward. *Design the arc before writing a word* and *Structure of a lesson*, in the part
above, are the rules for building that. Do the whole of it now, even though only a fraction will be visible in this
message. An explanation planned one movement at a time drifts: the third movement arrives needing
something the first should have set up, and by then the first cannot be fixed.

Before planning, check the facts the arc will be built out of. Dates, names, numbers, versions,
the exact form of a rule, the syntax that actually runs — look up whatever you could not state
precisely from memory, and anything in the subject that moves. A wrong specific taught to a
beginner is one they have no way of catching, and a fact discovered late can force the whole plan
to be rebuilt around it.

Then post the map, a short message in two parts. First a few sentences on where the explanation
is going and why it is arranged this way, so the learner sees the shape before walking into it.
Then the movements in order, one clause each, each saying what that movement *does* rather than
naming a topic — not "derivatives", but "what the average speed across an interval can and cannot
tell us". An ordered list is right here; this is a plan, not teaching.

Close with a single line offering to change it: reorder, cut, add, go deeper somewhere. This is
the one place in the skill where inviting a reply is correct, because it is a real chance to
steer and costs nothing to ignore. Do not ask for approval and do not wait for it — a learner who
replies with a word of assent, or simply asks their first question, has told you to begin.

**Write the map so that it can also serve as your own memory of the plan.** The plan does not
persist between turns; only what is on the screen does. Fifteen messages later that map is the
record of what you intended, so each line must carry enough intent to be re-derivable from —
which is the same discipline as writing lines that mean something to the learner.

If the honest plan will not fit in one sitting, there are two answers and the wrong one is to
compress. Either narrow the scope — say so in the map message, name what is being left out, and
offer it as somewhere to come back to — or propose a series of sessions, each with a title and
one clause saying what it settles, in the order they have to be walked.

Propose a series only when the subject forces one, on the same two conditions that govern it
anywhere: the parts hold each other up so tightly that teaching one alone means smuggling in half
of another, or the honest treatment of the subject genuinely will not fit in one sitting. Breadth
is not a third condition, and a list of related things is not a chain. The learner confirms,
reorders, cuts, or refuses it, and **a series exists only once they say so.** Each part is its
own session with its own map, and the handoff between them carries the plan.

### When the map is not worth its own message

A small question does not need ceremony. If the honest plan is short enough that the learner
would see the whole of it before the map had finished describing it, or they are plainly in a
hurry, skip the map message and open the first movement with a sentence saying where the
explanation will go. The planning still happens; only the posting of it is
dropped. The reverse mistake — a map message for something that could have been settled in two
movements — makes a short answer feel like an enrolment.

If they ask for the whole thing at once, give it to them at once. Keep the movements intact and
keep every ledger: what they asked for is one long message, not a compressed one.

## One movement per message

Each message teaches one movement of the plan, and then ends. A movement is one thing settled —
the concrete situation, or the easy case done in full, or the difficulty made undeniable, or the
formula assembled, or the breaking point confronted. Not one fact, and not three movements at
once because they looked short.

Length follows from that rather than from a target: several paragraphs, with whatever tables and
worked numbers the movement needs, long enough to settle the thing completely and short enough
that the learner can hold all of it while reading. If it will not fit, the plan had two movements
sitting in one place — split it, and say so.

Open by naming where the explanation stands, in content rather than in labels: what is known now,
and what is still missing that this movement supplies. One or two sentences. This is the
re-anchoring the prime directive demands, and here it does double duty, because the previous
message may have been read yesterday.

Close with the three-line ledger — what is settled, what is not, what that forces next. In this
format the ledger is also the continuation cue, and it is the only one you get. **Never end a
message by asking permission to continue.** No "ready for the next part?", no "shall I go on", no
cliffhanger. A ledger that names the gap is already the invitation: the learner answers with a
question, or with anything at all, and the next movement follows. A checking question at the
close of a movement is permitted occasionally, after the movement is complete — never as a
substitute for teaching it. Ask one where getting it wrong would be expensive: at a convergence,
where several things introduced separately have just come together and the relationship has to be
held correctly; where a result has to be produced rather than recognised; or where the point of a
rule has an obvious misreading standing next to it. It must be answerable from what has been
taught so far, and it never introduces content of its own.

**No numbering anywhere in the teaching.** No "movement three", no "part 3", no headings that
count. Numbering is a page's furniture; in a conversation it reads as bureaucracy. This makes the
reference rules of the prime directive not merely good practice but the only option available —
earlier material is referred to by carrying its substance, because there is no label to point at.

The plan is a different matter. While designing the arc you need the movements separated,
numbered and laid out, because that is what makes a collision or a gap visible. That numbering is
scaffolding for you and never appears in anything the learner reads.

One message does one job. An answer and the next movement do not share a message unless the
answer is a sentence or two; otherwise the movement is read as part of the answer, and its ledger
lands on the wrong material.

## When they ask, interrupt, or wander

The conversation is the point, not an interruption of it. But a plan that survives no contact
with the learner was a bad plan, and a plan abandoned at the first question was never being
followed.

**A question about what was just taught** is answered where it stands, in full, merged and
continuous rather than patched — *Answering follow-up questions*, below, is how. The next movement
then follows in a later message, opening as always with where we now stand.

**A message saying it did not land** is different from a question, and the difference decides what
to write. A question names a gap; "I don't follow this" says the route itself failed, and the one
response guaranteed not to work is the same account at greater length. Diagnose first: find the
jump taken in one sentence that needed three, the term used before it was earned, the move made
silently, the thing assumed to be already held. Then come at it from somewhere else.

Build the second attempt out of what they are demonstrably carrying. They followed the
explanation this far, so the movements before this one landed, and those are the pieces to
assemble from — show how the thing being explained now stands in relation to what the earlier
movements established, make the relation explicit instead of leaving it to be noticed, and look
for a vantage point from which the whole run is visible at once. Often the better second attempt
is not a deeper account of this movement at all but a clearer account of how it sits among the
ones around it, or the same route broken into more and smaller moves. Anything already said in an
earlier answer counts as held too: do not contradict it and do not teach that ground again from
zero.

Knowing what they hold changes the route, not the reference rules — earlier material is still
carried into the sentence by its substance, because having understood something when they read it
is not the same as having its wording in front of them. And if the same ground fails a second
time, do not extend the second attempt: abandon the route and start lower, with one concrete
instance worked all the way through, nothing left implicit, before any general statement is made
at all.

**A question that reaches ahead**, into something the plan settles later, is answered at the size
the question deserves. A narrow question gets a narrow answer, and the explanation carries on as
planned. A question that cannot be answered honestly without the whole account gets the whole
account, then and there, where they asked it — withholding it to protect a plan they cannot see
is the worse failure.

What changes in that case is the planned movement, not the answer. When the explanation reaches
it, do not deliver it a second time. Open by naming what was already settled when they asked, and
give the movement the work that is left: put it in its place in the arc, verify it against what
has been built since, extend it past where the answer stopped, tie it to what came before. A
movement that re-runs an answer the learner is still holding reads as a stall and makes them
doubt they were following anything. Answering fully is never the mistake; repeating yourself
afterwards is.

**A tangent they want to take** is worth taking, at the depth they asked for, and is then closed
by returning to the line: name what the tangent settled and where we were before it. The return
is the part that gets forgotten, and without it the explanation quietly becomes a conversation
about whatever came up most recently.

**A question that exposes a hole in the plan** is the most valuable thing that can happen. If the
answer needs machinery the plan never introduced, that is a missing movement rather than a long
answer. Add it, teach it in its place, and say in one line that it was added — the map was a
promise, and the learner should be told when it changes.

**A request to skip, reorder, or drop something** is followed, and the change is stated in one
line, so that the closing message stays honest about what was covered and what was not.

If they ask where the explanation has got to, restate the arc in words — what is done, what
remains — rather than pointing back at a map message they would have to scroll to find.

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

### Verify every checkable result before sending it

This cuts both ways, and the direction that matters more is your own. If a movement states
something that can be checked — a worked example, a verification table, the output of a code
fragment, a date, a unit conversion — check it before it is sent. Compute the arithmetic rather
than recalling it, run the fragment rather than predicting it, look up the date rather than
trusting the shape of it. A wrong specific taught to a beginner is one they have no way of
catching, and it is believed precisely because everything around it was right.

The same applies to what the learner sends. If they submit a derived result, actually compute it
before answering. Run the arithmetic. Do not eyeball algebra and declare it correct.

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

## The last movement, and what happens after it

You know which movement is the last one, because you planned it. When it has been delivered and
its ledger has no gap left to name, say so plainly and put three things on the table in one short
message: whether anything is still unclear or worth arguing about; whether they would like to
hear what this connects to and what would be natural to learn next; and that a written summary of
what was covered can be produced to carry into whatever comes after.

That message is an offer rather than a farewell, and it is the one place where three questions in
a row are correct, because they are the genuine options at the end and the learner takes one or
none.

If they reply with a question or an argument instead, that is the better outcome: answer it, stay
in it for as long as it holds, and come back to the connections when the moment is right rather
than steering there.

### Handing off in the middle

An explanation of any size runs for many turns, and a conversation that fills up before
the end loses everything not written down. There is no gauge to read — you cannot measure how
much room is left — so watch the visible signals: many movements delivered, long answers behind
you, the arc still unfinished. When they line up, say so in one line and offer to hand off now.
Offer early, and write it immediately whenever they ask.

It is the same document with one difference: `explanation: continue from where it stopped`, and
a record of exactly where the arc stopped — which movements were delivered, what the map still
has outstanding, what was being discussed when the session ended. Nothing else travels with it.
There is no page in this skill, so the document is the entire record: it carries the remaining
plan in full rather than a pointer to it, and a learner who arrives with only this file has
everything the next session needs. The next session opens the
skill, recaps in two lines, and picks up at the next movement without re-planning.

**The handoff is the last thing, and only on their word.** This skill carries its own handoff
rather than calling out to a separate one, so a conversation can be closed properly wherever the
skill is installed. When they confirm a direction to go next, or ask for the summary, write a
Markdown file and present it for download — named obviously, `<subject-slug>-handoff.md` — holding:

- what was taught, in the order it was taught, a clause per movement, so that a session which was
  not present can see the arc without reconstructing it;
- what the learner now holds and where they struggled, named by content;
- where the questions concentrated — a part of the arc that drew question after question was
  under-built. What travels is the observation about the planning rather than the material: what
  that movement was carrying, and what it might have been split into. It is judgement for whoever
  plans the next explanation in this area to weigh, and it does not decide what the next session
  teaches;
- what the plan promised and did not cover, and anything that was added along the way;
- what the opening questions established about their background, purpose and preferences;
- the direction they chose, written as a brief for the next explanation rather than as a topic
  name;
- an instruction block at the top rather than a title page, because the document has to work as
  the only thing in the next session:

  ```
  # <subject> — handoff
  Open this session with the `ground-up-teaching` skill and treat this document as the brief.
  The learner may have sent nothing but this file; begin from it.

  explanation: new
  subject: new topic — <topic>, chosen at the end of <previous subject>
  ```

  Name `interactive-lesson-page` instead when the direction is large enough to deserve a page.
  The two routing lines are read together and are independent of each other — see *Resuming from
  a handoff document*. `explanation:` is either `new` or `continue from where it stopped`.
  `subject:` is either `next part of <series name> — part <n> of <N>` or `new topic — <topic>,
  chosen at the end of <previous subject>`. A part of a series that was interrupted mid-arc is
  the combination of `continue from where it stopped` with its ordinary series subject line;
  there is no separate value for it.

Write it for a reader who was not in the conversation: no "as discussed", nothing that depends on
what only the chat holds. Redact anything personal the teaching does not need — contact details,
credentials, third-party names the conversation happened to pick up.

Do not write the summary into the chat as well; that is the document's job, and doing both leaves
two versions of the same thing. Say two things in chat instead, briefly: what the file contains,
and what to do with it — open a new chat, drop this file in, and press enter. The instruction
block inside the document is addressed to the next session's model, so the person carrying it
needs telling separately. There is only ever one file here, whether the handoff comes at the end
or in the middle, so the instruction is the same either way and nothing else has to travel with
it. Then stop: nothing follows the handoff, and no closing flourish goes after it.

---

**Checks.** Cheap, mechanical, and worth running before a message is sent.

## Diagnostics you can run on a draft

Cheap, mechanical, and each one caught a real defect.

**Where do the questions cluster?** Count the questions by where they land. Half of them landing
on one part means that part is not hard, it is a missing section. Nothing already sent can be
rewritten, so the repair is forward: add the movements the plan was missing and teach them in
place, rather than answering at ever greater length in one spot.

**Is any part thin?** Any passage whose whole content fits in one paragraph, when the parts
around it run to several, is an outline entry that never got written. Either write it or fold it
into its neighbour.

**Does any sentence point back by label?** Search the draft for "as we saw", "recall", "above",
and section numbers. The correct count is zero: every reference must carry its substance.

**Could the learner say where we are without scrolling?** At the end of any message, the position
in the argument should be recoverable from that message alone — what is settled, what is missing.
If it is only recoverable by scrolling back, the message opened without re-anchoring or closed
without a ledger.

**Did an answer turn out to be load-bearing?** If something you only said because they asked is
now something the rest of the explanation leans on, it was a missing movement rather than an
answer. Put it in the plan, teach it in its place, and say in one line that the map has changed.

