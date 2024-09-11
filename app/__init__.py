from flask import Flask
from flask_sqlachemy import SQLAlchemy
from flask_jwt_exttended import JWTManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:://app.db' 
app.config[''36b95f1494a6e760f4ad0bc83958b56b061272bb8b21277fbbba4009cdeab754'']

db = SQLAlchemy(app)
jwt = JWTManager(app)

from app import routes

if __name__ = '__main__':
    app.run(debug=True)
