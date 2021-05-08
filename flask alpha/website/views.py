from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')

def home():
  return render_template("Telos.html")

@views.route('/products') 

def products():
  return  render_template("products.html")

@views.route('/webapp')

def webapp():
  return "<p>click url to download</p>"
