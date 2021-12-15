from datetime import datetime
from flaskblog import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Private_Info(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), unique=True, nullable=False)
    birthday = db.Column(db.String(100), unique=True, nullable=False)
    gender = db.Column(db.String(100), unique=True, nullable=False)
    race = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"Test('{self.user_id}', '{self.email}', '{self.password}', '{self.birthday}', '{self.gender}', '{self.race}')"

class Bucket_to_Category(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    category_id = db.Column(db.String(100), db.ForeignKey('category.category_id'), nullable=False)

    def __repr__(self):
        return f"Test('{self.post_id}', '{self.user_id}', '{self.category_id}')"


class Category(db.Model):
    category_id = db.Column(db.Integer, primary_key=True)
    category_description = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"Test('{self.category_id}', '{self.category_description}')"

class Location(db.Model): #user location information
    location_id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(100), unique=True, nullable=False)
    state = db.Column(db.String(20), unique=True, nullable=False)
    country = db.Column(db.String(20), unique=True, nullable=False)
    zipcode = db.Column(db.Integer, unique=True, nullable=False)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)


    def __repr__(self):
        return f"Test('{self.location_id}', '{self.city}', '{self.state}', '{self.country}', '{self.zipcode}')"

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    # location = db.relationship('Location', backref="user_location", lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
