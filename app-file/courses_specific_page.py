import streamlit as st

def app():
    course = st.session_state.get("selected_course", "Course")
    st.title(f"{course} Page 📓")

    # Adding any specific content or functionality for the course page here
    st.write(f"Welcome to the {course} page.")
    st.write(f"Check our your assignments below!")

    # Add a navigation link back to the courses or main app
    page = st.selectbox("Choose a page", ["Course Page", "Courses", "Main App"])
    if page == "Courses":
        st.session_state.current_page = "Courses"
    elif page == "Main App":
        st.session_state.current_page = "Main App"
