from typing import Generator

import streamlit as st
from pydantic import BaseModel

from src.backend import check_liveliness
from src.common import get_words, shorten_url
from src.text import Text


class StreamlitConfig(BaseModel):
    """Configuration for Streamlit app."""

    page_title: str = Text.TITLE.value
    message_space: str = Text.ENTER_MESSAGE.value
    qr_code_button: str = Text.QR_CODE_BUTTON.value
    url_button: str = Text.URL_BUTTON.value
    invalid_url: str = Text.INVALID_URL.value
    general_error: str = Text.ERROR.value
    no_url_provided: str = Text.NO_URL_PROVIDED.value


def retrieve_shorturl(url: str) -> Generator[str, None, None] | None:
    with st.spinner("Shortening URL..."):
        status, _ = check_liveliness(url)
        if not status:
            return None
        short_url = shorten_url(url)
        return get_words(short_url)
