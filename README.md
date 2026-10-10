# LeetSpeak encoder/decoder

[![Tests](https://github.com/Monotoba/leetspeak-encoder-decoder/actions/workflows/tests.yml/badge.svg)](https://github.com/Monotoba/leetspeak-encoder-decoder/actions/workflows/tests.yml)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Status](https://img.shields.io/badge/status-experimental-orange)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

Turn text into playful 1337 substitutions, or decode it into best-effort readable
text. Use the Python CLI for messages and UTF-8 files, or import the two functions
in your own scripts. No third-party dependencies are needed.

```text
Hello, World!  →  |-|3||0, W0r|d!  →  Hello, world!
```

**Experimental:** decoding is lossy, and the language maps are community drafts.
This is character substitution, not encryption, translation or automatic language
recognition. Original capitalization, ambiguous characters and deleted characters
cannot be recovered reliably.

## Try it

Use Python 3.10+; no package installation is required:

```sh
git clone https://github.com/Monotoba/leetspeak-encoder-decoder.git
cd leetspeak-encoder-decoder
python leetspeak.py --help
python leetspeak.py --encode --message "Hello, World!"
python leetspeak.py --decode --message "|-|3||0, W0r|d!"
python leetspeak.py --encode --language uk --input examples/decoded_text_uk.txt
```

Select exactly one operation (`--encode` or `--decode`) and one input (`--message`
or `--input`). `--output FILE` writes only the transformed text as UTF-8 and
replaces an existing file. Without it, a labeled result prints once to the terminal.
`--verbose` additionally prints word and character counts. An empty message is
valid. See the [manual](manual.md) for options, errors and decoding rules.

## Use from Python

```python
from multilang import encode_leet, decode_leet

encoded = encode_leet("Hello, World!", "en")
print(encoded)               # |-|3||0, W0r|d!
print(decode_leet(encoded))   # Hello, world!
```

## Language-map status

Thirty identifiers are accepted, but they do **not** represent thirty fully
implemented language systems. `--help` lists the identifiers.

| Identifiers | Current mapping |
| --- | --- |
| en | Eleven Latin-letter substitutions |
| da, de, es, fi, fr, fr_ca, haw, id, it, ms, nl, no, pl, pt_br, ro, sv, tr, vi | Same Latin table as en; no language-specific accented-letter coverage |
| he, hi, iu, ja, ko, th, zh | Latin placeholder table; no native-script substitution coverage |
| ar, el, ru, uk | Distinct Arabic, Greek or Cyrillic draft tables; incomplete and potentially ambiguous |

Many replacement tokens collide, particularly in the draft Arabic/Cyrillic maps.
Decoding selects the longest matching token and uses the last dictionary entry
for an ambiguous case-insensitive token, then applies sentence-style casing to
the entire result. It does not use NLTK or a word dictionary. The legacy dictionary
module lookup is metadata only; it does not add linguistic decoding.

The Arabic source table contains duplicate keys (Python retains the last value)
and removes the elongation mark `ـ` during encoding. The decoder cannot recreate
removed marks. Language experts and native speakers are especially welcome to
improve these tables with examples and tests.

## Development and contributions

```sh
python -m unittest discover -s tests -v
```

CI runs on Linux, Windows and Intel macOS with Python 3.10/3.12. Tests cover token
boundaries, ambiguous/empty tokens, Unicode, CLI argument validation and file I/O.
The existing `examples/` files are historical demonstrations, not verified
round-trip fixtures.

See [CONTRIBUTING.md](CONTRIBUTING.md) for focused starter tasks. Report a concrete
input, selected language, expected output and actual output in an
[issue](https://github.com/Monotoba/leetspeak-encoder-decoder/issues). No release
or PyPI package is currently published. See [changes](CHANGELOG.md).

Licensed under the [MIT License](LICENSE).
