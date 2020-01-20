# step1
# 

from flask import Flask
from flask import request
from flask import render_template
import db

app = Flask(__name__)


@app.route('/')
def index():
    country_list=db.get_country_list()
    return render_template('start.html', country_list=country_list)

@app.route('/delete_record')
def delete():
    
app.run(host='127.0.0.1', port=5000, debug=True)
