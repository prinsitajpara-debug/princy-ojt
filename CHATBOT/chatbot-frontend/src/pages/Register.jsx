import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import {
  FiMessageSquare,
  FiMail,
  FiLock,
  FiUser,
  FiSun,
  FiMoon,
} from 'react-icons/fi';
import toast from 'react-hot-toast';
import { useAuth } from '../hooks/useAuth';
import { validateRegisterForm } from '../utils/authValidation';
import PasswordRules from '../components/PasswordRules';
import styles from './Auth.module.css';

export default function Register({ darkMode, onToggleDarkMode }) {
  const { register } = useAuth();
  const navigate = useNavigate();
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const validation = validateRegisterForm({
      name,
      email,
      password,
      confirmPassword,
    });

    if (!validation.valid) {
      toast.error(validation.message);
      return;
    }

    setLoading(true);

    try {
      const user = await register(name, email, password, confirmPassword);
      navigate('/login', {
        replace: true,
        state: { email: user.email, fromRegister: true },
      });
    } catch (error) {
      toast.error(error.message || 'Registration failed');
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
          <h1 className={styles.title}>Create Account</h1>
          <p className={styles.subtitle}>Register to start chatting with AI</p>
        </div>

        <form className={styles.form} onSubmit={handleSubmit} noValidate>
          <div className={styles.field}>
            <FiUser className={styles.icon} />
            <input
              type="text"
              placeholder="Full name"
              value={name}
              onChange={(e) => setName(e.target.value)}
              disabled={loading}
              required
              minLength={2}
              autoComplete="name"
            />
          </div>

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
              minLength={8}
              maxLength={128}
              autoComplete="new-password"
            />
          </div>

          <PasswordRules password={password} />

          <div className={styles.field}>
            <FiLock className={styles.icon} />
            <input
              type="password"
              placeholder="Confirm password"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
              disabled={loading}
              required
              minLength={8}
              maxLength={128}
              autoComplete="new-password"
            />
          </div>

          {confirmPassword && password !== confirmPassword && (
            <p className={styles.fieldError}>Passwords do not match</p>
          )}

          <button type="submit" className={styles.submitBtn} disabled={loading}>
            {loading ? 'Creating account...' : 'Create Account'}
          </button>
        </form>

        <p className={styles.switch}>
          Already have an account?{' '}
          <Link to="/login">Sign in</Link>
        </p>
      </div>
    </div>
  );
}
