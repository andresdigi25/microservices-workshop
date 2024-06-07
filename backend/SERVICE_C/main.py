from service import process_output
from model import TRACKER
from logger import logger as logging
import os
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource


API_PREFIX = os.environ.get('API_PREFIX', '')
API_PORT = int(os.environ.get('API_PORT', 5002))

app = Flask(__name__)
api = Api(app)



def check_tracker_existence_and_abort(user_id):
    if user_id not in TRACKER:
        abort(404, message="User {} doesn't exist".format(user_id))

parser = reqparse.RequestParser()
parser.add_argument('task')

# Todo
#   show a single user item and lets you delete them
class Tracker(Resource):
    def get(self, user_id):
        check_tracker_existence_and_abort(user_id)
        return TRACKER[user_id]

    def delete(self, user_id):
        check_tracker_existence_and_abort(user_id)
        del TRACKER[user_id]
        return '', 204

    def put(self, user_id):
        args = parser.parse_args()
        email = {'email': args['email']}
        TRACKER[user_id] = email
        return email, 201


# TrackerList
#   shows a list of all trackers, and lets you POST to add new emails
class TrackerList(Resource):
    def get(self):
        logging.info("returning all trackers")
        logging.warn(f"Calling trackers")
        return process_output(TRACKER)

    def post(self):
        args = parser.parse_args()
        user_id = 'user%d' % (len(TRACKER) + 1)
        TRACKER[user_id] = {'email': args['email']}
        return TRACKER[user_id], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(TrackerList, f'{API_PREFIX}/tracker')
api.add_resource(Tracker, f'{API_PREFIX}/tracker/<string:user_id>')


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=API_PORT)
