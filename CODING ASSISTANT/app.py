"""
app.py
------
The Streamlit interface. This is the file you run to launch the app.
It doesn't contain any AI logic itself, it just collects what the user
types, calls the right function from assistant.py, and displays the result.
"""

import streamlit as st
from assistant import (
    generate_code,
    explain_code,
    find_bugs,
    convert_code,
    generate_docs,
    generate_tests,
)

st.set_page_config(page_title="AI Coding Assistant", page_icon="💻")
st.title("💻 AI Coding Assistant")
st.caption("Generate, explain, debug, convert, document, and test code.")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
    ["Generate", "Explain", "Find Bugs", "Convert", "Document", "Unit Tests"]
)

with tab1:
    st.subheader("Generate code from a description")
    prompt = st.text_area("Describe what you want", key="gen")
    if st.button("Generate", key="gen_btn"):
        with st.spinner("Writing code..."):
            st.code(generate_code(prompt))

with tab2:
    st.subheader("Explain existing code")
    code = st.text_area("Paste your code", key="explain")
    if st.button("Explain", key="explain_btn"):
        with st.spinner("Reading through it..."):
            st.write(explain_code(code))

with tab3:
    st.subheader("Find bugs in code")
    code = st.text_area("Paste your code", key="bugs")
    if st.button("Check for bugs", key="bugs_btn"):
        with st.spinner("Checking..."):
            st.write(find_bugs(code))

with tab4:
    st.subheader("Convert code to another language")
    code = st.text_area("Paste your code", key="convert")
    target = st.text_input("Target language (e.g. Java, JavaScript, Pandas)")
    if st.button("Convert", key="convert_btn"):
        with st.spinner("Converting..."):
            st.code(convert_code(code, target))

with tab5:
    st.subheader("Generate documentation")
    code = st.text_area("Paste your code", key="docs")
    if st.button("Write docs", key="docs_btn"):
        with st.spinner("Writing docs..."):
            st.code(generate_docs(code))

with tab6:
    st.subheader("Generate unit tests")
    code = st.text_area("Paste your code", key="tests")
    if st.button("Generate tests", key="tests_btn"):
        with st.spinner("Writing tests..."):
            st.code(generate_tests(code))
