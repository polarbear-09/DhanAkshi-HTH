import random
import datetime

# Sample rewards & challenges
REWARDS = [
    "🎉 You've unlocked a 10% boost to your savings this week!",
    "🎁 Special Reward: One guilt-free coffee treat on us! ☕",
    "🚀 Your savings streak earns you a surprise financial tip!",
    "🏆 You've climbed the leaderboard! Keep saving!",
    "💎 Bonus Challenge: Save ₹500 this week and earn a mystery perk!"
]

MYSTERY_CHALLENGES = [
    "💡 No-Spend Challenge: Avoid impulse purchases for 3 days!",
    "📉 Cut the Costs: Reduce one unnecessary expense this week.",
    "🚀 Micro-Savings Boost: Save an extra ₹100 each day for a week.",
    "🌱 Investment Start: Research and invest ₹500 into a new opportunity.",
    "🎯 Budget Mastery: Stick to a self-made budget for 7 days!"
]

class Gamification:
    def __init__(self):
        self.user_streaks = {}  # {user_id: streak_count}
        self.leaderboard = {}  # {user_id: total_saved}
    
    def update_streak(self, user_id, saved_today):
        """
        Updates the user's savings streak.
        """
        if user_id not in self.user_streaks:
            self.user_streaks[user_id] = 0
        
        if saved_today:
            self.user_streaks[user_id] += 1
        else:
            self.user_streaks[user_id] = 0  # Reset streak if no savings
        
        return f"🔥 Your current streak: {self.user_streaks[user_id]} days!"

    def get_leaderboard(self):
        """
        Returns the top savers leaderboard.
        """
        sorted_leaderboard = sorted(self.leaderboard.items(), key=lambda x: x[1], reverse=True)
        return "\n".join([f"🏅 {i+1}. User {user} - ₹{saved}" for i, (user, saved) in enumerate(sorted_leaderboard[:5])])

    def add_to_leaderboard(self, user_id, amount_saved):
        """
        Adds user's savings to the leaderboard.
        """
        if user_id not in self.leaderboard:
            self.leaderboard[user_id] = 0
        self.leaderboard[user_id] += amount_saved

    def get_random_reward(self):
        """
        Returns a random reward for completing challenges or streaks.
        """
        return random.choice(REWARDS)

    def get_random_challenge(self):
        """
        Returns a mystery financial challenge.
        """
        return random.choice(MYSTERY_CHALLENGES)

if __name__ == "__main__":
    game = Gamification()

    # Simulate a user saving
    user_id = "user_123"
    print(game.update_streak(user_id, True))  # User saves money today
    game.add_to_leaderboard(user_id, 1500)  # Adding ₹1500 to leaderboard
    
    # Show leaderboard
    print("\n🏆 Leaderboard:")
    print(game.get_leaderboard())

    # Generate mystery challenges & rewards
    print("\n🎲 Mystery Challenge:", game.get_random_challenge())
    print("\n🎁 Reward Unlocked:", game.get_random_reward())
