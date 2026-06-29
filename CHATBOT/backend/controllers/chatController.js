import { generateReply } from '../services/geminiService.js';
import Chat from '../models/Chat.js';

function buildHistoryFromChats(chats) {
  const history = [];

  for (const chat of chats) {
    history.push({ role: 'user', content: chat.question });
    history.push({ role: 'assistant', content: chat.answer });
  }

  return history;
}

/**
 * POST /api/chat
 * Save question + answer for the authenticated user only.
 */
export async function sendMessage(req, res, next) {
  try {
    const { message } = req.body;
    const userId = req.user._id;

    if (!message || typeof message !== 'string' || !message.trim()) {
      return res.status(400).json({
        success: false,
        message: 'Message is required and must be a non-empty string',
      });
    }

    const trimmedMessage = message.trim();

    const previousChats = await Chat.find({ user: userId }).sort({ createdAt: 1 });
    const history = buildHistoryFromChats(previousChats);
    const reply = await generateReply(trimmedMessage, history);

    const savedChat = await Chat.create({
      user: userId,
      question: trimmedMessage,
      answer: reply,
    });

    res.status(200).json({
      reply,
      chat: {
        id: savedChat._id,
        question: savedChat.question,
        answer: savedChat.answer,
        createdAt: savedChat.createdAt,
      },
    });
  } catch (error) {
    next(error);
  }
}

/**
 * GET /api/chat/history
 * Return only the logged-in user's chats in chronological order.
 */
export async function getChatHistory(req, res, next) {
  try {
    const chats = await Chat.find({ user: req.user._id })
      .sort({ createdAt: 1 })
      .select('question answer createdAt')
      .lean();

    const formatted = chats.map((chat) => ({
      id: chat._id,
      question: chat.question,
      answer: chat.answer,
      createdAt: chat.createdAt,
    }));

    res.status(200).json({ chats: formatted });
  } catch (error) {
    next(error);
  }
}

/**
 * DELETE /api/chat/:chatId
 * Delete a single chat entry belonging to the authenticated user.
 */
export async function deleteChat(req, res, next) {
  try {
    const { chatId } = req.params;

    if (!chatId) {
      return res.status(400).json({
        success: false,
        message: 'Chat ID is required',
      });
    }

    const deleted = await Chat.findOneAndDelete({
      _id: chatId,
      user: req.user._id,
    });

    if (!deleted) {
      return res.status(404).json({
        success: false,
        message: 'Chat not found',
      });
    }

    res.status(200).json({ success: true, message: 'Chat deleted successfully' });
  } catch (error) {
    next(error);
  }
}

/**
 * DELETE /api/chat
 * Clear all chat history for the authenticated user.
 */
export async function clearChatHistory(req, res, next) {
  try {
    await Chat.deleteMany({ user: req.user._id });
    res.status(200).json({ success: true, message: 'Chat history cleared' });
  } catch (error) {
    next(error);
  }
}
