from flask import Blueprint, render_template, flash, redirect, url_for
from ..forms import UserForm
from ..models import User, db

admin = Blueprint("admin", __name__, url_prefix="/admin")


@admin.route("/")
def index():
    form = UserForm()
    return render_template("admin/index.html", form=form)


@admin.route("/adduser", methods=["POST"])
def add_user():
    form = UserForm()
    if form.validate_on_submit():
        user = User(form.name.data, form.family.data, form.age.data)
        db.session.add(user)
        db.session.commit()
        flash("User added successfully", "success")
        return redirect(url_for('admin.index'))
