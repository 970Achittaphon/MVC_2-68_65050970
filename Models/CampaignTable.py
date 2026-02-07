from Models.Database import db
from Models.Campaign import Campaign

class CampaignTable:
    # find_all: ดึงข้อมูลแคมเปญทั้งหมด
    @staticmethod
    def find_all():
        return Campaign.query.all()

    # add_campaign: เพิ่มแคมเปญใหม่ 
    @staticmethod
    def add_campaign(year, constituency):
        try:
            new_camp = Campaign(year=year, constituency=constituency)
            db.session.add(new_camp)
            db.session.commit()
            return True
        except:
            return False