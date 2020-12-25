from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    family = db.Column(db.String(150), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    @property
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "family": self.family,
            "age": self.age
        }

    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        self.age = age

    def __repr__(self):
        return f"User({self.name},{self.family},{self.age})"