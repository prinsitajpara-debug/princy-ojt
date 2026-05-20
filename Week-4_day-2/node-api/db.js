let users = [
  { id: 1, name: "John" },
  { id: 2, name: "Alice" },
];

const getUsers = () => users;

const getUserById = (id) => {
  const user = users.find((u) => u.id === id);
  if (!user) {
    const err = new Error("User not found");
    err.name = "NotFoundError";
    throw err;
  }
  return user;
};

module.exports = { getUsers, getUserById };