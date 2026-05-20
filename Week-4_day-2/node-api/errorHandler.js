const errorHandler = (err, res) => {
  console.error("Error Log:", err.message);

  let statusCode = 500;
  let code = "INTERNAL_ERROR";

  // Custom error types
  if (err.name === "ValidationError") {
    statusCode = 422;
    code = "VALIDATION_ERROR";
  }

  if (err.name === "NotFoundError") {
    statusCode = 404;
    code = "NOT_FOUND";
  }

  res.writeHead(statusCode, {
    "Content-Type": "application/json",
  });

  res.end(
    JSON.stringify({
      error: err.message || "Something went wrong",
      code,
    })
  );
};

module.exports = errorHandler;