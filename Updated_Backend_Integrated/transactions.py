import time
import random
from database import log_spending
from datetime import datetime

def automate_transaction(user_id, category, min_amount, max_amount):
    """
    Simulates an automated financial transaction and logs it in Google Sheets.
    The transaction amount is randomly chosen between min_amount and max_amount.
    """
    amount = round(random.uniform(min_amount, max_amount), 2)
    emotions = ["Happy", "Stressed", "Impulsive", "Calm", "Regretful"]
    emotion = random.choice(emotions)

    # Log the transaction
    log_spending(user_id, category, amount, emotion)
    print(f"Transaction logged: {category} - ${amount} ({emotion})")

def start_auto_transactions(user_id, interval=10):
    """
    Runs an automated transaction every 'interval' seconds (default: 10 sec).
    Categories are randomly selected for variety.
    """
    categories = ["Food", "Shopping", "Bills", "Entertainment", "Savings"]

    try:
        while True:
            category = random.choice(categories)
            automate_transaction(user_id, category, min_amount=5, max_amount=100)
            time.sleep(interval)  # Wait before next transaction
    except KeyboardInterrupt:
        print("\nAuto transactions stopped.")

if __name__ == "__main__":
    user_id = "test_user"
    start_auto_transactions(user_id)
