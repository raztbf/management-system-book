#!/usr/bin/env python3
"""Convert the-tipping-point.pdf (pdftotext -layout output) into clean markdown.

The PDF carries an embedded, imperfect OCR text layer (no page images exist, so
re-OCR is impossible). This script therefore does three things:
  1. structural recovery  -- strip running heads, reflow paragraphs across page
                             breaks, rebuild chapter/section headings, drop caps
  2. dehyphenation        -- rejoin words broken at line ends, keeping real hyphens
  3. conservative OCR repair -- fix character-confusion typos and split words,
                             only when the correction is unambiguous
"""
import re, collections, sys

SRC = '/tmp/tp-layout.txt'
raw = open(SRC, encoding='utf-8', errors='replace').read()
pages = raw.split('\f')

BODY_START, ENDNOTES_START = 8, 265
ACK_START, INDEX_START, INDEX_END = 276, 278, 285

# page index of each chapter opener -> (numeral line, title lines to drop, heading)
CHAPTERS = [
    (8,   1, 'Introduction'),
    (20,  4, '1. The Three Rules of Epidemics'),
    (35,  6, '2. The Law of the Few: Connectors, Mavens, and Salesmen'),
    (94,  6, "3. The Stickiness Factor: Sesame Street, Blue's Clues, and the Educational Virus"),
    (138, 7, '4. The Power of Context (Part One): Bernie Goetz and the Rise and Fall of New York City Crime'),
    (174, 6, '5. The Power of Context (Part Two): The Magic Number One Hundred and Fifty'),
    (198, 4, '6. Case Study: Rumors, Sneakers, and the Power of Translation'),
    (221, 5, '7. Case Study: Suicide, Smoking, and the Search for the Unsticky Cigarette'),
    (258, 3, '8. Conclusion: Focus, Test, and Believe'),
]
# the drop-cap reconstruction can leave a mangled opening word; fix explicitly
OPENING_FIX = [
    (r'^Nof long ago', 'Not long ago'),
    (r'^Oof the afternoon', 'On the afternoon'),
]

# phrase-level OCR errors a dictionary pass cannot catch (both words are valid)
PHRASE_FIX = [
    (r'\bit sold lour times\b', 'it sold four times'),
    (r'\bthe ebb and How of\b', 'the ebb and flow of'),
    (r'\bthe transformation of unknown\b', 'the transformation of unknown'),
    (r'\bhear rapid tire\b', 'hear rapid fire'),
    (r'\bI lush Puppies\b', 'Hush Puppies'),
    (r'\bHast New York\b', 'East New York'),
    (r'\bstood up On the stage\b', 'stood up on the stage'),
    (r'\bwithin five\' years\b', 'within five years'),
    (r'\bhappening all Over the\b', 'happening all over the'),
    (r'\bfrom tunning into\b', 'from running into'),
    (r'\brunning intu\b', 'running into'),
    (r'\bin a short, time\b', 'in a short time'),
    (r'\ba rush\. first the designer\b', 'a rush. First the designer'),
    (r'\bJohn Bartlctt\b', 'John Bartlett'),
    (r'\s—\s-\s', ' — '),
]

# ------------------------------------------------------------------ lexicon
DICT = set()
try:
    DICT = {w.strip().lower() for w in open('/usr/share/dict/words') if w.strip()}
except OSError:
    pass
for w in list(DICT):
    DICT |= {w + 's', w + 'es', w + 'd', w + 'ed', w + 'ing', w + 'ly'}
    if w.endswith('e'):
        DICT |= {w[:-1] + 'ing', w[:-1] + 'ed'}
    if w.endswith('y'):
        DICT |= {w[:-1] + 'ies', w[:-1] + 'ied'}
DICT |= {"don't", "doesn't", "didn't", "isn't", "wasn't", "aren't", "weren't",
         "can't", "won't", "wouldn't", "couldn't", "shouldn't", "it's", "that's",
         "there's", "they're", "we're", "you're", "i'm", "he's", "she's", "let's",
         "i've", "we've", "they've", "you've", "i'd", "we'd", "they'd", "he'd",
         "i'll", "we'll", "they'll", "you'll", "he'll", "she'll", "hasn't",
         "haven't", "hadn't", "ain't", "who's", "what's", "here's"}

