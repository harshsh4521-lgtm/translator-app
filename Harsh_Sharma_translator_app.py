import streamlit as st
from googletrans import Translator

# UI
st.title("🌍 Simple Language Translator (Google Translate)")

# Language options
languages = {
    'English': 'en',
    'French': 'fr',
    'German': 'de',
    'Spanish': 'es',
    'Hindi': 'hi',
    'Arabic': 'ar',
    'Chinese (Simplified)': 'zh-cn'
}

# Language selection
src_lang = st.selectbox("Select source language", list(languages.keys()))
tgt_lang = st.selectbox("Select target language", list(languages.keys()))

# Text input
text = st.text_area("Enter text to translate", height=100)

# Translate button
if st.button("Translate"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        with st.spinner("Translating..."):
            translator = Translator()
            translation = translator.translate(text, src=languages[src_lang], dest=languages[tgt_lang])
            st.success(f"**Translated Text:** {translation.text}")
