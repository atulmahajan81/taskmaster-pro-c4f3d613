# test_models.py

import pytest
from sqlalchemy.exc import IntegrityError
from backend.models import User, Task, Category

@pytest.mark.asyncio
async def test_user_model_constraints(session):
    """Test user model constraints such as unique email"""
    user = User(email='unique@example.com', password_hash='hashed_pw')
    session.add(user)
    await session.commit()

    with pytest.raises(IntegrityError):
        duplicate_user = User(email='unique@example.com', password_hash='hashed_pw')
        session.add(duplicate_user)
        await session.commit()

@pytest.mark.asyncio
async def test_task_model_relationship(session):
    """Test task-user relationship"""
    user = User(email='taskowner@example.com', password_hash='hashed_pw')
    session.add(user)
    await session.commit()
    task = Task(user_id=user.id, title='Test Task', priority='low')
    session.add(task)
    await session.commit()
    retrieved_task = session.query(Task).filter(Task.user_id == user.id).first()
    assert retrieved_task.title == 'Test Task'