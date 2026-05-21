const http = require("http");
const url = require("url");
const { users } = require("./db");

const server = http.createServer((req, res) => {
  if (req.method === "GET" && req.url.startsWith("/users")) {
    
    // 1. Parse URL + Query Params
    const parsedUrl = url.parse(req.url, true);
    const query = parsedUrl.query;

    let page = parseInt(query.page) || 1;
    let limit = parseInt(query.limit) || 2;
    let role = query.role;

    // 2. Start with all users
    let filteredUsers = [...users];

    // 3. FILTERING (role filter)
    if (role) {
      filteredUsers = filteredUsers.filter(
        (user) => user.role === role
      );
    }

    // 4. TOTAL COUNT (after filtering)
    const total = filteredUsers.length;

    // 5. PAGINATION LOGIC
    const startIndex = (page - 1) * limit;
    const endIndex = startIndex + limit;

    const paginatedData = filteredUsers.slice(startIndex, endIndex);

    // 6. RESPONSE FORMAT (production style)
    const response = {
      data: paginatedData,
      total: total,
      page: page,
      limit: limit,
    };

    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify(response));
  }
});

server.listen(3000, () => {
  console.log("Server running on port 3000");
});