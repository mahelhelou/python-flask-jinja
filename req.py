import json
import requests
import flask
from flask import render_template
import jinja2

# Category class
class Category:
	def getData(self):
		url = 'http://staging.bldt.ca/api/method/build_it.user_api.home.get_home/data/main_categories'
		response = requests.get(url)
		return response.text

category = Category()
values_of_category = category.getData()

# Product class
class Product:
	def getData(self):
		url = 'http://staging.bldt.ca/api/method/build_it.user_api.home.get_home/data/main_categories'
		response = requests.get(url)
		return response.text

product = Product()
values_of_product = product.getData()

app = flask.Flask(__name__)
@app.route("/template.html")

def home():
	res = requests.get("http://staging.bldt.ca/api/method/build_it.user_api.home.get_home")
	data = res.text
	data = json.loads(data)

	context = {}
	context['title'] = "gsg"
	context['main_categories'] = data['data']['main_categories']
	data_product = json.loads(values_of_product)
	context['featured_items'] = data_product['data']['featured_items']
	return render_template("template.html",**context)


app.run(debug=True)
