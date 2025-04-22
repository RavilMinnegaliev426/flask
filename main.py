from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

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


@app.route('/data')
def data():
    return jsonify({'key': 'value'})


if __name__ == '__main__':
    app.run(debug=True)


# sql
# подключение базы данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'


db.create_all()

user = User.query.first()
print(user)


new_user = User(username='newuser', email='email@example.com')
db.session.add(new_user)
db.session.commit()


User.query.filter_by(username='newuser').first()
