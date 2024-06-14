from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_returns_ok_and_hello_word():
    client = TestClient(app)  # arrange (organização)
    response = client.get('/')  # act (ação)
    assert response.status_code == HTTPStatus.OK  # assert (afirmação)
    assert response.json() == {'message': 'Hello World'}  # assert (afirmação)
