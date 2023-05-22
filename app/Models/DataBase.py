from app.config import db
from app.Models.Category import Category
from app.Models.Information import Information
from app.Models.User import User
from app.Models.Product import Product
from app.Models.Admin import Admin
import base64

def addCategory(name, photo):
	photo = base64.b64encode(photo.read())
	db.session.add(Category(name, photo))
	return db.session.commit()
	


def getCategory():
	return Category.query.all() 


def getInfromation():
	return Information.query.all()

def getUser(login, password):
	return db.session.query(User.id, User.login, User.email).filter((User.login == login) | (User.email == login) | (User.phone == login)).filter(User.password == password).first()



def registryUser(login, password, email, phone):
	user = User(login, password, email, phone)
	db.session.add(user)
	db.session.commit()
	return user
	
def addProduct(name, description, photo, category_id):
	photo = base64.b64encode(photo.read())
	db.session.add(Product(name, description, photo, category_id))
	return db.session.commit()


def getProduct(category):
	return Product.query.filter_by(category_id=category).all() 



def getAdmin(user_id):
	return Admin.query.filter_by(id=user_id).first()