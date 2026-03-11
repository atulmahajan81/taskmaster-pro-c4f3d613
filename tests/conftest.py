# conftest.py

import pytest
from httpx import AsyncClient
from asgi_lifespan import LifespanManager
from unittest.mock import AsyncMock
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from backend.main import app
from backend.database import Base, get_async_session

DATABASE_URL = 'sqlite+aiosqlite:///:memory:'

@pytest.fixture(scope='session')
def event_loop():
    return asyncio.get_event_loop()

@pytest.fixture(scope='session')
async def async_client():
    async with LifespanManager(app):
        async with AsyncClient(app=app, base_url='http://testserver') as ac:
            yield ac

@pytest.fixture(scope='session')
async def test_db():
    engine = create_async_engine(DATABASE_URL, echo=True)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    yield async_session
    await engine.dispose()

@pytest.fixture(scope='function')
async def session(test_db):
    async with test_db() as session:
        yield session

@pytest.fixture(scope='function')
async def auth_tokens(async_client):
    # Mock implementation for token retrieval
    return {'access_token': 'test_access_token', 'refresh_token': 'test_refresh_token'}

@pytest.fixture(scope='function')
async def create_user(session):
    # Factory function to create a user
    async def _create_user(email: str, password: str):
        pass
    return _create_user