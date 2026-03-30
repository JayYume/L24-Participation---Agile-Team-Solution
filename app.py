import streamlit as st
import pandas as pd
import logic

if 'student_list' not in st.session_state:
    st.session_state['student_list'] = []

st.title("Faculty Grade Dashboard")
if st.session_state['student_list']:
    df = pd.DataFrame(st.session_state['student_list'])
    
    # Task C: Metrics
    avg, high, low = logic.calculate_stats(df)
    col1, col2, col3 = st.columns(3)
    col1.metric("Average", f"{avg:.1f}")
    col2.metric("Highest", high)
    col3.metric("Lowest", low)
    
    # Task D: Visualization
    st.subheader("Grade Distribution")
    dist_data = logic.get_grade_distribution(df)
    st.bar_chart(dist_data)
    
    # Task C: Data Table
    st.subheader("Current Roster")
    st.dataframe(df, use_container_width=True)
else:
    st.info("Please add student data to view analytics.")