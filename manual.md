# LeetSpeak CLI and API manual

Use Python 3.10+ from the repository directory. No external dependencies are needed.

```sh
python leetspeak.py -e -m "Hello, World!"
python leetspeak.py -d -m "|-|3||0, W0r|d!"
python leetspeak.py -e -lang uk -i examples/decoded_text_uk.txt -o encoded.txt
```

## Options

| Option | Meaning |
| --- | --- |
| -e, --encode | Apply the selected character substitutions |
| -d, --decode | Greedy best-effort decoding, with sentence-style result casing |
| -lang, --language | Map identifier; default en; CLI accepts upper/lowercase IDs |
| -m, --message | Literal text, including an empty string |
| -i, --input | UTF-8 input file |
| -o, --output | UTF-8 output file; existing contents are replaced |
| -v, --verbose | Print transformed text word/character counts |
| -h, --help | Show usage and accepted language identifiers |

Exactly one operation and exactly one input are required. Conflicting/missing
options and unsupported language identifiers return exit status 2. File or encoding
errors return 1 without a traceback. Successful operations and help return 0.
Without an output file, one labeled result prints to stdout. With an output file,
only verbose counts print to stdout; the file contains no label or added newline.
Input line breaks are preserved by the transformations (text-file I/O uses Python's
normal newline conversion). File writes are not atomic and may truncate an existing
file before a later error. Use separate input/output paths and retain originals.

## How substitution works

Encoding tests each character's uppercase form against the selected mapping and
leaves unmapped characters as supplied. It does not normalize Unicode or preserve
case information for replaced letters.

Decoding ignores empty replacement values, compares nonempty tokens without case,
and tests longer tokens first. Every matched token consumes exactly its own
length. When several source letters share a case-insensitive token, the last
entry wins; there is no word-level disambiguation. The accumulated output uses
`str.capitalize()`, which capitalizes its first character and lowercases the rest.
Original case, literal digits that resemble tokens, collisions and removed
characters cannot be recovered reliably. For example, `48` decodes to `Ab`, while
`|-|17` decodes to `Hit`. This is not a reversible cipher.

## API

```python
from multilang import encode_leet, decode_leet, get_character_replacement_dict

encoded = encode_leet("Hello, World!", "en")
decoded = decode_leet(encoded, "en")
replacements = get_character_replacement_dict("en")
```

API language identifiers are exact keys (unlike the case-normalizing CLI).
Unknown identifiers raise ValueError. `get_character_replacement_dict` returns the
shared mutable table; treat it as read-only unless intentionally customizing it.
`create_reverse_dict` excludes empty tokens and normalizes token keys to uppercase.
`get_language_dictionary_module` retains legacy metadata and may print warnings;
it does not import a package or perform linguistic decoding.

See the [README language status table](README.md#language-map-status) before
assuming native-script support. Existing example files predate the regression
fixes and are illustrative rather than verified inverse pairs.
