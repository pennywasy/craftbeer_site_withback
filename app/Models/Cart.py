from app.config import db
from sqlalchemy.schema import PrimaryKeyConstraint

class Cart(db.Model):
	__tablename__ = 'cart'
	__table_args__ = (
		PrimaryKeyConstraint('user_id', 'product_id'),
	)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=False)
	product_id = db.Column(db.Integer, db.ForeignKey('product.id'), unique=False)
	count = db.Column(db.Integer)

	def __init__(self, user_id, product_id):
		self.user_id = user_id
		self.product_id = product_id
		self.count = 1


	def addCount(self):
		self.count += 1

	def subCount(self):
		self.count -= 1
