# LeetSpeak 0.1.0a1 — Initial experimental alpha

A dependency-free Python CLI and API for playful 1337 substitutions and
best-effort decoding. This alpha is intended for evaluation and contributions;
it does not claim complete multilingual support or reversible encoding.

## Included

- Encoding/decoding of messages and UTF-8 files with the existing draft maps.
- Correct token consumption: adjacent substitutions no longer lose characters.
- Longest-token-first, case-insensitive decoding; empty reverse tokens excluded.
- CLI validation requiring one operation/input, support for empty messages,
  controlled file/encoding errors, and one printed result.
- Regression tests, cross-platform CI, badges, corrected documentation and
  contributor guidance. MIT license remains unchanged.

## Run from source

Download and extract a GitHub source archive. From its project directory with
Python 3.10+:

```sh
python leetspeak.py --help
python leetspeak.py --encode --message "Hello, World!"
python leetspeak.py --decode --message "|-|3||0, W0r|d!"
python -m unittest discover -s tests -v
```

Expected transformation: Hello, World! → |-|3||0, W0r|d! → Hello, world!
No third-party dependencies or pip installation are required. No PyPI package
or wheel is provided. See [manual](manual.md) for file/output options and errors.

## Validation

15 regression tests pass locally. Release preparation uses six CI configurations:
Linux, Windows and Intel macOS with Python 3.10/3.12, covering token boundaries,
Unicode, input/output files, missing/conflicting arguments and controlled errors.
Successful CI verifies this code behavior, not linguistic accuracy of draft maps.

## Known shortcomings

- Decoding is lossy. Case, literal digits resembling tokens, ambiguous mappings
  and characters removed during encoding cannot be recovered reliably.
- Thirty identifiers are accepted, but most reuse the English Latin table.
  Hebrew, Hindi, Inuktitut, Japanese, Korean, Thai and Chinese have Latin-only
  placeholders. Arabic, Greek, Russian and Ukrainian tables remain unverified
  community drafts. See the [map-status table](README.md#language-map-status).
- The Arabic table contains duplicate source keys; Python retains their final
  values. Token collisions use the last dictionary entry, and encoding removes
  the elongation mark. There is no word-level disambiguation or language detection.
- Decoding applies sentence-style casing to the whole output. Unicode is not
  normalized. Historical example-file pairs are demonstrations, not verified
  round-trip fixtures.
- --output replaces existing contents. Writes are not atomic and may leave a
  truncated/partial file after errors. Keep original files and use separate paths.
- The API exposes mutable mapping dictionaries. The legacy language-dictionary
  helper returns metadata only; it does not load NLTK or improve decoding.

This tool performs text substitution, not encryption or translation. Native-speaker
map reviews and tested examples are the main contribution priorities.
