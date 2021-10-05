class DevelopmentConfig():
   TESTING = True
   UPLOAD_FOLDER = '/uploads'
   SQLALCHEMY_DATABASE_URI = 'mysql://faris404:12345678@localhost/flask_auth'
   SQLALCHEMY_TRACK_MODIFICATIONS = False
   BASE_URL = 'http://localhost:5000'
   JWT_SECRET_KEY = '1234567890'
   SECRET_KEY = 'qwerty'