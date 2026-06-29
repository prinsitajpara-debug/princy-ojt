# Chatbot Backend API

Full-stack AI Chatbot backend with Node.js, Express, MongoDB, JWT Authentication, and Google Gemini API.

## Tech Stack

- Node.js + Express.js
- MongoDB + Mongoose
- JWT Authentication + bcryptjs
- Google AI Studio (Gemini 2.5 Flash)

## Setup

### 1. Install dependencies

```bash
npm install
```

### 2. Configure environment

Copy `.env.example` to `.env` and fill in values:

```env
PORT=5000
MONGODB_URI=mongodb://127.0.0.1:27017/chatbot
JWT_SECRET=your_super_secret_jwt_key
JWT_EXPIRES_IN=7d
GEMINI_API_KEY=your_google_ai_studio_api_key
```

### 3. Start MongoDB

Make sure MongoDB is running locally, or use MongoDB Atlas connection string in `MONGODB_URI`.

### 4. Run server

```bash
npm run dev
```

## API Endpoints

### Authentication

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| POST | `/api/auth/register` | No | Register new user |
| POST | `/api/auth/login` | No | Login and get JWT |
| GET | `/api/auth/profile` | Yes | Get logged-in user |

### Chat (Protected — requires JWT)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/chat` | Send message to Gemini |
| GET | `/api/chat/history` | Get user's chats |
| DELETE | `/api/chat/:chatId` | Delete a chat |

### Headers for protected routes

```http
Authorization: Bearer <your_jwt_token>
```

## Security

- Passwords hashed with bcrypt (12 rounds)
- JWT tokens expire in 7 days (configurable)
- Chat routes protected by auth middleware
- Secrets stored in `.env` only
