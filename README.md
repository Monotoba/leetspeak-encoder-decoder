# leetspeak-encoder-decoder

## Introduction

The **leetspeak-encoder-decoder** provides a versatile Leet Speak encoder and decoder tool that supports multiple languages. Leet Speak, also known as 1337 speak, is an alternative alphabet used primarily on the internet, where characters are replaced with various combinations of ASCII characters.

## Contents

1. [Overview](#overview)
2. [Usage](#usage)
3. [Supported Languages](#supported-languages)
4. [Contribution](#contribution)
5. [Examples](#examples)

## Overview

### Getting LeetSpeak
Simply download or clone the repository on GitHub at github.com/monotoba/leetspeak-encoder-decoder

```bash
git clone https://github.com/monotoba/leetspeak-encoder-decoder
```

### 1. **multilang.py**
The `multilang.py` module is the core of the Leet Speak encoder and decoder. It provides character replacement dictionaries for various languages, allowing users to encode and decode text. The module includes:

- A dictionary of character replacements for multiple languages.
- Functions to get the character replacement dictionary and language dictionary module based on language identifiers.
- Leet Speak encoding and decoding functions.

### 2. **leetspeak.py**
The `leetspeak.py` script serves as the command-line interface for the Leet Speak encoder and decoder. It supports encoding and decoding of text strings and can read from/write to files. The script utilizes the `multilang.py` module.


## Usage

### 1. **multilang.py Usage**

The `multilang.py` module can be used in your Python projects. Here is an example:

```python
if __name__ == '__main__':
    language_id = 'en'

    # Get and display the character replacement dictionary
    char_replacement_dict = get_character_replacement_dict(language_id)
    print(f"The character replacement dictionary for language '{language_id}' is: {char_replacement_dict}")

    # Get and display the language dictionary module
    language_dict = get_language_dictionary_module(language_id)
    print(f"The language dictionary for language  '{language_id}' is: {language_dict}")

    # Test encoding and decoding
    test_text = "Hello, World!"
    encoded_text = encode_leet(test_text, language_id)
    decoded_text = decode_leet(encoded_text, language_id)

    print(f"Encoded Text: {encoded_text}")
    print(f"Decoded Text: {decoded_text}")
```

### 2. **leetspeak.py Usage**

The `leetspeak.py` script is designed for command-line usage. It supports the following arguments:

- `-e` or `--encode`: Encode clear text into Leet Speak.
- `-d` or `--decode`: Decode Leet Speak text into clear text.
- `-lang` or `--language`: Specify the language (default is 'en').
- `-m` or `--message`: Provide the text string to encode or decode.
- `-i` or `--input`: Specify the input file name for encoded/decoded text if not using the -m flag.
- `-o` or `--output`: Specify the output file name to save encoded/decoded text to.
- `-v` or `--verbose`: Display additional information about the text.
- 
Note: that either the -m flag or the -i flag must be use to provide input to the script.
Likewise, either -e or -d flag must be passed to indicate the input will be encoded or decoded.

Here is an example command:

```bash
python leetspeak.py --encode --language en --message "Hello, World!" --output encoded.txt
```

## Example Usage
The repo contains an examples folder that contains both encoded and decoded example text files.
These files are named either decoded_text_<land_id>.txt or encoded_text_<lang_id>.txt. 
Where <lang_id>is a placeholder for the ISO 639 language identifier such as "en" and "fr".

```bash
python leetspeak -d -i examples/encoded_text_en.txt
```

This will decode the example file encoded_text_en.txt and display the decoded text in the terminal.

```bash
python leetspeak.py -e -lang uk -i examples/decoded_text_uk.txt
```

This will encode the text in the Ukrainian example file examples/decoded_text_uk.txt and display the encoded text in the terminal.

```bash
python leetspeak -v -e -lang ar -i examples/decoded_text_ar.txt -o encoded_text_ar.txt
```
This will encode the text in the Arabic example file and write the encoded text to the encoded_text_ar.txt file. 
The use of the -v flag will also display information about the encoded text in the terminal. 

## Supported Languages

The Leet Speak encoder and decoder currently support the following languages:

- Arabic (`ar`)
- Danish (`da`)
- German (`de`)
- Greek (`el`)
- English (`en`)
- Spanish (`es`)
- Finnish (`fi`)
- French (`fr`)
- French (Canada) (`fr_ca`)
- Hebrew (`he`)
- Hindi (`hi`)
- Hawaiian (`haw`)
- Indonesian (`id`)
- Inuktitut (`iu`)
- Italian (`it`)
- Japanese (`ja`)
- Korean (`ko`)
- Malay (`ms`)
- Dutch (`nl`)
- Norwegian (`no`)
- Polish (`pl`)
- Portuguese (Brazil) (`pt_br`)
- Romanian (`ro`)
- Russian (`ru`)
- Swedish (`sv`)
- Thai (`th`)
- Turkish (`tr`)
- Ukrainian (`uk`)
- Vietnamese (`vi`)
- Chinese (`zh`)

## Contribution

The repository welcomes contributions to correct and enhance language support. If you have knowledge of Leet Speak in a 
language not currently supported or you find inaccuracies, please contribute by submitting a pull request. I am not 
multilingual and some of the supported languages simple use the english alphabet at the moment. If you can provide
language data for any of these languages please clone the repo and create a pull request with your updates. They will 
be greatly appreciated! 

## Examples

For more examples and detailed usage scenarios, please refer to the provided example code in the `multilang.py` module and the `leetspeak.py` scripts and the [User Manual](manual.md).

Feel free to experiment with different languages and text inputs to explore the versatility of the Leet Speak encoder and decoder. Your feedback and contributions are highly appreciated!
