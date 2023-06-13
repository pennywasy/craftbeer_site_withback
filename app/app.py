from flask import Flask, render_template, request, redirect, url_for, session
from app.config import app
from app.Models.DataBase import *


@app.route('/')
def index():
	session['side'] = '/'
	Category = getCategory()
	Information = getInfromation()
	return render_template('index.html', Category=Category, Information=Information)


@app.route('/admin/category/', methods=['GET', 'POST'])
def admin_category():
	if not getAdmin(session['id']):
		return redirect(url_for('index'))
	if request.method != 'POST':
		return render_template('admin_category.html')
	name = request.form.get('name')
	photo = request.files['photo']
	addCategory(name, photo)
	return


@app.route('/admin/product/', methods=['GET', 'POST'])
def admin_product():
	
	Category = getCategory()
	if not getAdmin(session['id']):
		return redirect(url_for('index'))
	if request.method != 'POST':
		return render_template('admin_product.html', Category=Category)

	name = request.form.get('name')
	price = request.form.get('price')
	description = request.form.get('description')
	photo = request.files['photo']
	category_id = request.form.get('category_id')
	try:
		addProduct(name, price, description, photo, category_id)
		return "Карточка товара успешно загружена"
	except:
		return "Произошла ошибка"




@app.route('/login/', methods=['POST', 'GET'])
def login():
	if request.method != 'POST':
		return render_template('login.html')
	login = request.form.get('login')
	password = request.form.get('password')
	if user := getUser_byPassword(login, password):
		session['isAuth'] = True
		session['login'] = login
		session['id'] = user.id
		session['email'] = user.email


		return redirect(session['side'])

	return render_template('login.html', message='Не верный логин или пароль')	
				



@app.route('/registry/', methods=['POST', 'GET'])
def registry():
	if request.method != 'POST':
		return render_template('registry.html')

	login = request.form.get('login')
	password = request.form.get('password')
	email = request.form.get('email')
	phone = request.form.get('phone')
	photo = request.files['avatar']
	try:
		error = ''
		user = registryUser(login, password, email, phone, photo)
		session['isAuth'] = True
		session['login'] = login
		session['id'] = user.id
		session['email'] = user.email
		return redirect(url_for('index'))
		print('pass')
	except Exception as e:
		print(e)
		error = 'Вы используете уже существующие данные'
		return render_template('registry.html', error=error)
			



@app.route('/personal/')
def personal():
	session['side'] = '/personal/'
	if not session['isAuth']:
		return redirect(url_for('index'))

	user = getUser_byId(session['id'])
	Category = getCategory()
	return render_template('personal.html', Category=Category, user=user)



@app.route('/catalog/<category>/<page>', methods=['GET'])
def catalog(category, page):
	session['side'] = f'/catalog/{category}/{page}'
	Category = getCategory()
	product = getProducts_byCategory(category, page)	
	countPages = product[0] // 20 + 1
	return render_template('catalog.html', Category=Category, product=product[1], countPages=countPages)


@app.route('/catalog/product/<product>', methods=['GET'])
def product(product):
	Category = getCategory()
	product = getProducts_byName(product)
	return render_template('product.html', Category=Category, product=product)


@app.route('/cart/')
def cart():
	Category = getCategory()
	cart = getCartItem(session['id'])
	SumCart = getSumCart(session['id'])
	return render_template('cart.html', Category=Category, cart=cart, SumCart=SumCart)


@app.route('/addCart/', methods=['POST'])
def addCart():
	product_id = request.form.get('product_id')
	try:
		addCountCartItem(session['id'], product_id)
		return "+1"
	except Exception as e:
		addCartItem(session['id'], product_id)
		return "Товар добавлен в корзину"


@app.route('/addItemCart/', methods=['POST'])
def addItemCart():
	product_id = request.form.get('product_id')
	return f"{addCountCartItem(session['id'], product_id)}"

@app.route('/subItemCart/', methods=['POST'])
def subItemCart():
	product_id = request.form.get('product_id')
	return f"{subCountCartItem(session['id'], product_id)}"


@app.route('/deleteItemCart', methods=['POST'])
def deleteItemCart():
	product_id = request.form.get('product_id')
	return deleteItemCart_byId(session['id'], product_id)

@app.route('/logout/')
def logout():
	session['isAuth'] = False
	session['login'] = ''
	session['id'] = ''
	session['email'] = ''
	return redirect(session['side'])



@app.route('/personal/update/avatar', methods=['POST'])
def personalUpdateAvatar():
	photo = request.files['avatar']
	updateUserAvatar(session['id'], photo)
	return redirect(url_for('personal'))


@app.route('/personal/update/data', methods=['POST'])
def personalUpdateData():
	login = request.form.get('login')
	email = request.form.get('email')
	phone = request.form.get('phone')
	updateUserData(session['id'], login, email, phone)
	return redirect(url_for('personal'))


@app.route('/personal/update/password', methods=['POST'])
def personalUpdatePassword():
	password = request.form.get('password')
	updateUserPassword(session['id'], password)
	return redirect(url_for('personal'))


@app.route('/cart/getTotalPrice/', methods=['POST'])
def getTotalPrice():
	return f"{getSumCart(session['id']).sum_cart}"