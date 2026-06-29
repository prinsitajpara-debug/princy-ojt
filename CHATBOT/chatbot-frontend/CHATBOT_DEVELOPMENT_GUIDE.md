# Chatbot Frontend — Prompt & Step-by-Step Development Guide

This document contains:
1. The **original prompt** used to generate the chatbot frontend
2. A **step-by-step explanation** of how the project was built and how API integration works

---

## Table of Contents

- [Part A: Original Prompt](#part-a-original-prompt)
- [Part B: Development Order](#part-b-development-order-what-was-built-first)
- [Part C: Project Setup](#part-c-step-1--project-setup)
- [Part D: Global Styles](#part-d-step-2--global-styles-first-globalcss)
- [Part E: API Layer](#part-e-step-3--api-layer-apijs--line-by-line)
- [Part F: useChat Hook](#part-f-step-4--the-brain-usechatjs)
- [Part G: UI Components](#part-g-step-5--ui-components-smallest--largest)
- [Part H: App.jsx](#part-h-step-6--appjsx-glue-everything)
- [Part I: Entry Point](#part-i-step-7--entry-point-mainjsx)
- [Part J: User Journey](#part-j-complete-user-journey-one-message)
- [Part K: Architecture](#part-k-architecture-summary)
- [Part L: Build Checklist](#part-l-how-to-build-this-yourself-checklist)
- [Part M: Backend API](#part-m-backend-api-requirements)

---

# Part A: Original Prompt

> Copy of the full prompt used to create this chatbot frontend.

---

# Cursor Prompt for Complete Chatbot Frontend

Create a modern, production-ready chatbot frontend using React + Vite.

## Requirements

### Layout

The application should have:

1. Left Sidebar
2. Main Chat Area
3. Header/Navbar
4. Chat Input Section

---

## Sidebar Features

* Fixed sidebar on the left.
* Display application logo and name.
* "New Chat" button.
* List of previous chats.
* Ability to select a previous chat.
* Delete chat option.
* Responsive collapse on mobile devices.

---

## Header Features

* Display chatbot title.
* Dark/Light mode toggle.
* User profile icon.

---

## Chat Window Features

* Display chat messages in a scrollable area.
* User messages aligned right.
* Bot messages aligned left.
* Message timestamps.
* Auto-scroll to the latest message.
* Different styling for user and bot messages.

---

## Chat Input Features

* Multiline textarea.
* Send button.
* Press Enter to send.
* Shift + Enter for a new line.
* Disable input while loading.

---

## State Management

Use React hooks.

Maintain:

```javascript
const [messages, setMessages] = useState([]);
const [loading, setLoading] = useState(false);
const [chatHistory, setChatHistory] = useState([]);
const [darkMode, setDarkMode] = useState(false);
```

Message object format:

```javascript
{
  id: Date.now(),
  role: "user" | "assistant",
  content: "",
  timestamp: new Date()
}
```

---

## Folder Structure

```text
src/
├── components/
│   ├── Sidebar.jsx
│   ├── Header.jsx
│   ├── ChatWindow.jsx
│   ├── ChatMessage.jsx
│   ├── ChatInput.jsx
│   └── Loader.jsx
│
├── services/
│   └── api.js
│
├── hooks/
│   └── useChat.js
│
├── styles/
│   └── global.css
│
├── App.jsx
└── main.jsx
```

---

## Styling Requirements

* Use CSS Modules or Tailwind CSS.
* Modern UI similar to ChatGPT.
* Rounded message bubbles.
* Smooth hover effects.
* Fully responsive design.
* Dark and Light theme support.
* Beautiful loading animations.

---

## API Integration

Create `services/api.js` with Axios.

Implement:

```javascript
sendMessage(message)
getChatHistory()
deleteChat(chatId)
```

Use placeholder API endpoint:

```javascript
http://localhost:5000/api/chat
```

Include proper error handling.

---

## Additional Features

* Typing indicator.
* Copy response button.
* Regenerate response button.
* Loading spinner.
* Empty state screen.
* Toast notifications for errors.
* Markdown support for bot responses.
* Code syntax highlighting.

---

## NPM Packages

Install and configure:

```bash
axios
react-icons
react-markdown
react-syntax-highlighter
react-hot-toast
```

---

Generate all React components, CSS files, folder structure, and provide complete code for each file.
Use best coding practices and clean component architecture.
Generate production-quality code.

---

# Part B: Development Order (What Was Built First)

A **bottom-up** approach was used: foundation first, then logic, then UI, then connect everything.

```text
1. Install packages
       ↓
2. global.css (theme variables)
       ↓
3. api.js (HTTP layer)
       ↓
4. useChat.js (brain / state)
       ↓
5. Small UI pieces (Loader, ChatMessage)
       ↓
6. Bigger UI (Sidebar, Header, ChatInput)
       ↓
7. ChatWindow (combines messages)
       ↓
8. App.jsx (wires everything)
       ↓
9. main.jsx (entry point)
```

### Why this order?

| Layer | File | Purpose |
|-------|------|---------|
| Foundation | `global.css` | Colors, fonts, dark/light theme variables |
| Data layer | `api.js` | Talks to backend — no React here |
| Logic layer | `useChat.js` | All state + business rules |
| UI layer | Components | Only display data and call functions |
| Glue | `App.jsx` | Connects hook → components |

**Rule:** UI components should **not** call Axios directly. They call functions from `useChat`, which calls `api.js`.

---

# Part C: Step 1 — Project Setup

The project uses Vite + React. Required packages were installed:

```bash
npm install axios react-icons react-markdown react-syntax-highlighter react-hot-toast
```

| Package | Role |
|---------|------|
| `axios` | HTTP requests to backend |
| `react-icons` | Icons (send, menu, moon, etc.) |
| `react-markdown` | Render bot replies as Markdown |
| `react-syntax-highlighter` | Highlight code blocks |
| `react-hot-toast` | Error/success popups |

Folder structure created:

```text
src/components/   → UI pieces
src/services/     → API calls
src/hooks/        → State logic
src/styles/       → Global CSS
```

---

# Part D: Step 2 — Global Styles First (`global.css`)

Before any component, **CSS variables** were defined for theming:

```css
[data-theme='light'] {
  --bg-primary: #ffffff;
  --text-primary: #0d0d0d;
  --accent: #10a37f;
  /* ... */
}

[data-theme='dark'] {
  --bg-primary: #212121;
  --text-primary: #ececec;
  /* ... */
}
```

When `darkMode` is `true`, JavaScript sets `data-theme="dark"` on `<html>`. All components use `var(--bg-primary)` etc., so the whole app switches theme without rewriting every component.

---

# Part E: Step 3 — API Layer (`api.js`) — Line by Line

This file is **pure JavaScript** — no React. It only handles HTTP.

### Lines 1–11: Create Axios instance

```javascript
import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000/api/chat';

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 30000,
  headers: {
    'Content-Type': 'application/json',
  },
});
```

| Line | What it does |
|------|--------------|
| 1 | Import Axios library |
| 3 | Set base URL — all requests start here |
| 5–11 | Create one Axios instance with shared config (URL, 30s timeout, JSON header) |

### Lines 13–23: Error interceptor

```javascript
api.interceptors.response.use(
  (response) => response,
  (error) => {
    const message =
      error.response?.data?.message ||
      error.response?.data?.error ||
      error.message ||
      'An unexpected error occurred';
    return Promise.reject(new Error(message));
  }
);
```

| Part | What it does |
|------|--------------|
| Success handler | Pass response through unchanged |
| Error handler | Extract message from server or network error |
| `Promise.reject` | Throw clean `Error` so UI can show it in a toast |

### Lines 25–31: `sendMessage()`

```javascript
export async function sendMessage(message, chatId = null) {
  const { data } = await api.post('/', {
    message,
    chatId,
  });
  return data;
}
```

- **HTTP:** `POST http://localhost:5000/api/chat/`
- **Body:** `{ message: "Hello", chatId: "chat_123" }`
- **Returns:** Server JSON, e.g. `{ reply: "Hi there!" }`

### Lines 33–36: `getChatHistory()`

```javascript
export async function getChatHistory() {
  const { data } = await api.get('/history');
  return data;
}
```

- **HTTP:** `GET http://localhost:5000/api/chat/history`
- **Returns:** e.g. `{ chats: [...] }`

### Lines 38–41: `deleteChat()`

```javascript
export async function deleteChat(chatId) {
  const { data } = await api.delete(`/${chatId}`);
  return data;
}
```

- **HTTP:** `DELETE http://localhost:5000/api/chat/chat_123`

---

# Part F: Step 4 — The Brain (`useChat.js`)

This custom hook holds **all state** and **all actions**.

### F.1 — State variables

```javascript
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
```

| State | Meaning |
|-------|---------|
| `messages` | Messages in the **current** chat |
| `loading` | Waiting for API reply |
| `chatHistory` | List of all chats (sidebar) |
| `darkMode` | Light/dark theme |
| `currentChatId` | Which chat is open |
| `sidebarOpen` | Mobile sidebar open/closed |
| `historyLoaded` | Finished loading history on startup |

### F.2 — Load history on app start

```javascript
useEffect(() => {
  async function fetchHistory() {
    try {
      const data = await api.getChatHistory();
      const chats = data.chats || data || [];
      if (chats.length > 0) {
        setChatHistory(chats);
        setCurrentChatId(chats[0].id);
        setMessages(chats[0].messages || []);
      } else {
        // fallback to localStorage
      }
    } catch {
      // fallback to localStorage if API fails
    } finally {
      setHistoryLoaded(true);
    }
  }
  fetchHistory();
}, []);
```

**Flow:**
1. App mounts → `useEffect` runs once (`[]` dependency).
2. Try `getChatHistory()` from API.
3. If success → use server chats.
4. If fail or empty → use `localStorage`.
5. Set `historyLoaded = true` so `App.jsx` can show the main UI.

### F.3 — Send message (full API integration)

**Sequence when user sends a message:**

```text
User types "Hello" + Enter
    → ChatInput calls onSend("Hello")
    → useChat.handleSendMessage("Hello")
    → User message added to UI immediately (optimistic UI)
    → setLoading(true)
    → api.sendMessage("Hello", chatId)
    → POST http://localhost:5000/api/chat
    → Backend returns { reply: "Hi!" }
    → Assistant message added to messages
    → Saved to chatHistory + localStorage
    → setLoading(false)
    → ChatWindow re-renders
```

**Step-by-step in code:**

```javascript
// Step 1: Validate
const trimmed = content.trim();
if (!trimmed || loading) return;

// Step 2: Ensure a chat exists
const chatId = ensureCurrentChat();

// Step 3: Build user message object
const userMessage = {
  id: Date.now(),
  role: 'user',
  content: trimmed,
  timestamp: new Date(),
};

// Step 4: Show user message immediately
const updatedMessages = [...messages, userMessage];
setMessages(updatedMessages);
setLoading(true);

// Step 5: Call API
try {
  const response = await api.sendMessage(trimmed, chatId);

  const assistantMessage = {
    id: Date.now() + 1,
    role: 'assistant',
    content: response.reply || response.message || response.content,
    timestamp: new Date(),
  };

  setMessages([...updatedMessages, assistantMessage]);
  updateChatInHistory(chatId, ...);
} catch (error) {
  toast.error(error.message);
  // Show error bubble in chat
} finally {
  setLoading(false);
}
```

### F.4 — Other handlers

| Handler | What it does |
|---------|--------------|
| `handleNewChat` | Creates empty chat, clears messages |
| `handleSelectChat` | Loads messages from selected chat |
| `handleDeleteChat` | Calls API delete + removes from local state |
| `handleRegenerate` | Re-sends last user message to API |
| `toggleDarkMode` | Flips theme + saves to localStorage |

---

# Part G: Step 5 — UI Components (Smallest → Largest)

### G.1 — `Loader.jsx`
Simple spinner + typing dots. Used while loading.

### G.2 — `ChatMessage.jsx`
- Receives one `message` object.
- User → plain text, right-aligned.
- Bot → `react-markdown` + syntax highlighter, left-aligned.
- Copy and Regenerate buttons on bot messages.

### G.3 — `ChatInput.jsx`

```javascript
const handleSubmit = () => {
  if (!input.trim() || loading) return;
  onSend(input);      // → handleSendMessage from useChat
  setInput('');
};

const handleKeyDown = (e) => {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault();
    handleSubmit();   // Enter = send
  }
  // Shift + Enter = new line (default textarea behavior)
};
```

- `onSend` comes from `App` → `handleSendMessage` from `useChat`.
- `disabled={loading}` while waiting for API.

### G.4 — `ChatWindow.jsx`

```javascript
{messages.map((message, index) => (
  <ChatMessage
    key={message.id}
    message={message}
    isLast={index === lastAssistantIndex}
    onRegenerate={onRegenerate}
    loading={loading}
  />
))}
```

- Maps `messages` array → one `ChatMessage` per item.
- Auto-scroll via `bottomRef.scrollIntoView()` when `messages` or `loading` changes.
- Shows empty state when no messages.

### G.5 — `Sidebar.jsx` & `Header.jsx`

- **Sidebar:** shows `chatHistory`, select/delete chat, New Chat button.
- **Header:** title, dark mode toggle, mobile menu button.

Both only receive **props** and call **callbacks** — no API calls inside.

---

# Part H: Step 6 — `App.jsx` (Glue Everything)

```javascript
function App() {
  const {
    messages,
    loading,
    chatHistory,
    handleSendMessage,
    handleNewChat,
    // ... all from useChat()
  } = useChat();

  return (
    <div className={styles.app}>
      <Sidebar chatHistory={chatHistory} onNewChat={handleNewChat} ... />
      <main>
        <Header title={currentChat?.title} darkMode={darkMode} ... />
        <ChatWindow messages={messages} loading={loading} ... />
        <ChatInput onSend={handleSendMessage} loading={loading} />
      </main>
    </div>
  );
}
```

**Data flow pattern:**

```text
useChat (state + functions)
    ↓ props down
Components (display + user events)
    ↑ callbacks up
useChat (updates state, calls API)
```

---

# Part I: Step 7 — Entry Point (`main.jsx`)

```javascript
import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import './styles/global.css';
import App from './App.jsx';

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>
);
```

1. Load global CSS.
2. Mount `App` into `#root` in `index.html`.
3. React takes over from here.

---

# Part J: Complete User Journey (One Message)

| Step | What happens | Where |
|------|----------------|-------|
| 1 | User types "Hello" and presses Enter | `ChatInput` |
| 2 | `handleSubmit()` → `onSend("Hello")` | `ChatInput` |
| 3 | `handleSendMessage("Hello")` runs | `useChat` |
| 4 | User bubble appears instantly | `setMessages` |
| 5 | `setLoading(true)` | Input disabled, typing dots show |
| 6 | `api.post('/', { message, chatId })` | `api.js` → backend |
| 7 | Backend returns `{ reply: "Hi!" }` | Port 5000 |
| 8 | Assistant bubble added | `setMessages` again |
| 9 | Saved to `chatHistory` + localStorage | `updateChatInHistory` |
| 10 | `setLoading(false)` | UI ready for next message |
| 11 | `ChatWindow` re-renders with new messages | React |

---

# Part K: Architecture Summary

```text
┌─────────────────────────────────────────────────────────┐
│  main.jsx                                                │
│    └── App.jsx                                           │
│          ├── useChat()  ← BRAIN (state + API logic)      │
│          ├── Sidebar    ← props: chatHistory, callbacks  │
│          ├── Header       ← props: title, darkMode         │
│          ├── ChatWindow   ← props: messages, loading     │
│          └── ChatInput    ← props: onSend, loading       │
│                                                          │
│  useChat.js                                              │
│    └── api.js  ← HTTP only (axios)                       │
│          └── http://localhost:5000/api/chat              │
└─────────────────────────────────────────────────────────┘
```

### File map

```text
src/
├── main.jsx              → Entry point
├── App.jsx               → Layout + wire components
├── App.module.css        → App layout styles
├── hooks/
│   └── useChat.js        → All state & logic
├── services/
│   └── api.js            → Axios HTTP calls
├── styles/
│   └── global.css        → Theme variables + reset
└── components/
    ├── Sidebar.jsx       → Chat list
    ├── Header.jsx        → Top bar
    ├── ChatWindow.jsx    → Message list
    ├── ChatMessage.jsx   → Single message bubble
    ├── ChatInput.jsx     → Text input + send
    └── Loader.jsx        → Spinner + typing indicator
```

---

# Part L: How to Build This Yourself (Checklist)

1. **Create Vite React app** → `npm create vite@latest`
2. **Install packages** → `axios`, `react-icons`, `react-markdown`, `react-syntax-highlighter`, `react-hot-toast`
3. **Write `api.js`** → one function per endpoint
4. **Write `useChat.js`** → state + call `api.js`
5. **Write small components** → Loader, ChatMessage
6. **Write layout components** → Sidebar, Header, ChatInput, ChatWindow
7. **Write `App.jsx`** → `useChat()` + pass props to components
8. **Style with CSS Modules** → one `.module.css` per component + `global.css`
9. **Test** → `npm run dev`, connect backend on port 5000

### Run commands

```bash
cd chatbot-frontend
npm install
npm run dev      # development
npm run build    # production build
```

---

# Part M: Backend API Requirements

For the frontend to work fully, your backend should expose:

| Method | Endpoint | Request Body | Response |
|--------|----------|--------------|----------|
| `POST` | `/api/chat` | `{ message, chatId }` | `{ reply: "..." }` |
| `GET` | `/api/chat/history` | — | `{ chats: [{ id, title, messages }] }` |
| `DELETE` | `/api/chat/:chatId` | — | success |

### Message object format

```javascript
{
  id: 1719234567890,
  role: "user" | "assistant",
  content: "Hello!",
  timestamp: "2024-06-24T12:00:00.000Z"
}
```

### Chat object format

```javascript
{
  id: "chat_1719234567890",
  title: "Hello!",
  messages: [ /* message objects */ ],
  createdAt: "2024-06-24T12:00:00.000Z",
  updatedAt: "2024-06-24T12:05:00.000Z"
}
```

### Fallback behavior

Until the backend exists:
- Chat history is stored in **localStorage** (`chatbot_history` key)
- Sending a message shows an **error toast** if the server is unreachable
- The app still works offline for viewing saved chats

---

*Generated for the CHATBOAT project — chatbot-frontend*
