# Contributing

Keep changes focused on the existing CLI and mapping functions. Use Python 3.10+
and run `python -m unittest discover -s tests -v`; no dependencies are required.
Add a regression test for every behavior change and a clear local Git commit.

Useful starter contributions:

- Replace native-script placeholder maps with documented community substitutions.
- Review the Arabic duplicate keys and Cyrillic token collisions with native speakers.
- Add checked input/output examples explaining ambiguity rather than claiming exact reversibility.
- Improve error messages or decoding performance while retaining documented behavior.

For mapping changes, include the language, source characters, intended tokens,
collision policy and concrete examples. Do not claim a universal LeetSpeak standard
or rely on a word dictionary that is not implemented. Preserve unrelated maps and
public function names. CI must pass before merging.

Report bugs through GitHub issues with Python/OS version, command, input and
expected/actual output. Pull requests should explain the user-visible fix and tests.
