from flask import Flask
from config import Config, MailConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object(Config)
app.config.from_object(MailConfig)
db = SQLAlchemy(app)
mail = Mail(app)
migrate = Migrate(app, db)

from app.model import Mail
from app import routes
