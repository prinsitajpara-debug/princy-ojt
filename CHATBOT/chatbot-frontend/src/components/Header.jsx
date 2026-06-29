import { useState, useRef, useEffect } from 'react';
import { FiMenu, FiSun, FiMoon, FiUser, FiLogOut } from 'react-icons/fi';
import styles from './Header.module.css';

export default function Header({
  title,
  darkMode,
  user,
  onToggleDarkMode,
  onToggleSidebar,
  onLogout,
}) {
  const [menuOpen, setMenuOpen] = useState(false);
  const menuRef = useRef(null);

  useEffect(() => {
    function handleClickOutside(e) {
      if (menuRef.current && !menuRef.current.contains(e.target)) {
        setMenuOpen(false);
      }
    }
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  const handleLogout = () => {
    setMenuOpen(false);
    onLogout?.();
  };

  const displayName = user?.name || user?.email?.split('@')[0] || 'User';

  return (
    <header className={styles.header}>
      <div className={styles.left}>
        <button
          className={styles.menuBtn}
          onClick={onToggleSidebar}
          aria-label="Toggle sidebar"
        >
          <FiMenu />
        </button>
        <h1 className={styles.title}>{title || 'ChatBot Assistant'}</h1>
      </div>

      <div className={styles.actions}>
        <button
          className={styles.iconBtn}
          onClick={onToggleDarkMode}
          aria-label={darkMode ? 'Switch to light mode' : 'Switch to dark mode'}
        >
          {darkMode ? <FiSun /> : <FiMoon />}
        </button>

        <div className={styles.profileMenu} ref={menuRef}>
          <button
            className={styles.profileBtn}
            onClick={() => setMenuOpen((prev) => !prev)}
            aria-label="User menu"
            aria-expanded={menuOpen}
          >
            <FiUser />
          </button>

          {menuOpen && (
            <div className={styles.dropdown}>
              <div className={styles.userInfo}>
                <span className={styles.userName}>{displayName}</span>
                <span className={styles.userEmail}>{user?.email}</span>
              </div>
              <button className={styles.logoutBtn} onClick={handleLogout}>
                <FiLogOut />
                <span>Logout</span>
              </button>
            </div>
          )}
        </div>
      </div>
    </header>
  );
}
