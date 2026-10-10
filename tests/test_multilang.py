import unittest

from multilang import (create_reverse_dict, decode_leet, encode_leet,
                       get_character_replacement_dict, language_data)


class MappingTests(unittest.TestCase):
    def test_adjacent_tokens_are_not_skipped(self):
        self.assertEqual(decode_leet('48'), 'Ab')
        self.assertEqual(decode_leet('|-|17'), 'Hit')

    def test_multi_character_tokens_take_priority(self):
        self.assertEqual(decode_leet('|_|'), 'U')
        self.assertEqual(decode_leet('|-|3||0, W0r|d!'), 'Hello, world!')

    def test_unknown_characters_and_spacing_survive(self):
        self.assertEqual(decode_leet('🙂\n48!'), '🙂\nab!')
        self.assertEqual(encode_leet('🙂\nAB!'), '🙂\n48!')

    def test_empty_replacement_cannot_match_every_position(self):
        self.assertNotIn('', create_reverse_dict({'A': '4', 'ـ': ''}))
        self.assertEqual(decode_leet('🙂!', 'ar'), '🙂!')

    def test_case_insensitive_replacement_values(self):
        self.assertEqual(decode_leet('r', 'ru'), 'Г')
        self.assertEqual(decode_leet('R', 'ru'), 'Г')

    def test_lossy_case_and_collision_policy_is_explicit(self):
        self.assertEqual(decode_leet(encode_leet('HeLLo')), 'Hello')
        self.assertEqual(create_reverse_dict({'A': 'x', 'B': 'X'}), {'X': 'B'})

    def test_empty_and_unsupported_input(self):
        self.assertEqual(encode_leet(''), '')
        self.assertEqual(decode_leet(''), '')
        with self.assertRaises(ValueError):
            get_character_replacement_dict('invalid')

    def test_each_configured_map_handles_unicode(self):
        for language in language_data:
            with self.subTest(language=language):
                encoded = encode_leet('AB 🙂\n', language)
                self.assertIsInstance(decode_leet(encoded, language), str)
                self.assertIn('🙂', encoded)


if __name__ == '__main__':
    unittest.main()
