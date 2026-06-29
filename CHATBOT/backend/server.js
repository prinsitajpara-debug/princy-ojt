import 'dotenv/config';
import express from 'express';
import cors from 'cors';
import { connectDB } from './config/db.js';
import { syncChatIndexes } from './utils/syncIndexes.js';
import chatRoutes from './routes/chatRoutes.js';
import authRoutes from './routes/authRoutes.js';
import { errorMiddleware, notFoundMiddleware } from './middleware/errorMiddleware.js';

const app = express();
const PORT = process.env.PORT || 5000;

const requiredEnv = ['GEMINI_API_KEY', 'JWT_SECRET'];
const missing = requiredEnv.filter((key) => !process.env[key]);
if (missing.length > 0) {
  console.error(`Missing required environment variables: ${missing.join(', ')}`);
  process.exit(1);
}

await connectDB();
await syncChatIndexes();

app.use(cors());
app.use(express.json());

app.get('/health', (req, res) => {
  res.status(200).json({ status: 'ok', message: 'Chatbot API is running' });
});

app.use('/api/auth', authRoutes);
app.use('/api/chat', chatRoutes);

app.use(notFoundMiddleware);
app.use(errorMiddleware);

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
  console.log(`Auth API: http://localhost:${PORT}/api/auth`);
  console.log(`Chat API: http://localhost:${PORT}/api/chat`);
});
