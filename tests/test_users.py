# test_users.py

import pytest

@pytest.mark.asyncio
async def test_create_user(async_client, session):
    """Test creating a new user"""
    response = await async_client.post('/api/v1/users', json={'email': 'newuser@example.com', 'password': 'newpassword'})
    assert response.status_code == 201

@pytest.mark.asyncio
async def test_get_user_details(async_client, auth_tokens):
    """Test retrieving user details"""
    response = await async_client.get('/api/v1/users/me', headers={'Authorization': f"Bearer {auth_tokens['access_token']}"})
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_update_user(async_client, auth_tokens):
    """Test updating user information"""
    response = await async_client.put('/api/v1/users/me', headers={'Authorization': f"Bearer {auth_tokens['access_token']}"}, json={'email': 'updated@example.com'})
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_delete_user(async_client, auth_tokens):
    """Test deleting a user account"""
    response = await async_client.delete('/api/v1/users/me', headers={'Authorization': f"Bearer {auth_tokens['access_token']}"})
    assert response.status_code == 204

@pytest.mark.asyncio
async def test_list_users(async_client, auth_tokens):
    """Test listing all users"""
    response = await async_client.get('/api/v1/users', headers={'Authorization': f"Bearer {auth_tokens['access_token']}"})
    assert response.status_code == 200