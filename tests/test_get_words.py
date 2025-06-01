import pytest

from src.common import get_words


@pytest.mark.parametrize(
    "sentence, expected",
    [
        ("Hello", ["H", "e", "l", "l", "o"]),
        ("World", ["W", "o", "r", "l", "d"]),
        (
            "Streamlit is great!",
            ["S", "t", "r", "e", "a", "m", "l", "i", "t", " ", "i", "s", " ", "g", "r", "e", "a", "t", "!"],
        ),
        ("Python 3.8+", ["P", "y", "t", "h", "o", "n", " ", "3", ".", "8", "+"]),
    ],
)
def test_get_words(sentence, expected):
    result = list(get_words(sentence))
    assert result == expected, f"Expected {expected} but got {result} for input '{sentence}'"
