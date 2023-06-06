from app.config import db
from app.Models.Category import Category
from app.Models.Information import Information
from app.Models.User import User
from app.Models.Product import Product
from app.Models.Admin import Admin
from app.Models.Cart import Cart
from sqlalchemy import func
import base64

def addCategory(name, photo):
	photo = base64.b64encode(photo.read())
	db.session.add(Category(name, photo))
	return db.session.commit()
	


def getCategory():
	return Category.query.all() 


def getInfromation():
	return Information.query.all()

def getUser_byPassword(login, password):
	return db.session.query(User.id, User.login, User.email).filter((User.login == login) | (User.email == login) | (User.phone == login)).filter(User.password == password).first()


def getUser_byId(id):
	return User.query.filter_by(id=id).first()


def updateUserPassword(id, password):
	User.query.filter_by(id=id).update(dict(password=password))
	db.session.commit()
	return

def updateUserData(id, login, email, phone):
	User.query.filter_by(id=id).update(dict(login=login, email=email, phone=phone))
	db.session.commit()
	return

def updateUserAvatar(id, photo):
	photo = base64.b64encode(photo.read())
	User.query.filter_by(id=id).update(dict(avatar=photo))
	db.session.commit()
	return

def registryUser(login, password, email, phone, photo):
	photo = base64.b64encode(photo.read())
	user = User(login, password, email, phone, photo)
	db.session.add(user)
	db.session.commit()
	return user
	
def addProduct(name, price, description, photo, category_id):
	photo = base64.b64encode(photo.read())
	db.session.add(Product(name, price, description, photo, category_id))
	return db.session.commit()


def getProducts_byCategory(category, page):
	page = int(page)
	query = Product.query.filter_by(category_id=category)
	return (len(query.all()), query.slice(20*(page-1), 20*page).all())

def getProducts_byName(name):
	return Product.query.filter_by(name=name).first() 


def getAdmin(user_id):
	return Admin.query.filter_by(id=user_id).first()


def addCartItem(user_id, product_id):
	db.session.add(Cart(user_id, product_id))
	db.session.commit()
	return


def addCountCartItem(user_id, product_id):
	cart = Cart.query.filter_by(user_id=user_id, product_id=product_id).first()
	count = cart.count + 1
	cart.addCount()
	db.session.commit()
	return count

def subCountCartItem(user_id, product_id):
	cart = Cart.query.filter_by(user_id=user_id, product_id=product_id).first()
	count = cart.count + 1
	cart.subCount()
	db.session.commit()
	return count

def deleteItemCart_byId(user_id, product_id):
	Cart.query.filter_by(user_id=user_id, product_id=product_id).delete()
	db.session.commit()
	return


def getCartItem(user_id):
	cartItem = db.session.query(Product, Cart).join(Cart, Cart.product_id == Product.id).join(User, User.id == Cart.user_id)
	# cartItem = Product.query.join(Cart, Cart.product_id == Product.id).join(User, User.id == Cart.user_id)
	cartItem = cartItem.filter(User.id == user_id)
	return cartItem


def getSumCart(user_id):
	SumCart = db.session.query(func.sum(Product.price * Cart.count).label('sum_cart')).join(Cart, Cart.product_id == Product.id).join(User, User.id == Cart.user_id)
	SumCart = SumCart.filter(User.id == user_id).first()

	return SumCart