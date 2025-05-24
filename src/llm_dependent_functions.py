"""
Simple functions that depend on LLMs for character analysis.

What matters is that we call outside the function. From testing perspective, 
this is somewhat similar to other API calls or database queries,
"""

from langchain_openai import ChatOpenAI
from langchain_core.runnables import Runnable
from typing import Optional
from pydantic import BaseModel, Field

MODEL_NAME = "gemma3:1b"

class CharacterAnalysis(BaseModel):
    """Schema for character analysis results"""
    name: str = Field(description="Character name")
    role: str = Field(description="Character's role in the story")
    personality: str = Field(description="Character's personality traits")
    significance: str = Field(description="Character's significance to the plot")
    relationships: str = Field(description="Character's key relationships")

def analyze_character(
    model_structured: Runnable, 
    character_name: str, 
    fragments: list[str] = []
) -> Optional[CharacterAnalysis]:
    """ Analyze a character from text fragments using a structured LLM."""
    combined_text = "\n\n".join(fragments)
    
    messages = [
        {"role": "system", "content": "You are a literary analyst specialized in analyzing characters from novels."},
        {"role": "user", "content": f"""
Based on the following text fragments from a book
analyze the character of {character_name}. The text fragments are in Polish.

TEXT FRAGMENTS:
{combined_text}

Please analyze who this character is, their role in the story, personality traits, significance to the plot,
and key relationships.
"""}
    ]
    
    try:
        analysis = model_structured.invoke(messages)
        return analysis
    except Exception as e:
        print(f"Error analyzing {character_name}: {str(e)}")
        return None


def get_chat_model(
        model_name: str = MODEL_NAME, 
        base_url: str = 'http://localhost:11434/v1', 
        api_key: str = 'ollama') -> Runnable:
    """ Create a structured LLM model for character analysis."""
    model = ChatOpenAI(
        model=model_name,
        base_url=base_url,
        api_key=api_key
    )
    
    return model