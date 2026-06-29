import { useState } from 'react';
import ReactMarkdown from 'react-markdown';
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { oneDark } from 'react-syntax-highlighter/dist/esm/styles/prism';
import { FiCopy, FiCheck, FiRefreshCw } from 'react-icons/fi';
import styles from './ChatMessage.module.css';

function formatTime(date) {
  return new Date(date).toLocaleTimeString([], {
    hour: '2-digit',
    minute: '2-digit',
  });
}

export default function ChatMessage({
  message,
  isLast,
  onRegenerate,
  loading,
}) {
  const [copied, setCopied] = useState(false);
  const isUser = message.role === 'user';

  const handleCopy = async () => {
    try {
      await navigator.clipboard.writeText(message.content);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch {
      /* clipboard unavailable */
    }
  };

  return (
    <div
      className={`${styles.message} ${isUser ? styles.user : styles.assistant} ${
        message.isError ? styles.error : ''
      }`}
    >
      <div className={styles.bubble}>
        {isUser ? (
          <p className={styles.text}>{message.content}</p>
        ) : (
          <div className={styles.markdown}>
            <ReactMarkdown
              components={{
                code({ className, children, ...props }) {
                  const match = /language-(\w+)/.exec(className || '');
                  const codeString = String(children).replace(/\n$/, '');

                  if (match) {
                    return (
                      <SyntaxHighlighter
                        style={oneDark}
                        language={match[1]}
                        PreTag="div"
                        customStyle={{
                          margin: '8px 0',
                          borderRadius: '8px',
                          fontSize: '13px',
                        }}
                        {...props}
                      >
                        {codeString}
                      </SyntaxHighlighter>
                    );
                  }

                  return (
                    <code className={styles.inlineCode} {...props}>
                      {children}
                    </code>
                  );
                },
              }}
            >
              {message.content}
            </ReactMarkdown>
          </div>
        )}

        <div className={styles.footer}>
          <span className={styles.timestamp}>{formatTime(message.timestamp)}</span>

          {!isUser && (
            <div className={styles.actions}>
              <button
                className={styles.actionBtn}
                onClick={handleCopy}
                aria-label="Copy response"
                title="Copy"
              >
                {copied ? <FiCheck /> : <FiCopy />}
              </button>
              {isLast && onRegenerate && (
                <button
                  className={styles.actionBtn}
                  onClick={onRegenerate}
                  disabled={loading}
                  aria-label="Regenerate response"
                  title="Regenerate"
                >
                  <FiRefreshCw />
                </button>
              )}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
