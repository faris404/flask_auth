from flask import make_response
from flask import render_template

class Secure:

   def __init__(self,app,db):

      self.app = app
      self.db = db

   