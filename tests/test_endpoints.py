def test_hello_world(client):
    response = client.get('/hello-world')

    assert response.text == 'Hello, world!'


def test_get_number(client):
    for number in range(10):
        response = client.get(f'/{number}')

        assert response.json() == {'number': number}
