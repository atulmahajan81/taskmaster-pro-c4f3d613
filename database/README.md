# TaskMaster Pro Database Schema

## Overview
The TaskMaster Pro database schema is designed to support a productivity application with key entities including Users, Tasks, and Categories. This document outlines the structure, relationships, and constraints of the database schema.

## Schema Diagram

- **Users**: Each user has a unique email and a password hash.
- **Tasks**: Tasks are associated with users, have a title, optional due date, and a priority level (Low, Medium, High).
- **Categories**: Categories are linked to users and can encompass multiple tasks.

## Tables

### Users
- **id**: UUID, Primary Key
- **email**: VARCHAR(255), Unique
- **password_hash**: VARCHAR(255)
- **created_at**: TIMESTAMPTZ, default to NOW()
- **updated_at**: TIMESTAMPTZ, auto-updates

### Tasks
- **id**: UUID, Primary Key
- **user_id**: UUID, Foreign Key referencing users(id)
- **title**: VARCHAR(255)
- **due_date**: DATE, optional
- **priority**: VARCHAR(50), checked for valid values
- **created_at**: TIMESTAMPTZ, default to NOW()
- **updated_at**: TIMESTAMPTZ, auto-updates

### Categories
- **id**: UUID, Primary Key
- **user_id**: UUID, Foreign Key referencing users(id)
- **name**: VARCHAR(255)
- **created_at**: TIMESTAMPTZ, default to NOW()
- **updated_at**: TIMESTAMPTZ, auto-updates

## Setup Instructions

1. Ensure PostgreSQL is installed and running.
2. Create a database named `taskmaster_pro`.
3. Run the `schema.sql` script to set up the tables.
4. Use Alembic to apply migrations:
   ```
   alembic upgrade head
   ```
5. Load seed data by running the `seed_data.sql` or `seed_data.py` script.
6. Configure your application to connect to the database using the connection string:
   ```
   postgresql+asyncpg://user:password@localhost:5432/taskmaster_pro
   ```

## Scalability Considerations

- **Caching**: Use Redis to cache frequently accessed data with a TTL of 5 minutes.
- **Horizontal Scaling**: The application can scale horizontally by adding more instances.
- **Indexing**: Optimized indexing on commonly queried fields like `email`, `user_id`, and `due_date`.
- **Async Tasks**: Use Celery for handling background tasks efficiently.