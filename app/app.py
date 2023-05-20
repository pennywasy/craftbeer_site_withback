from flask import Flask, render_template, request
from app.config import app
from app.Models.DataBase import *



@app.route('/')
def index():
	Category = getCategory()
	Information = getInfromation()
	return render_template('index.html', Category=Category, Information=Information)


@app.route('/admin', methods=['GET', 'POST'])
def admin():
	addInformation()
	if request.method == 'POST':
		name = request.form.get('name')
		photo = request.files['photo']
		addCategory(name, photo)
	return render_template('admin.html')
