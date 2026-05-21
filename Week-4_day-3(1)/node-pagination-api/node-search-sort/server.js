const http = require("http");

const users = require("./db");

const server = http.createServer((req, res) => {

  if (req.method === "GET" && req.url.startsWith("/users")) {

    const url = new URL(req.url, "http://localhost:3000");

    const search = url.searchParams.get("search");

    let result = [...users];

    if (search) {

      const value = search.toLowerCase();

      result = result.filter((user) => {
        return (
          user.name.toLowerCase().includes(value) ||
          user.email.toLowerCase().includes(value)
        );
      });
    }

    res.writeHead(200, {
      "Content-Type": "application/json"
    });

    res.end(JSON.stringify(result));
  }
});

server.listen(3000, () => {
  console.log("Server running on port 3000");
});