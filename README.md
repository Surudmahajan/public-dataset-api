# 📊 Public Dataset API — Single File Project

Welcome to the Public Dataset API, a lightweight and beginner-friendly project that shows how to build a fully functional API service using FastAPI, all inside one Python file (app.py).

With this simple project, you’ll learn how to handle user registration, secure login, and unique API key generation, backed by a local SQLite database.
It’s perfect for students, developers, and anyone who wants a clean example of building a real-world API with a user dashboard, password hashing, and HTML templates — all without complicated setups or extra files.
---

## 🚀 Features

- Everything in **one file** (`app.py`)
- User **registration** and **login**
- Passwords are **securely hashed**
- Every user gets a **unique API key**
- Uses **SQLite** (`users.db`) which is created automatically
- Simple **HTML pages** for login and dashboard

---

## ⚙️ Tech Used

- **Python**
- **FastAPI**
- **SQLite**
- **Jinja2** (for HTML templates)
- **python-multipart** (for handling form data)

---

## 🗝️ How It Works

- New users can **register** with their email and password — then they get an **API key**.
- Returning users can **log in** and see their **API key** again.
- User info is saved in **`users.db`** with **hashed passwords**.

---

## ✅ How To Run This Project

1. **Clone this project**  
   Download it from GitHub or clone it using `git`.

2. **Create a virtual environment**  
   Use Python’s `venv` to keep your packages clean.

3. **Activate the virtual environment**  
   - **Windows:** run the `activate` script in the `.venv\Scripts` folder  
   - **macOS/Linux:** use `source .venv/bin/activate`

4. **Install the required packages**  
   Install FastAPI, Uvicorn, Jinja2, and python-multipart using `pip`.

5. **Run the app**  
   Use Uvicorn to start the server. The app will be available at `http://127.0.0.1:8000`.

6. **Visit the site in your browser**  
   You will see the **signup and login form**. Register or log in and see your **API key** on the **dashboard**.

---

## 📌 Important Routes

- `/` → Signup and login page
- `/do-register` → Handles registration
- `/do-login` → Handles login
- `/dashboard` → Shows the user’s API key

---

## ✍️ Contributing

Pull requests are welcome! Fork this repo, make your changes, and open a PR.

---

## 👤 Author

**Surud Mahajan**

---

## ⚖️ License

This project is under the **MIT License**.









