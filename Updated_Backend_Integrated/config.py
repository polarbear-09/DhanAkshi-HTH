import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

class Config:
    # General Settings
    PROJECT_NAME = "DhanAkshi"
    VERSION = "1.0"
    
    # API Keys (Replace with actual keys or use .env)
    DEEPSEEK_AI_KEY = os.getenv("DEEPSEEK_AI_KEY", "your-deepseek-api-key")
    HUME_AI_KEY = os.getenv("HUME_AI_KEY", "your-hume-ai-key")


    # Database (Google Sheets Integration)
    GOOGLE_SHEETS_CREDENTIALS = os.getenv("GOOGLE_SHEETS_CREDENTIALS", r"backend/google_sheets_key.json")


    # WebSocket Settings (for real-time updates)
    WEBSOCKET_URL = "ws://localhost:8000/ws"

    # Crisis Mode Settings
    CRISIS_MODE_APPS = ["Amazon", "Flipkart", "Stock Trading", "Crypto Trading"]
    
    # Gamification Settings
    REWARD_POINTS_PER_DAY = 10  # Points awarded for sticking to budget
    
    # Voice Assistant Settings
    ENABLE_VOICE_ASSISTANT = True  # Set to False if voice assistant is not needed

# Create an instance of Config
config = Config()
