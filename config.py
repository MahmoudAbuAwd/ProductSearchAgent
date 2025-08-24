# config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
    
    # Gemini model configuration
    GEMINI_MODEL = "gemini-2.0-flash-exp"
    
    # Search configuration
    MAX_SEARCH_RESULTS = 5
    SEARCH_TIMEOUT = 30