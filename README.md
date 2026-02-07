# MVC_2-68_65050970

##ข้อ 1
###a.ไฟล์ใดทําหน้าที่อะไรใน MVC และทํางานร่วมกันอย่างไร

####Models (M)
1.Class Model ได้แก่ Campaign.py, Politicaian.py, Promise.py, PromiseUpdate.py, User.py ทำหน้าที่เป็นโครงสร้างข้อมูล ทำหน้าที่บอกว่าข้อมูลเป็นอย่างไร ความสัมพันธ์เป็นอย่างไร
2.Class Table ได้แก่ CampaignTable.py, PoliticaianTable.py, PromiseTable.py, PromiseUpdateTable.py, UserTable.py ทำหน้าที่เป็นส่วน Logic ของตารางข้อมูลนั้นๆ เช่น การดึงข้อมูล การคัดกรองข้อมูล หรือตรวจสอบตาม Business Rule ก่อนจะบันทึก
1.PoliticianTable.py: ค้นหานักการเมืองและตรวจสอบรหัส 8 หลัก (ห้ามขึ้นต้นด้วย 0)
2.PromiseTable.py: จัดการดึงข้อมูลคำสัญญา (เช่น เรียงตามวันที่) และอัปเดตสถานะ
3.PromiseUpdateTable.py: ตรวจสอบ Business Rule ว่าหากสถานะคำสัญญาคือ "เงียบหาย" จะไม่อนุญาตให้เพิ่มความคืบหน้า
4.UserTable.py: จัดการการพิสูจน์ตัวตน (Authenticate)
5.CampaignTable.py: จัดการเพิ่มหรือดึงข้อมูล Campaign

####Views (V)
ตาม Requirement
1.all_promises.html: ทำหน้าที่แสดงคำสัญญาทั้งหมด เรียงตามวันที่ประกาศ (ใหม่ ไป เก่า)
2.promise_detail.html: ทำหน้าที่แสดงรายละเอียดคำสัญญา ประวัติการอัปเดต และมีปุ่มให้อัปเดตความคืบหน้า
3.update_promise.html: สำหรับ admin ทำหน้าที่เพิ่มความคืบหน้าของคำสัญญา โดยจะต้องใส่รายละเอียดความคืบหน้า และ สามารถเปลี่ยนสถานะของคำสัญญาได้
4.politician_info.html: ทำหน้าที่แสดงคำสัญญาทั้งหมดของนักการเมืองเฉพาะของคนๆนั้น
เพิ่มเติม
5.layout_html: ทำหน้าที่เป็นโครงสร้างหลักของหน้าเว็บ (Navbar, Sidebar, Flash Messages) ที่ทุกหน้าใช้ร่วมกัน และเป็นทางไปสู่ views อื่นๆ 
6.login_html: ทำหน้าที่เป็นหน้า login ยืนยันตัวตน (Authentication) ตามข้อ 6 เพื่อแยกระหว่าง user กับ admin โดยใช้ username, password
7.all_politicians.html: ทำหน้าที่เป็นหน้ารวมของนักการเมืองทุกคนในระบบ ที่สามารถกดเข้าไปดูการรายละเอียดของคำสัญญาได้

####Controllers (C)
1.AuthController.py: ควบคุมการเข้าสู่ระบบ (Login) และออกจากระบบ (Logout) พร้อมเก็บข้อมูลลงใน Session
2.PoliticianController.py: ควบคุมการแสดงรายชื่อนักการเมืองทุกคน และหน้าโปรไฟล์ของนักการเมืองแต่ละท่าน
3.PromiseController.py: ควบคุมหน้าจอเกี่ยวกับคำสัญญา เช่น การแสดงรายการทั้งหมด, การดูรายละเอียด และการตรวจสอบสิทธิ์ Admin ก่อนยอมให้เข้าหน้าอัปเดต

