const express = require("express");
const morgan = require("morgan");
const cors = require("cors");
const helmet = require("helmet");

const userRoutes = require("./routes/user.routes");
const errorHandler = require("./middleware/error.middleware");

const app = express();

/* MIDDLEWARE */
app.use(express.json());

app.use(morgan("dev"));

app.use(cors());

app.use(helmet());

/* ROOT ROUTE */
app.get("/", (req, res) => {
  res.send("Express User CRUD API Running");
});

/* ROUTES */
app.use("/api/users", userRoutes);

/* ERROR ROUTE TEST */
app.get("/error", (req, res) => {
  throw new Error("Test error");
});

/* ERROR HANDLER */
app.use(errorHandler);

/* SERVER */
const PORT = 5000;

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});