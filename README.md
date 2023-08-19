# Multi Language Digits Converter

The **Multi Language Digits Converter** is a Python module that allows you to convert digits between different languages including Bangla, Hindi, Urdu, Malayalam, Thai, Arabic, and Farsi. This module provides methods to easily convert digits from one language to another.
The `conDigits` module provides a class for converting numeric digits from English to various languages. It supports a wide range of languages and numeral systems, allowing you to easily convert numbers into different scripts and representations.

## Features

- Converts digits between different languages
- Simple and easy-to-use methods for digit conversion.

## Languages & How to Use
- Bangla: বাংলা (to\_bangla)
- Hindi: हिन्दी (to\_hindi)
- Urdu: اُردو (to\_urdu)
- Malayalam: മലയാളം (to\_malayalam)
- Thai: ไทย (to\_thai)
- Arabic: العربية (to\_arabic)
- Farsi: فارسی (to\_farsi)
- Japanese: 日本語 (to\_japanese)
- Korean: 한국어 (to\_korean)
- Telugu: తెలుగు (to\_telugu)
- Tamil: தமிழ் (to\_tamil)
- Greek: Ελληνικά (to\_greek)
- Hebrew: עִבְרִית (to\_hebrew)
- Georgian: ქართული (to\_georgian)
- Armenian: հայերեն (to\_armenian)
- Amharic: አማርኛ (to\_amharic)
- Nepali: नेपाली (to\_nepali)
- Sinhala: සිංහල (to\_sinhala)
- Mongolian: Монгол (to\_mongolian)

## Installation

You can simply clone this GitHub repository to use the module:
```bash
git clone https://github.com/awaleedpk/multi-language-digits-converter.git
```
# How to Import multi_language_digits_converter
```
import multi_language_digits_converter
convertDigits = multi_language_digits_converter.conDigits()
```
# Get the list of available languages
```
languages = convertDigits.available()
print(languages)
```


# Convert numbers to different scripts
```
converted_japanese = convertDigits.to_japanese(1234567890)
print(converted_japanese)

converted_urdu = convertDigits.to_urdu(1234567890)
print(converted_japanese)

converted_hindi = convertDigits.to_hindi(1234567890)
print(converted_japanese)
```
