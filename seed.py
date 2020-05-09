"""Seed file for blogly app"""
from models import User,Post, db
from app import app



#creat all tables
db.drop_all()
db.create_all()

u1 = User(first_name="Zara", last_name="Beautiful", image_url="https://images.unsplash.com/photo-1535930891776-0c2dfb7fda1a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60")
u2 = User(first_name="Kody", last_name="Cute", image_url="https://images.unsplash.com/photo-1561984142-7fabd0b4c9b4?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60")
u3 = User(first_name="Kayle", last_name="Simpson", image_url="https://images.unsplash.com/flagged/photo-1583958211970-af3e1596ef32?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60")
u4 = User(first_name="Jayson", last_name="Dermaco", image_url="https://images.unsplash.com/photo-1566489564594-f2163930c034?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60")


p1 = Post(title="Treat Day", content="Lorem ipsum dolor sit amet consectetur adipisicing elit. Est pariatur quae sint eos architecto dolore enim quas", user_id=1)
p2 = Post(title="Great Buzz", content="Est pariatur quae sint eos architecto dolore enim quas. Non magni voluptatum, labore commodi dolor quidem, necessitatibus illo dolore sint laboriosam ea!", user_id=2)
p3 = Post(title="Won the lottery", content="Lorem ipsum dolor sit amet consectetur adipisicing elit. Est pariatur quae sint eos architecto dolore enim quas.", user_id=3)
p4 = Post(title="Snooze n Loose", content="Est pariatur quae sint eos architecto dolore enim quas. Non magni voluptatum, labore commodi dolor quidem, necessitatibus illo dolore sint laboriosam ea!", user_id=4)

db.session.add_all([u1, u2, u3, u4])
db.session.commit()



# db.session.add_all([p1, p2, p3, p4])
# db.session.commit()


