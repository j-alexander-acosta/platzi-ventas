from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hola, Ingenieros de Software egresados de Platzi'


if __name__ == '__main__':
    app.run()