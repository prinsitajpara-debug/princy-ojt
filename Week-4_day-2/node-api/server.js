const http = require("http");
const errorHandler = require("./errorHandler");
const asyncWrapper = require("./utils/asyncWrapper");
const {
  getAllUsers,
  getSingleUser,
} = require("./routes");

const server = http.createServer(async (req, res) => {
  try {
    // GET /users
    if (req.method === "GET" && req.url === "/users") {
      return await asyncWrapper(getAllUsers)(req, res);
    }

    // GET /users/:id
    if (req.method === "GET" && req.url.startsWith("/users/")) {
      return await asyncWrapper(getSingleUser)(req, res);
    }

    // 404 fallback
    res.writeHead(404, {
      "Content-Type": "application/json",
    });

    res.end(
      JSON.stringify({
        error: "Route not found",
        code: "NOT_FOUND",
      })
    );
  } catch (err) {
    //  CENTRAL ERROR HANDLER
    errorHandler(err, res);
  }
});

server.listen(3000, () => {
  console.log("🚀 Server running on port 3000");
});