import streamlit as st
import pandas as pd
import logic

if 'student_list' not in st.session_state:
    st.session_state['student_list'] = []

st.title("Faculty Grade Dashboard")

if st.session_state['student_list']:
    df = pd.DataFrame(st.session_state['student_list'])
    
    avg, high, low = logic.calculate_stats(df)
    col1, col2, col3 = st.columns(3)
    col1.metric("Average", f"{avg:.1f}")
    col2.metric("Highest", high)
    col3.metric("Lowest", low)
    
    st.subheader("Grade Distribution")
    dist_data = logic.get_grade_distribution(df)
    st.bar_chart(dist_data)

    st.subheader("Current Roster")
    st.dataframe(df, use_container_width=True)
else:
    st.info("No students added yet. Use the sidebar to enter data.")


if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Student", "Grade"])

with st.sidebar:
    st.header("Entry Form")
    name = st.text_input("Student Name")
    score = st.number_input("Score", 0, 100, 85)
    if st.button("Add Student"):
        new_entry = pd.DataFrame({"Student": [name], "Grade": [score]})
        st.session_state.data = pd.concat([st.session_state.data, new_entry], ignore_index=True)
main
