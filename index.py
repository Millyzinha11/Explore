from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello World!"


@app.route('/contacts')
def contacts():
    return "Diga o que você quer!"


if __name__ == '__main__':
    app.run(debug=True)
