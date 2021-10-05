from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import DevelopmentConfig
from flask_perm import Perm
from flask_jwt_extended import current_user,jwt_required
# from flask.ext.manager import Manager
from flask_script import Manager

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
api = Api(app)
jwt = JWTManager(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
perm = Perm(app)
manager = Manager(app)
perm.register_commands(manager)

# from . import db,jwt,perm



class User(db.Model):
   id = db.Column(db.Integer, primary_key=True,autoincrement=True)
   name = db.Column(db.String(80), nullable=False)
   email = db.Column(db.String(150), unique=True, nullable=False)
   password = db.Column(db.String(250))


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.filter_by(id=identity['id']).one_or_none()

# @jwt_required
# @perm.current_user_loader(lambda:current_user)


@perm.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@perm.users_count_loader
def load_users_count():
    return User.query.all()

@perm.users_loader
def load_users(filter_by={}, sort_field='id', sort_dir='desc', offset=0, limit=20):
    sort = getattr(getattr(User, sort_field), sort_dir)()
    return User.query.filter_by(**filter_by).order_by(sort).offset(offset).limit(limit).all()


