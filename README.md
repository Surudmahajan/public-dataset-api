 ##📊 Public Dataset API — Single File Project
This is a simple Public Dataset API built with FastAPI — everything is inside one Python file (app.py).
Users can register, log in, and get a unique API key.
The project uses a local SQLite database and HTML templates.

##🚀 Features
Everything in one file (app.py)

User registration and login

Passwords are securely hashed

Every user gets a unique API key

Uses SQLite database (users.db) which is created automatically

Simple HTML pages for login and dashboard

##📂 Project Structure
app.py — the main FastAPI app (one file)

templates/ — contains login.html and dashboard.html

users.db — the SQLite database (created automatically)

README.md — this file

##⚙️ Tech Used
Python

FastAPI

SQLite

Jinja2 (for HTML templates)

python-multipart (for handling form data)

##🗝️ How It Works

New users can register with their email and password — then they get an API key.

Returning users can log in and see their API key again.

User info is saved in users.db with hashed passwords.

##✅ How To Run This Project
Clone this project to your computer
Download it from GitHub or clone it using git.

Create a virtual environment
Use Python’s venv to keep your packages clean.

Activate the virtual environment
On Windows: run the activate script in the .venv\Scripts folder.
On macOS/Linux: use source .venv/bin/activate.

Install the required packages
Install FastAPI, Uvicorn, Jinja2, and python-multipart using pip.

Run the app
Use Uvicorn to start the server.
The app will be available at http://127.0.0.1:8000.

Visit the site in your browser
You will see the signup and login form. Register or log in and see your API key on the dashboard.

##📌 Important Routes
/ — signup and login page

/do-register — handles registration

/do-login — handles login

/dashboard — shows the user’s API key

##✍️ Contributing
Pull requests are welcome! Fork this repo, make your changes, and open a PR.

##✍🏻Author
Surud Mahajan

##⚖️ License
This project is under the MIT License.










