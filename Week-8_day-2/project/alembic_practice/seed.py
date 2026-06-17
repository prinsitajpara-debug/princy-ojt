from faker import Faker

from database import SessionLocal
from models import User, Role, Post

fake = Faker()


def seed_roles(session):

    if session.query(Role).count() > 0:
        print("Roles already exist")
        return

    roles = [
        Role(name="Admin"),
        Role(name="Editor"),
        Role(name="User")
    ]

    session.add_all(roles)
    session.commit()

    print("Roles inserted")


def seed_users(session):

    if session.query(User).count() > 0:
        print("Users already exist")
        return

    users = []

    for _ in range(10):
        users.append(
            User(
                name=fake.name(),
                email=fake.unique.email()
            )
        )

    session.add_all(users)
    session.commit()

    print("Users inserted")


def seed_posts(session):

    if session.query(Post).count() > 0:
        print("Posts already exist")
        return

    users = session.query(User).all()

    posts = []

    for _ in range(20):
        posts.append(
            Post(
                title=fake.sentence(),
                content=fake.text(),
                user_id=fake.random_element(users).id
            )
        )

    session.add_all(posts)
    session.commit()

    print("Posts inserted")


def main():

    session = SessionLocal()

    seed_roles(session)
    seed_users(session)
    seed_posts(session)

    session.close()

    print("Database seeded successfully")


if __name__ == "__main__":
    main()