from Models.Database import db
from datetime import datetime

class PromiseUpdate(db.Model):
    __tablename__ = 'promise_updates'
    
    # รหัสความคืบหน้า
    id = db.Column(db.Integer, primary_key=True)
    # วันที่อัพเดต
    update_date = db.Column(db.DateTime, default=datetime.now)
    # รายละเอียดความคืบหน้า
    detail = db.Column(db.Text, nullable=False)
    
    # Foreign Key: เชื่อมกับคำสัญญา
    promise_id = db.Column(db.Integer, db.ForeignKey('promises.id'), nullable=False)