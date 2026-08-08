# Build and validation

The page grows past 100KB within a few turns. Editing it blind will corrupt it. Use this
procedure every time.

## Building the first version

Write it in parts rather than one enormous call:

1. `create_file` the head: doctype, fonts, all CSS, empty `<body>`.
2. Write body sections to separate temporary files with bash heredocs (`cat > part1.html <<
   'PARTEOF'`). Quoted heredoc delimiters prevent shell expansion of `$` and backticks.
3. Write the script as its own part.
4. Splice with Python, asserting the replacement actually happened:

```python
out = head.replace("<body>\n</body>", "<body>\n" + body + "\n</body>")
assert out != head, "splice failed"
```

## Editing later

Every edit is an anchored string replacement with an assertion that the anchor appears exactly
once. This is what prevents silent partial edits:

```python
anchor = '...unique existing text...'
assert src.count(anchor) == 1
src = src.replace(anchor, new_block)
```

Choose anchors from stable content — the tail of an existing answer string, a full step
`<article>` block. Never anchor on something that repeats across steps.

## Validation after every single edit

Run all three checks. They take seconds and catch the failures that would otherwise destroy
the lesson.

**1. HTML tag balance** — parse with `html.parser.HTMLParser`, tracking a stack and skipping
void elements. Report mismatches and anything left unclosed.

**2. JavaScript syntax** — extract the script block and run `node --check`. A syntax error
means every button on the page stops working, including on steps you did not touch.

**3. Registry integrity** — extract the object literals — `ANSWERS`, `CHECKS`, `ASIDES`,
`DISCUSS`, `KIND_LABEL` — and `eval` them in node, then print the number of entries and threads.
Only the step-keyed registries are checked against the step list: `ANSWERS`, `CHECKS` and
`ASIDES`, whose keys carry a `-a<n>` suffix to strip first. `DISCUSS` is a flat list with no keys
and `KIND_LABEL` is keyed by category name, so both are exempt — checking them against step ids
reports a failure on a correct file, which is worse than not checking at all. Their check is that
they parse and that every entry has the fields the rendering expects.

```bash
node -e "
const s=require('fs').readFileSync('check.js','utf8');
eval(s.match(/var ANSWERS = \{[\s\S]*?\n\};/)[0]);
Object.keys(ANSWERS).forEach(k=>console.log(k,'->',ANSWERS[k].map(i=>(i.thread||[]).length).join(',')));
"
```

Also confirm the step count is unchanged and that every `<article class="step">` still contains
`.extras` and `.acts`.

## Verify every checkable claim before publishing it

If the lesson states a result that can be checked — a worked example, a verification table, a
check of the learner's own answer, the output of a code fragment, a date, a conversion — check it
first. Arithmetic gets computed in Python; a code fragment gets run; anything else gets looked up
rather than recalled. Do not publish a result you have not produced.

```python
def s(t): return 1.5*t*t
a = 2.4
for h in (1, 0.1, 0.01):
    print(h, (s(a+h)-s(a))/h, 7.2 + 1.5*h)
```

## Generate diagrams from a script, not by hand-typing coordinates

Write the SVGs in a small Python module that emits them as strings, then substitute them into
the body through placeholder comments (`<!--FIG:name-->`) at splice time. Three reasons: the
coordinate arithmetic is done by the machine, the Thai entity-encoding helper is applied
uniformly, and a diagram can be regenerated after a scale change without editing markup.

Give the module a scale function per figure rather than typing pixel values:

```python
def sx(t, off=0): return off + 38 + t * 68      # data units -> screen x
def sy(v):        return 198 - v * 16.4         # data units -> screen y
```

Then check that nothing escapes the frame before shipping. Lines drawn from a point with a
steep slope are the usual offender — they get silently clipped by the viewport:

```python
for m in re.finditer(r'\b(c?)(x|y)(1|2)?="(-?[\d.]+)"', svg):
    axis, val = m.group(2), float(m.group(4))
    lim = W if axis == 'x' else H
    if val < -2 or val > lim + 2:
        print("out of frame:", m.group(0))
```

## The validation script

Keep this as a file and run it after every edit. Each check below caught a real failure.

