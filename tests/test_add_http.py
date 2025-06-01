import pytest

from src.common import add_http


@pytest.mark.parametrize(
    "url, expected",
    [
        ("example.com", "https://example.com"),
        ("http://example.com", "http://example.com"),
        ("https://example.com", "https://example.com"),
        ("ftp://example.com", "https://ftp://example.com"),
        ("www.example.com", "https://www.example.com"),
        ("", "https://"),
    ],
)
def test_add_http(url, expected):
    assert add_http(url) == expected, f"Expected {expected} but got {add_http(url)} for input {url}"
