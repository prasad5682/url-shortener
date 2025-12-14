URL Shortener Service with Analytics

Project Overview
-----------------
This project is a URL Shortener service similar to bit.ly or TinyURL. It converts long URLs into short, easy-to-share links and tracks analytics for every redirect.

The application is built using FastAPI and SQLite, focusing on clean API design, proper database modeling, and reliable backend functionality.

Objective
---------
• Generate short URLs for long URLs
• Redirect users using HTTP 302 status code
• Track click analytics such as click count, timestamp, IP address, and User-Agent
• Handle invalid requests gracefully

Tech Stack
----------
• Python
• FastAPI
• SQLite
• SQLAlchemy
• Swagger / OpenAPI

Project Structure
-----------------
url-shortener folder contains:
main.py
database.py
models.py
schemas.py
utils.py
README.md
.gitignore

Database Design
---------------
UrlMapping Table
• id (Primary Key)
• original_url
• short_code (Unique)
• created_at

Click Table
----------
• id (Primary Key)
• url_id (Foreign Key)
• ip_address
• user_agent
• clicked_at

Short Code Generation
---------------------
A random alphanumeric string of 6 characters is generated for each URL.
Before saving, the system checks whether the short code already exists in the database.
If a collision occurs, a new short code is generated until a unique one is found.

API Endpoints
-----------------
POST /api/shorten
Creates a shortened URL.
Input contains the original URL.
Response returns a generated short code.

Example behavior:
Original URL is submitted and a short code like 3H5NUK is returned.

GET /short_code
Redirects the user to the original URL using HTTP 302 status code.
Each redirect records click analytics.

GET /api/stats/short_code
Returns analytics data for the given short code.
Response includes total number of clicks.

Error Handling
Returns HTTP 404 Not Found when an invalid short code is requested.
Handles invalid input gracefully without crashing the application.

How to Run Locally
-------------------------
Step 1: Clone the repository
Clone the GitHub repository and move into the project directory.

Step 2: Create and activate virtual environment
Create a Python virtual environment and activate it.

Step 3: Install dependencies
Install FastAPI, Uvicorn, SQLAlchemy, and other required libraries.

Step 4: Run the application
Start the FastAPI server using Uvicorn with reload enabled.

Step 5: Open Swagger UI
Open browser and visit http://127.0.0.1:8000/docs
 to test APIs.

API Testing
Swagger UI is available at /docs
OpenAPI specification is available at /openapi.json

Learning Outcomes
• REST API development using FastAPI
• Database modeling with SQLAlchemy
• Handling unique constraints and collisions
• Implementing click analytics tracking
• Proper use of HTTP status codes