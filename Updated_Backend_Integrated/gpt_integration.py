import deepseek
import os
from config import DEEPSEEK_API_KEY

# Set OpenAI API Key
deepseek.api_key = DEEPSEEK_API_KEY

def generate_financial_advice(prompt):
    """
    Generates AI-powered financial advice based on user input.
    """
    try:
        response = deepseek.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are a financial therapy assistant."},
                      {"role": "user", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error generating advice: {e}"

def generate_saving_tips(user_spending_pattern):
    """
    Provides AI-generated personalized saving tips.
    """
    prompt = f"Analyze this spending pattern and suggest smart saving tips: {user_spending_pattern}"
    return generate_financial_advice(prompt)

def generate_emotional_support_message(user_emotion):
    """
    Generates an emotional support message based on detected emotion.
    """
    prompt = f"A user feels {user_emotion}. Provide a short, empathetic financial therapy response."
    return generate_financial_advice(prompt)

if __name__ == "__main__":
    # Example usage
    print(generate_financial_advice("How do I control impulse spending?"))
