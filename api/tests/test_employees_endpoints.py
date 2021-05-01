def test_get_endpoint(client):
    response = client.get('/v1/employees')
    response_body = response.get_json()

    response_data = response_body.get('data')
    assert response.status_code == 200
    assert type(response_data) == dict
    assert response_body.get('message') == "successfully retrieved employees"


def test_post_endpoint(client):
    payload = {
        "employee_id": "E00009",
        "first_name": "John",
        "last_name": "Keynes",
        "age": "29",
        "join_date": "2021-01-15"
        }
    response = client.post('/v1/employees', headers={"Content-Type": "application/json"}, json=payload)
    response_body = response.get_json()

    response_data = response_body.get('data')

    assert response.status_code == 201
    assert type(response_data) == dict
    assert response_body.get('message') == "successfully created employee"


def test_patch_endpoint(client):
    payload = {
        "first_name": "Test",
    }
    response = client.patch('/v1/employees/E00009', headers={"Content-Type": "application/json"}, json=payload)
    response_body = response.get_json()

    response_data = response_body.get('data')

    assert response.status_code == 200
    assert type(response_data) == dict
    assert response_body.get('message') == "updated employee data successfully"


def test_delete_endpoint(client):
    response = client.delete('/v1/employees/E00009', headers={"Content-Type": "application/json"})
    response_body = response.get_json()

    response_data = response_body.get('data')

    assert response.status_code == 200
    assert type(response_data) == str
    assert response_body.get('message') == "deleted employee data successfully"
