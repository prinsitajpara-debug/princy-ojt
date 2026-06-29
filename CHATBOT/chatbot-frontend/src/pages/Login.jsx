import { useState, useEffect } from 'react';
import { Link, useNavigate, useLocation } from 'react-router-dom';
import { FiMessageSquare, FiMail, FiLock, FiSun, FiMoon } from 'react-icons/fi';
import toast from 'react-hot-toast';
import { useAuth } from '../hooks/useAuth';
import { validateLoginForm } from '../utils/authValidation';
import styles from './Auth.module.css';

export default function Login({ darkMode, onToggleDarkMode }) {
  const { login } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();
  const [email, setEmail] = useState(() => location.state?.email || '');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (location.state?.fromRegister) {
      toast.success('Registration complete! Please sign in to open the chatbot.');
      navigate(location.pathname, { replace: true, state: {} });
    }
  }, [location.pathname, location.state?.fromRegister, navigate]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const validation = validateLoginForm({ email, password });
    if (!validation.valid) {
      toast.error(validation.message);
      return;
    }

    setLoading(true);

    try {
      const user = await login(email, password);
      toast.success(`Welcome, ${user.name}! Opening chatbot...`);
      navigate('/chatbot', { replace: true });
    } catch (error) {
      toast.error(error.message || 'Login failed');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className={styles.page}>
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
          <p className={styles.subtitle}>Sign in to continue to your assistant</p>
        </div>

        <form className={styles.form} onSubmit={handleSubmit} noValidate>
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
              minLength={6}
              maxLength={128}
              autoComplete="current-password"
            />
          </div>

          <button type="submit" className={styles.submitBtn} disabled={loading}>
            {loading ? 'Signing in...' : 'Sign In to Chatbot'}
          </button>
        </form>

        <p className={styles.switch}>
          Don&apos;t have an account?{' '}
          <Link to="/register">Create account</Link>
        </p>
      </div>
    </div>
  );
}
