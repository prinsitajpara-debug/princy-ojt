const request = require("supertest");
const app = require("../src/app");

describe("User API Tests", () => {

  // GET all users
  test("GET /users should return all users", async () => {
    const res = await request(app).get("/users");

    expect(res.statusCode).toBe(200);
    expect(Array.isArray(res.body)).toBe(true);
  });

  // FILTER
  test("GET /users?role=admin returns only admins", async () => {
    const res = await request(app).get("/users?role=admin");

    expect(res.statusCode).toBe(200);
    expect(res.body.every(u => u.role === "admin")).toBe(true);
  });

  // CREATE USER (happy path)
  test("POST /users creates user", async () => {
    const res = await request(app)
      .post("/users")
      .send({
        name: "Ravi",
        email: "ravi@test.com",
        role: "user"
      });

    expect(res.statusCode).toBe(201);
    expect(res.body.email).toBe("ravi@test.com");
  });

  // ERROR 400
  test("POST invalid email returns 400", async () => {
    const res = await request(app)
      .post("/users")
      .send({
        name: "Bad",
        email: "bademail",
        role: "user"
      });

    expect(res.statusCode).toBe(400);
  });

  // DELETE 404
  test("DELETE unknown id returns 404", async () => {
    const res = await request(app).delete("/users/999999");

    expect(res.statusCode).toBe(404);
  });

});