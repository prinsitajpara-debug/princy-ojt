import { useState, useEffect, useCallback } from 'react';
import toast from 'react-hot-toast';
import * as api from '../services/api';

function chatsToMessages(chats) {
  const messages = [];

  for (const chat of chats) {
    const time = new Date(chat.createdAt);
    messages.push({
      id: `${chat.id}-user`,
      chatId: chat.id,
      role: 'user',
      content: chat.question,
      timestamp: time,
    });
    messages.push({
      id: `${chat.id}-assistant`,
      chatId: chat.id,
      role: 'assistant',
      content: chat.answer,
      timestamp: time,
    });
  }

  return messages;
}

function chatsToSidebar(chats) {
  return chats.map((chat) => ({
    id: chat.id,
    title:
      chat.question.slice(0, 40) + (chat.question.length > 40 ? '...' : ''),
    question: chat.question,
    answer: chat.answer,
    createdAt: chat.createdAt,
  }));
}

export function useChat(userId) {
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const [chatHistory, setChatHistory] = useState([]);
  const [darkMode, setDarkMode] = useState(() => {
    const stored = localStorage.getItem('chatbot_dark_mode');
    return stored ? JSON.parse(stored) : false;
  });
  const [currentChatId, setCurrentChatId] = useState(null);
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [historyLoaded, setHistoryLoaded] = useState(false);
  const [isComposingNew, setIsComposingNew] = useState(false);

  useEffect(() => {
    document.documentElement.setAttribute('data-theme', darkMode ? 'dark' : 'light');
    localStorage.setItem('chatbot_dark_mode', JSON.stringify(darkMode));
  }, [darkMode]);

  const loadUserHistory = useCallback(async () => {
    if (!userId) {
      setMessages([]);
      setChatHistory([]);
      setHistoryLoaded(true);
      return;
    }

    setHistoryLoaded(false);

    try {
      const data = await api.getChatHistory();
      const chats = data.chats || [];
      setChatHistory(chatsToSidebar(chats));

      if (!isComposingNew) {
        setMessages(chatsToMessages(chats));
      }
    } catch (error) {
      toast.error(error.message || 'Failed to load chat history');
      setMessages([]);
      setChatHistory([]);
    } finally {
      setHistoryLoaded(true);
    }
  }, [userId, isComposingNew]);

  useEffect(() => {
    loadUserHistory();
  }, [loadUserHistory]);

  const handleNewChat = useCallback(() => {
    setIsComposingNew(true);
    setCurrentChatId(null);
    setMessages([]);
    setSidebarOpen(false);
  }, []);

  const handleSelectChat = useCallback(
    (chatId) => {
      setIsComposingNew(false);
      setCurrentChatId(chatId);
      setSidebarOpen(false);
      loadUserHistory();
    },
    [loadUserHistory]
  );

  const handleDeleteChat = useCallback(
    async (chatId) => {
      try {
        await api.deleteChat(chatId);
        toast.success('Chat deleted');
        setIsComposingNew(false);
        await loadUserHistory();
      } catch (error) {
        toast.error(error.message || 'Failed to delete chat');
      }
    },
    [loadUserHistory]
  );

  const handleSendMessage = useCallback(
    async (content) => {
      const trimmed = content.trim();
      if (!trimmed || loading || !userId) return;

      const userMessage = {
        id: `temp-${Date.now()}`,
        role: 'user',
        content: trimmed,
        timestamp: new Date(),
      };

      setMessages((prev) => [...prev, userMessage]);
      setLoading(true);
      setIsComposingNew(false);

      try {
        const response = await api.sendMessage(trimmed);

        const assistantMessage = {
          id: `temp-${Date.now() + 1}`,
          role: 'assistant',
          content:
            response.reply ||
            response.message ||
            response.content ||
            'No response received.',
          timestamp: new Date(),
        };

        setMessages((prev) => [...prev, assistantMessage]);
        await loadUserHistory();
      } catch (error) {
        toast.error(error.message || 'Failed to send message');
        setMessages((prev) => [
          ...prev,
          {
            id: `error-${Date.now()}`,
            role: 'assistant',
            content:
              error.message?.includes('busy') || error.message?.includes('try again')
                ? `${error.message} Please try again.`
                : `Sorry, something went wrong: ${error.message || 'Please try again.'}`,
            timestamp: new Date(),
            isError: true,
          },
        ]);
      } finally {
        setLoading(false);
      }
    },
    [loading, userId, loadUserHistory]
  );

  const handleRegenerate = useCallback(async () => {
    const lastUserIndex = [...messages].reverse().findIndex((m) => m.role === 'user');
    if (lastUserIndex === -1 || loading) return;

    const actualIndex = messages.length - 1 - lastUserIndex;
    const userMessage = messages[actualIndex];
    const lastChat = chatHistory[chatHistory.length - 1];

    setLoading(true);

    try {
      if (lastChat?.id) {
        await api.deleteChat(lastChat.id);
      }

      setMessages(messages.slice(0, actualIndex));
      await handleSendMessage(userMessage.content);
    } catch (error) {
      toast.error(error.message || 'Failed to regenerate response');
    } finally {
      setLoading(false);
    }
  }, [messages, loading, chatHistory, handleSendMessage]);

  const toggleDarkMode = useCallback(() => {
    setDarkMode((prev) => !prev);
  }, []);

  const currentChat = chatHistory.find((c) => c.id === currentChatId);

  return {
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
    reloadHistory: loadUserHistory,
  };
}
