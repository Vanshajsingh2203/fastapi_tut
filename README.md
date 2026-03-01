# FastAPI Blog API 🚀

A modular, RESTful API for a blog application built with FastAPI. This project demonstrates core backend engineering principles, including database management, Object-Relational Mapping (ORM), strict data validation, and secure user authentication.

## 🌟 Features

* **CRUD Operations:** Complete Create, Read, Update, and Delete functionality for blog posts.
* **User Management:** Secure user registration and retrieval system.
* **Data Validation:** Strict input and output schema enforcement using Pydantic.
* **Database ORM:** Seamless database interactions using SQLAlchemy.
* **Secure Passwords:** Industry-standard password hashing utilizing Bcrypt (`passlib`).
* **Modular Routing:** Clean and scalable codebase architecture using FastAPI's `APIRouter`.
* **Database Migrations:** Version-controlled database schema updates using Alembic.
* **Interactive Documentation:** Automatic Swagger UI generation for easy API testing.

## 🛠️ Tech Stack

* **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
* **Language:** Python 3
* **Server:** Uvicorn
* **Database:** SQLite
* **ORM:** SQLAlchemy
* **Data Validation:** Pydantic
* **Migrations:** Alembic
* **Security/Hashing:** Passlib (Bcrypt)

## 📂 Project Structure

```text
├── alembic/                # Database migration scripts
├── blog/                   # Main application module
│   ├── routers/            # Modular API routes
│   │   ├── authentication.py
│   │   ├── blog.py
│   │   └── user.py
│   ├── database.py         # SQLAlchemy engine and session management
│   ├── hashing.py          # Cryptographic functions for password security
│   ├── main.py             # FastAPI application instance and router inclusion
│   ├── models.py           # SQLAlchemy database blueprints (Tables)
│   └── schemas.py          # Pydantic data validation contracts
├── blog.db                 # SQLite database file
├── alembic.ini             # Alembic configuration
└── requirements.txt        # Project dependencies


🚀 Installation & Setup

1. Clone the repository
-> git clone [https://github.com/Vanshajsingh2203/fastapi_tut.git](https://github.com/Vanshajsingh2203/fastapi_tut.git)
->cd fastapi_tut

2. Create and activate a virtual environment
Windows:
->python -m venv fastapi-env
->fastapi-env\Scripts\activate

Linux/Mac:
->python3 -m venv fastapi-env
->source fastapi-env/bin/activate

3. Install dependencies
->pip install -r requirements.txt

4. Run database migrations
->alembic upgrade head

5. Start the development server
->uvicorn blog.main:app --reload

📖 API Documentation
Once the server is running, FastAPI automatically generates interactive API documentation. You can access it by navigating to:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

From the Swagger UI, you can directly test the /login, /user, and /blog endpoints.
