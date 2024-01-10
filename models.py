"""Demo file showing off a model for SQLAlchemy."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class User(db.Model):
    """User."""

    __tablename__ = "users"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.String(30), unique=True,
                     nullable=False)
    last_name = db.Column(db.String(30), unique=True, nullable=True)
    image_url = db.Column(db.String(255))

    # """def greet(self):
       # ""Greet using name.""

        # return f"I'm {self.first_name} {self.last_name or 'thing'}" """

    # def feed(self, units=10):
    #   ""Nom nom nom.""

    #    self.hunger -= units
    #   self.hunger = max(self.hunger, 0)"""

    def __repr__(self):
        """Show info about user."""

        u = self
        return f"<User {u.id} {u.first_name} {u.last_name} {u.image_url}>"

    # @classmethod
    # def get_by_species(cls, species):
      # "" Get all pets matching that species.""

       # return cls.query.filter_by(species=species).all()"""
