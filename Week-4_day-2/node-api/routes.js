const { getUsers, getUserById } = require("./db");

const getAllUsers = async (req, res) => {
  const users = getUsers();

  res.writeHead(200, {
    "Content-Type": "application/json",
  });

  res.end(JSON.stringify(users));
};

const getSingleUser = async (req, res) => {
  const id = Number(req.url.split("/")[2]);

  if (!id) {
    const err = new Error("Invalid ID");
    err.name = "ValidationError";
    throw err;
  }

  const user = getUserById(id);

  res.writeHead(200, {
    "Content-Type": "application/json",
  });

  res.end(JSON.stringify(user));
};

module.exports = {
  getAllUsers,
  getSingleUser,
};