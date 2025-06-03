import streamlit as st

from src.backend import generate_qr
from src.common import add_http
from src.front_end import StreamlitConfig, retrieve_shorturl


def main():
    st_config = StreamlitConfig()
    st.title(st_config.page_title)
    input_url = st.text_input(st_config.message_space)
    if input_url:
        input_url = add_http(input_url)

    if st.button(st_config.qr_code_button, use_container_width=True):
        if not input_url:
            st.error(st_config.no_url_provided)

        else:
            qr_path = generate_qr(input_url)
            st.image(qr_path, caption=f'{input_url}')

    if st.button(st_config.url_button, use_container_width=True):
        if not input_url:
            st.error(st_config.no_url_provided)

        else:
            shorten_url = retrieve_shorturl(input_url)
            if not shorten_url:
                st.error(st_config.invalid_url)
                st.stop()
            st.write_stream(shorten_url)


if __name__ == "__main__":
    main()
