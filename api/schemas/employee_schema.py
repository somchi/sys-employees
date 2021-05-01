from marshmallow import Schema, fields, ValidationError, validates


class EmployeeSchema(Schema):
    employee_id = fields.Str(default='')
    first_name = fields.Str(default='')
    last_name = fields.Str(default='')
    age = fields.Str(default='')
    join_date = fields.Str(default='')
