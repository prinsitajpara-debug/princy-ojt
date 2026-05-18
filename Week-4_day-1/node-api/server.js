const http = require("http");
const fs = require("fs");
const path = require("path");

// Create server
const server = http.createServer((req, res) => {
  // Check method and route
  if (req.method === "GET" && req.url === "/users") {
    
    // Build path to JSON file
    const filePath = path.join(__dirname, "users.json");

    // Read file asynchronously (non-blocking)
    fs.readFile(filePath, "utf-8", (err, data) => {
      if (err) {
        res.writeHead(500, { "Content-Type": "application/json" });
        return res.end(JSON.stringify({ error: "Failed to read file" }));
      }

      // Send response
      res.writeHead(200, { "Content-Type": "application/json" });
      res.end(data);
    });

  } else {
    // Handle other routes
    res.writeHead(404, { "Content-Type": "application/json" });
    res.end(JSON.stringify({ error: "Route not found" }));
  }
});

// Start server
const PORT = 3000;

server.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});