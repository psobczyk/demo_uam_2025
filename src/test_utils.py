"""
Run and compare results

pytest src/test_utils.py
pytest src/test_utils.py -k "clean"
pytest src/test_utils.py -k "clean or words"
pytest src/test_utils.py -k "count and words"
"""


import pytest
from src.utils import count_words_in_text, clean_text, count_chars_in_text

def test_count_words_in_text():
    text = "Hello, world!"
    assert count_words_in_text(text) == 2

def test_count_chars_in_text():
    text = "Bardzo długie zdanie!"
    assert count_chars_in_text(text) == 21, "Nie zgadza się liczba znaków"

def valid_api_config():
    return False

def test_clean_text():
    if not valid_api_config():
        pytest.skip("API config unsupported")

    text = """Hello,# world! 123
    
    123
    
    """
    assert clean_text(text) == "Hello, world! 123"

@pytest.mark.parametrize("text", [
    "tekst o 4 słowach",
    "tekst który ma 5 słów",
    "tekst który ma 6 słów",
    "",
])
def test_count_words_in_text_parametrized(text):
    assert count_words_in_text(text) == len(text.split()), "Nie zgadza się liczba słów"