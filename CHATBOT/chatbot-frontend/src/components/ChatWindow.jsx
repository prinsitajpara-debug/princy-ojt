import { useEffect, useRef } from 'react';
import { FiMessageSquare } from 'react-icons/fi';
import ChatMessage from './ChatMessage';
import { TypingIndicator } from './Loader';
import styles from './ChatWindow.module.css';

export default function ChatWindow({
  messages,
  loading,
  onRegenerate,
  onSuggestionClick,
}) {
  const bottomRef = useRef(null);
  const containerRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, loading]);

  const lastAssistantIndex = [...messages]
    .map((m, i) => (m.role === 'assistant' ? i : -1))
    .filter((i) => i !== -1)
    .pop();

  if (messages.length === 0 && !loading) {
    return (
      <div className={styles.empty}>
        <div className={styles.emptyIcon}>
          <FiMessageSquare />
        </div>
        <h2 className={styles.emptyTitle}>Start a new conversation...</h2>
        <p className={styles.emptyText}>
          Ask me anything — coding, writing, learning, or daily questions.
          Your chat history is saved securely to your account only.
        </p>
        <div className={styles.suggestions}>
          {[
            'Explain quantum computing simply',
            'Write a Python function to sort a list',
            'Help me plan a weekend trip',
          ].map((suggestion) => (
            <button
              key={suggestion}
              type="button"
              className={styles.suggestion}
              onClick={() => onSuggestionClick?.(suggestion)}
            >
              {suggestion}
            </button>
          ))}
        </div>
      </div>
    );
  }

  return (
    <div className={styles.window} ref={containerRef}>
      <div className={styles.messages}>
        {messages.map((message, index) => (
          <ChatMessage
            key={message.id}
            message={message}
            isLast={index === lastAssistantIndex}
            onRegenerate={onRegenerate}
            loading={loading}
          />
        ))}

        {loading && (
          <div className={styles.typingWrapper}>
            <div className={styles.typingBubble}>
              <TypingIndicator />
            </div>
          </div>
        )}

        <div ref={bottomRef} />
      </div>
    </div>
  );
}
