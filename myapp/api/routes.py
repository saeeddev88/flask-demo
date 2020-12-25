from flask import Blueprint, jsonify, request
from ..models import db, User

api = Blueprint("api", __name__, url_prefix="/api")


@api.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    users = [user.serialize for user in users]
    return jsonify(users)


@api.route("/users/<int:id>", methods=["GET"])
def get_user(id):
    user = User.query.get(id)
    if not user:
        return {"error_message": "User doesn't exist ..."}, 404
    return jsonify(user.serialize)


@api.route("/users", methods=["POST"])
def add_user():
    json = request.get_json()
    try:
        user = User(json["name"], json["family"], json["age"])
        db.session.add(user)
        db.session.commit()
        return jsonify(user.serialize), 200
    except Exception as ex:
        return {"error_message": f"{ex}"}


@api.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    user = User.query.get(id)
    if not user:
        return {"error_message": "User doesn't exist ..."}, 404
    db.session.delete(user)
    db.session.commit()
    return '', 204
