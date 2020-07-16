from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object("project.config.Config")
CORS(app)
db = SQLAlchemy(app)

from project.main.route.home import home_routes
app.register_blueprint(home_routes)

