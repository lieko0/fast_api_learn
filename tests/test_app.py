from http import HTTPStatus


def test_read_root_returns_ok_and_hello_word(client):
    response = client.get('/')  # act (ação)
    assert response.status_code == HTTPStatus.OK  # assert (afirmação)
    assert response.json() == {'message': 'hello hello'}  # assert (afirmação)
