# Backend Internship Home Assignment

This project implements a Flask server that interacts with the OpenAI API to answer questions and stores both questions and answers in a PostgreSQL database. It is dockerized for easy deployment using Docker Compose.

## Prerequisites

- Docker Compose Desktop
- Python 3.10
- Postman (for testing the API endpoints)

## Getting Started

1. **Clone the Repository**

2. **Configure Environment Variables**

Update the environment variables in `docker-compose.yml` and `alembic.ini` to match your local setup:

- **docker-compose.yml**:
  ```yaml
  environment:
    - POSTGRES_DB=<YOUR_POSTGRES_DB_NAME>
    - POSTGRES_PASSWORD=<YOUR_POSTGRES_PASSWORD>
    - POSTGRES_USER=<YOUR_POSTGRES_USER_NAME>
    - POSTGRES_HOST=<YOUR_POSTGRES_HOST>
    - POSTGRES_PORT=<YOUR_POSTGRES_PORT>
    - OPENAI_API_KEY=<YOUR_OPENAI_KEY>
  ```

- **alembic.ini**:
  ```
  sqlalchemy.url = postgresql+psycopg2://<YOUR_POSTGRES_USER_NAME>:<YOUR_POSTGRES_PASSWORD>@<YOUR_POSTGRES_HOST>:<YOUR_POSTGRES_PORT>/<YOUR_POSTGRES_DB_NAME>
  ```

 ### Docker
  The project uses Docker to containerize the Flask application, tests, and PostgreSQL database.
  If you run this project for the first time, run compose commad with the `--build` flag:
  ```
   docker-compose up --build -d
  ```
  To rerun the containers:
  ```
  docker-compose up -d
  ```
 
  This command builds and starts the Flask server, tests and PostgreSQL containers.

5. **Access the Server**

  The Flask server should now be running at `http://127.0.0.1:5000` by default.

## Using Postman

To test the `/ask` endpoint with Postman:

- **Method**: POST
- **URL**: `http://127.0.0.1:5000/ask`
- **Body**: JSON format
```json
{
   "question": "Ask your question here"
}
```
![WhatsApp Image 2024-07-09 at 10 06 50](https://github.com/netanel97/insait_assignment/assets/101398032/cf8f5306-7d9e-4506-be9f-06c03504837b)
![WhatsApp Image 2024-07-09 at 10 07 34](https://github.com/netanel97/insait_assignment/assets/101398032/5aa18b6c-4fb4-42d8-988b-01486328a03a)

## Database Migration
  The initial database migration is handled using Alembic. Upon starting the containers for the first time, Alembic scripts will automatically create the necessary tables (questions and answers) in your PostgreSQL database.

## Database Schema
* answers table:
  * id: Integer, primary key, autoincrement
  * question_id: Integer, foreign key referencing questions.id, not null
  * answer: Text, not null
  * created_at: DateTime, default: current timestamp
 

* questions table:
  * id: Integer, primary key, autoincrement
  * question: Text, not null
  * created_at: DateTime, default: current timestamp
```mermaid
erDiagram
    QUESTIONS {
        int id
        string question
        datetime created_at
    }
    ANSWERS {
        int id
        int question_id
        string answer
        datetime created_at
    }
    QUESTIONS ||--o{ ANSWERS : "question_id"
```






