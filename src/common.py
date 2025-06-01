import time
from typing import Generator

import pyshorteners as short


def get_words(sentence: str) -> Generator[str, None, None]:
    for word in sentence:
        yield word
        time.sleep(0.05)


def shorten_url(url: str) -> str:
    s = short.Shortener()
    return s.tinyurl.short(url)


def add_http(url: str) -> str:
    if not url.startswith("http://") and not url.startswith("https://"):
        return "https://" + url
    return url
