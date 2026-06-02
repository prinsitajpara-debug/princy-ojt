# from src.oop_module import User, AdminUser, Post, Comment


# def test_user_creation():
#     user = User("john")
#     assert user.username == "john"


# def test_create_post():
#     user = User("john")
#     post = user.create_post("hello")
#     assert post.content == "hello"


# def test_post_author():
#     user = User("john")
#     post = user.create_post("test")
#     assert post.author == "john"


# def test_add_like():
#     post = Post("hi", "john")
#     post.add_like()
#     assert post.likes == 1


# def test_add_comment():
#     post = Post("hi", "john")
#     comment = Comment("nice", "alice")
#     post.add_comment(comment)
#     assert len(post.comments) == 1


# def test_admin_ban_user():
#     admin = AdminUser("admin")
#     user = User("john")
#     assert "banned" in admin.ban_user(user)

from src.oop_module import User, AdminUser, Post, Comment


def test_user_creation():
    user = User("john")
    print("User created:", user.username)
    assert user.username == "john"


def test_create_post():
    user = User("john")
    post = user.create_post("hello")
    print("Post created with content:", post.content)
    assert post.content == "hello"


def test_post_author():
    user = User("john")
    post = user.create_post("test")
    print("Post author:", post.author)
    assert post.author == "john"


def test_add_like():
    post = Post("hi", "john")
    post.add_like()
    print("Likes after like:", post.likes)
    assert post.likes == 1


def test_add_comment():
    post = Post("hi", "john")
    comment = Comment("nice", "alice")
    post.add_comment(comment)
    print("Total comments:", len(post.comments))
    assert len(post.comments) == 1


def test_admin_ban_user():
    admin = AdminUser("admin")
    user = User("john")
    result = admin.ban_user(user)
    print("Ban result:", result)
    assert "banned" in result