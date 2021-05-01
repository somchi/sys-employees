def test_home_endpoint(client):
    response = client.get('/')
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body.get('message') == "Welcome to sys-employees!"


def test_v1_home_endpoint(client):
    response = client.get('/v1/')
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body.get('message') == "Welcome to sys-employees v1 API!"

