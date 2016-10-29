from flask import Flask
from flask import Blueprint

app = Flask(__name__)

app.secret_key = 'secret key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

from todo import main as todo_routes
from api import main as api_routes

app.register_blueprint(todo_routes)
app.register_blueprint(api_routes,
                       url_prefix='/api')

if __name__ == '__main__':
    config=dict(
        host='127.0.0.1',
        port=3000,
        debug=True,
    )
    app.run(**config)