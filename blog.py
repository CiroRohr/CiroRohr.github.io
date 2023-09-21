 from flask import Blueprint, Flask, render_template

 app = Flask(__name__)

 @bp.route('/')
 def index():
     return render_template('temp.html')
