"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.getUsers = getUsers;
exports.getUserById = getUserById;
exports.createUser = createUser;
exports.updateUser = updateUser;
exports.deleteUser = deleteUser;
let users = [
    {
        id: 1,
        name: "prinsi",
        email: "prinsi@gmail.com",
        age: 21,
    },
    {
        id: 2,
        name: "jiya",
        email: "jiya@gmail.com",
        age: 17,
    },
];
//get all users
function getUsers() {
    return users;
}
//get singel use
function getUserById(id) {
    return users.find((user) => user.id === id);
}
//add new user
function createUser(data) {
    const newUser = {
        id: users.length + 1,
        ...data,
    };
    users.push(newUser);
    return newUser;
}
// UPDATE USER
function updateUser(id, data) {
    const user = users.find((u) => u.id === id);
    if (!user) {
        return null;
    }
    Object.assign(user, data);
    return user;
}
// DELETE USER
function deleteUser(id) {
    const initialLength = users.length;
    users = users.filter((user) => user.id !== id);
    return users.length < initialLength;
}
