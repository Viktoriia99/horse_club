from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
#manager = Manager(app)
app.config.from_object(Config)

bootstrap = Bootstrap(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# from app.controllers import home_controller
# from app.controllers import support_controller
# from app import routes
# # from app import errors
# from app.models import user, post
