#!/usr/bin/python3
# routes.py


from flask import Blueprint
from flask import render_template
#app.url_map.strict_slashes = False

views = Blueprint('views', __name__)

@views.route('/')
#@views.route('/index')
def home():
    return render_template('home.html')

@views.route('/blog-post')
def blog():
    return render_template('blog_post.html')