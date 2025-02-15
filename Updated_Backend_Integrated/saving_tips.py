import random

class SavingTips:
    def __init__(self):
        self.general_tips = [
            "Try the 50/30/20 rule: 50% for needs, 30% for wants, 20% for savings. 📊",
            "Automate your savings! Set up an auto-transfer to your savings account. 💰",
            "Cut back on impulse buys—wait 24 hours before making a purchase. ⏳",
            "Meal prep instead of eating out—it saves money and time! 🍱",
            "Use cashback and discount apps to save on daily expenses. 💳",
            "Try a ‘No Spend Challenge’ for a week and track how much you save! 🚀",
            "Cancel unused subscriptions—those small charges add up! 📉",
            "Set a savings goal and track your progress weekly. 📈",
            "Buy in bulk for non-perishable goods to save in the long run. 🛒",
            "Use public transport instead of cabs to cut down travel expenses. 🚌"
        ]

    def get_general_tip(self):
        """
        Returns a random general saving tip.
        """
        return random.choice(self.general_tips)

    def get_custom_saving_tip(self, spending_pattern):
        """
        Analyzes spending habits and provides personalized saving tips.
        """
        if "food delivery" in spending_pattern.lower():
            return "🍽️ Reduce food delivery expenses by cooking at home. Try meal planning!"
        elif "shopping" in spending_pattern.lower():
            return "🛍️ Try a '30-day rule'—if you still want it after 30 days, buy it."
        elif "subscriptions" in spending_pattern.lower():
            return "🎥 Review your subscriptions! Are you using all of them?"
        elif "travel" in spending_pattern.lower():
            return "✈️ Consider off-season travel for cheaper flights and hotels!"
        elif "entertainment" in spending_pattern.lower():
            return "🎟️ Look for free events and budget-friendly activities in your area."
        else:
            return self.get_general_tip()

if __name__ == "__main__":
    tips = SavingTips()

    # Example Usage
    print("💡 General Saving Tip:")
    print(tips.get_general_tip())

    print("\n🔍 Custom Saving Tip (for a shopping spender):")
    print(tips.get_custom_saving_tip("shopping, fashion, and accessories"))
