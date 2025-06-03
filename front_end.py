import streamlit as st

from src.backend import check_liveliness
from src.common import add_http, get_words, shorten_url
from src.text import CLICK_BUTTON, ENTER_MESSAGE, TITLE


def generate_ui():
    st.title(TITLE)
    input_url = st.text_input(ENTER_MESSAGE)
    if st.button(CLICK_BUTTON):
        if not input_url:
            st.error("Please enter a URL.")
            st.stop()
        with st.spinner("Shortening URL..."):
            input_url = add_http(input_url)
            status, _ = check_liveliness(input_url)

            if not status:
                st.error('Website is not accessible.' 'Please check the URL and try again.')
                st.stop()

            short_url = shorten_url(input_url)
            st.write_stream(get_words(short_url))
        st.success("URL shortened successfully!")


if __name__ == "__main__":
    generate_ui()
