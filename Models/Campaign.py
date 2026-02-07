from Models.Database import db

class Campaign(db.Model):
    __tablename__ = 'campaigns'
    
    # รหัสแคมเปญหาเสียง
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    # ปีการเลือกตั้ง
    year = db.Column(db.Integer, nullable=False) 
    # เขตเลือกตั้ง
    constituency = db.Column(db.String(100), nullable=False) 
    
    # ความสัมพันธ์: แคมเปญหาเสียง 1 แคมเปญ มีได้หลายคำสัญญา
    promises = db.relationship('Promise', backref='campaign', lazy=True)