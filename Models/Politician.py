from Models.Database import db

class Politician(db.Model):
    __tablename__ = 'politicians'
    
    # รหัส 8 หลัก (PK)
    id = db.Column(db.Integer, primary_key=True)
    # ชื่อนักการเมือง
    name = db.Column(db.String(100), nullable=False)
    # พรรคการเมือง
    party = db.Column(db.String(100), nullable=False)

    # ความสัมพันธ์: นักการเมือง 1 คน มีได้หลายคำสัญญา
    promises = db.relationship('Promise', backref='politician', lazy=True)