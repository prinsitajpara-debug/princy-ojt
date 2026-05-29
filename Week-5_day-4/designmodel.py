from dataclasses import dataclass
from typing import List

#  COMMENT (DATACLASS) 
@dataclass
class Comment:
    message: str
    author: str


# USER 
class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.posts: List["Post"] = []
        self.is_banned = False

    # username property 
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not value or len(value) < 3:
            raise ValueError("Username must be at least 3 characters")
        self._username = value

    #  password property (encapsulation) 
    @property
    def password(self):
        return "******"  

    @password.setter
    def password(self, value):
        if len(value) < 4:
            raise ValueError("Password too weak")
        self._password = value  
    #  features 
    def create_post(self, content: str):
        if self.is_banned:
            print(f"{self.username} is banned and cannot create posts.")
            return None

        post = Post(author=self.username, content=content)
        self.posts.append(post)
        return post

    def edit_profile(self, new_username: str):
        self.username = new_username


#  ADMIN USER 
class AdminUser(User):
    def delete_comment(self, post: "Post", comment: Comment):
        if comment in post.comments:
            post.comments.remove(comment)
            print(f"Admin deleted comment: {comment.message}")

    def ban_user(self, user: User):
        user.is_banned = True
        print(f"User {user.username} has been banned")


#  POST 
class Post:
    def __init__(self, author: str, content: str):
        self.author = author
        self.content = content
        self.comments: List[Comment] = []
        self.likes = 0

    def add_comment(self, comment: Comment):
        self.comments.append(comment)

    def add_like(self):
        self.likes += 1

    def like_count(self):
        return self.likes

    def show(self):
        print("\n--- POST ---")
        print(f"Author: {self.author}")
        print(f"Content: {self.content}")
        print(f"Likes: {self.likes}")
        print("Comments:")
        for c in self.comments:
            print(f"- {c.author}: {c.message}")

if __name__ == "__main__":

  
    u1 = User("prinsi", "pass123")
    u2 = User("bob", "mypwd")

    admin = AdminUser("admin", "admin123")

    post1 = u1.create_post("Hello world from Prinsi!")

 
    post1.add_like()
    post1.add_like()

    c1 = Comment("Nice post!", "bob")
    c2 = Comment("Thanks!", "prinsi")

    post1.add_comment(c1)
    post1.add_comment(c2)

   
    admin.delete_comment(post1, c1)

    admin.ban_user(u2)
    post1.show()
    u2.create_post("I should not be allowed")