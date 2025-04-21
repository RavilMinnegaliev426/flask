from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('./index.html', name="user")


@app.route('/form')
def form():
    return render_template('./form.html')


@app.route('/about')
def about():
    return 'This is the about page'


@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    return f'Hello, {name}'


# @app.route('/data')
# def data():
#     return jsonify({'key': 'value'})


if __name__ == '__main__':
    app.run(debug=True)
