import axios from 'axios';

const api = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_BASE_URL,
  withCredentials: true
});

api.interceptors.request.use(
  config => {
    // Add JWT token if present
    return config;
  },
  error => Promise.reject(error)
);

api.interceptors.response.use(
  response => response,
  error => {
    if (error.response?.status === 401) {
      // Handle Unauthorized error
    }
    return Promise.reject(error);
  }
);

export default api;