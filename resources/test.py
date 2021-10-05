from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import current_user

class Test(Resource):
   @jwt_required(locations=['cookies'])
   def get(self):
      user = get_jwt_identity()
      print(request)
      print(request.get_json())
      print(request.headers)
      print(request.args)
      print(user)
      print(current_user)
      return 'hello world'


class Test1(Resource):
   def get(self,name):
      
      return name
