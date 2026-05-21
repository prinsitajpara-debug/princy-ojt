const { users } = require("../db");

// GET /users?role=admin
exports.getUsers = (req, res) => {
  let result = users;

  if (req.query.role) {
    result = result.filter(u => u.role === req.query.role);
  }

  res.status(200).json(result);
};

// POST /users
exports.createUser = (req, res, next) => {
  try {
    const { name, email, role } = req.body;

    if (!email.includes("@")) {
      const err = new Error("Invalid email");
      err.status = 400;
      throw err;
    }

    const newUser = {
      id: Date.now(),
      name,
      email,
      role
    };

    users.push(newUser);

    res.status(201).json(newUser);
  } catch (err) {
    next(err);
  }
};

// DELETE /users/:id
exports.deleteUser = (req, res, next) => {
  try {
    const id = Number(req.params.id);

    const index = users.findIndex(u => u.id === id);

    if (index === -1) {
      const err = new Error("User not found");
      err.status = 404;
      throw err;
    }

    users.splice(index, 1);

    res.status(204).send();
  } catch (err) {
    next(err);
  }
};