# test_integration.py

import pytest

@pytest.mark.asyncio
async def test_full_integration_flow(async_client):
    """Test full end-to-end flow: register → login → create resource → read → update → delete"""
    # Register
    response = await async_client.post('/api/v1/auth/register', json={'email': 'integration@example.com', 'password': 'password123'})
    assert response.status_code == 201
    
    # Login
    response = await async_client.post('/api/v1/auth/login', json={'email': 'integration@example.com', 'password': 'password123'})
    assert response.status_code == 200
    access_token = response.json()['access_token']
    
    # Create Task
    response = await async_client.post('/api/v1/tasks', headers={'Authorization': f"Bearer {access_token}"}, json={'title': 'Integration Task', 'due_date': '2023-12-31', 'priority': 'high'})
    assert response.status_code == 201
    task_id = response.json()['task_id']
    
    # Read Task
    response = await async_client.get(f'/api/v1/tasks/{task_id}', headers={'Authorization': f"Bearer {access_token}"})
    assert response.status_code == 200
    
    # Update Task
    response = await async_client.put(f'/api/v1/tasks/{task_id}', headers={'Authorization': f"Bearer {access_token}"}, json={'title': 'Updated Task', 'due_date': '2024-01-01', 'priority': 'medium'})
    assert response.status_code == 200
    
    # Delete Task
    response = await async_client.delete(f'/api/v1/tasks/{task_id}', headers={'Authorization': f"Bearer {access_token}"})
    assert response.status_code == 204