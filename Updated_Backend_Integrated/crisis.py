import time
from database import update_crisis_mode
from chatbot import send_alert

def activate_crisis_mode(user_id):
    """
    Activates Crisis Mode for a user by updating the database
    and sending an alert.
    """
    try:
        update_crisis_mode(user_id, status=True)
        send_alert(user_id, "🚨 Crisis Mode Activated! We've temporarily blocked impulse spending apps to help you stay on track. Breathe. You got this! 💙")
        return {"status": "success", "message": "Crisis Mode activated successfully."}
    except Exception as e:
        return {"status": "error", "message": f"Failed to activate Crisis Mode: {e}"}

def deactivate_crisis_mode(user_id):
    """
    Deactivates Crisis Mode for a user.
    """
    try:
        update_crisis_mode(user_id, status=False)
        send_alert(user_id, "✅ Crisis Mode Deactivated! You're back in control. Remember, mindful spending is key. 💰✨")
        return {"status": "success", "message": "Crisis Mode deactivated successfully."}
    except Exception as e:
        return {"status": "error", "message": f"Failed to deactivate Crisis Mode: {e}"}

if __name__ == "__main__":
    # Example Usage
    user_id = "user_123"

    print(activate_crisis_mode(user_id))
    time.sleep(5)  # Simulate some time passing
    print(deactivate_crisis_mode(user_id))
