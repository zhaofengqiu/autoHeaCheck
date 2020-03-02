from exts import db
class Info(db.Model):
    __tablename__ = "info"
    name = db.Column(db.String(20),)
    sex = db.Column(db.String(2))
    schoolnum = db.Column(db.String(20), primary_key=True)
    bumen = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(40))
    def to_dict(self):
        user_dict = {
            "name": self.name,
            "sex": self.sex,
            "schoolnum": self.schoolnum,
            "bumen": self.bumen,
            "phone": self.phone,
            "email":self.email
        }
        return user_dict
db.create_all()
