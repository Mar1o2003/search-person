from app import db

class Person(db.Model):
    __tablename__ = 'people'

    id_ern = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String(50))
    name = db.Column(db.String(50))
    patronymic = db.Column(db.String(50))
    date_of_birth = db.Column(db.Date)
    gender = db.Column(db.Integer)
