import { useState, useRef, useEffect } from 'react';
import { FiSend } from 'react-icons/fi';
import styles from './ChatInput.module.css';

export default function ChatInput({ onSend, loading }) {
  const [input, setInput] = useState('');
  const textareaRef = useRef(null);

  useEffect(() => {
    const textarea = textareaRef.current;
    if (textarea) {
      textarea.style.height = 'auto';
      textarea.style.height = `${Math.min(textarea.scrollHeight, 200)}px`;
    }
  }, [input]);

  const handleSubmit = () => {
    if (!input.trim() || loading) return;
    onSend(input);
    setInput('');
    if (textareaRef.current) {
      textareaRef.current.style.height = 'auto';
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit();
    }
  };

  return (
    <div className={styles.container}>
      <div className={styles.inputWrapper}>
        <textarea
          ref={textareaRef}
          className={styles.textarea}
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Send a message..."
          rows={1}
          disabled={loading}
          aria-label="Message input"
        />
        <button
          className={styles.sendBtn}
          onClick={handleSubmit}
          disabled={!input.trim() || loading}
          aria-label="Send message"
        >
          <FiSend />
        </button>
      </div>
      <p className={styles.hint}>
        Press Enter to send, Shift + Enter for new line
      </p>
    </div>
  );
}
