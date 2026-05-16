"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const userService_1 = require("./services/userService");
// GET USERS
console.log("All Users:");
console.log((0, userService_1.getUsers)());
// GET USER BY ID
console.log("\nSingle User:");
console.log((0, userService_1.getUserById)(1));
// CREATE USER
const newUser = (0, userService_1.createUser)({
    name: "Drashti",
    email: "drashti@gmail.com",
    age: 28,
});
console.log("\nCreated User:");
console.log(newUser);
// UPDATE USER
const updatedUser = (0, userService_1.updateUser)(1, {
    name: "januu updated",
    age: 18,
});
console.log("\nUpdated User:");
console.log(updatedUser);
// DELETE USER
const isDeleted = (0, userService_1.deleteUser)(2);
console.log("\nDeleted:");
console.log(isDeleted);
// FINAL USERS
console.log("\nFinal Users:");
console.log((0, userService_1.getUsers)());
