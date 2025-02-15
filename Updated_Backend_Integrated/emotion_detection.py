import os
import requests

# Load API key from environment variables
HUME_API_KEY = os.getenv("HUME_API_KEY")

# Hume AI API endpoint
HUME_API_URL = "https://api.hume.ai/v1/emotions"

def analyze_emotion(text):
    """
    Sends text data to Hume AI to analyze emotions.
    
    Args:
        text (str): The user input text related to financial behavior.

    Returns:
        dict: Emotion analysis result.
    """
    if not HUME_API_KEY:
        raise ValueError("Hume API Key is missing! Please set it in the .env file.")

    headers = {
        "Authorization": f"Bearer {HUME_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "text": text
    }

    try:
        response = requests.post(HUME_API_URL, json=payload, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
        data = response.json()
        
        # Extract top detected emotions
        emotions = data.get("emotions", [])
        if emotions:
            return emotions
        else:
            return {"message": "No strong emotions detected."}
    
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to analyze emotions: {str(e)}"}

# Example usage
if __name__ == "__main__":
    test_text = "I feel guilty after spending too much on shopping."
    result = analyze_emotion(test_text)
    print("Emotion Analysis Result:", result)
