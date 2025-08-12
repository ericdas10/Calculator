# Math Operations API - Flask Microservice

This project implements a RESTful microservice for basic mathematical operations using Python and Flask. The service supports operations such as Fibonacci calculation, factorial, and power, and includes persistent request logging and intelligent caching for performance.

## Features

* REST API built with Flask
* SQLite or SQL Server database support
* Mathematical operations:

  * Fibonacci (`/api/fibonacci`)
  * Factorial (`/api/factorial`)
  * Power (`/api/pow`)
* Persistent logging of all requests in the database
* Caching mechanism (database-based) for all operations:

  * Seed-based incremental calculation for Fibonacci and Factorial
  * Composite key caching for Power
* User registration and login endpoints
* Input validation with Pydantic
* Code quality ensured with flake8

## Technologies Used

* Python 3.11+
* Flask
* SQLAlchemy
* SQL Server (via `pyodbc`)
* Pydantic
* Flask-CORS
* flake8

## Example Usage

### POST /api/fibonacci

```json
{
  "n": 10
}
```

### POST /api/factorial

```json
{
  "n": 5
}
```

### POST /api/pow

```json
{
  "base": 2,
  "exponent": 3
}
```

### POST /api/register

```json
{
  "username": "user1",
  "password": "pass123"
}
```

### POST /api/login

```json
{
  "username": "user1",
  "password": "pass123"
}
```

## Project Structure

```
app/
├── model/                # Pydantic + ORM models
├── persistence/          # Database setup + repositories
├── services/             # Business logic, API controller
├── config/               # Settings and environment config
├── __init__.py           # Flask app factory
run.py                    # Application entry point
```

## Notes

* CORS is enabled for local frontend integration
* API is prepared for integration with a React client
* JWT authentication can be added easily later
