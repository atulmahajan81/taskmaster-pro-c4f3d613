import { useQuery } from 'react-query';
import api from '../api';
import { Category } from '../types';

export const useCategories = () => {
  return useQuery<Category[], Error>('categories', async () => {
    const { data } = await api.get('/api/v1/categories');
    return data.categories;
  });
};