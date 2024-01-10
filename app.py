"""Demo app using SQLAlchemy."""

from flask import Flask, request, url_for, redirect, render_template
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "SECRET!"
debug = DebugToolbarExtension(app)


@app.route("/")
def list_users():
    """List users."""

    users = User.query.all()
    return render_template("lists.html", users=users)

@app.route("/create_user")
def add_user():
    """add user."""

    return render_template("addUser.html")



@app.route("/create_user", methods=["POST"])
def post_user():
    """redirect to list if form submitted."""

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['image_url']

    user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(user)
    db.session.commit()

    """Redirect to the route given."""
    return redirect(f"/{user.id}")

@app.route("/<int:user_id>/edit", methods=["GET", "POST"])
def edit_user(user_id):
    """Edit user profile."""
    user = User.query.get_or_404(user_id)

    if request.method == "POST":
        user.first_name = request.form['first_name']
        user.last_name = request.form['last_name']
        user.image_url = request.form['image_url']
        db.session.commit()
        return redirect(f"/{user.id}")

    return render_template("editUser.html", user=user)

@app.route("/<int:user_id>/delete", methods=["GET","POST"])
def delete_user(user_id):
    """Delete user profile."""
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect("/")

@app.route("/<int:user_id>")
def show_user(user_id):
    """Show info on a single user."""

    user = User.query.get_or_404(user_id)
    return render_template("detail.html", user=user)
