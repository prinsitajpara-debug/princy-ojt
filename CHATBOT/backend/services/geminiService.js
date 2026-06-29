import { GoogleGenAI } from '@google/genai';

const MODELS = ['gemini-2.0-flash', 'gemini-1.5-flash', 'gemini-2.5-flash'];
const MAX_RETRIES = 3;
const MAX_HISTORY = 20;

const SYSTEM_INSTRUCTION = `You are a helpful, knowledgeable AI assistant.
Answer every question clearly, accurately, and completely.
If the user asks for more information or follow-up details, expand on your previous answer.
Use markdown formatting when helpful (headings, bullet points, code blocks).
Never refuse reasonable questions.`;

let aiClient = null;

function getClient() {
  if (!process.env.GEMINI_API_KEY) {
    throw new Error('GEMINI_API_KEY is not configured in environment variables');
  }

  if (!aiClient) {
    aiClient = new GoogleGenAI({
      apiKey: process.env.GEMINI_API_KEY,
    });
  }

  return aiClient;
}

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function parseErrorMessage(error) {
  try {
    const parsed = JSON.parse(error.message);
    return parsed?.error?.message || error.message;
  } catch {
    return error.message || 'Unknown AI error';
  }
}

function isRetryableError(error) {
  const message = (error.message || '').toLowerCase();
  const status = error.status || error.code;

  return (
    status === 429 ||
    status === 503 ||
    message.includes('429') ||
    message.includes('503') ||
    message.includes('high demand') ||
    message.includes('resource_exhausted') ||
    message.includes('unavailable') ||
    message.includes('rate limit')
  );
}

function buildContents(history, userMessage) {
  const contents = [];
  const recentHistory = history.slice(-MAX_HISTORY);

  for (const msg of recentHistory) {
    if (!msg.content || msg.isError) continue;

    contents.push({
      role: msg.role === 'assistant' ? 'model' : 'user',
      parts: [{ text: msg.content }],
    });
  }

  contents.push({
    role: 'user',
    parts: [{ text: userMessage }],
  });

  return contents;
}

/**
 * Send message with conversation history, retries, and model fallback.
 */
export async function generateReply(userMessage, history = []) {
  const ai = getClient();
  const contents = buildContents(history, userMessage);
  let lastError = null;

  for (const model of MODELS) {
    for (let attempt = 0; attempt < MAX_RETRIES; attempt++) {
      try {
        const response = await ai.models.generateContent({
          model,
          contents,
          config: {
            systemInstruction: SYSTEM_INSTRUCTION,
            temperature: 0.7,
            maxOutputTokens: 2048,
          },
        });

        const text = response.text?.trim();

        if (text) {
          if (model !== MODELS[0]) {
            console.log(`[Gemini] Used fallback model: ${model}`);
          }
          return text;
        }

        throw new Error('Gemini returned an empty response');
      } catch (error) {
        lastError = error;
        const message = parseErrorMessage(error);
        console.warn(
          `[Gemini] ${model} attempt ${attempt + 1} failed: ${message}`
        );

        if (isRetryableError(error) && attempt < MAX_RETRIES - 1) {
          await sleep(1500 * (attempt + 1));
          continue;
        }

        break;
      }
    }
  }

  const finalMessage = parseErrorMessage(lastError);
  throw new Error(
    finalMessage.includes('high demand') || finalMessage.includes('UNAVAILABLE')
      ? 'AI is busy right now. Please wait a few seconds and try again.'
      : finalMessage || 'Failed to get AI response. Please try again.'
  );
}
