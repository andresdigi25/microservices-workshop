from service import process_output
from model import TODOS
from logger import logger as logging
import os
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource


API_PREFIX = os.environ.get('API_PREFIX', '')
API_PORT = int(os.environ.get('API_PORT', 5000))

app = Flask(__name__)
api = Api(app)



def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task')

# Todo
#   show a single todo item and lets you delete them
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


# TodoList
#   shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        logging.info("returning all todos")
        logging.warn(f"Calling todos")
        return process_output(TODOS)

    def post(self):
        args = parser.parse_args()
        todo_id = 'todo%d' % (len(TODOS) + 1)
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, f'{API_PREFIX}/todos')
api.add_resource(Todo, f'{API_PREFIX}/todos/<string:todo_id>')


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=API_PORT)