CORPUS = collections.Counter(w.lower() for w in re.findall(r"[A-Za-z']{2,}", raw))
HYPHENATED = collections.Counter(
    m.lower() for m in re.findall(r"[A-Za-z]{2,}-[A-Za-z]{2,}", raw))


def known(w):
    w = w.lower().strip("'")
    return len(w) > 1 and (w in DICT or CORPUS[w] >= 8)


# ------------------------------------------------------------- dehyphenation
def join_hyphen(a, b):
    ca = re.sub(r"[^A-Za-z']+$", '', a)
    m = re.match(r"[A-Za-z']+", b)
    cb = m.group(0) if m else ''
    if not ca or not cb:
        return a + b
    solid = (ca + cb).lower()
    if HYPHENATED[(ca + '-' + cb).lower()] >= 1:
        return a + '-' + b
    if solid in DICT or CORPUS[solid] >= 2:
        return a + b
    if known(ca) and known(cb):          # two real words -> real compound hyphen
        return a + '-' + b
    return a + b


def dehyphenate(lines):
    out = []
    for ln in lines:
        if out and re.search(r'[A-Za-z]-$', out[-1].rstrip()):
            out[-1] = join_hyphen(out[-1].rstrip()[:-1], ln.lstrip())
        else:
            out.append(ln)
    return out


# ------------------------------------------------------------- OCR repair
CONFUSIONS = [
    ('c', 'e'), ('e', 'c'), ('l', 'i'), ('i', 'l'), ('l', 'f'), ('f', 'l'),
    ('t', 'f'), ('f', 't'), ('i', 't'), ('t', 'i'), ('rn', 'm'), ('m', 'rn'),
    ('c', 'o'), ('o', 'c'), ('u', 'n'), ('n', 'u'), ('h', 'b'), ('b', 'h'),
    ('v', 'y'), ('y', 'v'), ('s', 'g'), ('g', 's'), ('0', 'o'), ('1', 'l'),
    ('ii', 'n'), ('li', 'h'), ('d', 'cl'), ('cl', 'd'),
]
# unambiguous whole-word fixes seen throughout this particular scan
MANUAL = {
    'ot': 'of', 'ol': 'of', 'oi': 'of', 'irom': 'from', 'lrom': 'from',
    'thai': 'that', 'thc': 'the', 'tbe': 'the', 'lhe': 'the', 'tor': 'for',
    'docs': 'does', 'wc': 'we', 'bv': 'by', 'arc': 'are', 'arcn': 'aren',
    'ils': 'its', 'iis': 'its', 'anil': 'and', 'aiul': 'and', 'aud': 'and',
    'lie': 'he', 'llie': 'the', 'nol': 'not', 'ihe': 'the', 'ihat': 'that',
    'iu': 'in', 'lo': 'to', 'sav': 'say', 'wav': 'way', 'mav': 'may',
    'onlv': 'only', 'verv': 'very', 'anv': 'any', 'thev': 'they',
    'hv': 'by', 'ihis': 'this', 'wiih': 'with', 'whcn': 'when',
}
ENDNOTE_HEADINGS = [
    ('INTRODUCTION', 'Introduction'),
    ('ONE', 'Chapter One: The Three Rules of Epidemics'),
    ('TWO', 'Chapter Two: The Law of the Few'),
    ('THREE', 'Chapter Three: The Stickiness Factor'),
    ('FOUR', 'Chapter Four: The Power of Context (Part One)'),
    ('FIVE', 'Chapter Five: The Power of Context (Part Two)'),
    ('SIX', 'Chapter Six: Case Study'),
    ('SEVEN', 'Chapter Seven: Case Study'),
    ('EIGHT', 'Chapter Eight: Conclusion'),
]


