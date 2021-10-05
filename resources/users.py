from flask import request
from flask import jsonify
from flask import make_response
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import set_access_cookies
from flask_jwt_extended import unset_jwt_cookies

from models import User,db

class Users(Resource):
   
   def get(self):
      users = User.query.all()
      res = [
         {
            "id":u.id,
            "name":u.name,
            "email":u.email,
         }
         for u in users
      ]
      return res
   
   def post(self):
      try:
         data = request.get_json()
         user = User(**data)
         db.session.add(user)
         db.session.commit()
         return 'success'
      except Exception as e:
         print(e)
         return 'error'

class UserLogin(Resource):
   
   def post(self):
      try:
         data = request.get_json()
         user = User.query.filter(User.email == data['email'],User.password == data['password']).first()
         if user:
            token = create_access_token(identity={'id':user.id,'user':user.email,'role':'admin'})
            resp = make_response(jsonify({'msg':'Success'}),200)
            set_access_cookies(resp, token)
            return resp
         return 'invalid user'
      except Exception as e:
         print(e)
         return 'error'



   @jwt_required(locations=['cookies'])
   def delete(self):
      try:
         resp = make_response(jsonify({'msg':'Success'}),200)
         unset_jwt_cookies(resp)
         return resp
      except Exception as e:
         print(e)
         return make_response(jsonify({'msg': 'Server Error'}), 500)