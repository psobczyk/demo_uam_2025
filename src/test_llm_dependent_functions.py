"""
Mock object help testing the analyze_character function
even if the ChatOpenAI model is not available.

This is a dummy example since we explicitly pass a mock runnable
to the analyze_character function. Checkout the test_character_analyzer.py
for a more realistic example.
"""

from unittest.mock import MagicMock, ANY
from src.llm_dependent_functions import CharacterAnalysis, analyze_character


def test_chat_with_structured_output_monkeypatch(monkeypatch):
    # Mock data
    mock_response = CharacterAnalysis(
        name="Harry Potter",
        role="The Chosen One",
        personality="Brave and loyal",
        significance="Central to the plot",
        relationships="Best friends with Hermione and Ron"
    )
    
    # Create a mock runnable that returns our mock response
    mock_runnable = MagicMock()
    mock_runnable.invoke = MagicMock(return_value=mock_response)
    
    result = analyze_character(mock_runnable, "Harry Potter", ["Some text about Harry"])
    
    # Verify the mock was called correctly with any argument
    mock_runnable.invoke.assert_called_once_with(ANY)
    
    # Assertions
    assert isinstance(result, CharacterAnalysis)
    assert result.name == "Harry Potter"
    assert result.role == "The Chosen One"
    assert result.personality == "Brave and loyal"
    assert result.significance == "Central to the plot"
    assert result.relationships == "Best friends with Hermione and Ron"
