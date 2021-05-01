from flask_restful import Resource, reqparse
from flask import request
import json
import os
from flask_apispec.views import MethodResource
from api.schemas.employee_schema import EmployeeSchema


class Employees(MethodResource, Resource):
    # retrieve employees data
    def get(self):
        try:
            '''
                This retrieves the entire employees ans specific employees if the employee id is provided
            '''
            parser = reqparse.RequestParser()
            parser.add_argument('employee_id', type=str, trim=True, required=False)

            args = parser.parse_args()

            employee_id = args.employee_id

            # open and read the json file while data is stored
            employees = open(os.path.join(os.getcwd(), "data.json"), "r")
            data = json.load(employees)
            employees.close()
            result = None

            if employee_id is None:
                result = {'employees': data}
            else:
                for employee in data:
                    if employee_id == employee['employee_id']:
                        result = {'employees': [employee]}
                    break

            return {
                'status': 'success',
                'data': result,
                'message': 'successfully retrieved employees'
            }, 200

        except Exception as e:
            with open(os.path.join(os.getcwd(), "error.log"), "a") as file:
                file.write(str(e) + '\n')
            return {
                'status': 'failed',
                'data': None,
                'message': str(e)
            }, 500

    # create employee data
    def post(self, **kwargs):
        try:
            '''
                This endpoint is called to add new set of employee.
            '''
            # all the data sent via the request body will available on the json_data variable
            json_data = request.get_json()

            if request.content_type != 'application/json':
                return {
                   'status': 'failed',
                   'data': None,
                   'message': "content type must be application/json"
                }, 400
            '''
                Check the validity of the data, whether the data was sent 
                and if it was sent to be sure it is not empty
            '''

            req_fields = ["employee_id", "first_name", "last_name", "age", "join_date"]
            for field in req_fields:
                if field not in json_data:
                    return {
                       'status': 'failed',
                       'data': None,
                       'message': field + ' is required'
                    }, 400
                elif json_data[field] == '':
                    return {
                       'status': 'failed',
                       'data': None,
                       'message': field + ' cannot be empty'
                    }, 400
                elif type(json_data[field]) != str:
                    return {
                       'status': 'failed',
                       'data': None,
                       'message': field + ' must be string'
                    }, 400
                else:
                    pass

            file = open(os.path.join(os.getcwd(), "data.json"), "r+")
            data = json.load(file)

            if len(data) != 0:
                for item in data:
                    if json_data['employee_id'] == item['employee_id']:
                        return {
                           'status': 'failed',
                           'data': None,
                           'message': 'employee_id must be unique'
                        }, 400
                data.append(json_data)
            else:
                data.append(json_data)

            file.seek(0)
            json.dump(data, file, indent=4)

            return {
               'status': 'success',
               'data': json_data,
               'message': 'successfully created employee'
            }, 201

        except Exception as e:
            with open(os.path.join(os.getcwd(), "error.log"), "a") as file:
                file.write(str(e) + '\n')
            return {
               'status': 'failed',
               'data': str(e),
               'message': str(e)
            }, 500


# Employee update
class EmployeesUpdates(MethodResource, Resource):
    # update part or all of an employee's data
    def patch(self, employee_id):
        try:
            # As with the post request all the data sent via the request body will available on the json_data variable
            json_data = request.get_json()

            if request.content_type != 'application/json':
                return {
                   'status': 'failed',
                   'data': None,
                   'message': "content type must be application/json"
                }, 400
            # the id of will be accessible with the employee_id.

            """
                This endpoint is used to handle data update on a specific dataset
            """
            db = open(os.path.join(os.getcwd(), "data.json"), "r+")
            data = json.load(db)

            found_id = False

            for i in range(len(data)):
                employee = data[i]
                if employee_id == employee['employee_id']:
                    found_id = True
                    for key in employee:
                        if key in json_data:
                            # ensure employee_id is not been updated
                            if key == 'employee_id':
                                return {
                                   'status': 'failed',
                                   'data': None,
                                   'message': key + ' cannot be updated'
                               }, 400
                            else:
                                employee[key] = json_data[key]
                    print(employee)
                    data[i] = employee
                    db.seek(0)
                    json.dump(data, db, indent=4)

            msg = 'updated employee data successfully' if found_id else 'employee not found'
            status = 'success' if found_id else 'failed'
            status_code = 200 if found_id else 400

            return {
               'status': status,
               'data': {'employee_id': employee_id},
               'message': msg
            }, status_code
        except Exception as e:
            with open(os.path.join(os.getcwd(), "error.log"), "a") as file:
                file.write(str(e) + '\n')
            return {
               'status': 'failed',
               'data': None,
               'message': str(e)
            }, 500

    # remove am employee
    def delete(self, employee_id):
        try:
            """
                This will handle removal of a specific dataset from the entire dataset
            """
            db = open(os.path.join(os.getcwd(), "data.json"), "r+")
            data = json.load(db)
            found_id = False

            count = 1

            while count < len(data):
                employee = data[count]
                if employee_id == employee['employee_id']:
                    data.pop(count)
                    found_id = True
                count += 1

            file = open(os.path.join(os.getcwd(), "data.json"), 'w')
            json.dump(data, file, indent=4)

            msg = 'deleted employee data successfully' if found_id else 'employee not found'
            status = 'success' if found_id else 'failed'
            status_code = 200 if found_id else 400

            return {
               'status': status,
               'data': employee_id,
               'message': msg
            }, status_code

        except Exception as e:
            with open(os.path.join(os.getcwd(), "error.log"), "a") as file:
                file.write(str(e) + '\n')
            return {
               'status': 'failed',
               'data': None,
               'message': str(e)
            }, 500
