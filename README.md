Spell Checker and Grammar Assistant

This Python code provides a user-friendly Streamlit application for spell checking and grammar correction. It leverages the following libraries:

textblob: Offers text processing functionalities, including spell checking.
languagetool_python: Provides grammar correction capabilities.
streamlit: Enables the creation of interactive web apps.
Key Features:

Spell Correction: Identifies and corrects misspelled words using TextBlob's correct() method.
Grammar Correction: Highlights potential grammatical errors using LanguageTool's powerful rule-based approach.
Text Input & Output: Accepts text input from a text area and displays the corrected text directly within the Streamlit app.
File Upload & Correction: Enables uploading of text files for spell and grammar checking, displaying the corrected content in the app.
Installation:

Create a new Python environment (recommended).

Install the required libraries:

Bash
pip install textblob languagetool_python streamlit
Use code with caution.

Usage:

Save the code as a Python file (e.g., spell_checker_app.py).

Run the app from your terminal:

Bash
streamlit run spell_checker_app.py
Use code with caution.

A web app window will open in your default browser.

Explanation:

Import Libraries:

Python
from textblob import TextBlob
from language_tool_python import LanguageTool
import streamlit as st
Use code with caution.

SpellCheckerModule Class:

__init__(): Initializes the class with a TextBlob object for spell correction and a LanguageTool instance for grammar checking.
correct_spell(): Splits the input text into words, corrects them using TextBlob, and returns the corrected text as a string.
correct_grammar(): Uses LanguageTool to check for grammatical errors. It extracts the rule IDs of the errors, counts them, and returns appropriate messages.
Streamlit App Setup:

st.title(): Sets the app title.
st.text_area(): Creates a text area for user input with a label.
corrected_text: Stores the corrected text output from correct_spell().
corrected_grammar: Stores the grammar error message or an empty string from correct_grammar().
st.button(): Creates a button that, when clicked, triggers the correction process.
st.text(): Displays the corrected text and grammar check results.
File Upload Functionality:

st.file_uploader(): Creates a file upload component.
If a file is uploaded:
readable_file: Reads the uploaded file content and decodes it for proper text processing.
corrected_file_text: Corrects spelling in the file using correct_spell().
corrected_file_grammar: Checks grammar for the file using correct_grammar().
Corrected text and grammar check results are displayed.
