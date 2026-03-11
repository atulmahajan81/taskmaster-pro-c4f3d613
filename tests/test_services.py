# test_services.py

import pytest
from unittest.mock import MagicMock
from backend.services.user_service import UserService

@pytest.mark.asyncio
async def test_user_service_create_user(session):
    """Test user service for creating a user"""
    user_service = UserService(session)
    user_service.hash_password = MagicMock(return_value='hashed_password')
    user = await user_service.create_user('serviceuser@example.com', 'password123')
    assert user.email == 'serviceuser@example.com'

@pytest.mark.asyncio
async def test_user_service_get_user(session):
    """Test user service for retrieving a user"""
    user_service = UserService(session)
    user = await user_service.get_user_by_email('serviceuser@example.com')
    assert user.email == 'serviceuser@example.com'