def endnote_heading(chunk):
    """Recognise an all-caps endnote divider and return its canonical title."""
    letters = re.sub(r'[^A-Za-z]', '', chunk)
    if not letters or len(chunk) > 80:
        return None
    if sum(c.isupper() for c in letters) / len(letters) < 0.8:
        return None                       # body text, not a divider
    flat = letters.upper()
    if flat.startswith('INTRODUCTION'):
        return 'Introduction'
    if not flat.startswith('CHAPTER'):
        return None
    tail = flat[len('CHAPTER'):]
    for key, title in ENDNOTE_HEADINGS[1:]:
        if tail.startswith(key) or tail.startswith(key.replace('W', '*')):
            return title
    if tail.startswith('T') and 'LAW' in flat:      # "CHAPTER T*0"
        return 'Chapter Two: The Law of the Few'
    return None


PROTECT = {'i', 'a', 'ii', 'iii', 'iv', 'vi', 'vii', 'viii', 'ix', 'xi', 'xii',
           'pp', 'vol', 'no', 'et', 'al', 'ed', 'eds', 'ibid', 'op', 'cit',
           'tv', 'ny', 'us', 'uk', 'hiv', 'aids', 'abc', 'cbs', 'nbc', 'ctw',
           'pbs', 'mit', 'ph', 'md', 'jr', 'sr', 'st', 'mr', 'mrs', 'ms', 'dr'}


def restore_case(src, fixed):
    if src.isupper() and len(src) > 1:
        return fixed.upper()
    if src[:1].isupper():
        return fixed[:1].upper() + fixed[1:]
    return fixed


def fix_token(tok):
    low = tok.lower()
    if low in PROTECT or not re.fullmatch(r"[A-Za-z']+", tok):
        return tok
    if low in MANUAL:
        return restore_case(tok, MANUAL[low])
    if known(tok):
        return tok
    if CORPUS[low] >= 6:          # frequent -> a real proper noun, leave alone
        return tok
    cands = set()
    for a, b in CONFUSIONS:
        if a not in low:
            continue
        for m in re.finditer(re.escape(a), low):
            v = low[:m.start()] + b + low[m.start() + len(a):]
            if v != low and v in DICT and CORPUS[v] >= 3:
                cands.add(v)
    if len(cands) == 1:
        return restore_case(tok, cands.pop())
    return tok


TOKEN_RE = re.compile(r"[A-Za-z']+")


def repair_tokens(text):
    return TOKEN_RE.sub(lambda m: fix_token(m.group(0)), text)


SPACED_RE = re.compile(r"\b(?:[A-Za-z]\s){2,}[A-Za-z]\b")


def collapse_letterspacing(text):
    """Rejoin 'p h e n o m e n o n' -> 'phenomenon' (endnote pages set words
    letter by letter). Only applied when the joined form is a real word."""
    def go(m):
        joined = re.sub(r"\s+", "", m.group(0))
        if len(joined) >= 4 and (joined.lower() in DICT or CORPUS[joined.lower()] >= 2):
            return joined
        return m.group(0)
    text = SPACED_RE.sub(go, text)
    # 'T i p - ping' / 'N e w' leftovers next to a normal word fragment
    text = re.sub(r"\bp p\.", "pp.", text)
    text = re.sub(r"\bn o\.", "no.", text)
    text = re.sub(r"\bN e w\b", "New", text)
    text = re.sub(r"\bd r a w\b", "draw", text)
    return text


def rejoin_split_words(text):
    """Rejoin words the OCR broke with a space ('expla nations', 'Man hattan')."""
    def go(m):
        a, b = m.group(1), m.group(2)
        if known(a) and known(b):
            return m.group(0)
        solid = (a + b).lower()
        if solid in DICT and CORPUS[solid] >= 2:
            return a + b
        return m.group(0)
    return re.sub(r"\b([A-Za-z]{2,})\s+([a-z]{2,})\b", go, text)


# ---------------------------------------------------------------- page tidy
SECTION_RE = re.compile(r'^\s{6,}([\dJlIO]{1,2})\s*[.,]\s*$')
_DIGIT_OCR = str.maketrans({'J': '3', 'l': '1', 'I': '1', 'O': '0'})

RUNNING_HEADS = {
    'THETIPPINGPOINT', 'INTRODUCTION', 'THETHREERULESOFEPIDEMICS',
    'THELAWOFTHEFEW', 'THESTICKINESSFACTOR', 'THEPOWEROFCONTEXT',
    'RUMORSSNEAKERSANDTRANSLATION', 'SUICIDESMOKINGANDTHEUNSTICKYCIGARETTE',
    'CONCLUSION', 'ENDNOTES', 'INDEX', 'ACKNOWLEDGMENTS',
}


