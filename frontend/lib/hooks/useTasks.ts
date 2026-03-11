import { useQuery } from 'react-query';
import api from '../api';
import { Task } from '../types';

export const useTasks = () => {
  return useQuery<Task[], Error>('tasks', async () => {
    const { data } = await api.get('/api/v1/tasks');
    return data.tasks;
  });
};