1. **Tag balance** — `html.parser.HTMLParser` with a stack, skipping void elements. Report
   mismatches and anything left open.
2. **JavaScript syntax** — extract the script block, `node --check`.
3. **Registry integrity** — `eval` the five object literals in node and print the entry and
   thread counts. For the step-keyed registries only — `ANSWERS`, `CHECKS`, `ASIDES` (the step is
   the part of the key before `-a`) — confirm every key exists as a step in the page. `DISCUSS`
   and `KIND_LABEL` are not step-keyed and are checked only for parsing and field shape.
4. **Step inventory** — count `<article class="step">`, print the id list, and confirm it is
   unchanged from the previous version.
5. **Step structure** — every step contains `.crux`, `.extras` and `.acts`, and they appear in
   that order with `.acts` last.
6. **Required element ids** — the script queries about two dozen ids by hand; a renamed
   container fails silently at runtime. Assert each one exists in the markup.
7. **No browser storage, no external code** — assert `localStorage` and `sessionStorage` appear
   nowhere, and that the only external reference in the file is the Google Fonts stylesheet: no
   CDN script, no syntax highlighter, nothing the page would lose offline.
8. **Storage key unchanged** — extract the `STORE_KEY` constant and compare it against the
   previous version of the file. It must be identical on every edit of a lesson in progress. A
   changed key silently resets the learner's marked steps, and nothing on the page reports it.
9. **Class coverage** — collect every class used in the body, subtract every class defined in
   the stylesheet, and print the difference. Expect only the known hook classes used purely as
   JavaScript selectors.
10. **Placeholders consumed** — assert no `<!--FIG:` remains and no heredoc delimiter leaked.
11. **Aside integrity** — every `data-aside` in the markup has an `ASIDES` entry and every
    `ASIDES` key has exactly one button in the markup; no aside button sits inside `.crux`,
    `.extras` or `.acts`; print the count per step so the quota is visible at a glance.

    ```bash
    node -e "
    const s=require('fs').readFileSync('check.js','utf8');
    eval(s.match(/var ASIDES = \{[\s\S]*?\n\};/)[0]);
    Object.keys(ASIDES).forEach(k=>console.log(k,'->',ASIDES[k].title,'| thread',(ASIDES[k].thread||[]).length));
    "
    ```

12. **Series rail** — in a series build only: exactly one `.series` block exists, the position
    line and the list agree on the lesson count, exactly one `<li>` carries `here`, and the
    next-lesson payload opens with the end-of-lesson tag and names the next lesson.

## Quality gates on the content, not just the code

Run these on the built file before delivering. They are the mechanical half of the pedagogy
rules and take seconds. They do not replace the reading pass described at the end of the build
section of `SKILL.md` — the finished page read from the top as somebody meeting the subject for
the first time — which is what catches everything a script cannot see.

Print the visible prose of each step side by side so the shape of the lesson can be read at a
glance rather than measured:

```python
# strip tags per step and print the opening of each step's visible prose
blocks = re.findall(r'(<article class="step"[\s\S]*?</article>)', src)
for b in blocks:
    txt = re.sub(r'<[^>]+>', '', re.sub(r'<svg[\s\S]*?</svg>', '', b))
    txt = re.sub(r'\s+', ' ', txt).strip()
    print(re.search(r'data-id="([^"]+)"', b).group(1), '|', txt[:120])
```

- **No step is an outline entry.** Read the list: a step whose whole content would fit in one
  paragraph, among steps that run to several, was never written. There is no character threshold
  here — the subject decides how much a step needs — but the difference between a written step and
  a listed one is visible immediately when they are read side by side.
- **Zero section-marker references in body text**, once the `.step-no`, `.sec-no` and lesson-map
  cells are excluded. Anything else is a forward or backward citation by number.
- **Crux count equals step count.**
- **Figure count is small and each figure sits in the step that argues for it.** Print the
  data-id of every step containing an `<svg>` and read the list; a diagram in the wrong step is
  decoration.
- **Sidebar agrees with the body.** Every sidebar entry names something the body has already
  introduced, and every load-bearing term in the panel appears in the body with its English at
  its first occurrence. Print each entry next to the step that introduces it; an entry with no
  home in the body is either a preview or a leftover.
