# sys-employees

## Application Setup
### Install the required libs. To do so run
pip install -r requirements.txt

To run the project locally use the command \
__flask run__
### Usage
> __To retrieve entire data__ \
__url__  /employees\
__method__ GET\
__output__  
` {
"status": "success",
"data": {
"employees": [
    {
        "employee_id": "E00001",
        "first_name": "John",
        "last_name": "Keynes",
        "age": "29",
        "join_date": "2021-01-15"
    },
    {
        "employee_id": "E00002",
        "first_name": "Chisom",
        "last_name": "Robinson",
        "age": "54",
        "join_date": "2020-05-24"
    }
 ]
},
"message": "successfully retrieved employees"
}`

> __To retrieve a single employee__ \
__url__  /employees \
__method__ GET \
__output__  
`{
"status": "success",
"data": {
"employees": [
    {
        "employee_id": "E00001",
        "first_name": "John",
        "last_name": "Keynes",
        "age": "29",
        "join_date": "2021-01-15"
    },
   ] 
  } 
}`

> __To create an employee__ \
__url__  /employees \
__method POST__ \
__payload__ \
`{
"employee_id": "E00002",
"first_name": "John",
"last_name": "Keynes",
"age": "29",
"join_date": "2021-01-15"
}` \
__output__ \
`{
    "status": "success",
    "data": {
        "employee_id": "E00002",
        "first_name": "John",
        "last_name": "Keynes",
        "age": "29",
        "join_date": "2021-01-15"
    },
    "message": "successfully created employee"
}`

>__To update an employee__ \
__url__  /employees/employee_id \
__method__ PATCH \
__output__ \
`{
    "status": "success",
    "data": {
        "first_name": "Henry"
    },
    "message": "updated employee data successfully"
}`

>__To delete an employee__ \
__url__  /employees/employee_id \
__method__ DELETE \
__output__ \
`{
    "status": "success",
    "data": "E00001",
    "message": "deleted employee data successfully"
}`