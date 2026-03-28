import streamlit as st
import pandas as pd

if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Student", "Grade"])

with st.sidebar:
    st.header("Entry Form")
    name = st.text_input("Student Name")
    score = st.number_input("Score", 0, 100, 85)
    if st.button("Add Student"):
        new_entry = pd.DataFrame({"Student": [name], "Grade": [score]})
        st.session_state.data = pd.concat([st.session_state.data, new_entry], ignore_index=True)