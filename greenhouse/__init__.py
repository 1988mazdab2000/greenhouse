
from flask import Flask

app = Flask(__name__)

app.secret_key = 'development key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://pi2:Greenhouse9000@localhost/development'
from greenhouse.models import db
db.init_app(app)
import greenhouse.routes

#below added per tutorial

if __name__ == "__main__":
	app.run()
