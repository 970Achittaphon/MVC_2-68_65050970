from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from Models.PromiseTable import PromiseTable
from Models.PromiseUpdateTable import PromiseUpdateTable
from Models.PoliticianTable import PoliticianTable
from Models.Database import db 

promise_controller = Blueprint('promise_controller', __name__)

# 3.1 หน้ารวมคำสัญญาทั้งหมด
@promise_controller.route('/promises')
def all_promises():
    # เรียงตามวันที่ประกาศจาก PromiseTable
    promises = PromiseTable.get_all_sorted()
    return render_template('all_promises.html', promises=promises)

# 3.2 หน้ารายละเอียดคำสัญญา
@promise_controller.route('/promise/<int:promise_id>')
def promise_detail(promise_id):
    promise = PromiseTable.find_by_id(promise_id)
    if not promise:
        flash("ไม่พบคำสัญญาที่ระบุ", "danger")
        return redirect(url_for('promise_controller.all_promises'))
    return render_template('promise_detail.html', promise=promise)

# 3.3 หน้าอัปเดตความคืบหน้า (GET: แสดงฟอร์ม, POST: บันทึกข้อมูล)
@promise_controller.route('/promise/<int:promise_id>/update', methods=['GET', 'POST'])
def update_promise(promise_id):
    # เช็คสิทธิ์ Admin ตามโจทย์ข้อ 6
    if session.get('role') != 'ADMIN':
        flash("เฉพาะผู้ดูแลระบบเท่านั้นที่สามารถอัปเดตข้อมูลได้", "warning")
        return redirect(url_for('promise_controller.promise_detail', promise_id=promise_id))

    promise = PromiseTable.find_by_id(promise_id)
    if not promise:
        return redirect(url_for('promise_controller.all_promises'))

    if request.method == 'POST':
        detail = request.form.get('detail')
        new_status = request.form.get('new_status') # รับค่าสถานะใหม่จาก Select
        
        # 1. บันทึกรายละเอียดลงใน PromiseUpdateTable (Business Rule ข้อ 4)
        success, message = PromiseUpdateTable.add_update(promise_id, detail)
        
        if success:
            # 2. อัปเดตสถานะของคำสัญญาในตาราง Promise
            # เรียกใช้ update_status ที่ได้เขียนไว้ใน PromiseTable
            PromiseTable.update_status(promise_id, new_status)
            
            flash("บันทึกความคืบหน้าและอัปเดตสถานะเรียบร้อยแล้ว", "success")
            # เมื่ออัปเดตเสร็จ ต้องกลับไปหน้ารายละเอียดคำสัญญา (Business Rule ข้อ 4)
            return redirect(url_for('promise_controller.promise_detail', promise_id=promise_id))
        else:
            flash(message, "danger")
            return render_template('update_promise.html', promise=promise)

    return render_template('update_promise.html', promise=promise)