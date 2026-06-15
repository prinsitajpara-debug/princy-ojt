# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship

# from app.database import Base


# class Role(Base):
#     __tablename__ = "roles"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, unique=True)

#     users = relationship("User", back_populates="role")


# class User(Base):
#     __tablename__ = "userss"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     email = Column(String, unique=True, index=True)
#     password_hash = Column(String)

#     role_id = Column(Integer, ForeignKey("roles.id"))

#     role = relationship("Role", back_populates="userss")



from sqlalchemy import Column, Integer, String
from app.database import Base


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True)
    name = Column(String)


class User(Base):
    __tablename__ = "userss"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password_hash = Column(String)
    role_id = Column(Integer)