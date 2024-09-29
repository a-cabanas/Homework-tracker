import streamlit as st


def main():
    if "current_page" not in st.session_state:
        st.session_state.current_page = "Home 🏠"

    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Choose a page", ["Home 🏠", "Courses 📚", "Course Page 📘"])

    st.session_state.current_page = page

    if st.session_state.current_page == "Home 🏠":
        from app import app
        app()
    elif st.session_state.current_page == "Courses 📚":
        from courses import app
        app()
    elif st.session_state.current_page == "Course Page 📘":
        from courses_specific_page import app
        app()

if __name__ == "__main__":
    main()
