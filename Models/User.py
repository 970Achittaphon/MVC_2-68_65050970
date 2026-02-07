from Models.Database import db

class User(db.Model):
    __tablename__ = 'users'
    
    # id ผู้ใช้
    id = db.Column(db.Integer, primary_key=True)
    # username
    username = db.Column(db.String(50), unique=True, nullable=False)
    # password
    password = db.Column(db.String(100), nullable=False)
    
    # 'ADMIN' หรือ 'USER'
    role = db.Column(db.String(20), nullable=False) 