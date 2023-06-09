from app.config import db

class User(db.Model):
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	login = db.Column(db.String(150), nullable=False, unique=True)
	password = db.Column(db.String(150), nullable=False)
	email = db.Column(db.String(150), nullable=False, unique=True)
	phone = db.Column(db.String(150), nullable=False, unique=True)
	birthday = db.Column(db.Date, nullable=False)
	avatar = db.Column(db.BLOB)


	def __init__(self, login, password, email, phone, birthday, avatar):
		self.login = login
		self.password = password
		self.email = email
		self.phone = phone
		self.birthday = birthday
		self.avatar = avatar

	def __repr__(self):
		return f"{self.avatar}"[2:-1]