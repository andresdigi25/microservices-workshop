
from logger import logger as logging
import os
from flask import Flask
from flask_restful import request, Api, Resource


API_PREFIX = os.environ.get('API_PREFIX', '')
API_PORT = int(os.environ.get('API_PORT', 5003))

app = Flask(__name__)
api = Api(app)



class Login(Resource):
    def post(self):
        username = request.get_json().get('username')
        password = request.get_json().get('password')
        logging.info(f'username: {username} password: {password}')

        if username== 'pinga' and password=='pinga':
            logging.info('user login correctly')
            return{'ok': 'user login correctly'}, 201
        logging.error('user login failed')
        return {'error': '422 Unprocessable Entity'}, 422
    
##
## Actually setup the Api resource routing here
##
api.add_resource(Login, f'{API_PREFIX}/login')


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=API_PORT)
