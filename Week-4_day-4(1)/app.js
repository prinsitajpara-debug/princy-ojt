const express = require("express");
const swaggerJsDoc = require("swagger-jsdoc");
const swaggerUi = require("swagger-ui-express");
const fs = require("fs");
const path = require("path");

const userRoutes = require("./routes/user.routes");

const app = express();
app.use(express.json());

/*  ROOT ROUTE (FIX)  */
app.get("/", (req, res) => {
  res.send("User CRUD API is running");
});

/*  Swagger Configuration  */
const swaggerOptions = {
  definition: {
    openapi: "3.0.0",
    info: {
      title: "User CRUD API",
      version: "1.0.0",
      description: "Simple User CRUD API with Swagger Documentation",
    },
    servers: [
      {
        url: "http://localhost:3000",
      },
    ],

    /* Schemas */
    components: {
      schemas: {
        User: {
          type: "object",
          properties: {
            id: { type: "integer", example: 1 },
            name: { type: "string", example: "Princy" },
            email: { type: "string", example: "princy@gmail.com" },
          },
        },

        CreateUserInput: {
          type: "object",
          required: ["name", "email"],
          properties: {
            name: { type: "string", example: "John" },
            email: { type: "string", example: "john@gmail.com" },
          },
        },

        UpdateUserInput: {
          type: "object",
          properties: {
            name: { type: "string", example: "John Updated" },
            email: { type: "string", example: "johnupdated@gmail.com" },
          },
        },

        ErrorResponse: {
          type: "object",
          properties: {
            error: { type: "string", example: "User not found" },
          },
        },

        PaginatedResponse: {
          type: "object",
          properties: {
            page: { type: "integer", example: 1 },
            limit: { type: "integer", example: 10 },
            total: { type: "integer", example: 50 },
            data: {
              type: "array",
              items: {
                $ref: "#/components/schemas/User",
              },
            },
          },
        },
      },
    },
  },

  apis: ["./routes/*.js"],
};

const swaggerDocs = swaggerJsDoc(swaggerOptions);

/*  Ensure docs folder exists  */
const docsDir = path.join(__dirname, "docs");

if (!fs.existsSync(docsDir)) {
  fs.mkdirSync(docsDir);
}

/*  Save Swagger JSON  */
const swaggerFilePath = path.join(docsDir, "swagger.json");

fs.writeFileSync(
  swaggerFilePath,
  JSON.stringify(swaggerDocs, null, 2),
  "utf-8"
);

console.log("Swagger JSON saved at /docs/swagger.json");

/*  Swagger UI  */
app.use(
  "/api-docs",
  swaggerUi.serve,
  swaggerUi.setup(swaggerDocs)
);

/* Swagger JSON Endpoint  */
app.get("/swagger.json", (req, res) => {
  res.setHeader("Content-Type", "application/json");
  res.json(swaggerDocs);
});

/*  Routes  */
app.use("/users", userRoutes);

/* Server Start */
const PORT = 3000;

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
  console.log(`Swagger UI: http://localhost:${PORT}/api-docs`);
  console.log(`Swagger JSON: http://localhost:${PORT}/swagger.json`);
});