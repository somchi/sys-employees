from flask import Flask, jsonify, Blueprint, send_from_directory
from flask_restful import Api
# from flask_bcrypt import Bcrypt
from apispec import APISpec
from flask_cors import CORS
from flask_jwt_extended import JWTManager
import os
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec


# api resources
from api.resources.employees import Employees
from api.resources.employees import EmployeesUpdates

app = Flask(__name__, instance_relative_config=True, static_url_path='', static_folder='static/')

app.url_map.strict_slashes = False
app.config.from_object("config.settings")
app.config.from_pyfile("settings.py", silent=True)

app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Employees Management Sys',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/v1/swagger/',
    'APISPEC_SWAGGER_UI_URL': '/v1/swagger-ui/'
})

CORS(app, resources={r'/v1/*'})

# flask_bcrypt = Bcrypt(app)
jwt = JWTManager(app)

api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)

docs = FlaskApiSpec(app)

api.add_resource(Employees, '/employees', endpoint='employees')
api.add_resource(EmployeesUpdates, '/employees/<string:employee_id>', endpoint='employeesupdates')
app.register_blueprint(api_blueprint, url_prefix='/v1')


@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to sys-employees!"
    })


@app.route('/v1/static/<path:filename>')
def send_js(filename):
    t = send_from_directory('../static', filename, as_attachment=True)
    return t


@app.route('/v1/')
def v1_home():
    return jsonify({
        "message": "Welcome to sys-employees v1 API!"
    })


docs.register(home)
docs.register(Employees, blueprint='api')
docs.register(EmployeesUpdates, blueprint='api')
docs.register(v1_home)

if __name__ == "__main__":
    print(True)
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port, host='127.0.0.1')
