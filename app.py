import streamlit as st
from deep_translator import GoogleTranslator
st.title("Language Translator")
text = st.text_input("Enter text")
source = st.selectbox("From", ["en", "ur", "fr", "es"])
target = st.selectbox("To", ["ur", "en", "fr", "es"])
if st.button("Translate"):
    if text:
        result = GoogleTranslator(source=source, target=target).translate(text)
        st.success(result)
    else:
        st.warning("Please enter text")