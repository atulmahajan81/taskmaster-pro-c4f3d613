# Database

## Schema Overview

The primary database used is PostgreSQL. The schema consists of tables for users, tasks, categories, and their relationships.

## Entity Relationships

- **Users**: Contains user information such as email and password hashes.
- **Tasks**: Contains task details such as title, due date, and priority.
- **Categories**: Contains categories to which tasks can be assigned.

## Migration Guide

Database migrations are managed using Alembic.

1. **Create a New Migration**
   ```bash
   alembic revision --autogenerate -m "Description of migration"
   ```

2. **Apply Migrations**
   ```bash
   alembic upgrade head
   ```

3. **Rollback Migrations**
   ```bash
   alembic downgrade -1
   ```