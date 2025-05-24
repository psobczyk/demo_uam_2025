from langchain_openai import ChatOpenAI
from typing import Optional, List
from pydantic import BaseModel, Field

MODEL_NAME = "gemma3:1b"
BASE_URL = "http://localhost:11434/v1"
API_KEY = "ollama"

class CharacterAnalysis(BaseModel):
    """ Schema for character analysis results"""
    name: str = Field(description="Character name")
    role: str = Field(description="Character's role in the story")
    personality: str = Field(description="Character's personality traits")
    significance: str = Field(description="Character's significance to the plot")
    relationships: str = Field(description="Character's key relationships")


class CharacterAnalyzer:
    """ Class for analyzing literary characters using an LLM."""
    
    def __init__(
        self, 
        model_name: str = MODEL_NAME, 
        base_url: str = BASE_URL, 
        api_key: str = API_KEY
    ):
        """ Initialize the character analyzer. """
        self.model_name = model_name
        self.base_url = base_url
        self.api_key = api_key
        self._model = None
        self._structured_model = None
        
    def _initialize_model(self) -> None:
        """ Initialize the language model if not already done."""
        if self._model is None:
            self._model = ChatOpenAI(
                model=self.model_name,
                base_url=self.base_url,
                api_key=self.api_key
            )
            self._structured_model = self._model.with_structured_output(CharacterAnalysis)
    
    def analyze_character(
        self, 
        character_name: str, 
        fragments: List[str]
    ) -> Optional[CharacterAnalysis]:
        """ Analyze a character from text fragments. """
        self._initialize_model()
        combined_text = "\n\n".join(fragments)
        
        messages = [
            {"role": "system", "content": "You are a literary analyst specialized in analyzing characters from novels."},
            {"role": "user", "content": f"""
Based on the following text analyze the character of {character_name}. 
The text fragments are in Polish.

TEXT FRAGMENTS:
{combined_text}

Please analyze who this character is, their role in the story, personality traits, significance to the plot,
and key relationships.
"""}
        ]
        
        try:
            analysis = self._structured_model.invoke(messages)
            return analysis
        except Exception as e:
            print(f"Error analyzing {character_name}: {str(e)}")
            return None
    