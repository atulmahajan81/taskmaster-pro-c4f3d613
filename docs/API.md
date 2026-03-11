# API Reference

## Authentication

### Register a New User

- **Endpoint**: `/api/v1/auth/register`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "email": "user@example.com",
    "password": "password123"
  }
  ```
- **Response**:
  ```json
  {
    "message": "User registered successfully."
  }
  ```

### User Login

- **Endpoint**: `/api/v1/auth/login`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "email": "user@example.com",
    "password": "password123"
  }
  ```
- **Response**:
  ```json
  {
    "access_token": "eyJhbGci...",
    "refresh_token": "dGhpcy..."
  }
  ```

## Task Management

### Retrieve a List of Tasks

- **Endpoint**: `/api/v1/tasks`
- **Method**: `GET`
- **Query Parameters**: `page`, `limit`, `search`, `priority`
- **Response**:
  ```json
  {
    "tasks": [
      {
        "id": "uuid",
        "title": "Task Title",
        "due_date": "2023-11-01",
        "priority": "high"
      }
    ]
  }
  ```

### Create a New Task

- **Endpoint**: `/api/v1/tasks`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "title": "New Task",
    "due_date": "2023-11-01",
    "priority": "high"
  }
  ```
- **Response**:
  ```json
  {
    "task_id": "uuid"
  }
  ```

## Categories

### Retrieve Categories

- **Endpoint**: `/api/v1/categories`
- **Method**: `GET`
- **Response**:
  ```json
  {
    "categories": ["Work", "Personal"]
  }
  ```

### Create a New Category

- **Endpoint**: `/api/v1/categories`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "name": "Work"
  }
  ```
- **Response**:
  ```json
  {
    "category_id": "uuid"
  }
  ```