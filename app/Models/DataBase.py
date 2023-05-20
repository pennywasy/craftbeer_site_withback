from app.config import db
from app.Models.Category import Category
from app.Models.Information import Information
# from PIL import Image
# from io import BytesIO
import base64

def addCategory(name, photo):
	photo = base64.b64encode(photo.read())
	db.session.add(Category(name, photo))
	db.session.commit()
	return


def getCategory():
	return Category.query.all() 


def getInfromation():
	return Information.query.all()