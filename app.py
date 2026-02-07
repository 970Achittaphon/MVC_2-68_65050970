import os
from flask import Flask, redirect, url_for
from Models.Database import db

# Import Models ทั้งหมดเพื่อให้ SQLAlchemy รู้จักตารางและความสัมพันธ์
from Models.User import User
from Models.Politician import Politician
from Models.Campaign import Campaign
from Models.Promise import Promise
from Models.PromiseUpdate import PromiseUpdate

# นำเข้า Controllers (Blueprints)
from Controllers.AuthController import auth_controller
from Controllers.PromiseController import promise_controller
from Controllers.PoliticianController import politician_controller

app = Flask(__name__, template_folder='Views/templates')
app.config['SECRET_KEY'] = 'election_2569_key'

# ตั้งค่า Database ให้ถอนออกมาอยู่ที่ Root เสมอ
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'election_2569.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# ลงทะเบียน Blueprints
app.register_blueprint(auth_controller)
app.register_blueprint(promise_controller)
app.register_blueprint(politician_controller)

@app.route('/')
def index():
    return redirect(url_for('promise_controller.all_promises'))

if __name__ == '__main__':
    app.run(debug=True)