import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

# Google Sheets setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
key_path = os.path.join(BASE_DIR, "google_sheets_key.json")

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(key_path, scope)
client = gspread.authorize(creds)

spreadsheet = client.open("Financial_Therapy_DB")
users_sheet = spreadsheet.worksheet("Users")
spending_sheet = spreadsheet.worksheet("Spending_Log")

def add_user(user_id, name, email):
    """
    Adds a new user to the Users worksheet.
    """
    try:
        users_sheet.append_row([user_id, name, email, "FALSE"])  # Default crisis_mode_status to FALSE
        return {"status": "success", "message": f"User {name} added."}
    except Exception as e:
        return {"status": "error", "message": f"Failed to add user: {e}"}

def log_spending(user_id, category, amount, emotion, timestamp):
    """
    Logs a user's spending transaction.
    """
    try:
        spending_sheet.append_row([user_id, category, amount, emotion, timestamp])
        return {"status": "success", "message": "Spending logged successfully."}
    except Exception as e:
        return {"status": "error", "message": f"Failed to log spending: {e}"}

def get_all_users():
    """
    Retrieves all users from the Users worksheet.
    """
    try:
        users = users_sheet.get_all_records()
        return users
    except Exception as e:
        return {"status": "error", "message": f"Failed to retrieve users: {e}"}

def get_spending_logs(user_id):
    """
    Retrieves all spending logs for a specific user.
    """
    try:
        logs = spending_sheet.get_all_records()
        user_logs = [log for log in logs if log["user_id"] == user_id]
        return user_logs
    except Exception as e:
        return {"status": "error", "message": f"Failed to retrieve spending logs: {e}"}

def update_crisis_mode(user_id, status):
    """
    Updates the crisis mode status (True/False) in the Users worksheet.
    """
    try:
        users = users_sheet.get_all_records()
        for index, user in enumerate(users, start=2):  # Start from row 2 (row 1 has headers)
            if user["user_id"] == user_id:
                users_sheet.update_cell(index, 4, "TRUE" if status else "FALSE")
                return {"status": "success", "message": f"Crisis mode set to {status} for {user_id}"}
        return {"status": "error", "message": f"User {user_id} not found"}
    except Exception as e:
        return {"status": "error", "message": f"Database update failed: {e}"}

if __name__ == "__main__":
    print(add_user("user_123", "Alice", "alice@example.com"))
    print(log_spending("user_123", "Food", 15, "Happy", "2025-02-14 10:00:00"))
    print(get_all_users())
    print(get_spending_logs("user_123"))
    print(update_crisis_mode("user_123", True))
