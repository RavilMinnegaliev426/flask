from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('./index.html', name="user")


@app.route('/about')
def about():
    return 'This is the about page'


@app.route('/greet/<name>')
def greet(name):
  return f'Hello, {name}!'


if __name__ == '__main__':
    app.run(debug=True)
