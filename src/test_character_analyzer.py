"""
Comment out 
monkeypatch.setattr(
        "src.character_analyzer.ChatOpenAI", 
        MagicMock(return_value=mock_chat)
    )
to see that either:
- test fails as model is not available
- test fails, as model output is different than our expected mocked values
"""

from unittest.mock import MagicMock
from src.character_analyzer import CharacterAnalyzer, CharacterAnalysis


def test_character_analyzer_analysis(monkeypatch):
    """Test the analyze_character method."""
    # Create mock response
    mock_response = CharacterAnalysis(
        name="Sherlock Holmes",
        role="Brilliant detective",
        personality="Analytical, eccentric",
        significance="Main character",
        relationships="Partner to Dr. Watson"
    )
    
    # Create mock setup
    mock_invoke = MagicMock(return_value=mock_response)
    mock_structured = MagicMock()
    mock_structured.invoke = mock_invoke
    mock_chat = MagicMock()
    mock_chat.with_structured_output = MagicMock(return_value=mock_structured)
    
    # Patch ChatOpenAI
    monkeypatch.setattr(
        "src.character_analyzer.ChatOpenAI", 
        MagicMock(return_value=mock_chat)
    )
    
    # Create analyzer and analyze character
    analyzer = CharacterAnalyzer()
    result = analyzer.analyze_character("Sherlock", ["Sherlock is a detective"])
    
    # Verify results
    assert result.name == "Sherlock Holmes"
    assert result.role == "Brilliant detective"
    
    # Check that the messages were correctly formatted
    invoke_args = mock_invoke.call_args[0][0]
    assert any("Sherlock" in arg.get("content", "") for arg in invoke_args if isinstance(arg, dict))
    assert any("detective" in arg.get("content", "") for arg in invoke_args if isinstance(arg, dict))