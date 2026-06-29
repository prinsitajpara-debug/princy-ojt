import axios from 'axios';
import { getToken, clearAuth } from './auth';

const API_BASE_URL = 'http://localhost:5000/api/chat';

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 60000,
  headers: {
    'Content-Type': 'application/json',
  },
});

api.interceptors.request.use((config) => {
  const token = getToken();
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      clearAuth();
      window.location.href = '/login';
    }

    const message =
      error.response?.data?.message ||
      error.response?.data?.error ||
      error.message ||
      'An unexpected error occurred';
    return Promise.reject(new Error(message));
  }
);

export async function sendMessage(message) {
  const { data } = await api.post('/', {
    message,
  });
  return data;
}

export async function getChatHistory() {
  const { data } = await api.get('/history');
  return data;
}

export async function deleteChat(chatId) {
  const { data } = await api.delete(`/${chatId}`);
  return data;
}

export default api;
