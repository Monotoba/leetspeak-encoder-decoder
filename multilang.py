#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""
multilang.py - Multilingual Character Replacement Module

This module provides character replacement dictionaries for various languages to support text encoding and decoding.
It includes language-specific dictionaries and modules for decoding.

Author: R. Morgan

Usage:
- Use `get_character_replacement_dict(lang_id)` to obtain the character replacement dictionary for a specific language.
- Use `get_language_dictionary_module(lang_id)` to get the module to import for language dictionary based on the language identifier.

Example:
    if __name__ == '__main__':
        language_id = 'en'

        char_replacement_dict = get_character_replacement_dict(language_id)
        print(f"The character replacement dictionary for language '{language_id}' is: {char_replacement_dict}")

        language_dict = get_language_dictionary_module(language_id)
        print(f"The language dictionary for language  '{language_id}' is: {language_dict}")

"""

# Define the dictionary of character replacements and language dictionary modules
language_data = {
'ar': (
    {'ا': '4', 'ب': '8', 'ت': '7', 'ث': '6', 'ج': '9', 'ح': '|-|', 'خ': 'x', 'د': '|)', 'ذ': '0', 'ر': '®',
     'ز': '2', 'س': '5', 'ش': '$', 'ص': '|_', 'ض': '|_', 'ط': '7', 'ظ': 'z', 'ع': '3', 'غ': '9', 'ف': '|*', 'ق': 'q',
     'ك': '|<', 'ل': '|', 'م': '|v|', 'ن': '|\\|', 'ه': '|-|', 'و': '0', 'ي': '1', 'ؤ': '|_|',
     'ة': 'h', 'و': 'w', 'ج': 'j', 'د': 'd', 'ت': 't', 'ك': 'k', 'ل': 'l', 'أ': 'a', 'ر': 'r', 'م': 'm', 'ي': 'y',
     'س': 's', 'ح': 'h', 'ف': 'f', 'ن': 'n', 'ء': '`', 'ق': 'q', 'ط': 't', 'ع': 'e', 'ه': 'h', 'ئ': '}', 'و': 'o',
     'ج': 'j', 'د': 'd', 'ة': 'a', 'و': 'w', 'ج': 'j', 'د': 'd', 'ت': 't', 'ك': 'k', 'ل': 'l', 'أ': 'a', 'ر': 'r',
     'م': 'm', 'ي': 'y', 'س': 's', 'ح': 'h', 'ف': 'f', 'ن': 'n', 'ء': '`', 'ق': 'q', 'ط': 't', 'ع': 'e', 'ه': 'h',
     'ئ': '}', 'ـ': ''},
    'custom'),
    'da': (
        {'A': '4', 'B': '8', 'L': '|', 'E': '3', 'G': '9', 'H': '|-|', 'I': '1', 'O': '0', 'S': '5', 'T': '7', 'U': '|_|'},
        'custom'),
    'de': (
        {'A': '4', 'B': '8', 'L': '|', 'E': '3', 'G': '9', 'H': '|-|', 'I': '1', 'O': '0', 'S': '5', 'T': '7', 'U': '|_|'},
        'nltk'),
    'el': (
        {'Α': '4', 'Β': '8', 'Λ': '|', 'Ε': '3', 'Γ': '9', 'Η': '|-|', 'Ι': '1', 'Ο': '0', 'Σ': '5', 'Τ': '7', 'Υ': '|_|'},
        'custom'),
    'en': (
        {'A': '4', 'B': '8', 'L': '|', 'E': '3', 'G': '9', 'H': '|-|', 'I': '1', 'O': '0', 'S': '5', 'T': '7', 'U': '|_|'},
        'nltk'),
    'es': (
        {'A': '4', 'B': '8', 'L': '|', 'E': '3', 'G': '9', 'H': '|-|', 'I': '1', 'O': '0', 'S': '5', 'T': '7', 'U': '|_|'},
        'nltk'),
    'fi': (
        {'A': '4', 'B': '8', 'L': '|', 'E': '3', 'G': '9', 'H': '|-|', 'I': '1', 'O': '0', 'S': '5', 'T': '7', 'U': '|_|'},
        'custom'),
    'fr': (
        {'A': '4', 'B': '8', 'L': '|', 'E': '3', 'G': '9', 'H': '|-|', 'I': '1', 'O': '0', 'S': '5', 'T': '7', 'U': '|_|'},
        'nltk'),
    'fr_ca': (
        {'A': '4', 'B': '8', 'L': '|', 'E': '3', 'G': '9', 'H': '|-|', 'I': '1', 'O': '0', 'S': '5', 'T': '7', 'U': '|_|'},
        'nltk'),
    'he': (
        {'A': '4', 'B': '8', 'L': '|', 'E': '3', 'G': '9', 'H': '|-|', 'I': '1', 'O': '0', 'S': '5', 'T': '7', 'U': '|_|'},
        'custom'),
    'hi': (
        {'A': '4', 'B': '8', 'L': '|', 'E': '3', 'G': '9', 'H': '|-|', 'I': '1', 'O': '0', 'S': '5', 'T': '7', 'U': '|_|'},
        'custom'),
    'haw': (
        {'A': '4', 'B': '8', 'L': '|', 'E': '3', 'G': '9', 'H': '|-|', 'I': '1', 'O': '0', 'S': '5', 'T': '7', 'U': '|_|'},
        'custom'),
    'id': (
        {'A': '4', 'B': '8', 'L': '|', 'E': '3', 'G': '9', 'H': '|-|', 'I': '1', 'O': '0', 'S': '5', 'T': '7', 'U': '|_|'},
        'custom'),
    'iu': (
        {'A': '4', 'B': '8', 'L': '|', 'E': '3', 'G': '9', 'H': '|-|', 'I': '1', 'O': '0', 'S': '5', 'T': '7', 'U': '|_|'},
        'custom'),
    'it': (
        {'A': '4', 'B': '8', 'L': '|', 'E': '3', 'G': '9', 'H': '|-|', 'I': '1', 'O': '0', 'S': '5', 'T': '7', 'U': '|_|'},
        'nltk'),
    'ja': (
        {'A': '4', 'B': '8', 'L': '|', 'E': '3', 'G': '9', 'H': '|-|', 'I': '1', 'O': '0', 'S': '5', 'T': '7', 'U': '|_|'},
        'nltk'),
    'ko': (
        {'A': '4', 'B': '8', 'L': '|', 'E': '3', 'G': '9', 'H': '|-|', 'I': '1', 'O': '0', 'S': '5', 'T': '7', 'U': '|_|'},
        'custom'),
    'ms': (
        {'A': '4', 'B': '8', 'L': '|', 'E': '3', 'G': '9', 'H': '|-|', 'I': '1', 'O': '0', 'S': '5', 'T': '7', 'U': '|_|'},
        'custom'),
    'nl': (
        {'A': '4', 'B': '8', 'L': '|', 'E': '3', 'G': '9', 'H': '|-|', 'I': '1', 'O': '0', 'S': '5', 'T': '7', 'U': '|_|'},
        'nltk'),
    'no': (
        {'A': '4', 'B': '8', 'L': '|', 'E': '3', 'G': '9', 'H': '|-|', 'I': '1', 'O': '0', 'S': '5', 'T': '7', 'U': '|_|'},
        'custom'),
    'pl': (
        {'A': '4', 'B': '8', 'L': '|', 'E': '3', 'G': '9', 'H': '|-|', 'I': '1', 'O': '0', 'S': '5', 'T': '7', 'U': '|_|'},
        'nltk'),
    'pt_br': (
        {'A': '4', 'B': '8', 'L': '|', 'E': '3', 'G': '9', 'H': '|-|', 'I': '1', 'O': '0', 'S': '5', 'T': '7', 'U': '|_|'},
        'nltk'),
    'ro': (
        {'A': '4', 'B': '8', 'L': '|', 'E': '3', 'G': '9', 'H': '|-|', 'I': '1', 'O': '0', 'S': '5', 'T': '7', 'U': '|_|'},
        'custom'),
    'ru': (
        {'А': '4', 'Б': '6', 'В': 'B', 'Г': 'r', 'Д': 'g', 'Е': 'e', 'Є': '3', 'Ж': 'ж', 'З': '3', 'И': 'u', 'І': 'i',
         'Ї': 'i', 'Й': 'й', 'К': 'k', 'Л': 'l', 'М': 'M', 'Н': 'H', 'О': '0', 'П': 'n', 'Р': 'p', 'С': 'c', 'Т': 'T',
         'У': 'y', 'Ф': 'ф', 'Х': 'x', 'Ц': 'u', 'Ч': '4', 'Ш': 'ш', 'Щ': 'щ', 'Ь': 'b', 'Ю': '10', 'Я': '9'}, 'nltk'),
    'sv': (
        {'A': '4', 'B': '8', 'L': '|', 'E': '3', 'G': '9', 'H': '|-|', 'I': '1', 'O': '0', 'S': '5', 'T': '7', 'U': '|_|'},
        'custom'),
    'th': (
        {'A': '4', 'B': '8', 'L': '|', 'E': '3', 'G': '9', 'H': '|-|', 'I': '1', 'O': '0', 'S': '5', 'T': '7', 'U': '|_|'},
        'custom'),
    'tr': (
        {'A': '4', 'B': '8', 'L': '|', 'E': '3', 'G': '9', 'H': '|-|', 'I': '1', 'O': '0', 'S': '5', 'T': '7', 'U': '|_|'},
        'custom'),
    'uk': (
        {'А': '4', 'Б': '6', 'В': 'B', 'Г': 'r', 'Д': 'g', 'Е': 'e', 'Є': '3', 'Ж': 'ж', 'З': '3', 'И': 'u', 'І': 'i',
         'Ї': 'i', 'Й': 'й', 'К': 'k', 'Л': 'l', 'М': 'M', 'Н': 'H', 'О': '0', 'П': 'n', 'Р': 'p', 'С': 'c', 'Т': 'T',
         'У': 'y', 'Ф': 'ф', 'Х': 'x', 'Ц': 'u', 'Ч': '4', 'Ш': 'ш', 'Щ': 'щ', 'Ь': 'b', 'Ю': '10', 'Я': '9'}, 'nltk'),
    'vi': (
        {'A': '4', 'B': '8', 'L': '|', 'E': '3', 'G': '9', 'H': '|-|', 'I': '1', 'O': '0', 'S': '5', 'T': '7', 'U': '|_|'},
        'custom'),
    'zh': (
        {'A': '4', 'B': '8', 'L': '|', 'E': '3', 'G': '9', 'H': '|-|', 'I': '1', 'O': '0', 'S': '5', 'T': '7', 'U': '|_|'},
        'nltk'),
}


def get_character_replacement_dict(lang_id: str) -> dict:
    """
    Get the character replacement dictionary for a given language.

    Args:
        lang_id (str): Language identifier.

    Returns:
        dict: Character replacement dictionary for the specified language.

    Raises:
        ValueError: If the language ID is not supported.
    """
    if lang_id in language_data:
        char_replacement_dict, _ = language_data[lang_id]
        return char_replacement_dict
    else:
        raise ValueError(f"Unsupported language ID: '{lang_id}'.")

def create_reverse_dict(original_dict):
    return {v: k for k, v in original_dict.items()}

def get_language_dictionary_module(lang_id: str) -> str:
    """
    Get the module to import for language dictionary based on the language identifier.

    Args:
        lang_id (str): Language identifier.

    Returns:
        str: Module to import for language dictionary.

    Raises:
        ValueError: If the language ID is not supported.
    """
    if lang_id in language_data:
        _, module_to_import = language_data[lang_id]

        if module_to_import == 'custom':
            print(f"Warning: The language '{lang_id}' requires a custom language dictionary for decoding.")
            print("Defaulting to language dictionary NLTK for decoding.")
            module_to_import = 'nltk'
    else:
        raise ValueError(f"Unsupported language ID: '{lang_id}'.")

    return module_to_import


def decode_leet(cypher_text: str, lang_id: str = 'en'):
    """
    Decode leet speak text into its original alphabetical form.

    Args:
        cypher_text (str): Leet speak text to decode.
        lang_id (str): ISO language indicator.

    Returns:
        str: Decoded text.
    """
    dictionary = get_character_replacement_dict(lang_id)
    reverse_lookup_dict = create_reverse_dict(dictionary)
    decoded_text = ''

    i = 0
    while i < len(cypher_text):
        found_multi_char = False
        for multi_char in sorted(reverse_lookup_dict.keys(), key=len, reverse=True):
            if cypher_text[i:i + len(multi_char)].lower() == multi_char:
                decoded_text += reverse_lookup_dict[multi_char].lower()
                i += len(multi_char)
                found_multi_char = True
                break

        if not found_multi_char:
            char = cypher_text[i].lower()
            if char in reverse_lookup_dict:
                decoded_text += reverse_lookup_dict[char].lower()
            else:
                decoded_text += char
            i += 1

    # TODO: Add support for language dictionaries to be used for decoding in case of ambiguity
    decoded_text = decoded_text.capitalize()
    return decoded_text


def encode_leet(input_text: str, lang_id: str='en'):
    """
    Encode the input text using Leet (1337) speak.

    Parameters:
    - input_text (str): The input text to be encoded.
    - lang_id (str): The language ID.

    Returns:
    - output_text (str): The Leet encoded text.
    """
    dictionary = get_character_replacement_dict(lang_id)
    output_text = ""

    for char in input_text:
        # Check if the character is in the replacement dictionary
        if char.upper() in dictionary:
            output_text += dictionary[char.upper()]
        else:
            output_text += char

    return output_text


# Example usage in a main guard:
if __name__ == '__main__':
    language_id = 'en'

    # Get and display the character replacement dictionary
    char_replacement_dict = get_character_replacement_dict(language_id)
    print(f"The character replacement dictionary for language '{language_id}' is: {char_replacement_dict}")

    # Get and display the language dictionary module
    language_dict = get_language_dictionary_module(language_id)
    print(f"The language dictionary for language  '{language_id}' is: {language_dict}")

    # Test encoding
    test_text = "Even if you're on the right track, you'll get run over if you just sit there."
    # Apply leet-speak encoding using the dictionary
    encoded_text = encode_leet(test_text, language_id)
    encoded_text = encoded_text.capitalize()
    print(f"Encoded Text: {encoded_text}")

    # Test decoding
    # Use the encoded text from the previous step
    clear_text = decode_leet(encoded_text, language_id)
    clear_text = clear_text.capitalize()
    print(f"Decoded Text: {clear_text}")
