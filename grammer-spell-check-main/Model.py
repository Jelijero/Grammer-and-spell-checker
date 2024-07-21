from textblob import TextBlob
from language_tool_python import LanguageTool
import streamlit as st
from textblob import TextBlob
from language_tool_python import LanguageTool




class SpellCheckerModule:
    def __init__(self):
        self.spell_check = TextBlob("")
        self.grammar_check = LanguageTool('en-US')

    def correct_spell(self, text):
        # Hello, World, subscribe, to my channel
        words = text.split()
        corrected_words = []
        for word in words:
            corrected_word = str(TextBlob(word).correct())
            corrected_words.append(corrected_word)
        return " ".join(corrected_words)

    def correct_grammar(self, text):
        matches = self.grammar_check.check(text)

        found_mistakes = []
        for mistake in matches:
            found_mistakes.append(mistake.ruleId)
        found_mistakes_count = len(found_mistakes)
        if found_mistakes_count>0:
            return found_mistakes, found_mistakes_count
        else:
            return str("")

        
    
spell_checker_module = SpellCheckerModule()
st.title("Grammer and spell checker")
text=st.text_area(label="Enter your text")

corrected_text=spell_checker_module.correct_spell(text)
corrected_grammar=spell_checker_module.correct_grammar(text)
st.button("Submit")

st.text("Corrected Text")
st.text(corrected_text)
st.text("Grammatical mistakes found")
st.text(corrected_grammar)
text_file=st.file_uploader("Upload")
if text_file:
    readable_file = text_file.read().decode('utf-8', errors='ignore')
    corrected_file_text = spell_checker_module.correct_spell(readable_file)
    corrected_file_grammar, _ = spell_checker_module.correct_grammar(readable_file)
    st.text("Corrected Text")
    st.text(corrected_file_text)
    st.text("Grammatical mistakes found")
    st.text(corrected_file_grammar)