const express = require("express");
const userRoutes = require("./routes/user.routes");
const errorMiddleware = require("./error.middleware");

const app = express();

app.use(express.json());

app.use("/users", userRoutes);

app.use(errorMiddleware);

module.exports = app;