#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""
Leet Speak Encoder/Decoder

This script allows users to encode clear text into leet speak and decode leet speak text
into best-effort readable text. It supports multiple languages and provides
a customizable dictionary for leet speak substitutions.

Author: R. Morgan
AKA: CodeRancher
Date: January 20, 2024
"""

import argparse
import sys

from multilang import encode_leet, decode_leet, language_data


def display_info(text):
    """
    Display information about the text, including length in words and characters.

    Args:
        text (str): Text to analyze.
    """
    word_count = len(text.split())
    char_count = len(text)
    print(f'Text Length: {word_count} words, {char_count} characters')

def main(argv=None):
    """
    Main function to handle command-line arguments and execute leet speak encoding/decoding.
    """
    parser = argparse.ArgumentParser(description='Leet Speak Encoder/Decoder')
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('-e', '--encode', action='store_true', help='Encode clear text into leet speak')
    mode.add_argument('-d', '--decode', action='store_true', help='Decode leet speak text into clear text')
    parser.add_argument('-lang', '--language', default='en', type=str.lower, choices=sorted(language_data),
                        help='Replacement-map identifier (default: en)')
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument('-m', '--message', help='Text string to encode or decode')
    source.add_argument('-i', '--input', help='File name to read encoded/decoded text')
    parser.add_argument('-o', '--output', help='File name to save encoded/decoded text')
    parser.add_argument('-v', '--verbose', action='store_true', help='Display additional information about the text')
    args = parser.parse_args(argv)

    try:
        if args.message is not None:
            input_text = args.message
        else:
            with open(args.input, 'r', encoding='utf-8') as file:
                input_text = file.read()

        transform = encode_leet if args.encode else decode_leet
        output_text = transform(input_text, args.language)
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as file:
                file.write(output_text)
        else:
            label = 'Encoded' if args.encode else 'Decoded'
            print(f'{label} Text: {output_text}')
        if args.verbose:
            display_info(output_text)
    except (OSError, UnicodeError) as error:
        parser.exit(1, f'{parser.prog}: {error}\n')
    return 0

if __name__ == '__main__':
    sys.exit(main())

