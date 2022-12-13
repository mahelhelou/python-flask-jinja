import json
import requests
import flask
from flask import render_template
import jinja2

# object class

# Category Class
class Category:
 def getData(self):
    url = 'http://staging.bldt.ca/api/method/build_it.user_api.home.get_home/data/main_categories'
    response = requests.get(url)
    return response.text

# Category Object
category = Category()
values_of_category = category.getData()

#################################################

# Product Class
class Product:
 def getData(self):
    url = 'http://staging.bldt.ca/api/method/build_it.user_api.home.get_home/data/main_categories'
    response = requests.get(url)
    return response.text


# Product Object
product = Product();
values_of_product = product.getData()

        # _______________________________________________________________-

app =flask.Flask(__name__)
@app.route("/template.html")
def home():
    res = requests.get("http://staging.bldt.ca/api/method/build_it.user_api.home.get_home")
    data = res.text
    data = json.loads(data)
    # print(type(data), res.text)
    # print(data['data']['main_categories'][5]['image'])

    context = {}
    context['title'] = "gsg"
    context['main_categories'] = data['data']['main_categories']
    data_product = json.loads(values_of_product)
    context['featured_items'] = data_product['data']['featured_items']
    return render_template("template.html",**context)


app.run(debug=True)
