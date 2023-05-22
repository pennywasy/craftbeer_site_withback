# from sqlalchemy.schema import PrimaryKeyConstraint
from app.config import db

class Category(db.Model):

	__tablename__ = 'category'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(100), nullable=False)
	photo = db.Column(db.BLOB)

	product_id = db.relationship('Product', backref='product')

	def __init__(self, name, photo):
		self.name = name
		self.photo = photo

	def __repr__(self):
		return f"{self.photo}"[2:-1]