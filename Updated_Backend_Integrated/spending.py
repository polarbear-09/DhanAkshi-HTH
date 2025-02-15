import random

class SpendingTracker:
    def __init__(self):
        self.categories = ["Food", "Shopping", "Entertainment", "Transport", "Bills", "Subscriptions", "Other"]
        self.spending_data = []

    def log_spending(self, amount, category, description=""):
        """
        Logs a spending entry.
        """
        if category not in self.categories:
            return f"⚠️ Invalid category. Choose from: {', '.join(self.categories)}"
        
        self.spending_data.append({
            "amount": amount,
            "category": category,
            "description": description
        })
        return f"✅ Logged: ₹{amount} on {category}. {description}"

    def get_total_spent(self):
        """
        Returns the total amount spent.
        """
        return sum(entry["amount"] for entry in self.spending_data)

    def get_spent_by_category(self):
        """
        Returns spending breakdown by category.
        """
        category_totals = {category: 0 for category in self.categories}
        for entry in self.spending_data:
            category_totals[entry["category"]] += entry["amount"]
        return category_totals

    def get_saving_tip(self):
        """
        Provides a random saving tip.
        """
        tips = [
            "Try a 'No Spend Day' challenge! 🚫💸",
            "Use a budgeting app to track your expenses. 📊",
            "Set a spending limit for non-essential categories. 🎯",
            "Pack home-cooked meals instead of ordering food. 🍱",
            "Avoid impulse buys—stick to a shopping list! 📝"
        ]
        return random.choice(tips)

if __name__ == "__main__":
    tracker = SpendingTracker()

    # Example Usage
    print(tracker.log_spending(500, "Food", "Dinner with friends"))
    print(tracker.log_spending(1200, "Shopping", "Bought new shoes"))
    
    print("\n💰 Total Spent:", tracker.get_total_spent())
    
    print("\n📊 Spending Breakdown:", tracker.get_spent_by_category())

    print("\n💡 Saving Tip:", tracker.get_saving_tip())
