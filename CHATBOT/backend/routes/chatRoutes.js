import { Router } from 'express';
import {
  sendMessage,
  getChatHistory,
  deleteChat,
  clearChatHistory,
} from '../controllers/chatController.js';
import { protect } from '../middleware/authMiddleware.js';

const router = Router();

router.use(protect);

router.post('/', sendMessage);
router.get('/history', getChatHistory);
router.delete('/all', clearChatHistory);
router.delete('/:chatId', deleteChat);

export default router;
