from Models.Database import db
from Models.Promise import Promise
from sqlalchemy import desc

class PromiseTable:
    @staticmethod
    def get_all_sorted():
        """โจทย์ 3 ระบุ: แสดงคำสัญญาทั้งหมด เรียงตามวันที่ประกาศ"""
        return Promise.query.order_by(desc(Promise.announced_date)).all()

    @staticmethod
    def find_by_id(promise_id):
        """ใช้สำหรับดึงข้อมูลคำสัญญา 1 ข้อเพื่อแสดงหน้ารายละเอียด (Detail)"""
        return Promise.query.get(promise_id)

    @staticmethod
    def find_by_politician(pol_id):
        """โจทย์ 3 ระบุ: แสดงคำสัญญาทั้งหมดของนักการเมืองแต่ละคน"""
        return Promise.query.filter_by(politician_id=pol_id).all()
    
    @staticmethod
    def update_status(promise_id, new_status):
        promise = Promise.query.get(promise_id)
        if promise:
            promise.status = new_status
            db.session.commit()
            return True
        return False