from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index1():
    return render_template('index1.html')


@app.route('/second')
def index2():
    return render_template('index2.html')


app.run('127.0.0.1', 8080, debug=True)
