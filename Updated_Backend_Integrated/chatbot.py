from gpt_integration import generate_financial_advice, generate_saving_tips, generate_emotional_support_message
from database import update_crisis_mode

def send_alert(user_id, message):
    """
    Simulates sending a chatbot alert to the user.
    """
    try:
        print(f"🔔 Alert for {user_id}: {message}")
        return {"status": "success", "message": f"Alert sent to {user_id}"}
    except Exception as e:
        return {"status": "error", "message": f"Failed to send alert: {e}"}

def crisis_alert(user_id):
    """
    Activates crisis mode for a user and sends an alert.
    """
    update_result = update_crisis_mode(user_id, True)
    
    if update_result["status"] == "success":
        send_alert(user_id, "🚨 Crisis Mode Activated! We’ve restricted impulsive spending actions. Need help? Let’s talk.")
        return {"status": "success", "message": "Crisis mode activated and alert sent."}
    
    return {"status": "error", "message": "Failed to activate crisis mode."}

if __name__ == "__main__":
    print(crisis_alert("user_123"))
