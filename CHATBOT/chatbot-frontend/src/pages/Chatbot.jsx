import { useNavigate } from 'react-router-dom';
import { useAuth } from '../hooks/useAuth';
import { useChat } from '../hooks/useChat';
import Sidebar from '../components/Sidebar';
import Header from '../components/Header';
import ChatWindow from '../components/ChatWindow';
import ChatInput from '../components/ChatInput';
import Loader from '../components/Loader';
import styles from '../App.module.css';

export default function Chatbot() {
  const navigate = useNavigate();
  const { user, logout } = useAuth();

  const handleLogout = () => {
    logout();
    navigate('/login', { replace: true });
  };
  const {
    messages,
    loading,
    chatHistory,
    darkMode,
    currentChatId,
    currentChat,
    sidebarOpen,
    setSidebarOpen,
    historyLoaded,
    handleNewChat,
    handleSelectChat,
    handleDeleteChat,
    handleSendMessage,
    handleRegenerate,
    toggleDarkMode,
  } = useChat(user?.id);

  if (!historyLoaded) {
    return (
      <div className={styles.loadingScreen}>
        <Loader size="large" text="Loading chats..." />
      </div>
    );
  }

  return (
    <div className={styles.app}>
      <Sidebar
        chatHistory={chatHistory}
        currentChatId={currentChatId}
        onNewChat={handleNewChat}
        onSelectChat={handleSelectChat}
        onDeleteChat={handleDeleteChat}
        isOpen={sidebarOpen}
        onClose={() => setSidebarOpen(false)}
      />

      <main className={styles.main}>
        <Header
          title={currentChat?.title || 'ChatBot Assistant'}
          darkMode={darkMode}
          user={user}
          onToggleDarkMode={toggleDarkMode}
          onToggleSidebar={() => setSidebarOpen((prev) => !prev)}
          onLogout={handleLogout}
        />

        <ChatWindow
          messages={messages}
          loading={loading}
          onRegenerate={handleRegenerate}
          onSuggestionClick={handleSendMessage}
        />

        <ChatInput onSend={handleSendMessage} loading={loading} />
      </main>
    </div>
  );
}
