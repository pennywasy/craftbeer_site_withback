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
	if getAdmin(session['id']):
		if request.method == 'POST':
			name = request.form.get('name')
			photo = request.files['photo']
			addCategory(name, photo)
		return render_template('admin_category.html')

	return redirect(url_for('index'))

@app.route('/admin/product/', methods=['GET', 'POST'])
def admin_product():
	if getAdmin(session['id']):
		Category = getCategory()
		if request.method == 'POST':
			name = request.form.get('name')
			price = request.form.get('price')
			description = request.form.get('description')
			photo = request.files['photo']
			category_id = request.form.get('category_id')
			addProduct(name, price, description, photo, category_id)
		return render_template('admin_product.html', Category=Category) 


	return redirect(url_for('index'))


@app.route('/login/', methods=['POST', 'GET'])
def login():
	if request.method == 'POST':
		login = request.form.get('login')
		password = request.form.get('password')
		if user := getUser(login, password):
			session['isAuth'] = True
			session['login'] = login
			session['id'] = user.id
			session['email'] = user.email


			return redirect(session['side'])

		return render_template('login.html', message='Не верный логин или пароль')	
				

	return render_template('login.html')


@app.route('/registry/', methods=['POST', 'GET'])
def registry():
	if request.method == 'POST':
		login = request.form.get('login')
		password = request.form.get('password')
		email = request.form.get('email')
		phone = request.form.get('phone')
		try:
			error = ''
			user = registryUser(login, password, email, phone)
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
			

	return render_template('registry.html')


@app.route('/personal/')
def personal():
	session['side'] = '/personal/'
	if session['isAuth']:
		Category = getCategory()
		return render_template('personal.html', Category=Category)

	return redirect(url_for('index'))


@app.route('/catalog/<category>/', methods=['GET'])
def catalog(category):
	session['side'] = f'/catalog/{category}/'
	Category = getCategory()
	product = getProducts_byCategory(category)	
	return render_template('catalog.html', Category=Category, product=product)


@app.route('/catalog/product/<product>', methods=['GET'])
def product(product):
	Category = getCategory()
	product = getProducts_byName(product)
	return render_template('product.html', Category=Category, product=product)


@app.route('/logout/')
def logout():
	session['isAuth'] = False
	session['login'] = ''
	session['id'] = ''
	session['email'] = ''
	return redirect(session['side'])