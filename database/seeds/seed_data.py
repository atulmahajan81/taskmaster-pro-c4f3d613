import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta
from myapp.models import User, Task, Category
import random

DATABASE_URL = 'postgresql+asyncpg://user:password@localhost:5432/taskmaster_pro'

engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

async def seed_data():
    async with AsyncSessionLocal() as session:
        # Seed Users
        users = [
            User(email='admin@example.com', password_hash='hashed_password1'),
            User(email='user1@example.com', password_hash='hashed_password2'),
            User(email='user2@example.com', password_hash='hashed_password3')
        ]
        session.add_all(users)
        await session.commit()

        # Seed Categories
        categories = []
        for user in users:
            for i in range(3):
                category = Category(user_id=user.id, name=f'Category {i+1} for {user.email}')
                categories.append(category)
        session.add_all(categories)
        await session.commit()

        # Seed Tasks
        priorities = ['Low', 'Medium', 'High']
        tasks = []
        for user in users:
            for i in range(10):
                task = Task(
                    user_id=user.id,
                    title=f'Task {i+1} for {user.email}',
                    due_date=datetime.now().date() + timedelta(days=random.randint(0, 30)),
                    priority=random.choice(priorities)
                )
                tasks.append(task)
        session.add_all(tasks)
        await session.commit()

if __name__ == '__main__':
    asyncio.run(seed_data())