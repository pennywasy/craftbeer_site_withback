from app.config import db
from app.Models.Category import Category


class Product(db.Model):
	__tablename__ = "product"
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(100), nullable=False)
	description = db.Column(db.String(150), nullable=False)
	photo = db.Column(db.BLOB, nullable=False)

	category_id = db.Column(db.Integer, db.ForeignKey('category.id'), unique=False)

	def __init__(self, name, description, photo, category_id):
		self.name = name
		self.description = description
		self.photo = photo
		self.category_id = category_id

	def __repr__(self):
		return f"{self.photo}"[2:-1]