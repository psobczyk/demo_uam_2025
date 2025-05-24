"""
Feel free to change the file. Just make sure it's not empty.

pytest src/test_fixture_utils.py

Run 
pytest src/test_fixture_utils.py -s 
# to see print statements from fixtures and understand the difference between session and function scope.
"""

import pytest
from src.utils import count_words_in_text, clean_text


PATH_TO_FILE = "data/conrad-tajny-agent.txt"  # from wolnelektury.org
NUMBER_OF_CHARS = 1000

@pytest.fixture(scope='session')
def sample_text():
    print("\nLOADING sample text in session scope...\n", flush=True)
    with open(PATH_TO_FILE, 'r', encoding='utf-8') as f:
        raw_text = f.read()
    return raw_text[:NUMBER_OF_CHARS]

@pytest.fixture(scope='function')
def sample_text_function_scope():
    print("\nLOADING sample text in function scope...\n", flush=True)
    with open(PATH_TO_FILE, 'r', encoding='utf-8') as f:
        raw_text = f.read()
    return raw_text[:NUMBER_OF_CHARS]

def test_count_words_in_raw_text(sample_text, sample_text_function_scope):
    assert count_words_in_text(sample_text) > 0, \
            "The number of words in the raw text should be greater than 0."

def test_count_words_in_cleaned_text(sample_text, sample_text_function_scope):
    cleaned_text = clean_text(sample_text)
    assert count_words_in_text(cleaned_text) <= count_words_in_text(sample_text), \
            "The number of words in cleaned text should be less than the number of words in the raw text."
