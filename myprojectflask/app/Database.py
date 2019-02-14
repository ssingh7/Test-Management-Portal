from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    password = db.Column(db.String(60,nullable=False))
    
    def __repr__(self):
        return f"User('{self.username}')"
    
class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    testcaseName = db.Column(db.String(120),unique=True,nullable=False)
    status = db.Column(db.String(120),unique=False,nullable=False)
    
    def __repr__(self):
        return f"Post('{self.testcaseName}')"