import datetime
import random

# Enhanced future self motivational messages
FUTURE_MESSAGES = [
    "You're building a life of financial freedom. Keep stacking those wins! 💰✨",
    "Every rupee saved is a step closer to your dream future. Stay consistent! 🚀",
    "Imagine a future where money is no longer a stress. You're creating that future now! 😎",
    "Your savings today are funding future you’s best adventures. Keep going! 🌍🏖️",
    "You're not just saving money—you're creating opportunities. Keep believing in yourself! 💡",
]

def get_future_self_message():
    """
    Returns a random motivational message from the future self.
    """
    return f"🔮 Future You says: {random.choice(FUTURE_MESSAGES)}"

def generate_future_projection(current_savings, monthly_savings, months=12):
    """
    Projects future savings based on current savings and monthly savings.
    
    :param current_savings: Current amount saved
    :param monthly_savings: Amount saved per month
    :param months: Number of months to project (default: 12)
    :return: A string message with the projected savings and a personalized tip
    """
    future_savings = current_savings + (monthly_savings * months)
    future_date = (datetime.datetime.now() + datetime.timedelta(days=months * 30)).strftime("%B %Y")

    # Dynamic motivation based on savings progress
    if future_savings >= 100000:
        tip = "🔥 You're on fire! Consider investing a portion for higher returns."
    elif future_savings >= 50000:
        tip = "💡 Great progress! Maybe start an emergency fund or a travel budget."
    elif future_savings >= 10000:
        tip = "📈 Good work! Try automating your savings for even better consistency."
    else:
        tip = "⏳ Keep going! Even small savings add up over time. Your future self will thank you."

    return f"📅 By {future_date}, you could have saved ₹{future_savings:.2f}. {tip} 🚀"

if __name__ == "__main__":
    print(get_future_self_message())
    print(generate_future_projection(5000, 2000, 6))  # Example: ₹5000 saved, ₹2000 per month for 6 months
