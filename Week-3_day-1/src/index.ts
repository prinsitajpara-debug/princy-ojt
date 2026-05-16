import {
  getUsers,
  getUserById,
  createUser,
  updateUser,
  deleteUser,
} from "./services/userService";

// GET USERS
console.log("All Users:");
console.log(getUsers());

// GET USER BY ID
console.log("\nSingle User:");
console.log(getUserById(1));

// CREATE USER
const newUser = createUser({
  name: "Drashti",
  email: "drashti@gmail.com",
  age: 28,
});

console.log("\nCreated User:");
console.log(newUser);

// UPDATE USER
const updatedUser = updateUser(1, {
  name: "januu updated",
  age: 18,
});

console.log("\nUpdated User:");
console.log(updatedUser);

// DELETE USER
const isDeleted = deleteUser(2);

console.log("\nDeleted:");
console.log(isDeleted);

// FINAL USERS
console.log("\nFinal Users:");
console.log(getUsers());