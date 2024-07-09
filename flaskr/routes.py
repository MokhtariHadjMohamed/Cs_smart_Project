from flask import render_template, request
from flaskr import app

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    name = "world"
    if request.method == 'POST':
        name = request.form['name']
    return render_template('index.html', title='hobbies', name =name)