import styles from './Loader.module.css';

export default function Loader({ size = 'medium', text }) {
  return (
    <div className={styles.container} role="status" aria-label="Loading">
      <div className={`${styles.spinner} ${styles[size]}`}>
        <div className={styles.dot} />
        <div className={styles.dot} />
        <div className={styles.dot} />
      </div>
      {text && <span className={styles.text}>{text}</span>}
    </div>
  );
}

export function TypingIndicator() {
  return (
    <div className={styles.typing} aria-label="Assistant is typing">
      <span className={styles.typingDot} />
      <span className={styles.typingDot} />
      <span className={styles.typingDot} />
    </div>
  );
}
