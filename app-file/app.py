from streamlit_tags import st_tags, st_tags_sidebar

import datetime
from datetime import datetime as dt
import streamlit as st
import streamlit_calendar as st_cal

def app():
    # Initialize session state variables
    if "selected" not in st.session_state:
        st.session_state.selected = False

    if "selected_date" not in st.session_state:
        st.session_state.selected_date = None

    if "events" not in st.session_state:
        st.session_state.events = {}

    if "course_tags" not in st.session_state:
        st.session_state.course_tags = ['Calculus 1', 'Chemistry', 'Physics 1']

    if "event_tags" not in st.session_state:
        st.session_state.event_tags = ['Urgent', 'Home', 'Work', 'Personal', 'Other']

    # Function to display the calendar and handle date selection
    def display_calendar(year, month):
        selected_date = st_cal.calendar(year, month, key="calendar")
        if selected_date and 'dateClick' in selected_date:
            date_info = selected_date['dateClick']['date']
            # Parse the date string to a datetime object and format it to display only the date
            formatted_date = dt.strptime(date_info, "%Y-%m-%dT%H:%M:%S.%fZ").date()
            st.write('Selected date:', formatted_date)
            # Store the selected date in session state
            st.session_state.selected_date = formatted_date
            # Trigger page navigation
            st.session_state.selected = True

# # Welcome Sign hehe
    st.title("✨ Welcome to my Streamlit Homework Planner! ✨") ## title of the page
    st.divider() ## line divider

    # Display the calendar
    today = datetime.datetime.today()
    display_calendar(today.year, today.month)

    # st.sidebar.write("# Navigation")
    # st.sidebar.divider()  # line divider

    # Form to add new course tags
    st.sidebar.write("### Add New Course 🤓 :")
    with st.sidebar.form(key='add_course_tag_form'):
        new_course_tag = st.text_input('Input Course:')
        add_course_tag_button = st.form_submit_button(label='Add Course')

        if add_course_tag_button and new_course_tag:
            if new_course_tag not in st.session_state.course_tags:
                st.session_state.course_tags.append(new_course_tag)
                st.success(f"Course '{new_course_tag}' added successfully")

    # Form to add new event tags
    st.sidebar.write("### Add New Event Tags 📅 :")
    with st.sidebar.form(key='add_event_tag_form'):
        new_event_tag = st.text_input('Input Tag:')
        add_event_tag_button = st.form_submit_button(label='Add Event Tag')

        if add_event_tag_button and new_event_tag:
            if new_event_tag not in st.session_state.event_tags:
                st.session_state.event_tags.append(new_event_tag)
                st.success(f"Event tag '{new_event_tag}' added successfully")

    # Display tags to help organize the app/search for homeworks based on class
    # st.sidebar.write("### Classes:")
    # maxtags_sidebar = st.sidebar.slider('Number of courses?', 1, 7, 4, key='ehikwegrjifbwreuk')

    keyword = st.sidebar.multiselect(
        label='# Classes:',
        options=st.session_state.course_tags + st.session_state.event_tags,
        default=st.session_state.course_tags,
        key='class_tags'
    )

    st.sidebar.write("### Selected Classes:")
    st.sidebar.write(keyword)

    event_keywords = st.sidebar.multiselect(
        label='### Other tags:',
        options=st.session_state.event_tags,
        default=st.session_state.event_tags,
        key='ev_k_tags'
    )

    st.sidebar.write("### Other Tags:")
    st.sidebar.write(event_keywords)

    # Function to add new events with tags
    def add_event(date, event, tags):
        event_entry = {
            'description': event,
            'tags': tags
        }
        if date.strftime("%Y-%m-%d") not in st.session_state.events:
            st.session_state.events[date.strftime("%Y-%m-%d")] = []
        st.session_state.events[date.strftime("%Y-%m-%d")].append(event_entry)

    # Display specific page based on the selected date
    if st.session_state.selected and st.session_state.selected_date:
        selected_date = st.session_state.selected_date
        st.write(f"Page for {selected_date}")

        # Display existing events for the selected date
        events = st.session_state.events.get(selected_date.strftime("%Y-%m-%d"), [])
        st.write("Events:")
        if events:
            for event in events:
                tags = ', '.join(event['tags'])
                st.write(f" - {event['description']} [Tags: {tags}]")
        else:
            st.write("No events for this day.")

        # Form to add new events with tags
        with st.form(key='add_event_form'):
            new_event = st.text_input('Event description')
            # Use both course tags and event tags for suggesting tags to the user
            combined_tags = st.session_state.course_tags + st.session_state.event_tags
            new_event_tags = st.multiselect(
                label='Enter Tags:',
                options=combined_tags,
                key='event_tags_multiselect'
            )
            new_tags_input = st.text_input('New Tags (comma separated)')

            submit_button = st.form_submit_button(label='Add Event')

            if submit_button and new_event:
                # Add new tags if provided
                if new_tags_input:
                    new_tags = [tag.strip() for tag in new_tags_input.split(',')]
                    for tag in new_tags:
                        if tag not in combined_tags:
                            st.session_state.event_tags.append(tag)
                    new_event_tags.extend(new_tags)

                # Add the event to the list of events for the selected date
                add_event(selected_date, new_event, new_event_tags)
                st.success("Event added successfully")
