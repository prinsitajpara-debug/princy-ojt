import { FiPlus, FiMessageSquare, FiTrash2, FiX } from 'react-icons/fi';
import styles from './Sidebar.module.css';

export default function Sidebar({
  chatHistory,
  currentChatId,
  onNewChat,
  onSelectChat,
  onDeleteChat,
  isOpen,
  onClose,
}) {
  const handleDelete = (e, chatId) => {
    e.stopPropagation();
    onDeleteChat(chatId);
  };

  return (
    <>
      {isOpen && <div className={styles.overlay} onClick={onClose} aria-hidden="true" />}

      <aside className={`${styles.sidebar} ${isOpen ? styles.open : ''}`}>
        <div className={styles.header}>
          <div className={styles.logo}>
            <div className={styles.logoIcon}>
              <FiMessageSquare />
            </div>
            <span className={styles.logoText}>ChatBot</span>
          </div>
          <button
            className={styles.closeBtn}
            onClick={onClose}
            aria-label="Close sidebar"
          >
            <FiX />
          </button>
        </div>

        <button className={styles.newChatBtn} onClick={onNewChat}>
          <FiPlus />
          <span>New Chat</span>
        </button>

        <nav className={styles.chatList} aria-label="Chat history">
          {chatHistory.length === 0 ? (
            <p className={styles.emptyHistory}>No chat history yet</p>
          ) : (
            chatHistory.map((chat) => (
              <div
                key={chat.id}
                className={`${styles.chatItem} ${
                  chat.id === currentChatId ? styles.active : ''
                }`}
                onClick={() => onSelectChat(chat.id)}
                role="button"
                tabIndex={0}
                onKeyDown={(e) => e.key === 'Enter' && onSelectChat(chat.id)}
              >
                <FiMessageSquare className={styles.chatIcon} />
                <span className={styles.chatTitle}>{chat.title}</span>
                <button
                  className={styles.deleteBtn}
                  onClick={(e) => handleDelete(e, chat.id)}
                  aria-label={`Delete ${chat.title}`}
                >
                  <FiTrash2 />
                </button>
              </div>
            ))
          )}
        </nav>
      </aside>
    </>
  );
}
