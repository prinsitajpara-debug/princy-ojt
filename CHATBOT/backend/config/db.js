import dns from 'node:dns';
import mongoose from 'mongoose';

// Fix Node.js DNS issues on Windows that cause querySrv ECONNREFUSED
dns.setDefaultResultOrder('ipv4first');

export async function connectDB() {
  const srvUri = process.env.MONGODB_URI;
  const standardUri = process.env.MONGODB_URI_STANDARD;

  if (!srvUri && !standardUri) {
    console.error('MONGODB_URI or MONGODB_URI_STANDARD is required in backend/.env');
    process.exit(1);
  }

  const urisToTry = [standardUri, srvUri].filter(Boolean);

  for (const uri of urisToTry) {
    try {
      await mongoose.connect(uri, {
        serverSelectionTimeoutMS: 10000,
        family: 4,
      });
      console.log(`MongoDB connected: ${mongoose.connection.host}`);
      console.log(`Database: ${mongoose.connection.name}`);
      return;
    } catch (error) {
      const label = uri.startsWith('mongodb+srv') ? 'SRV' : 'Standard';
      console.warn(`${label} connection failed: ${error.message}`);
    }
  }

  console.error('\nAll MongoDB connection attempts failed.');
  console.error('Troubleshooting:');
  console.error('1. Atlas → Network Access → Allow 0.0.0.0/0');
  console.error('2. Verify username/password in backend/.env');
  console.error('3. Use MONGODB_URI_STANDARD (non-SRV) in backend/.env');
  process.exit(1);
}
