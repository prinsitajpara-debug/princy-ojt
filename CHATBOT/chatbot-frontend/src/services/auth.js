import {
  validateRegisterPassword,
  validateLoginPassword,
  validatePasswordMatch,
} from '../utils/passwordValidation.js';

const TOKEN_KEY = 'chatbot_token';
const USER_KEY = 'chatbot_user';
const API_BASE = 'http://localhost:5000/api/auth';

export function getToken() {
  return localStorage.getItem(TOKEN_KEY);
}

export function getStoredAuth() {
  try {
    const token = getToken();
    const stored = localStorage.getItem(USER_KEY);
    if (token && stored) {
      return { ...JSON.parse(stored), token };
    }
  } catch {
    /* ignore */
  }
  return null;
}

export function clearAuth() {
  localStorage.removeItem(TOKEN_KEY);
  localStorage.removeItem(USER_KEY);
}

export function saveAuth(user, token) {
  localStorage.setItem(TOKEN_KEY, token);
  localStorage.setItem(USER_KEY, JSON.stringify(user));
}

async function parseResponse(response) {
  try {
    return await response.json();
  } catch {
    return {};
  }
}

function isNetworkError(error) {
  return (
    error instanceof TypeError ||
    error.message?.includes('Failed to fetch') ||
    error.message?.includes('NetworkError')
  );
}

/**
 * Verify stored JWT and fetch user profile from backend.
 */
export async function fetchProfile() {
  const token = getToken();
  if (!token) return null;

  const response = await fetch(`${API_BASE}/profile`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  const data = await parseResponse(response);

  if (!response.ok) {
    clearAuth();
    throw new Error(data.message || 'Session expired. Please log in again.');
  }

  const user = {
    id: data.user.id,
    name: data.user.name,
    email: data.user.email,
    token,
  };

  saveAuth(user, token);
  return user;
}

export async function login(email, password) {
  const normalizedEmail = email.trim().toLowerCase();

  if (!normalizedEmail) {
    throw new Error('Email is required');
  }

  const passwordCheck = validateLoginPassword(password);
  if (!passwordCheck.valid) {
    throw new Error(passwordCheck.message);
  }

  const response = await fetch(`${API_BASE}/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: normalizedEmail, password }),
  });

  const data = await parseResponse(response);

  if (!response.ok) {
    throw new Error(data.message || 'Login failed');
  }

  const user = {
    id: data.user.id,
    name: data.user.name,
    email: data.user.email,
  };

  saveAuth(user, data.token);
  return { ...user, token: data.token };
}

export async function register(name, email, password, confirmPassword) {
  const normalizedEmail = email.trim().toLowerCase();
  const trimmedName = name.trim();

  if (!trimmedName || !normalizedEmail || !password || !confirmPassword) {
    throw new Error('All fields are required');
  }

  const passwordCheck = validateRegisterPassword(password);
  if (!passwordCheck.valid) {
    throw new Error(passwordCheck.message);
  }

  const matchCheck = validatePasswordMatch(password, confirmPassword);
  if (!matchCheck.valid) {
    throw new Error(matchCheck.message);
  }

  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(normalizedEmail)) {
    throw new Error('Please enter a valid email address');
  }

  try {
    const response = await fetch(`${API_BASE}/register`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        name: trimmedName,
        email: normalizedEmail,
        password,
        confirmPassword,
      }),
    });

    const data = await parseResponse(response);

    if (!response.ok) {
      throw new Error(data.message || 'Registration failed');
    }

    const user = {
      id: data.user.id,
      name: data.user.name,
      email: data.user.email,
    };

    return user;
  } catch (error) {
    if (!isNetworkError(error)) {
      throw error;
    }

    const networkError = new Error(
      'Cannot connect to backend. Please start the server: cd backend && npm run dev'
    );
    networkError.cause = error;
    throw networkError;
  }
}
