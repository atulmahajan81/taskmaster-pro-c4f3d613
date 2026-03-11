# test_pagination.py

import pytest

@pytest.mark.asyncio
async def test_task_pagination(async_client, auth_tokens):
    """Test task list pagination"""
    response = await async_client.get('/api/v1/tasks?page=1&limit=10', headers={'Authorization': f"Bearer {auth_tokens['access_token']}"})
    assert response.status_code == 200
    assert len(response.json()['tasks']) <= 10

@pytest.mark.asyncio
async def test_task_filtering(async_client, auth_tokens):
    """Test filtering tasks by priority"""
    response = await async_client.get('/api/v1/tasks?priority=high', headers={'Authorization': f"Bearer {auth_tokens['access_token']}"})
    assert response.status_code == 200
    for task in response.json()['tasks']:
        assert task['priority'] == 'high'