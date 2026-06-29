/**
 * Global error handling middleware.
 * Catches all errors passed via next(error) and returns a JSON response.
 */
export function errorMiddleware(err, req, res, next) {
  console.error(`[Error] ${err.message}`);

  const statusCode = err.statusCode || 500;

  res.status(statusCode).json({
    success: false,
    message: err.message || 'Internal Server Error',
  });
}

/**
 * Handle requests to undefined routes.
 */
export function notFoundMiddleware(req, res) {
  res.status(404).json({
    success: false,
    message: `Route not found: ${req.method} ${req.originalUrl}`,
  });
}
