# LeetSpeak Encoder/Decoder User Manual

## Table of Contents

1. [Quick Start](#quick-start)
2. [Introduction](#introduction)
3. [Installation](#installation)
4. [Usage](#usage)
   - [Command-Line Arguments](#command-line-arguments)
   - [Examples](#examples)
5. [Adding Additional Language Support](#adding-additional-language-support)
6. [Unsupported Languages](#unsupported-languages)
7. [Example Text Files](#example-text-files)
8. [Appendix: Adding Support for an Unsupported Language](#appendix-adding-support-for-an-unsupported-language)
9. [Contributing and Source Code](#contributing-and-source-code)

## Quick Start

1. Clone the repository from GitHub:

   ```bash
   git clone https://github.com/your_username/leetspeak.git
   ```

2. Navigate to the `leetspeak` directory:

   ```bash
   cd leetspeak
   ```

3. Run the LeetSpeak Encoder/Decoder:

   ```bash
   python leetspeak.py -e -lang en -m "Hello, World!" -o encoded.txt
   ```

   This command encodes the text "Hello, World!" using English leet speak and saves the result to a file named `encoded.txt`.

4. To decode the text back:

   ```bash
   python leetspeak.py -d -lang en -m "$(cat encoded.txt)" -o decoded.txt
   ```

   This command decodes the content of `encoded.txt` and saves the result to a file named `decoded.txt`.

## Introduction

Welcome to the LeetSpeak Encoder/Decoder user manual. This tool allows you to encode clear text into leet speak and decode leet speak text back into its original alphabetical form. The tool supports multiple languages and provides a customizable dictionary for leet speak substitutions.

## Installation

1. Clone the repository from GitHub:

   ```bash
   git clone https://github.com/your_username/leetspeak.git
   ```

2. Navigate to the `leetspeak` directory:

   ```bash
   cd leetspeak
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Command-Line Arguments

- `-e` or `--encode`: Encode clear text into leet speak.
- `-d` or `--decode`: Decode leet speak text into clear text.
- `-lang` or `--language`: Specify the language for encoding/decoding (default: 'en').
- `-m` or `--message`: The text string to encode or decode.
- `-i` or `--input`: The file name to read the encoded/decoded text from.
- `-o` or `--output`: The file name to write the encoded/decoded text to.
- `-v` or `--verbose`: Display additional information about the text.

### Examples

#### Encode Text:

```bash
python leetspeak.py -e -lang en -m "Hello, World!" -o encoded.txt
```

#### Decode Text:

```bash
python leetspeak.py -d -lang en -m "$(cat encoded.txt)" -o decoded.txt
```

## Adding Additional Language Support

To add additional language support to leetspeak, follow the proceedure outlined in [Appendix A](#appendix-a-adding-support-for-an-unsupported-language)

## Unsupported Languages

If a language is unsupported or lacks a dictionary module, the tool will raise an error. To handle this:

- Ensure the language is included in `multilang.py` with a valid dictionary.
- If a custom dictionary is required, specify it in the `language_data` list.
- If a language lacks a dictionary module, default to using the NLTK module by replacing the module name with `'nltk'`.

## Example Text Files

1. **example_text_to_encode.txt**

   ```
   This is an example text to encode using LeetSpeak.
   ```

2. **example_text_to_decode.txt**

   ```
   7h15 15 4n 3x4mpl3 73x7 70 d3c0d3 u51ng L337Sp34k.
   ```

## Appendix A: Adding Support for an Unsupported Language

To add support for additional languages, follow these steps:

1. Open `multilang.py`.
2. Add a new entry to the `language_data` list in the format:

   ```python
   ('language_id', {'4': 'A', '8': 'B', '|': 'L', ...}, 'module_name'),
   ```

   - Replace `'language_id'` with the ISO language indicator.
   - Replace the dictionary `{'4': 'A', '8': 'B', '|': 'L', ...}` with the leet speak substitutions for the language.
   - Replace `'module_name'` with the name of the module providing the language dictionary. Use `'custom'` if a custom dictionary is required.
   - Save the file. 
   - Create a pull request and share your work with the community.

Now, you can use the added language in the LeetSpeak Encoder/Decoder.

## Contributing and Source Code

To contribute or access the source code, visit the GitHub repository:

- GitHub Repository: [monotoba/leetspeak-encoder-decoder](https://github.com/Monotoba/leetspeak-encoder-decoder.git)

Feel free to submit issues or pull requests to enhance the tool further. Your contributions are appreciated!
