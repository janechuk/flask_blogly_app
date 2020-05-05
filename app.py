"""Blogly application."""

from flask import Flask, request, redirect, render_template
from models import db, connect_db, User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

#run this line of code on the command line to create the table only once
# db.create_all()

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "SECRET!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route("/")
def home_page():
    """Redirects users to homepage"""
    
    return redirect("/users")


@app.route("/users")
def list_users():
    """List pets and show add form."""

    users = User.query.all()
    return render_template("list.html", users=users)


@app.route("/users/new", methods=["GET"])
def show_form():
    """Renders form to add new user"""
    
    return render_template("form.html")


@app.route("/users/new", methods=["POST"])
def add_user():
    """Add user and redirect to list."""

    first_name = request.form['firstname']
    last_name = request.form['lastname']
    image_url = request.form['imageurl']
    # image_url = imageurl if imageurl else None

    user = User(first_name=first_name , last_name=last_name, image_url=image_url)
    db.session.add(user)
    db.session.commit()

    return redirect(f"/{user.id}")


@app.route("/<int:user_id>")
def show_user(user_id):
    """Show info on a single user."""

    user = User.query.get_or_404(user_id)
    return render_template("detail.html", user=user)


@app.route("/<int:user_id>/edit")
def edit_form_user(user_id):
    """Show Edit form displaying info on an existing user."""
    user = User.query.get_or_404(user_id)

    return render_template("edit.html", user=user)


@app.route("/<int:user_id>/edit", methods=["POST"])
def edit_user(user_id):
    """Edits existing user and redirect to list."""

    user = User.query.get_or_404(user_id)
    user.first_name = request.form['firstname']
    user.last_name = request.form['lastname']
    user.image_url = request.form['imageurl']
    
    db.session.add(user)
    db.session.commit()

    return redirect("/users")

@app.route('/users/<int:user_id>/delete', methods=["POST"])
def users_destroy(user_id):
    """Handle form submission for deleting an existing user"""

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect("/users")