from flask import render_template
from .import users

@users.route('/login')
def index():
    return render_template('login.html')