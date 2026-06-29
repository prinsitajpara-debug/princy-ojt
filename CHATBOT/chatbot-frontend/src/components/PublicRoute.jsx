import { Navigate } from 'react-router-dom';
import { useAuth } from '../hooks/useAuth';
import Loader from './Loader';
import styles from '../App.module.css';

export default function PublicRoute({ children }) {
  const { isAuthenticated, authLoading } = useAuth();

  if (authLoading) {
    return (
      <div className={styles.loadingScreen}>
        <Loader size="large" text="Loading..." />
      </div>
    );
  }

  if (isAuthenticated) {
    return <Navigate to="/chatbot" replace />;
  }

  return children;
}
