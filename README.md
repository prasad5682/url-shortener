# URL Shortener Service with Analytics

## Project Overview
This project is a URL Shortener service similar to bit.ly or TinyURL. It converts long URLs into short, easy-to-share links and tracks analytics for every redirect.

The application is built using FastAPI and SQLite, focusing on clean API design, proper database modeling, and reliable backend functionality.

---

## Objective
- Generate short URLs for long URLs
- Redirect users using HTTP 302 status code
- Track click analytics (count, timestamp, IP address, User-Agent)
- Handle invalid requests gracefully

---

## Tech Stack
- Python
- FastAPI
- SQLite
- SQLAlchemy
- Swagger / OpenAPI

---

## Project Structure
url-shortener/
├── main.py
├── database.py
├── models.py
├── schemas.py
├── utils.py
├── README.md
└── .gitignore

yaml
Copy code

---

## Database Design

### UrlMapping Table
- id (Primary Key)
- original_url
- short_code (Unique)
- created_at

### Click Table
- id (Primary Key)
- url_id (Foreign Key)
- ip_address
- user_agent
- clicked_at

---

## Short Code Generation
- A random alphanumeric string of 6 characters is generated.
- The system checks the database for existing short codes.
- If a collision occurs, a new code is generated until a unique one is found.

---

## API Endpoints

### POST /api/shorten
Creates a shortened URL.

Request:
```json
{
  "original_url": "https://www.google.com"
}
Response:

json
Copy code
{
  "short_code": "3H5NUK"
}
GET /{short_code}
Redirects to the original URL using HTTP 302 and records click analytics.

GET /api/stats/{short_code}
Returns analytics data for the given short code.

Response:

json
Copy code
{
  "short_code": "3H5NUK",
  "total_clicks": 5
}
Error Handling
Returns 404 Not Found for invalid short codes

Handles invalid input gracefully

How to Run Locally
Clone the repository

bash
Copy code
git clone https://github.com/prasad5682/url-shortener.git
cd url-shortener
Create and activate virtual environment

bash
Copy code
py -m venv venv
venv\Scripts\activate
Install dependencies

bash
Copy code
pip install fastapi uvicorn sqlalchemy pydantic
Run the application

bash
Copy code
uvicorn main:app --reload
Open Swagger UI

arduino
Copy code
http://127.0.0.1:8000/docs
API Testing
Swagger UI is available at /docs

OpenAPI specification available at /openapi.json

Learning Outcomes
REST API development using FastAPI

Database modeling with SQLAlchemy

Handling unique constraints and collisions

Implementing analytics tracking

Proper use of HTTP status codes

