import{User,CreateUserInput,UpdateUserInput} from '../types/user';

let users: User[] = [
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
export function getUsers():User[]{
    return users;
}

//get singel use
export function getUserById(id: number): User | undefined {
  return users.find((user) => user.id === id);
}

//add new user
export function createUser(data: CreateUserInput): User {
  const newUser: User = {
    id: users.length + 1,
    ...data,
  };

  users.push(newUser);

  return newUser;
}

// UPDATE USER
export function updateUser(
  id: number,
  data: UpdateUserInput
): User | null {
  const user = users.find((u) => u.id === id);

  if (!user) {
    return null;
  }

  Object.assign(user, data);

  return user;
}

// DELETE USER
export function deleteUser(id: number): boolean {
  const initialLength = users.length;

  users = users.filter((user) => user.id !== id);

  return users.length < initialLength;
}
