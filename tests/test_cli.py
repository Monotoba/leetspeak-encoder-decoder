import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run_cli(*args):
    return subprocess.run([sys.executable, str(ROOT / 'leetspeak.py'), *args],
                          capture_output=True, text=True, encoding='utf-8',
                          timeout=10)


class CliTests(unittest.TestCase):
    def test_help_without_third_party_dependencies(self):
        result = subprocess.run([sys.executable, '-S', str(ROOT / 'leetspeak.py'),
                                 '--help'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_encode_prints_once(self):
        result = run_cli('-e', '-m', 'Hello, World!')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, 'Encoded Text: |-|3||0, W0r|d!\n')

    def test_decode_and_uppercase_language_identifier(self):
        result = run_cli('-d', '-lang', 'EN', '-m', '48')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, 'Decoded Text: Ab\n')

    def test_empty_message_is_valid(self):
        self.assertEqual(run_cli('-e', '-m', '').stdout, 'Encoded Text: \n')

    def test_invalid_argument_combinations(self):
        for args in [(), ('-m', 'x'), ('-e',), ('-e', '-d', '-m', 'x'),
                     ('-e', '-m', 'x', '-i', 'missing'),
                     ('-e', '-lang', 'invalid', '-m', 'x')]:
            with self.subTest(args=args):
                result = run_cli(*args)
                self.assertEqual(result.returncode, 2)
                self.assertNotIn('Traceback', result.stderr)

    def test_utf8_file_output_and_verbose_count(self):
        with tempfile.TemporaryDirectory() as directory:
            source, output = Path(directory) / 'input.txt', Path(directory) / 'out.txt'
            source.write_text('AB 🙂\n', encoding='utf-8')
            result = run_cli('-e', '-i', str(source), '-o', str(output), '-v')
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(output.read_text(encoding='utf-8'), '48 🙂\n')
            self.assertEqual(result.stdout, 'Text Length: 2 words, 5 characters\n')

    def test_input_and_output_errors_are_controlled(self):
        with tempfile.TemporaryDirectory() as directory:
            invalid = Path(directory) / 'invalid.txt'
            invalid.write_bytes(b'\xff')
            for args in [('-e', '-i', str(Path(directory) / 'missing')),
                         ('-d', '-i', str(invalid)),
                         ('-e', '-m', 'AB', '-o', directory)]:
                with self.subTest(args=args):
                    result = run_cli(*args)
                    self.assertEqual(result.returncode, 1)
                    self.assertNotIn('Traceback', result.stderr)


if __name__ == '__main__':
    unittest.main()
