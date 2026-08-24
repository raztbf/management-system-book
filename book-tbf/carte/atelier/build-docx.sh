#!/usr/bin/env bash
# Construiește un singur .docx din toate capitolele din manuscris/.
# Rulează din orice director:  bash carte/atelier/build-docx.sh
set -euo pipefail

CARTE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MS="$CARTE/manuscris"
OUT="$CARTE/export"
mkdir -p "$OUT"

STAMP="$(date +%Y-%m-%d)"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

python3 - "$MS" "$TMP/combined.md" "$STAMP" <<'PY'
import sys, pathlib, re

ms, out, stamp = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]), sys.argv[3]
PAGEBREAK = '\n```{=openxml}\n<w:p><w:r><w:br w:type="page"/></w:r></w:p>\n```\n\n'

parts = ["""---
title: "The Business Framework"
author: "Răzvan Căzănescu"
subtitle: "Capitolele 1–3 · manuscris de lucru · %s"
lang: en
---

""" % stamp]

chapters = sorted(p for p in ms.glob("[0-9][0-9]-*.md"))
for i, f in enumerate(chapters):
    s = f.read_text()

    # subtitlul capitolului (### imediat după titlul H1) devine paragraf italic,
    # ca să nu concureze cu numerele de secțiune
    s = re.sub(r"(^# .+\n\n)### (.+)\n", r"\1*\2*\n", s, count=1, flags=re.M)

    # numerele de secțiune urcă la H2 ca să nu fie îngropate în cuprins
    s = re.sub(r"^### (\d+)$", r"## \1", s, flags=re.M)

    if i:
        parts.append(PAGEBREAK)
    parts.append(s.rstrip() + "\n")

out.write_text("\n".join(parts))
print(f"  {len(chapters)} capitole combinate")
PY

pandoc "$TMP/combined.md" \
  --from=markdown+raw_attribute \
  --to=docx \
  --resource-path="$MS" \
  --toc --toc-depth=1 \
  --standalone \
  --output="$OUT/The-Business-Framework.docx"

echo "  → $OUT/The-Business-Framework.docx"
