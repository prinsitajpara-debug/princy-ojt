import { useState } from 'react';
import { FiMessageSquare, FiMail, FiLock, FiUser, FiSun, FiMoon } from 'react-icons/fi';
import toast from 'react-hot-toast';
import styles from './Login.module.css';

export default function Login({
  onLogin,
  onRegister,
  darkMode,
  onToggleDarkMode,
}) {
  const [isRegister, setIsRegister] = useState(false);
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);
  const [redirecting, setRedirecting] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      if (isRegister) {
        const user = await onRegister(name, email, password);
        setRedirecting(true);
        toast.success(`Welcome, ${user.name || name}! Opening chatbot...`);
      } else {
        const user = await onLogin(email, password);
        setRedirecting(true);
        toast.success(`Welcome back, ${user.name || 'User'}! Opening chatbot...`);
      }
    } catch (error) {
      toast.error(error.message || 'Authentication failed');
      setRedirecting(false);
    } finally {
      setLoading(false);
    }
  };

  const toggleMode = () => {
    setIsRegister((prev) => !prev);
    setName('');
    setEmail('');
    setPassword('');
  };

  return (
    <div className={styles.page}>
      {redirecting && (
        <div className={styles.redirectOverlay}>
          <div className={styles.redirectCard}>
            <FiMessageSquare className={styles.redirectIcon} />
            <p>{isRegister ? 'Registration complete!' : 'Login successful!'}</p>
            <span>Opening chatbot...</span>
          </div>
        </div>
      )}
      <button
        type="button"
        className={styles.themeBtn}
        onClick={onToggleDarkMode}
        aria-label={darkMode ? 'Switch to light mode' : 'Switch to dark mode'}
      >
        {darkMode ? <FiSun /> : <FiMoon />}
      </button>

      <div className={styles.card}>
        <div className={styles.brand}>
          <div className={styles.logo}>
            <FiMessageSquare />
          </div>
          <h1 className={styles.title}>ChatBot</h1>
          <p className={styles.subtitle}>
            {isRegister
              ? 'Create an account to start chatting'
              : 'Sign in to continue to your assistant'}
          </p>
        </div>

        <form className={styles.form} onSubmit={handleSubmit}>
          {isRegister && (
            <div className={styles.field}>
              <FiUser className={styles.icon} />
              <input
                type="text"
                placeholder="Full name"
                value={name}
                onChange={(e) => setName(e.target.value)}
                disabled={loading}
                required
                autoComplete="name"
              />
            </div>
          )}

          <div className={styles.field}>
            <FiMail className={styles.icon} />
            <input
              type="email"
              placeholder="Email address"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              disabled={loading}
              required
              autoComplete="email"
            />
          </div>

          <div className={styles.field}>
            <FiLock className={styles.icon} />
            <input
              type="password"
              placeholder="Password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              disabled={loading}
              required
              minLength={isRegister ? 6 : 1}
              autoComplete={isRegister ? 'new-password' : 'current-password'}
            />
          </div>

          <button type="submit" className={styles.submitBtn} disabled={loading || redirecting}>
            {loading || redirecting
              ? isRegister
                ? 'Creating account...'
                : 'Signing in...'
              : isRegister
                ? 'Create Account & Continue'
                : 'Sign In'}
          </button>
        </form>

        <p className={styles.switch}>
          {isRegister ? 'Already have an account?' : "Don't have an account?"}{' '}
          <button type="button" onClick={toggleMode} disabled={loading}>
            {isRegister ? 'Sign in' : 'Sign up'}
          </button>
        </p>

        {!isRegister && (
          <div className={styles.demo}>
            <p>Demo credentials:</p>
            <code>demo@chatbot.com</code>
            <code>demo123</code>
          </div>
        )}
      </div>
    </div>
  );
}
