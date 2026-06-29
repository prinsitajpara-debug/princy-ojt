import { useState, useEffect, useCallback } from 'react';
import * as authService from '../services/auth';
import { AuthContext } from './authContext';

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [authLoading, setAuthLoading] = useState(true);

  useEffect(() => {
    async function initAuth() {
      const stored = authService.getStoredAuth();
      if (!stored?.token) {
        setAuthLoading(false);
        return;
      }

      try {
        const profile = await authService.fetchProfile();
        setUser(profile);
      } catch {
        setUser(null);
      } finally {
        setAuthLoading(false);
      }
    }

    initAuth();
  }, []);

  const login = useCallback(async (email, password) => {
    const authenticatedUser = await authService.login(email, password);
    setUser(authenticatedUser);
    return authenticatedUser;
  }, []);

  const register = useCallback(async (name, email, password, confirmPassword) => {
    return authService.register(name, email, password, confirmPassword);
  }, []);

  const logout = useCallback(() => {
    authService.clearAuth();
    setUser(null);
  }, []);

  return (
    <AuthContext.Provider
      value={{
        user,
        isAuthenticated: !!user,
        authLoading,
        login,
        register,
        logout,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
}
