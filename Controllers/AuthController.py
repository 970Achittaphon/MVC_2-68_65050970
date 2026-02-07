from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from Models.UserTable import UserTable

auth_controller = Blueprint('auth_controller', __name__)

@auth_controller.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = UserTable.authenticate(username, password)
        if user:
            session['user_id'] = user.id
            session['username'] = user.username
            session['role'] = user.role  # เก็บ 'ADMIN' หรือ 'USER'
            flash(f"ยินดีต้อนรับคุณ {user.username}", "success")
            return redirect(url_for('promise_controller.all_promises'))
        else:
            flash("ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง", "danger")
            
    return render_template('login.html')

@auth_controller.route('/logout')
def logout():
    session.clear()
    flash("ออกจากระบบเรียบร้อยแล้ว", "info")
    return redirect(url_for('auth_controller.login'))