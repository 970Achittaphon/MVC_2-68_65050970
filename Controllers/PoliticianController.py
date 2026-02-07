from flask import Blueprint, render_template, url_for
from Models.PoliticianTable import PoliticianTable
from Models.PromiseTable import PromiseTable

politician_controller = Blueprint('politician_controller', __name__)

# 3.4 หน้านักการเมือง (รวมคำสัญญาของคนนั้นๆ)
@politician_controller.route('/politician/<int:pol_id>')
def politician_profile(pol_id):
    politician = PoliticianTable.find_by_id(pol_id)
    if not politician:
        return "ไม่พบข้อมูลนักการเมือง", 404
    
    # ดึงคำสัญญาเฉพาะของนักการเมืองคนนี้
    promises = PromiseTable.find_by_politician(pol_id)
    return render_template('politician_info.html', politician=politician, promises=promises)

@politician_controller.route('/politicians')
def all_politicians():
    # ดึงรายชื่อนักการเมืองทั้งหมดจาก Table
    politicians = PoliticianTable.find_all()
    return render_template('all_politicians.html', politicians=politicians)