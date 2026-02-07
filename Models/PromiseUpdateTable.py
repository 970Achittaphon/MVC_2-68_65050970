from Models.Database import db
from Models.Promise import Promise
from Models.PromiseUpdate import PromiseUpdate

class PromiseUpdateTable:
    @staticmethod
    def add_update(promise_id, detail):
        promise = Promise.query.get(promise_id)
        
        # Business Rules: ถ้าสถานะ "เงียบหาย" ห้ามอัปเดต
        if promise.status == 'เงียบหาย':
            return False, "คำสัญญานี้ 'เงียบหาย' ไปแล้ว ไม่สามารถอัปเดตความคืบหน้าได้"
            
        try:
            new_update = PromiseUpdate(
                promise_id=promise_id,
                detail=detail
            )
            db.session.add(new_update)
            db.session.commit()
            return True, "อัปเดตความคืบหน้าสำเร็จ"
        except Exception as e:
            db.session.rollback()
            return False, str(e)