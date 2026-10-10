# Changelog

## Unreleased

- Fix decoding that skipped the character immediately following a matched token.
- Match replacement tokens case-insensitively and exclude empty reverse tokens.
- Remove unused langid dependency so help and CLI run with the standard library.
- Require one operation and one input, accept empty messages, reject unknown maps,
  report file/UTF-8 failures without tracebacks, and print encoded results once.
- Add regression tests, cross-platform CI, badges, working examples and accurate
  language-map/decoding limitations. Existing MIT license remains unchanged.

No tagged release or installable package is provided yet.