def strip_running_head(lines, first_only=False):
    """Drop the page's running head.

    Two edge cases: the head may be split over two lines (title, then page
    number), and OCR garbage may sit above it -- in which case the real head is
    the second line. `first_only` is for chapter openers, whose second line is
    part of the title block and must be kept.
    """
    idx = [i for i, ln in enumerate(lines) if ln.strip()]
    if not idx:
        return []
    first_is_head = re.sub(r'[^A-Za-z]', '', lines[idx[0]]).upper() in RUNNING_HEADS
    cut = idx[0]
    if len(idx) > 1 and not first_only:
        nxt = lines[idx[1]]
        stub = nxt.strip()
        is_num = len(stub) < 6 and re.fullmatch(r"[\d'.,]+", stub) \
            and not SECTION_RE.match(nxt)
        is_head = re.sub(r'[^A-Za-z]', '', nxt).upper() in RUNNING_HEADS
        if is_num or (is_head and not first_is_head):
            cut = idx[1]
    return lines[cut + 1:]


INDENT_NEW_PARA = 3


def clean_text(t):
    t = re.sub(r'\s+', ' ', t).strip()
    t = t.replace('“', '"').replace('”', '"')
    t = t.replace('‘', "'").replace('’', "'")
    t = re.sub(r'\s+([,.;:!?])', r'\1', t)
    t = re.sub(r'\(\s+', '(', t).replace(' )', ')')
    t = re.sub(r'\s*—\s*', ' — ', t)
    t = re.sub(r'\s{2,}', ' ', t)
    return t.strip()


def flush(items, buf, kind='p'):
    if buf:
        t = clean_text(' '.join(buf))
        if t:
            items.append((kind, t))
        buf.clear()


DROPCAP_RE = re.compile(r'^\s*([A-Za-z])\s{3,}(\S.*)$')


def _prefix_score(flat, remaining):
    """Fraction of `flat`'s letters matched, in order, at the head of `remaining`."""
    j, hits = 0, 0
    for ch in flat:
        k = remaining.find(ch, j, j + 4)
        if k >= 0:
            j, hits = k + 1, hits + 1
    return hits / len(flat) if flat else 0


def _consume(flat, remaining):
    j = 0
    for ch in flat:
        k = remaining.find(ch, j, j + 4)
        if k >= 0:
            j = k + 1
    return remaining[j:]


