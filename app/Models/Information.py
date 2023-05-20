from app.config import db



class Information(db.Model):
	__tablename__ = 'Information'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(100), nullable=False)
	description = db.Column(db.String(150), nullable=False)

	def __init__(self, name, description):
		self.name = name
		self.description = description