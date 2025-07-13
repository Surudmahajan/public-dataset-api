# 📊 Public Dataset API — Single File Project

This is a simple **Public Dataset API** built with **FastAPI** — all logic is inside **one file (`app.py`)**.  
Users can **register**, **log in**, and get a **unique API key**.  
Everything is done in **one Python file**, plus **HTML templates** in a `templates/` folder.

---

## 🚀 Features

- ✅ All backend logic in `app.py`
- ✅ User **registration** & **login**
- ✅ Secure **password hashing**
- ✅ Unique **API key** for each user
- ✅ SQLite database (`users.db`) — auto-created
- ✅ Clean HTML pages for login & dashboard
- ✅ No extra modules — **one-file backend**

---

## 📂 Project Structure

📂 public-dataset-api/
├── app.py
├── templates/
│ ├── login.html
│ ├── dashboard.html
├── users.db (created automatically)
├── README.md

yaml
Copy
Edit

---

## ⚙️ Tech Used

- **Python 3**
- **FastAPI**
- **SQLite**
- **Jinja2** (HTML templates)
- **python-multipart** (form data)

---

## 🗝️ How It Works

1️⃣ **New user?** → Register with email + password → get your API key  
2️⃣ **Returning user?** → Log in → see your API key again  
3️⃣ All routes are handled in `app.py`  
4️⃣ Database: `users.db` stores users with **hashed passwords** and API keys

---

## ✅ How To Run

# 1️⃣ **Clone this repository**

```bash
git clone https://github.com/Surudmahajan/public-dataset-api.git
cd public-dataset-api

2️⃣ Create & activate a virtual environment

Windows:

bash
Copy
Edit
python -m venv .venv
.venv\Scripts\activate
macOS/Linux:

bash
Copy
Edit
python3 -m venv .venv
source .venv/bin/activate
3️⃣ Install dependencies

bash
Copy
Edit
pip install fastapi uvicorn jinja2 python-multipart
4️⃣ Run the app

bash
Copy
Edit
uvicorn app:app --reload
5️⃣ Open your browser

Visit: http://127.0.0.1:8000

