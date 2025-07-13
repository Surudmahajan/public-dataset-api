from fastapi import FastAPI, Query, HTTPException, Body
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
import sqlite3
import uuid
import bcrypt

class UserRegister(BaseModel):
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

app = FastAPI()

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


def verify_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))


templates = Jinja2Templates(directory="templates")

# ✅ Example dataset
countries_data = [
    {"name": "India", "code": "IN", "currency": "INR", "timezone": "Asia/Kolkata"},
    {"name": "United States", "code": "US", "currency": "USD", "timezone": "America/New_York"},
    {"name": "Japan", "code": "JP", "currency": "JPY", "timezone": "Asia/Tokyo"},
]


# ✅ Request model for signup
class UserSignup(BaseModel):
    email: str


# ✅ /countries endpoint
@app.get("/countries")
def get_countries(api_key: str = Query(...)):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE api_key = ?", (api_key,))
    user = cursor.fetchone()
    conn.close()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid API key")

    return {"countries": countries_data}

@app.post("/register")
def register(user: UserRegister):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    hashed_pw = hash_password(user.password)
    api_key = str(uuid.uuid4())

    try:
        cursor.execute(
            "INSERT INTO users (email, password, api_key) VALUES (?, ?, ?)",
            (user.email, hashed_pw, api_key)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        raise HTTPException(status_code=400, detail="Email already registered.")

    conn.close()
    return {"email": user.email, "api_key": api_key}

@app.post("/login")
def login(user: UserLogin):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT password, api_key FROM users WHERE email = ?",
        (user.email,)
    )
    row = cursor.fetchone()
    conn.close()

    if row is None:
        raise HTTPException(status_code=400, detail="Invalid email or password.")

    hashed_pw, api_key = row

    if not verify_password(user.password, hashed_pw):
        raise HTTPException(status_code=400, detail="Invalid email or password.")

    return {"email": user.email, "api_key": api_key}


# ✅ /countries/{code} endpoint
@app.get("/countries/{code}")
def get_country_by_code(code: str, api_key: str = Query(...)):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE api_key = ?", (api_key,))
    user = cursor.fetchone()
    conn.close()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid API key")

    for country in countries_data:
        if country["code"].lower() == code.lower():
            return country

    raise HTTPException(status_code=404, detail="Country not found")



# ✅ /signup endpoint
@app.post("/signup")
def signup(user: UserSignup):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    api_key = str(uuid.uuid4())

    try:
        cursor.execute(
            "INSERT INTO users (email, api_key) VALUES (?, ?)",
            (user.email, api_key)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        raise HTTPException(status_code=400, detail="Email already registered.")

    conn.close()
    return {"email": user.email, "api_key": api_key}
@app.get("/", response_class=HTMLResponse)
def read_signup(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

from fastapi import Form
from fastapi.responses import RedirectResponse

# Serve login/register page
@app.get("/", response_class=HTMLResponse)
def show_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "message": ""})

# Handle registration form
@app.post("/do-register")
def do_register(request: Request, email: str = Form(...), password: str = Form(...)):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    hashed_pw = hash_password(password)
    api_key = str(uuid.uuid4())

    try:
        cursor.execute(
            "INSERT INTO users (email, password, api_key) VALUES (?, ?, ?)",
            (email, hashed_pw, api_key)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        return templates.TemplateResponse("login.html", {"request": request, "message": "Email already registered."})

    conn.close()
    return RedirectResponse(f"/dashboard?email={email}&api_key={api_key}", status_code=303)

# Handle login form
@app.post("/do-login")
def do_login(request: Request, email: str = Form(...), password: str = Form(...)):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT password, api_key FROM users WHERE email = ?", (email,))
    row = cursor.fetchone()
    conn.close()

    if row is None or not verify_password(password, row[0]):
        return templates.TemplateResponse("login.html", {"request": request, "message": "Invalid email or password."})

    api_key = row[1]
    return RedirectResponse(f"/dashboard?email={email}&api_key={api_key}", status_code=303)

# Dashboard page
@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request, email: str, api_key: str):
    return templates.TemplateResponse("dashboard.html", {"request": request, "email": email, "api_key": api_key})

