import random
from datetime import datetime
from app import app  
from Models.Database import db
from Models.User import User
from Models.Politician import Politician
from Models.Campaign import Campaign
from Models.Promise import Promise
from Models.PromiseUpdate import PromiseUpdate

def seed_data():
    with app.app_context():
        print("--- กำลังสร้างฐานข้อมูลใหม่... ---")
        db.drop_all()
        db.create_all()

        # 1. สร้างผู้ใช้งาน
        admin = User(username='admin', password='123', role='ADMIN')
        user = User(username='user', password='123', role='USER')
        db.session.add_all([admin, user])

        # 2. สร้างนักการเมือง 7 คน
        pols = [
            Politician(id=16900001, name='นายรังสิมันต์ โรมมิ่ง', party='พรรคก้าวใหม่'),
            Politician(id=26900002, name='ดร.เศรษฐา ทวีโชค', party='พรรคไทยก้าวหน้า'),
            Politician(id=36900003, name='เสี่ยหนู อนันต์', party='พรรคภูมิใจไทยแลนด์'),
            Politician(id=46900004, name='พลเอกประยุทธ์ จูเนียร์', party='พรรครวมไทยใจหนึ่ง'),
            Politician(id=56900005, name='นายชัชชาติ สิทธิพลัง', party='พรรคกรุงเทพแข็งแกร่ง'),
            Politician(id=66900006, name='มาดามแป้ง ใจดี', party='พรรคกีฬาเพื่อราษฎร์'),
            Politician(id=76900007, name='ลุงป้อม ใจบันดาลแรง', party='พรรคพลังแห่งรัฐ')
        ]
        db.session.add_all(pols)
        db.session.commit()

        # 3. สร้างเขตเลือกตั้ง
        campaigns = [
            Campaign(year=2569, constituency='กรุงเทพฯ เขต 1'),
            Campaign(year=2569, constituency='เชียงใหม่ เขต 1'),
            Campaign(year=2569, constituency='ขอนแก่น เขต 3'),
            Campaign(year=2569, constituency='ชลบุรี เขต 2')
        ]
        db.session.add_all(campaigns)
        db.session.commit()

        # รายการคำสัญญา (15 ข้อ)
        promises_list = [
            ('รถไฟฟ้า 20 บาทตลอดสาย', pols[1].id, 'กำลังดำเนินการ', campaigns[0].id),
            ('ปฏิรูปกองทัพสมัครใจ', pols[0].id, 'กำลังดำเนินการ', campaigns[0].id),
            ('สวนสาธารณะ 15 นาที', pols[4].id, 'กำลังดำเนินการ', campaigns[0].id),
            ('กัญชาเพื่อการแพทย์เสรี', pols[2].id, 'กำลังดำเนินการ', campaigns[1].id),
            ('ยกระดับบอลไทยไปบอลโลก', pols[5].id, 'กำลังดำเนินการ', campaigns[2].id),
            ('รถเมล์ไฟฟ้า EV ทั่วกรุง', pols[4].id, 'ยังไม่เริ่ม', campaigns[0].id),
            ('สวัสดิการเด็ก 6,000 บาท', pols[0].id, 'ยังไม่เริ่ม', campaigns[1].id),
            ('สร้างนิคมดิจิทัลขอนแก่น', pols[2].id, 'ยังไม่เริ่ม', campaigns[2].id),
            ('ประกันราคายางพารา', pols[3].id, 'ยังไม่เริ่ม', campaigns[3].id),
            ('เรียนฟรีปริญญาตรี', pols[4].id, 'ยังไม่เริ่ม', campaigns[0].id),
            ('แจกเงินดิจิทัลรอบ 3', pols[1].id, 'เงียบหาย', campaigns[0].id),
            ('หอชมเมืองสูงที่สุด', pols[3].id, 'เงียบหาย', campaigns[1].id),
            ('น้ำมันเบนซิน 25 บาท', pols[6].id, 'เงียบหาย', campaigns[2].id),
            ('ธนาคารน้ำใต้ดินหมู่บ้าน', pols[2].id, 'เงียบหาย', campaigns[2].id),
            ('แจก Tablet นักเรียนทุกคน', pols[5].id, 'เงียบหาย', campaigns[3].id)
        ]

        # 4. สร้างและใส่วันที่ตามเงื่อนไข
        for i, (desc_text, p_id, stat, c_id) in enumerate(promises_list):
            # กำหนดปีและเดือนตามลำดับ
            if i < 3:
                # 3 รายการแรก เป็นปี 2568 (ค.ศ. 2025)
                year = 2025 
                month = random.randint(1, 12)
            else:
                # 12 รายการที่เหลือ เป็นปี 2569 (ค.ศ. 2026)
                year = 2026
                # สุ่มเดือน 1 หรือ 2 เพื่อไม่ให้เกินวันปัจจุบัน (ก.พ. 2026)
                month = random.randint(1, 2) if year == 2026 else random.randint(1, 12)
            
            # สุ่มวัน (1-28 เพื่อเลี่ยงปัญหาจำนวนวันในแต่ละเดือนไม่เท่ากัน)
            day = random.randint(1, 28)
            
            # ป้องกันวันที่ในอนาคต (เนื่องจากวันนี้คือ 7 ก.พ. 2026)
            current_now = datetime.now()
            target_date = datetime(year, month, day)
            if target_date > current_now:
                target_date = current_now
            
            p = Promise(
                description=desc_text,
                politician_id=p_id,
                status=stat,
                campaign_id=c_id,
                announced_date=target_date
            )
            db.session.add(p)

        db.session.commit()
        print("--- Seed Data สำเร็จ: 2568 (3 ข้อ) และ 2569 (12 ข้อ) ---")

if __name__ == '__main__':
    seed_data()