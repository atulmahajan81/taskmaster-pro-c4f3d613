# test_tasks.py

import pytest

@pytest.mark.asyncio
async def test_create_task(async_client, auth_tokens):
    """Test creating a new task"""
    response = await async_client.post('/api/v1/tasks', headers={'Authorization': f"Bearer {auth_tokens['access_token']}"}, json={'title': 'Test Task', 'due_date': '2023-12-31', 'priority': 'high'})
    assert response.status_code == 201
    assert 'task_id' in response.json()

@pytest.mark.asyncio
async def test_get_task_list(async_client, auth_tokens):
    """Test retrieving a list of tasks"""
    response = await async_client.get('/api/v1/tasks', headers={'Authorization': f"Bearer {auth_tokens['access_token']}"})
    assert response.status_code == 200
    assert 'tasks' in response.json()

@pytest.mark.asyncio
async def test_update_task(async_client, auth_tokens):
    """Test updating a task"""
    task_id = 'some-task-id'
    response = await async_client.put(f'/api/v1/tasks/{task_id}', headers={'Authorization': f"Bearer {auth_tokens['access_token']}"}, json={'title': 'Updated Task', 'due_date': '2024-01-01', 'priority': 'medium'})
    assert response.status_code == 200
    assert response.json()['message'] == 'Task updated successfully'

@pytest.mark.asyncio
async def test_delete_task(async_client, auth_tokens):
    """Test deleting a task"""
    task_id = 'some-task-id'
    response = await async_client.delete(f'/api/v1/tasks/{task_id}', headers={'Authorization': f"Bearer {auth_tokens['access_token']}"})
    assert response.status_code == 204