NUMERALS = ['', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT']


def title_letters(heading, n):
    """Letters-only title block, minus the numeral (already eaten as running head)."""
    body = re.sub(r'^\d+\.\s*', '', heading)
    return re.sub(r'[^A-Z]', '', body.upper())


def opener_lines(lines, skip):
    """Chapter openers: drop the title block, then rebuild the drop-cap paragraph.

    The opener page looks like

            or Hush Puppies — the classic American
      F     brushed-suede shoes with the lightweight crepe
            sole — the Tipping Point came somewhere
    had been all but dead until that point. ...

    i.e. the initial capital is set apart and the first four lines are deeply
    indented and blank-separated. Collapse that block into one paragraph.
    """
    body, i = [], 0
    # `skip` here is the letters-only title block; consume lines while they are
    # still part of it (the numeral line was already eaten as a running head).
    if isinstance(skip, str):
        remaining = skip
        while i < len(lines):
            s = lines[i].strip()
            if not s:
                i += 1
                continue
            flat = re.sub(r'[^A-Za-z]', '', s).upper()
            # OCR mangles these lines, so match loosely: >=60% of chars in order
            if flat and _prefix_score(flat, remaining) >= 0.6:
                remaining = _consume(flat, remaining)
                i += 1
                continue
            break
        body = lines[i:]
    else:
        seen = 0
        for ln in lines:
            if ln.strip() and seen < skip:
                seen += 1
                continue
            if seen >= skip:
                body.append(ln)
    body = [ln for ln in body if ln.strip()]          # kill the decorative gaps
    block, rest, cap = [], [], ''
    for i, ln in enumerate(body):
        indent = len(ln) - len(ln.lstrip())
        m = DROPCAP_RE.match(ln)
        if m and not cap:
            cap = m.group(1).upper()
            block.append('   ' + m.group(2))
            continue
        if indent >= 3 and not rest:
            block.append(ln)
            continue
        rest = body[i:]
        break
    if block:
        block = dehyphenate(block)
        joined = '   ' + cap + re.sub(r'\s+', ' ', ' '.join(b.strip() for b in block))
        return [joined] + rest
    return body


def render_range(lo, hi, opener_skip=0, opener=False):
    items, buf, mode = [], [], ['p']
    for pi in range(lo, hi):
        lines = strip_running_head(pages[pi].split('\n'),
                                   first_only=(opener and pi == lo))
        if pi == lo and opener_skip:
            if opener:
                lines = opener_lines(lines, opener_skip)
            else:
                seen, kept = 0, []
                for ln in lines:
                    if ln.strip() and seen < opener_skip:
                        seen += 1
                        continue
                    kept.append(ln)
                lines = kept
        lines = dehyphenate(lines)
        # mark block quotes: 2+ consecutive indented lines (a normal paragraph
        # indents only its first line)
        solid = [ln for ln in lines if ln.strip()]
        quoted = set()
        i = 0
        while i < len(solid):
            if len(solid[i]) - len(solid[i].lstrip()) >= INDENT_NEW_PARA:
                j = i
                while (j < len(solid)
                       and len(solid[j]) - len(solid[j].lstrip()) >= INDENT_NEW_PARA):
                    j += 1
                if j - i >= 2:
                    quoted.update(id(x) for x in solid[i:j])
                i = j
            else:
                i += 1
        prev = None                       # note: NOT reset to 'gap' at page start
        for ln in lines:
            s = ln.rstrip()
            if not s.strip():
                if prev is not None:      # ignore the blank run under the head
                    prev = 'gap'
                continue
            m = SECTION_RE.match(s)
            if m:
                flush(items, buf, mode[0])
                mode[0] = 'p'
                items.append(('sec', m.group(1).translate(_DIGIT_OCR)))
                prev = None
                continue
            indent = len(s) - len(s.lstrip())
            isq = id(ln) in quoted
            if (indent >= INDENT_NEW_PARA and not isq) or prev == 'gap' \
                    or isq != (mode[0] == 'q'):
                flush(items, buf, mode[0])
                mode[0] = 'q' if isq else 'p'
            buf.append(s.strip())
            prev = 'cont'
    flush(items, buf, mode[0])
    return items


def _gutter(lines):
    """Column where the two index columns are separated by whitespace."""
    if not lines:
        return None
    w = max(len(l) for l in lines)
    blank = [c for c in range(w) if all(len(l) <= c or l[c] == ' ' for l in lines)]
    runs, cur = [], []
    for c in blank:
        if cur and c == cur[-1] + 1:
            cur.append(c)
        else:
            if cur:
                runs.append(cur)
            cur = [c]
    if cur:
        runs.append(cur)
    runs = [r for r in runs if 25 < r[0] < w - 15]
    return max(runs, key=len)[0] if runs else None


def index_entries():
    """Read the index in column order and emit one bullet per entry."""
    lines_out = []
    for pi in range(INDEX_START, INDEX_END):
        page = [l for l in pages[pi].split('\n') if l.strip()]
        page = page[1:]                                    # running head
        g = _gutter(page)
        cols = ([[l[:g] for l in page], [l[g:] for l in page]] if g else [page])
        for col in cols:
            entry = []
            for ln in col:
                if not ln.strip():
                    continue
                indent = len(ln) - len(ln.lstrip())
                # a deeply indented line continues the previous entry
                if entry and indent >= 6:
                    entry.append(ln.strip())
                else:
                    if entry:
                        lines_out += ['- ' + collapse_letterspacing(clean_text(' '.join(entry))), '']
                    entry = [ln.strip()]
            if entry:
                lines_out += ['- ' + collapse_letterspacing(clean_text(' '.join(entry))), '']
    return lines_out




# ------------------------------------------------------------------ assemble
out = [
    '# The Tipping Point',
    '',
    '**How Little Things Can Make a Big Difference**',
    '',
    '*Malcolm Gladwell — Little, Brown and Company, 2000*',
    '',
    '> **Notă despre conversie.** Text extras automat din PDF. Stratul de text al '
    'PDF-ului provine dintr-un OCR imperfect (PDF-ul nu conține imagini ale '
    'paginilor, deci nu poate fi re-scanat). Structura — capitole, secțiuni '
    'numerotate, citate, note — a fost reconstruită, iar erorile de OCR '
    'neambigue au fost corectate automat. Rămân greșeli izolate de litere, mai '
    'ales în nume proprii și în note. Secțiunea 4 din capitolul 7 lipsește din '
    'stratul de text al PDF-ului original. Numerele de pagină din note și index '
    'se referă la ediția tipărită.',
    '',
    '---',
    '',
    '## Cuprins',
    '',
]
for _, _, h in CHAPTERS:
    label = h
    anchor = re.sub(r'[^a-z0-9]+', '-', h.lower()).strip('-')
    out.append(f'- [{label}](#{anchor})')
out += ['- [Endnotes](#endnotes)', '- [Acknowledgments](#acknowledgments)',
        '- [Index](#index)', '', '---', '']

bounds = [c[0] for c in CHAPTERS] + [ENDNOTES_START]
for n, (start, skip, heading) in enumerate(CHAPTERS):
    items = render_range(start, bounds[n + 1],
                         opener_skip=title_letters(heading, n), opener=True)
    if items and items[0][0] == 'p':
        first = items[0][1]
        for pat, rep in OPENING_FIX:
            first = re.sub(pat, rep, first)
        items[0] = ('p', first)
    out += [f'## {heading}', '']
    for k, t in items:
        out.append(f'### {t}' if k == 'sec'
                   else ('> ' + t if k == 'q' else t))
        out.append('')
    out += ['---', '']

# --- endnotes -------------------------------------------------------------
out += ['## Endnotes', '']
for k, t in render_range(ENDNOTES_START, ACK_START):
    if k == 'sec':
        continue
    t = collapse_letterspacing(t)
    # each note starts with "Page N." -- give every one its own paragraph
    for chunk in re.split(r'(?=\bPage\s*\d{1,3}\s*\.)', t):
        chunk = chunk.strip()
        if not chunk:
            continue
        title = endnote_heading(chunk)
        if title:
            out += ['### ' + title, '']
            continue
        chunk = re.sub(r'^Page\s*(\d{1,3})\s*\.\s*', r'**Page \1.** ', chunk)
        out += [chunk, '']
out += ['---', '']

# --- acknowledgments -------------------------------------------------------
out += ['## Acknowledgments', '']
for k, t in render_range(ACK_START, INDEX_START):
    if k != 'sec':
        out += [collapse_letterspacing(t), '']
out += ['---', '']

# --- index ----------------------------------------------------------------
out += ['## Index', '',
        '*Index-ul ediției tipărite, recuperat din PDF. Coloanele originale au '
        'fost desfăcute; numerele de pagină sunt cele ale ediției tipărite și '
        'sunt frecvent deformate de OCR.*', '']
out += index_entries()

text = '\n'.join(out)

# ---- OCR repair pass over the book's prose only ---------------------------
# (front matter is our own Romanian note; the index is mostly proper nouns)
front, fsep, text = text.partition('\n## Introduction\n')
head, sep, index = text.partition('\n## Index\n')
head = rejoin_split_words(repair_tokens(head))
for pat, rep in PHRASE_FIX:
    head = re.sub(pat, rep, head)
head = re.sub(r'\b([A-Za-z]{2,})-\s+([a-z]{2,})\b',
              lambda m: join_hyphen(m.group(1), m.group(2)), head)
text = front + fsep + head + sep + index
text = re.sub(r'\n{3,}', '\n\n', text).rstrip() + '\n'

dest = sys.argv[1] if len(sys.argv) > 1 else '/tmp/tp.md'
open(dest, 'w', encoding='utf-8').write(text)
print(f'wrote {dest}: {len(text.split()):,} words, {len(text):,} chars')
