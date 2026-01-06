from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel

# --------------------
# APP
# --------------------
app = FastAPI()

# --------------------
# IN-MEMORY USER STORE
# --------------------
users_db = {}

# --------------------
# MODELS
# --------------------
class User(BaseModel):
    email: str
    password: str

class Question(BaseModel):
    question: str

# --------------------
# SIMPLE TOKEN AUTH
# --------------------
def create_token(email: str) -> str:
    return f"token-{email}"

def get_user_from_token(token: str):
    if not token or not token.startswith("token-"):
        raise HTTPException(status_code=401, detail="Invalid token")
    return token.replace("token-", "")

# --------------------
# ROUTES
# --------------------
@app.post("/register")
def register(user: User):
    if user.email in users_db:
        raise HTTPException(status_code=400, detail="User already exists")

    users_db[user.email] = user.password
    return {"message": "User registered"}

@app.post("/login")
def login(user: User):
    stored = users_db.get(user.email)
    if not stored or stored != user.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token(user.email)
    return {"token": token}

@app.post("/ask")
def ask(
    q: Question,
    authorization: str = Header(None)
):
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing Authorization header")

    token = authorization.replace("Bearer ", "")
    user_email = get_user_from_token(token)

    # --------------------
    # SIMULATED AI AGENT (LangChain-like flow)
    # --------------------
    summary = (
        "Summary: "
        + q.question.strip()[:150]
        + ("..." if len(q.question) > 150 else "")
    )

    # Simulated email sending
    print("EMAIL SENT")
    print("To:", user_email)
    print("Content:", summary)

    return {
        "user": user_email,
        "summary": summary
    }

