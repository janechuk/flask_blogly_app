
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()





class User(db.Model):

    """Models for Blogly."""
    __tablename__ = 'user'
    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    first_name = db.Column(db.String(50),
                    nullable=False,
                    unique=False)
    last_name = db.Column(db.String(50),
                    nullable=False,
                    unique=False)
    image_url = db.Column(db.String, nullable=False, default='https://images.unsplash.com/photo-1565945887714-d5139f4eb0ce?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60')


    def __repr__(self):
        """Show info about user"""

        u = self
        return f"<User {u.id} {u.first_name } {u.last_name} {u.image_url}>"

def connect_db(app):
    db.app = app
    db.init_app(app)