import Chat from '../models/Chat.js';

const LEGACY_CHAT_INDEXES = ['userId_1_chatId_1', 'userId_1', 'chatId_1'];

/**
 * Remove indexes from an older chat schema and align with the current model.
 */
export async function syncChatIndexes() {
  const collection = Chat.collection;

  try {
    const existing = await collection.indexes();

    for (const index of existing) {
      if (LEGACY_CHAT_INDEXES.includes(index.name)) {
        await collection.dropIndex(index.name);
        console.log(`Dropped legacy chat index: ${index.name}`);
      }
    }
  } catch (error) {
    console.warn(`Legacy chat index cleanup skipped: ${error.message}`);
  }

  await Chat.syncIndexes();
  console.log('Chat indexes synced');
}
