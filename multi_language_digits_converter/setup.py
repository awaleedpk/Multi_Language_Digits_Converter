import setuptools
 
with open("README.md", "r") as fh:
    long_description = fh.read()
 
setuptools.setup(
    #Here is the module name.
    name="multi_language_digits_converter",
 
    #version of the module
    version="0.0.1",
 
    #Name of Author
    author="Ahmad Waleed",
 
    #your Email address
    author_email="awaleedpk.com",
 
    #Small Description about module
    description="The Multi Language Digits Converter allows you to convert digits between different languages including Bangla, Hindi, Urdu, Malayalam, Thai, Arabic & etc ",
 
    long_description="The Multi Language Digits Converter is a Python module that allows you to convert digits between different languages including Bangla, Hindi, Urdu, Malayalam, Thai, Arabic, and Farsi. This module provides methods to easily convert digits from one language to another. The conDigits module provides a class for converting numeric digits from English to various languages. It supports a wide range of languages and numeral systems, allowing you to easily convert numbers into different scripts and representations.",
 
    #Specifying that we are using markdown file for description
    long_description_content_type="text/markdown",
 
    #Any link to reach this module, if you have any webpage or github profile
    url="https://github.com/awaleedpk/",
    packages=setuptools.find_packages(),
 
    #classifiers like program is suitable for python3, just leave as it is.
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)