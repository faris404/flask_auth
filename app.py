from models import app,api
from resources.users import UserLogin, Users
from resources.test import Test,Test1


api.add_resource(Users,'/users')
api.add_resource(UserLogin,'/user/login')
api.add_resource(Test,'/test')
api.add_resource(Test1,'/test/<string:name>')





if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=5000)