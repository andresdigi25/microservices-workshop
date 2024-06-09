from pycon_demo_library_python.util import process_output
from model import USERS
from pycon_demo_library_python.util import logger as logging
import os
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource


API_PREFIX = os.environ.get('API_PREFIX', '')
API_PORT = int(os.environ.get('API_PORT', 5001))

app = Flask(__name__)
api = Api(app)



def abort_if_user_doesnt_exist(user_id):
    if user_id not in USERS:
        abort(404, message="User {} doesn't exist".format(user_id))

parser = reqparse.RequestParser()
parser.add_argument('task')

# Todo
#   show a single user item and lets you delete them
class User(Resource):
    def get(self, user_id):
        abort_if_user_doesnt_exist(user_id)
        return USERS[user_id]

    def delete(self, user_id):
        abort_if_user_doesnt_exist(user_id)
        del USERS[user_id]
        return '', 204

    def put(self, user_id):
        args = parser.parse_args()
        email = {'email': args['email']}
        USERS[user_id] = email
        return email, 201


# UserList
#   shows a list of all users, and lets you POST to add new emails
class UserList(Resource):
    def get(self):
        logging.info("returning all users")
        return process_output(USERS)

    def post(self):
        args = parser.parse_args()
        user_id = 'user%d' % (len(USERS) + 1)
        USERS[user_id] = {'email': args['email']}
        return USERS[user_id], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(UserList, f'{API_PREFIX}/users')
api.add_resource(User, f'{API_PREFIX}/users/<string:user_id>')


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=API_PORT)
