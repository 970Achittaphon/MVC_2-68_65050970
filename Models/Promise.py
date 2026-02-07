from Models.Database import db
from datetime import datetime

class Promise(db.Model):
    __tablename__ = 'promises'
    
    # รหัสคำสัญญา
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # รายละเอียดคำสัญญา
    description = db.Column(db.Text, nullable=False)
    # วันที่ประกาศคำสัญญา
    announced_date = db.Column(db.DateTime, default=datetime.now)
    # สถานะ: ยังไม่เริ่ม, กำลังดำเนินการ, เงียบหาย
    status = db.Column(db.String(50), nullable=False, default='ยังไม่เริ่ม')
    
    # Foreign Keys
    # เชื่อมกับนักการเมือง
    politician_id = db.Column(db.Integer, db.ForeignKey('politicians.id'), nullable=False)
    # เชื่อมกับแคมเปญหาเสียง
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaigns.id'), nullable=True)

    # ความสัมพันธ์: หนึ่งคำสัญญามีหลายความคืบหน้า ตาม Business Rules
    updates = db.relationship('PromiseUpdate', backref='promise', lazy=True)