####การทำงานร่วมกัน
1. เมื่อผู้ใช้ส่งคำขอ (Request) ผ่านหน้าจอ (View):
-ผู้ใช้เริ่มปฏิสัมพันธ์กับระบบผ่านไฟล์ View เช่น คลิกดูรายละเอียดคำสัญญาในหน้า all_promises.html หรือกรอกข้อมูลในหน้า update_promise.html
-Controller (เช่น PromiseController) จะรับ Request นั้นมาประมวลผล
2. การประสานงานระหว่าง Controller และ Model:
-Controller จะเรียกใช้งาน Class Table (เช่น PromiseTable หรือ PromiseUpdateTable) เพื่อจัดการข้อมูล
-Class Table จะนำ Business Rule มาตรวจสอบ (เช่น ตรวจว่ารหัส 8 หลักหรือไม่ หรือสถานะเป็น "เงียบหาย" หรือไม่) โดยอ้างอิงโครงสร้างและความสัมพันธ์ของข้อมูลจาก Class Model (เช่น Promise, Politician)
-หลังจากประมวลผลเสร็จ Model จะส่งข้อมูล (Data Object) กลับมาให้ Controller
3. การส่งข้อมูลกลับไปแสดงผล (Response):
-Controller จะเลือกไฟล์ View ที่เหมาะสมและส่งข้อมูลที่ได้จาก Model ไปให้
-ไฟล์ View (เช่น promise_detail.html) จะรับข้อมูลมา Render และใช้ Logic ของ Jinja2 ในการแสดงผล เช่น การเปลี่ยนสี Badge ตามสถานะที่ได้รับมา
-หากเป็นการทำงานที่ต้องเปลี่ยนหน้า เช่น หลังจากอัปเดตความคืบหน้าสำเร็จ Controller จะใช้คำสั่ง redirect เพื่อพาผู้ใช้กลับไปที่ View อื่นตามเงื่อนไข (เช่น กลับไปหน้ารายละเอียดคำสัญญาตาม Business Rule ข้อ 4)
4. การควบคุมสิทธิ์ (Security Workflow):
-AuthController จะทำงานร่วมกับ UserTable เพื่อตรวจสอบตัวตนและเก็บสถานะ 'ADMIN' หรือ 'USER' ไว้ใน Session
-ในการทำงานที่สำคัญ เช่น การเข้าหน้า update_promise.html ตัว PromiseController จะตรวจสอบค่าใน Session ก่อน หากไม่ใช่ Admin ระบบจะไม่อนุญาตให้เข้าถึงหน้าจอนั้นและส่งข้อความเตือน (Flash Message) กลับไปที่ View แทน

###b.สรุป Routes/Actions หลัก และหน้าจอ View สําคัญ
####1.หน้ารวมคำสัญญาทั้งหมด
	-Views: ไฟล์ all_promises.html
	-Controllers: PromiseController.all_promises
	-Models: PromiseTable และ Promise
	การทำงาน: Controller จะรับ Request จากผู้ใช้แล้วเรียกใช้ฟังก์ชัน PromiseTable.get_all_sorted() ซึ่งฟังก์ชันนี้จะไป Query ข้อมูลจาก Model Promise โดยสั่งเรียงลำดับตามวันที่ประกาศจากใหม่ไปเก่า (desc(Promise.announced_date)) จากนั้น Controller จะส่งข้อมูลชุดนี้ไปให้ View all_promises.html เพื่อวนลูปแสดงผลคำสัญญาทั้งหมดในรูปแบบรายการ

####2.หน้ารายละเอียดคำสัญญา:
	-Views: ไฟล์ promise_detail.html
	-Controllers: PromiseController.promise_detail
	-Models: PromiseTable, Promise, และ PromiseUpdate
	การทำงาน: Controller รับ promise_id มาแล้วเรียกใช้ PromiseTable.find_by_id(promise_id) เพื่อดึงข้อมูลคำสัญญาหนึ่งข้อพร้อมกับประวัติความคืบหน้า (updates) ที่เชื่อมโยงกันอยู่จากตาราง PromiseUpdate จากนั้นส่งข้อมูลไปให้ View แสดงรายละเอียด โดยใน View นี้จะมีการตรวจสอบ Business Rule ว่าถ้าสถานะเป็น "เงียบหาย" จะทำการปิดการใช้งานปุ่มอัปเดตทันที

####3.หน้าอัปเดตความคืบหน้า:
	-Views: ไฟล์ update_promise.html
	-Controllers: PromiseController.update_promise
	-Models: PromiseUpdateTable, PromiseTable, และ PromiseUpdate
	การทำงาน: * GET: Controller ตรวจสอบสิทธิ์ ADMIN จาก Session หากผ่านจะดึงข้อมูลสัญญาจาก PromiseTable มาแสดงในฟอร์ม update_promise.html
		-POST: Controller รับรายละเอียดและสถานะใหม่จากฟอร์ม แล้วเรียกใช้ PromiseUpdateTable.add_update() เพื่อตรวจสอบกฎเหล็กว่า "ห้ามอัปเดตถ้าสถานะคือเงียบหาย" หากผ่านเงื่อนไข จะบันทึกข้อมูลลงใน PromiseUpdate และสั่ง PromiseTable.update_status() เพื่อเปลี่ยนสถานะคำสัญญาในฐานข้อมูลหลัก เมื่อเสร็จสิ้นจะทำการ Redirect กลับไปที่หน้ารายละเอียดคำสัญญาตามโจทย์กำหนด

####4.หน้านักการเมือง: 
	-Views: politician_info.html
	-Controllers: PoliticianController.politician_profile
	-Models: PoliticianTable และ PromiseTable
	การทำงาน: Controller รับ pol_id มาแล้วเรียก PoliticianTable.find_by_id() เพื่อดึงข้อมูลประวัตินักการเมือง และเรียก PromiseTable.find_by_politician() เพื่อดึงเฉพาะคำสัญญาที่นักการเมืองท่านนั้นเป็นเจ้าของ ข้อมูลทั้งสองส่วนจะถูกส่งไปที่ View politician_info.html เพื่อแสดงผลแบบแยกส่วนตามความรับผิดชอบของนักการเมืองแต่ละคน



