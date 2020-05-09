
from flask_sqlalchemy import SQLAlchemy
import datetime
db = SQLAlchemy()
DEFAULT_IMAGE_URL = 'https://images.unsplash.com/photo-1565945887714-d5139f4eb0ce?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60'





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
    image_url = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)


    def __repr__(self):
        """Show info about user"""

        u = self
        return f"<User {u.id} {u.first_name } {u.last_name} {u.image_url}>"

def connect_db(app):
    db.app = app
    db.init_app(app)




class Post(db.Model):

    """Models for Blogly."""
    __tablename__ = 'post'
    id = db.Column(db.Integer,
                    primary_key=True)
    title = db.Column(db.Text,
                    nullable=False)
    content = db.Column(db.Text,
                    nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                    default=datetime.datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref='post')