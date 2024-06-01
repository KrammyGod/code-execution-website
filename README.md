# code-execution-website

Frontend built using React, Typescript, and Tailwind CSS

Backend built using FastAPI

## How to run the project
The backend requires a PostgreSQL database, using [backend/.env.example](backend/.env.example), create a `.env` file filling out the database URL to connect to, filling in username, password, and database.

Then, the backend can be run by setting up a virtual environment using `python -m venv venv`, and install requirements using `pip install -r requirements.txt`. Then, run the backend using `uvicorn main:app --reload`.

For the frontend, the dependencies can be installed using `npm install`, and then run the frontend using `npm run dev`.
