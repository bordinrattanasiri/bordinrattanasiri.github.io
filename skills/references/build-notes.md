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

**3. Registry integrity** — extract the object literals and `eval` them in node, then print the
number of entries and threads:

```bash
node -e "
const s=require('fs').readFileSync('check.js','utf8');
eval(s.match(/var ANSWERS = \{[\s\S]*?\n\};/)[0]);
Object.keys(ANSWERS).forEach(k=>console.log(k,'->',ANSWERS[k].map(i=>(i.thread||[]).length).join(',')));
"
```

Also confirm the step count is unchanged and that every `<article class="step">` still contains
`.extras` and `.acts`.

## Verify the mathematics before publishing it

If the lesson states a numeric result — a worked example, a verification table, a check of the
learner's own answer — compute it in Python first. Do not publish arithmetic you have not run.

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
3. **Registry integrity** — `eval` the three object literals in node, print the entry and thread
   counts, and confirm every id used as a registry key exists as a step in the page.
4. **Step inventory** — count `<article class="step">`, print the id list, and confirm it is
   unchanged from the previous version.
5. **Step structure** — every step contains `.crux`, `.extras` and `.acts`, and they appear in
   that order with `.acts` last.
6. **Required element ids** — the script queries about two dozen ids by hand; a renamed
   container fails silently at runtime. Assert each one exists in the markup.
7. **No browser storage** — assert `localStorage` and `sessionStorage` appear nowhere.
8. **Class coverage** — collect every class used in the body, subtract every class defined in
   the stylesheet, and print the difference. Expect only the known hook classes used purely as
   JavaScript selectors.
9. **Placeholders consumed** — assert no `<!--FIG:` remains and no heredoc delimiter leaked.

## Quality gates on the content, not just the code

Run these on the built file before delivering. They are the mechanical half of the pedagogy
rules and take seconds.

```python
# density: strip tags per step and count characters of visible prose
blocks = re.findall(r'(<article class="step"[\s\S]*?</article>)', src)
for b in blocks:
    txt = re.sub(r'<[^>]+>', '', re.sub(r'<svg[\s\S]*?</svg>', '', b))
    print(re.search(r'data-id="([^"]+)"', b).group(1), len(re.sub(r'\s+', ' ', txt)))
```

- **No step under ~600 characters of prose.** Below that it is an outline entry.
- **Zero section-marker references in body text**, once the `.step-no`, `.sec-no` and lesson-map
  cells are excluded. Anything else is a forward or backward citation by number.
- **Crux count equals step count.**
- **Figure count is small and each figure sits in the step that argues for it.** Print the
  data-id of every step containing an `<svg>` and read the list; a diagram in the wrong step is
  decoration.

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

Copy the finished file to `/mnt/user-data/outputs/` and call `present_files`. Keep the same
filename across turns so the learner's progress and mental bookmark stay attached to one
document. A new filename is correct in exactly one case: when the lesson is being rebuilt
from scratch rather than extended, since the storage key changes with it and the old progress
state would otherwise be read into a different skeleton. In that case change the storage key
too.

## Custom diagrams

Hand-written inline SVG with a `viewBox` and `width:100%` scales correctly on a phone. Use the
page's CSS custom properties for stroke and fill so diagrams follow dark mode. Give every
diagram a `role="img"` and an `aria-label` describing what it shows.

Diagrams that earned their place in practice: a timeline showing one marker pinned while a
measured interval shrinks; a force decomposition on a slope showing which component causes
motion; a side-by-side of four isolated data points versus a continuous curve; a three-tier
stack showing repeated division producing a compound unit. Each made a distinction visible that
prose had already failed to convey.
