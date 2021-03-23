from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<name>')
def index(name=None):
    return render_template('index.html', name='qqqqqqqqqqqqqqqqqqq')


app.run('127.0.0.1', 8080, debug=True)
