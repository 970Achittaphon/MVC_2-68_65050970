from Models.Database import db
from Models.Politician import Politician

class PoliticianTable:
    @staticmethod
    def validate_id(pol_id):
        """ตรวจสอบรหัส 8 หลัก และตัวแรกไม่เป็น 0"""
        s_id = str(pol_id)
        if len(s_id) == 8 and s_id[0] != '0' and s_id.isdigit():
            return True
        return False

    @staticmethod
    def add_politician(pol_id, name, party):
        # 1. เช็คความถูกต้องของ Format
        if not PoliticianTable.validate_id(pol_id):
            return False, "รหัสนักการเมืองต้องเป็นตัวเลข 8 หลัก และตัวแรกห้ามเป็น 0"
        
        # 2. เช็คว่า ID ซ้ำหรือไม่
        if Politician.query.get(pol_id):
            return False, "รหัสนักการเมืองนี้มีอยู่ในระบบแล้ว"
            
        try:
            new_pol = Politician(id=int(pol_id), name=name, party=party)
            db.session.add(new_pol)
            db.session.commit()
            return True, "ลงทะเบียนนักการเมืองสำเร็จ"
        except Exception as e:
            db.session.rollback()
            return False, str(e)

    @staticmethod
    def find_all():
        return Politician.query.all()

    # ค้นหานักการเมืองตาม ID
    @staticmethod
    def find_by_id(pol_id):
        """ค้นหานักการเมืองตาม ID สำหรับหน้า Profile"""
        return Politician.query.get(pol_id)