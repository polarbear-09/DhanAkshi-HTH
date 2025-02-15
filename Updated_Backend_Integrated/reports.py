import datetime
import random

class FinancialReport:
    def __init__(self):
        self.user_reports = {}  # {user_id: {"spending": [], "savings": []}}

    def log_transaction(self, user_id, amount, category, transaction_type="spending"):
        """
        Logs a user's transaction (either spending or saving).
        """
        if user_id not in self.user_reports:
            self.user_reports[user_id] = {"spending": [], "savings": []}
        
        transaction = {
            "date": datetime.datetime.now().strftime("%Y-%m-%d"),
            "amount": amount,
            "category": category
        }

        if transaction_type == "spending":
            self.user_reports[user_id]["spending"].append(transaction)
        else:
            self.user_reports[user_id]["savings"].append(transaction)

    def generate_summary(self, user_id):
        """
        Generates a summary report for the user.
        """
        if user_id not in self.user_reports:
            return "📊 No financial data available. Start tracking your spending and savings!"

        spending = self.user_reports[user_id]["spending"]
        savings = self.user_reports[user_id]["savings"]

        total_spent = sum([t["amount"] for t in spending])
        total_saved = sum([t["amount"] for t in savings])

        report = f"📅 Report for {datetime.datetime.now().strftime('%B %Y')}\n"
        report += f"💸 Total Spent: ₹{total_spent}\n"
        report += f"💰 Total Saved: ₹{total_saved}\n"

        if total_spent > 0:
            top_category = max(set([t["category"] for t in spending]), key=[t["category"] for t in spending].count)
            report += f"🔍 Most spent on: {top_category}\n"

        if total_saved > total_spent:
            report += "🎉 Great job! You saved more than you spent this month. Keep it up! 🚀"
        else:
            report += "⚠️ Warning: Your expenses are higher than your savings. Try cutting down unnecessary spending!"

        return report

    def generate_smart_tips(self, user_id):
        """
        Provides AI-driven financial insights based on the user’s spending habits.
        """
        spending = self.user_reports.get(user_id, {}).get("spending", [])
        
        if not spending:
            return "🤖 No spending data found! Start tracking to receive smart tips."

        # Sample smart tips
        tips = [
            "Try setting a daily spending limit to avoid impulse buys! 💳",
            "Consider using the 50/30/20 rule for better financial control. 📊",
            "Look at your subscription services—are you using them all? 📉",
            "A no-spend challenge for a week could boost your savings! 🚀",
            "Try meal prepping to save on food expenses! 🍲"
        ]
        
        return f"💡 Smart Tip: {random.choice(tips)}"

if __name__ == "__main__":
    report = FinancialReport()

    # Simulate transactions
    user_id = "user_123"
    report.log_transaction(user_id, 500, "Food", "spending")
    report.log_transaction(user_id, 200, "Entertainment", "spending")
    report.log_transaction(user_id, 1500, "Savings", "savings")

    # Generate report
    print(report.generate_summary(user_id))

    # Get a smart tip
    print("\n📌 Financial Tip:")
    print(report.generate_smart_tips(user_id))