- **Register spot-check.** Grep the body for the markers of spoken language in whatever language
  the lesson is written in and expect the list to come back short and every hit to be justified.
  Build the pattern from that language's own spoken markers; Thai is the worked example because
  the line is sharpest there: `ครับ|ค่ะ|คะ|นะ|แบบว่า`. Thai does not space its words, so this flags
  candidates rather than failures — คะ sits inside คะแนน — and the hits are read, not deleted
  automatically. Then read one step aloud: it should sound like a book, not like talking.
- **A step is never rescued by its asides.** The step listing above strips the registries, so a
  thin step padded with side windows still reads as thin — which is the correct verdict.
- **Asides are few and genuinely optional.** Print every aside title with the step it hangs from.
  Read the list and ask of each one whether the lesson still teaches the whole topic with it
  deleted; anything that fails moves into the step. Most steps carry none, and a lesson with one
  on every step is decorating rather than teaching.
- **No aside reaches forward.** Search each aside body for the machinery of later steps and for
  the result a later step exists to derive. A side window is the easiest place in the page to
  spoil a payoff, because it is written last and read out of order.

### After rewriting a step

A rewritten step is the only edit that can damage the chain, so three of the gates above are run
again narrowly, on that step and its neighbours, before the file is delivered.

- **The key point is still the same one, and still appears only once.** Write out the key-point
  sentence of the rewritten step and of the steps on either side of it, and read the three
  together. An expanded step drifts into its neighbour's territory easily, and when it does, the
  next step becomes a repetition the learner reads as a stall.
- **Nothing the original established has vanished.** Diff the step against its previous version
  and account for every removal. Merging is a rewrite, not a replacement, and later steps read
  back into whatever this one set up.
- **The crux block still hands forward to the same place.** The step after this one did not
  change, so the third line of the block cannot have changed either.
- **The answer windows on this step still agree with it.** They were written against the old
  wording and they stay where they are; what must not happen is the main line now saying something
  the window contradicts. If one does, the main line is what was just repaired — reword the step
  so both can be read together, never edit the window to fit.

## Two traps specific to this page

**Inline SVG inside a JavaScript string must be quoted.** Building an SVG in Python and
interpolating it into a JS string literal silently produces a syntax error if the surrounding
quotes are lost. Verify with `node --check` immediately after any SVG insertion.

**Non-ASCII text inside SVG must be entity-encoded.** Thai and other non-Latin text in `<text>`
elements is unreliable when passed through the build chain as raw characters. Encode it:

```python
def th(s):
    return "".join(("&#%d;" % ord(c)) if ord(c) > 127 else c for c in s)
```

This applies only to SVG. Regular HTML body text is fine as raw UTF-8.

## Delivery

Deliver only a finished page. A build may take more than one turn of writing; nothing goes to the
learner until the whole plan is in the file and the checks pass.

Copy the finished file to `/mnt/user-data/outputs/` and call `present_files`. Keep the same
filename **and the same `STORE_KEY`** across turns, so the learner's progress, their mental
bookmark, and their marked steps all stay attached to one document. A new filename is correct in exactly one case: when the lesson is being rebuilt
from scratch rather than extended, since the old progress state would otherwise be read into a
different skeleton. In that case change `STORE_KEY` with it.

The next lesson of a series is the second such case: it is a new file with a new storage key and
its own step numbering, never an extension of the previous lesson's page. Name the files so the
order is visible on disk — `<series-slug>-lesson-2.html`.

## Custom diagrams

Hand-written inline SVG with a `viewBox` and `width:100%` scales correctly on a phone. Use the
page's CSS custom properties for stroke and fill so diagrams follow dark mode. Give every
diagram a `role="img"` and an `aria-label` describing what it shows.

A diagram earns its place when it makes visible a distinction that prose has already tried and
failed to convey — typically one of: something held fixed while something else changes, a whole
separated into the parts that do different work, or two situations set side by side so that the
difference between them can be seen rather than described. If you cannot say which distinction
the diagram carries, it is decoration.
