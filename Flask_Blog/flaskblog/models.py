from datetime import datetime
from flaskblog import db,login_manager
from flask_login import UserMixin
import sqlite3

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    job_name = db.Column(db.String(30), nullable=False)
    job_status = db.Column(db.Text, nullable=False)
    release_name=db.Column(db.Text,nullable=False)
    username = db.Column(db.Text,nullable=False)

    def __repr__(self):
        return f"Result('{self.job_name}', '{self.job_status}','{self.release_name}','{self.username}')"

class DetailResult(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    date_posted = db.Column(db.DateTime,nullable=False,default= datetime.utcnow)
    test_case_name = db.Column(db.Text,nullable=False)
    test_case_id = db.Column(db.Integer,nullable=False)
    screenshot_path=db.Column(db.Text)
    test_status = db.Column(db.Text,nullable=False)

    def __repr__(self):
        return f"Result('{self.test_case_name}', '{self.test_case_id}','{self.screenshot_path}','{self.test_status}')"


# command to get table details : cursor.execute("PRAGMA table_info(tablename)")