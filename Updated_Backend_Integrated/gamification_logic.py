import random
import json
import os
from datetime import datetime, timedelta

# Load or initialize gamification data
DATA_FILE = "gamification_data.json"

def load_gamification_data():
    """Loads the gamification data from a JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {"users": {}}

def save_gamification_data(data):
    """Saves the gamification data to a JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def update_streak(user_id):
    """Updates the user's spending streak based on daily check-ins."""
    data = load_gamification_data()
    user = data["users"].get(user_id, {"streak": 0, "last_check_in": None, "points": 0})

    today = datetime.now().date()
    last_check_in = datetime.strptime(user["last_check_in"], "%Y-%m-%d").date() if user["last_check_in"] else None

    if last_check_in == today:
        return {"message": "Already checked in today!", "streak": user["streak"]}
    
    if last_check_in and (today - last_check_in).days == 1:
        user["streak"] += 1  # Continue streak
    else:
        user["streak"] = 1  # Reset streak

    user["last_check_in"] = today.strftime("%Y-%m-%d")
    user["points"] += 10  # Reward points for consistency
    data["users"][user_id] = user
    save_gamification_data(data)

    return {"message": "Streak updated!", "streak": user["streak"], "points": user["points"]}

def get_leaderboard():
    """Generates a leaderboard sorted by highest points."""
    data = load_gamification_data()
    leaderboard = sorted(data["users"].items(), key=lambda x: x[1]["points"], reverse=True)
    return [{"user_id": user, "points": details["points"], "streak": details["streak"]} for user, details in leaderboard]

def mystery_challenge(user_id):
    """Assigns a random financial challenge to the user."""
    challenges = [
        {"challenge": "Save $5 today!", "reward": 20},
        {"challenge": "Avoid impulse shopping for 24 hours!", "reward": 30},
        {"challenge": "Find a way to earn an extra $10!", "reward": 40},
        {"challenge": "Cook at home instead of ordering takeout!", "reward": 25},
        {"challenge": "Review and optimize one monthly subscription!", "reward": 35},
    ]
    
    challenge = random.choice(challenges)
    data = load_gamification_data()
    
    if user_id not in data["users"]:
        data["users"][user_id] = {"streak": 0, "last_check_in": None, "points": 0}

    user = data["users"][user_id]
    user["current_challenge"] = challenge
    save_gamification_data(data)

    return challenge

def complete_challenge(user_id):
    """Marks the user's challenge as completed and rewards points."""
    data = load_gamification_data()
    
    if user_id not in data["users"] or "current_challenge" not in data["users"][user_id]:
        return {"message": "No active challenge!"}
    
    challenge = data["users"][user_id].pop("current_challenge")
    data["users"][user_id]["points"] += challenge["reward"]
    save_gamification_data(data)

    return {"message": "Challenge completed!", "reward": challenge["reward"], "total_points": data["users"][user_id]["points"]}

# Example usage
if __name__ == "__main__":
    user_id = "user123"

    print(update_streak(user_id))
    print(get_leaderboard())
    print(mystery_challenge(user_id))
    print(complete_challenge(user_id))
