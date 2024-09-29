import streamlit as st
from streamlit_tags import st_tags, st_tags_sidebar

## in case I add something to due with calendar here
import datetime
from datetime import datetime as dt

 
def app():
    st.title("Courses")

    # Ensure the 'selected_course' state variable is initialized
    if "selected_course" not in st.session_state:
        st.session_state.selected_course = None

    # Read courses from session state
    courses = st.session_state.get("course_tags", [])

    if courses:
        st.write("Courses:")
        for course in courses:
            if st.button(course):
                st.session_state.selected_course = course
                st.session_state.current_page = "Course Page"
    else:
        st.write("No courses available.")



    # Add a navigation link back to the main app
    if st.button('Go to Main App'):
        st.session_state.current_page = "Main App"
        st.experimental_rerun()

