URL Shortener Service with Analytics

Project Overview
-----------------
This project is a URL Shortener service similar to bit.ly or TinyURL. It converts long URLs into short, easy-to-share links and tracks analytics for every redirect.

The application is built using FastAPI and SQLite, focusing on clean API design, proper database modeling, and reliable backend functionality.

Objective
---------
• Generate short URLs for long URLs  
• Redirect users using HTTP 302 status code  
• Track click analytics (count, timestamp, IP address, User-Agent)  
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
• id (Primary Key)  
• url_id (Foreign Key)  
• ip_address  
• user_agent  
• clicked_at  

Short Code Generation
---------------------
The system uses the database auto-increment ID of each URL and converts it into a Base62 encoded string to generate the short code.  
This guarantees that every short code is unique without requiring collision checks or repeated database queries.

API Endpoints
-----------------
POST /api/shorten  
Accepts an original URL and returns a generated short code.

GET /{short_code}  
Redirects the user to the original URL using HTTP 302 and records a click.

GET /api/stats/{short_code}  
Returns the total number of clicks for the given short code.

Error Handling
--------------
Returns HTTP 404 Not Found for invalid short codes and handles invalid input safely.

How to Run Locally
-----------------
1. Clone the repository  
2. Create and activate a Python virtual environment  
3. Install dependencies  
4. Run the server using Uvicorn  
5. Open http://127.0.0.1:8000/docs to test APIs  

API Testing
-----------
Swagger UI is available at /docs  
OpenAPI specification is available at /openapi.json  

Learning Outcomes
-----------------
• REST API development using FastAPI  
• Database modeling with SQLAlchemy  
• Base62 short code generation  
• Click analytics tracking  
• Secure configuration and validation  
• Proper use of HTTP status codes  
