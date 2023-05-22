from app.config import db


class Admin(db.Model):
	__tablename__ = 'admins'
	id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
