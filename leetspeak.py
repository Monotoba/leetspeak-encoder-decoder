#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""
Leet Speak Encoder/Decoder

This script allows users to encode clear text into leet speak and decode leet speak text
back into its original alphabetical form. It supports multiple languages and provides
a customizable dictionary for leet speak substitutions.

Author: R. Morgan
AKA: CodeRancher
Date: January 20, 2024
"""

import argparse
from collections import Counter
from langid import classify  # Install langid: pip install langid

from multilang import encode_leet, decode_leet


def display_info(text):
    """
    Display information about the text, including length in words and characters.

    Args:
        text (str): Text to analyze.
    """
    word_count = len(text.split())
    char_count = len(text)
    print(f'Text Length: {word_count} words, {char_count} characters')

def main():
    """
    Main function to handle command-line arguments and execute leet speak encoding/decoding.
    """
    parser = argparse.ArgumentParser(description='Leet Speak Encoder/Decoder')
    parser.add_argument('-e', '--encode', action='store_true', help='Encode clear text into leet speak')
    parser.add_argument('-d', '--decode', action='store_true', help='Decode leet speak text into clear text')
    parser.add_argument('-lang', '--language', default='en', help='ISO language indicator (default: en)')
    parser.add_argument('-m', '--message', help='Text string to encode or decode')
    parser.add_argument('-i', '--input', help='File name to read encoded/decoded text')
    parser.add_argument('-o', '--output', help='File name to save encoded/decoded text')
    parser.add_argument('-v', '--verbose', action='store_true', help='Display additional information about the text')
    args = parser.parse_args()

    language_id = args.language.lower()

    if args.message:
        input_text = args.message
    elif args.input:
        with open(args.input, 'r', encoding='utf-8') as file:
            input_text = file.read()
    else:
        raise ValueError("Please provide either a text string (-m) or an input file (-i).")

    if args.encode:
        output_text = encode_leet(input_text, language_id)
        print(f'Encoded Leet Speak Text: {output_text}')

        if args.verbose:
            display_info(output_text)

        if args.output:
            with open(args.output, 'w', encoding='utf-8') as file:
                file.write(output_text)
        else:
            print(f"Encoded Text: {output_text}")

    elif args.decode:
        decoded_text = decode_leet(input_text, language_id)

        if args.verbose:
            display_info(decoded_text)

        if args.output:
            with open(args.output, 'w', encoding='utf-8') as file:
                file.write(decoded_text)
        else:
            print(f"Decoded Text: {decoded_text}")

if __name__ == '__main__':
    main()
