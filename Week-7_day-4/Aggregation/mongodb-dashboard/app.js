require("dotenv").config();

const dns = require("dns");
const { MongoClient } = require("mongodb");

dns.setServers(["8.8.8.8", "8.8.4.4"]);

async function run() {
  const client = new MongoClient(process.env.MONGO_URL);

  try {
    await client.connect();

    const db = client.db("analyticsDB");

    const users = db.collection("users");
    const sessions = db.collection("sessions");

    console.log("\n===== TASK 1: TOTAL USERS BY ROLE =====");

    const usersByRole = await users.aggregate([
      {
        $group: {
          _id: "$role",
          totalUsers: { $sum: 1 }
        }
      }
    ]).toArray();

    console.log(usersByRole);



    console.log("\n===== TASK 2: DAILY SIGNUPS =====");

    const signups = await users.aggregate([
      {
        $group: {
          _id: "$signupDate",
          signups: { $sum: 1 }
        }
      },
      {
        $sort: { _id: 1 }
      }
    ]).toArray();

    console.log(signups);



    console.log("\n===== TASK 3: TOP ACTIVE USERS =====");

    const activeUsers = await users.aggregate([
      {
        $lookup: {
          from: "sessions",
          localField: "_id",
          foreignField: "userId",
          as: "sessions"
        }
      },
      {
        $project: {
          name: 1,
          totalSessions: { $size: "$sessions" }
        }
      },
      {
        $sort: {
          totalSessions: -1
        }
      },
      {
        $limit: 10
      }
    ]).toArray();

    console.log(activeUsers);



    console.log("\n===== TASK 4: AVERAGE SESSION DURATION =====");

    const avgDuration = await sessions.aggregate([
      {
        $group: {
          _id: null,
          averageDuration: {
            $avg: "$duration"
          }
        }
      }
    ]).toArray();

    console.log(avgDuration);



    console.log("\n===== TASK 5: FINAL DASHBOARD =====");

    const dashboard = await users.aggregate([
      {
        $lookup: {
          from: "sessions",
          localField: "_id",
          foreignField: "userId",
          as: "sessionData"
        }
      },
      {
        $unwind: "$sessionData"
      },
      {
        $group: {
          _id: {
            userId: "$_id",
            name: "$name",
            role: "$role"
          },
          totalSessions: { $sum: 1 },
          avgDuration: { $avg: "$sessionData.duration" }
        }
      },
      {
        $project: {
          _id: 0,
          userId: "$_id.userId",
          name: "$_id.name",
          role: "$_id.role",
          totalSessions: 1,
          avgDuration: 1
        }
      }
    ]).toArray();

    console.log(dashboard);

  } catch (error) {
    console.log(error);
  } finally {
    await client.close();
  }
}

run();