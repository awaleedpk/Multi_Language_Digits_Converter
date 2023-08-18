# Multi Language Digits Converter

The **Multi Language Digits Converter** is a Python module that allows you to convert digits between different languages including Bangla, Hindi, Urdu, Malayalam, Thai, Arabic, and Farsi. This module provides methods to easily convert digits from one language to another.
The `conDigits` module provides a class for converting numeric digits from English to various languages. It supports a wide range of languages and numeral systems, allowing you to easily convert numbers into different scripts and representations.

## Features

- Converts digits between different languages: Bangla, Hindi, Urdu, Malayalam, Thai, Arabic, and Farsi.
- Simple and easy-to-use methods for digit conversion.

## Installation

You can simply clone this GitHub repository to use the module:

```bash
git clone https://github.com/your-username/multi-language-digits-converter.git
```
# conDigits Module Documentation


## Class: conDigits

### Constructor

```python
numbers = conDigits()
```
Methods
to_bangla(digits: int) -> str
Converts English digits to Bangla script.

to_hindi(digits: int) -> str
Converts English digits to Hindi script.

to_urdu(digits: int) -> str
Converts English digits to Urdu script.

to_malayalam(digits: int) -> str
Converts English digits to Malayalam script.

to_thai(digits: int) -> str
Converts English digits to Thai script.

to_arabic(digits: int) -> str
Converts English digits to Arabic script.

to_farsi(digits: int) -> str
Converts English digits to Farsi script.

to_japanese(digits: int) -> str
Converts English digits to Japanese script.

to_korean(digits: int) -> str
Converts English digits to Korean script.

to_telugu(digits: int) -> str
Converts English digits to Telugu script.

to_tamil(digits: int) -> str
Converts English digits to Tamil script.

to_russian(digits: int) -> str
Converts English digits to Russian script.

to_greek(digits: int) -> str
Converts English digits to Greek script.

to_hebrew(digits: int) -> str
Converts English digits to Hebrew script.

to_georgian(digits: int) -> str
Converts English digits to Georgian script.

to_armenian(digits: int) -> str
Converts English digits to Armenian script.

to_amharic(digits: int) -> str
Converts English digits to Amharic script.

to_nepali(digits: int) -> str
Converts English digits to Nepali script.

to_sinhala(digits: int) -> str
Converts English digits to Sinhala script.

to_mongolian(digits: int) -> str
Converts English digits to Mongolian script.

available() -> List[str]
Returns a list of languages supported by the module for digit conversion.


numbers = conDigits()
**Example Usage**

# Get the list of available languages
available_languages = numbers.available()
print(available_languages)

# Convert numbers to different scripts
converted_japanese = numbers.to_japanese(1234567890)
print(converted_japanese)

converted_armenian = numbers.to_armenian(9876543210)
print(converted_armenian)
