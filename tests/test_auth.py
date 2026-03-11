# test_auth.py

import pytest

@pytest.mark.asyncio
async def test_register_user(async_client):
    """Test registering a new user"""
    response = await async_client.post('/api/v1/auth/register', json={'email': 'user@example.com', 'password': 'password123'})
    assert response.status_code == 201
    assert response.json()['message'] == 'User registered successfully'

@pytest.mark.asyncio
async def test_register_user_missing_fields(async_client):
    """Test registering a user with missing fields"""
    response = await async_client.post('/api/v1/auth/register', json={'email': 'user@example.com'})
    assert response.status_code == 422
    
@pytest.mark.asyncio
async def test_login_user(async_client, create_user):
    """Test user login with valid credentials"""
    await create_user('user@example.com', 'password123')
    response = await async_client.post('/api/v1/auth/login', json={'email': 'user@example.com', 'password': 'password123'})
    assert response.status_code == 200
    assert 'access_token' in response.json()

@pytest.mark.asyncio
async def test_login_user_invalid_credentials(async_client):
    """Test user login with invalid credentials"""
    response = await async_client.post('/api/v1/auth/login', json={'email': 'nonexistent@example.com', 'password': 'wrongpassword'})
    assert response.status_code == 401

@pytest.mark.asyncio
async def test_token_refresh(async_client, auth_tokens):
    """Test refreshing access token"""
    response = await async_client.post('/api/v1/auth/refresh', json={'refresh_token': auth_tokens['refresh_token']})
    assert response.status_code == 200
    assert 'access_token' in response.json()

@pytest.mark.asyncio
async def test_logout_user(async_client, auth_tokens):
    """Test user logout"""
    response = await async_client.post('/api/v1/auth/logout', headers={'Authorization': f"Bearer {auth_tokens['access_token']}"})
    assert response.status_code == 200
    assert response.json()['message'] == 'Successfully logged out'