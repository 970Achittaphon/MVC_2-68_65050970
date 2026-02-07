from Models.Database import db
from Models.User import User

class UserTable:
    @staticmethod
    def authenticate(username, password):
        """ตรวจสอบการ Login"""
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            return user # ส่ง object user กลับไปเพื่อเอาไปเก็บใน session
        return None

    @staticmethod
    def create_user(username, password, role='USER'):
        if not User.query.filter_by(username=username).first():
            new_user = User(username=username, password=password, role=role)
            db.session.add(new_user)
            db.session.commit()
            return True
        return False