from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import add_user, log_spending, get_all_users, get_spending_logs, update_crisis_mode

# Initialize FastAPI app
app = FastAPI()

# ✅ Data Models
class User(BaseModel):
    user_id: str
    name: str
    email: str

class SpendingEntry(BaseModel):
    user_id: str
    category: str
    amount: float
    emotion: str
    timestamp: str

class CrisisModeToggle(BaseModel):
    user_id: str
    status: bool

# ✅ Root Endpoint
@app.get("/")
def home():
    return {"message": "Financial Therapy Assistant API is running!"}

# ✅ Add a new user
@app.post("/users/")
def create_user(user: User):
    try:
        add_user(user.user_id, user.name, user.email)
        return {"message": f"User {user.name} added successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ✅ Get all users
@app.get("/users/")
def list_users():
    return {"users": get_all_users()}

# ✅ Log a spending entry
@app.post("/spending/")
def add_spending(entry: SpendingEntry):
    try:
        log_spending(entry.user_id, entry.category, entry.amount, entry.emotion, entry.timestamp)
        return {"message": "Spending log added successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ✅ Get spending logs for a user
@app.get("/spending/{user_id}")
def user_spending(user_id: str):
    logs = get_spending_logs(user_id)
    if not logs:
        raise HTTPException(status_code=404, detail="No spending logs found for this user.")
    return {"spending_logs": logs}

# ✅ Update Crisis Mode status
@app.post("/crisis-mode/")
def toggle_crisis_mode(data: CrisisModeToggle):
    try:
        update_crisis_mode(data.user_id, data.status)
        return {"message": f"Crisis Mode updated to {data.status} for user {data.user_id}."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ✅ Run the FastAPI app (for local testing)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
