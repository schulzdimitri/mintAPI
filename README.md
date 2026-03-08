# mintAPI

A RESTful API for bank account management built with Python and Flask. It supports user registration, JWT-based authentication, and balance management backed by a SQLite database.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Environment Variables](#environment-variables)
  - [Database Setup](#database-setup)
  - [Running the Server](#running-the-server)
- [API Reference](#api-reference)
  - [Register User](#register-user)
  - [Login](#login)
  - [Edit Balance](#edit-balance)
- [Running Tests](#running-tests)
- [Architecture](#architecture)

---

## Features

- User registration with bcrypt password hashing
- JWT-based authentication with configurable expiration
- Protected route for balance management
- SQLite persistence
- Clean Architecture pattern (Controllers, Views, Models, Drivers)

## Tech Stack

| Layer        | Technology          |
| ------------ | ------------------- |
| Framework    | Flask 3.1.3         |
| Database     | SQLite (via sqlite3) |
| Auth         | PyJWT 2.11.0        |
| Hashing      | bcrypt              |
| Config       | python-dotenv 1.2.2 |
| Testing      | pytest              |

## Project Structure

```
mintAPI/
├── init/
│   └── schema.sql              # Database schema
├── src/
│   ├── configs/                # JWT and environment configs
│   ├── controllers/            # Business logic
│   ├── drivers/                # JWT and password utilities
│   ├── errors/                 # Error types and handler
│   ├── main/
│   │   ├── composer/           # Dependency injection composers
│   │   ├── middlewares/        # JWT auth middleware
│   │   ├── routes/             # Flask Blueprints
│   │   └── server/             # Flask app factory
│   ├── models/
│   │   ├── interface/          # Repository interfaces
│   │   ├── repositories/       # SQLite repository implementation
│   │   └── settings/           # DB connection handler
│   └── views/                  # Request/Response adapters
├── run.py                      # Application entry point
└── requirements.txt
```

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/schulzdimitri/mintAPI.git
cd mintAPI

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the project root:

```env
JWT_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_HOURS=24
```

| Variable                    | Description                        | Example   |
| --------------------------- | ---------------------------------- | --------- |
| `JWT_KEY`                   | Secret key used to sign JWT tokens | `s3cr3t`  |
| `ALGORITHM`                 | JWT signing algorithm              | `HS256`   |
| `ACCESS_TOKEN_EXPIRE_HOURS` | Token validity period in hours     | `24`      |

### Database Setup

Run the SQL schema to initialize the SQLite database:

```bash
sqlite3 storage.db < init/schema.sql
```

### Running the Server

```bash
python run.py
```

The server will start on `http://localhost:3000`.

---

## API Reference

### Register User

Creates a new user account.

**Endpoint:** `POST /bank/registry`

**Request Body:**

```json
{
  "username": "johndoe",
  "password": "strongpassword"
}
```

**Success Response — `201 Created`:**

```json
{
  "type": "User",
  "count": 1,
  "username": "johndoe"
}
```

---

### Login

Authenticates a user and returns a JWT token.

**Endpoint:** `POST /bank/login`

**Request Body:**

```json
{
  "username": "johndoe",
  "password": "strongpassword"
}
```

**Success Response — `200 OK`:**

```json
{
  "access": true,
  "username": "johndoe",
  "autorization": "<jwt_token>"
}
```

---

### Edit Balance

Updates the balance of a user. Requires JWT authentication.

**Endpoint:** `PATCH /bank/balance/:user_id`

**Headers:**

| Header          | Description                          |
| --------------- | ------------------------------------ |
| `Authorization` | `Bearer <jwt_token>`                 |
| `uid`           | The ID of the authenticated user     |

**Request Body:**

```json
{
  "new_balance": 1500.00
}
```

**Success Response — `200 OK`:**

```json
{
  "type": "User",
  "count": 1,
  "new_balance": 1500.00
}
```

**Error Responses:**

| Status | Description                             |
| ------ | --------------------------------------- |
| `400`  | Bad Request — invalid or missing fields |
| `401`  | Unauthorized — invalid or missing token |
| `404`  | Not Found — user does not exist         |

---

## Running Tests

```bash
pytest
```

Tests are co-located with their respective modules following the `*_test.py` naming convention.

---

## Architecture

mintAPI follows **Clean Architecture** principles, keeping business logic decoupled from frameworks and infrastructure:

```
Routes → Composers → Views → Controllers → Models/Drivers
```

- **Routes** — Flask Blueprints; only handle HTTP input/output.
- **Composers** — Wire dependencies together (dependency injection).
- **Views** — Adapt HTTP requests, invoke controllers, and format responses.
- **Controllers** — Pure business logic; no framework dependencies.
- **Models** — Data access layer (repository pattern over SQLite).
- **Drivers** — Low-level utilities (JWT, bcrypt).
- **Middlewares** — Cross-cutting concerns (JWT verification).
