from http import HTTPStatus

from fast_zero.schemas import ClientePublic


def test_create_cliente(client):
    response = client.post(
        '/clientes',
        json={
            'nome': 'alice',
            'cpf': '11111111111',
            'data_nasc': '1999-12-31',
            'email': 'alice@example.com',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'nome': 'alice',
        'cpf': '11111111111',
        'data_nasc': '1999-12-31',
        'email': 'alice@example.com',
        'id': 1,
    }


def test_create_cliente_cpf_already_exists(client, um_cliente):
    response = client.post(
        '/clientes',
        json={
            'nome': 'alice',
            'cpf': um_cliente.cpf,
            'data_nasc': '1999-12-31',
            'email': 'alice000@example.com',
        },
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {
        'detail': 'CPF already exists',
    }


def test_create_cliente_email_already_exists(client, um_cliente):
    response = client.post(
        '/clientes',
        json={
            'nome': 'alice',
            'cpf': '12312312311',
            'data_nasc': '1999-12-31',
            'email': um_cliente.email,
        },
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {
        'detail': 'Email already exists',
    }


def test_read_users(client):
    response = client.get('/clientes')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'clientes': []}


def test_read_users_with_users(client, um_cliente):
    cliente_schema = ClientePublic.model_validate(um_cliente).model_dump(
        mode='json'
    )
    response = client.get('/clientes/')
    assert response.json() == {'clientes': [cliente_schema]}


def test_get_cliente_by_id(client, um_cliente):
    response = client.get('/clientes/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'nome': um_cliente.nome,
        'cpf': um_cliente.cpf,
        'data_nasc': um_cliente.data_nasc.isoformat(),
        'email': um_cliente.email,
        'id': um_cliente.id,
    }


def test_get_cliente_by_id_not_found(client):
    response = client.get('/clientes/1')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {
        'detail': 'Client not found',
    }


def test_get_cliente_by_cpf(client, um_cliente):
    response = client.get('/clientes/cpf/', params={'cpf': um_cliente.cpf})
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'nome': um_cliente.nome,
        'cpf': um_cliente.cpf,
        'data_nasc': um_cliente.data_nasc.isoformat(),
        'email': um_cliente.email,
        'id': um_cliente.id,
    }


def test_get_cliente_by_cpf_not_found(client):
    response = client.get('/clientes/cpf/', params={'cpf': '11111111111'})
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {
        'detail': 'Client not found',
    }


def test_update_cliente(client, um_cliente):
    response = client.put(
        '/clientes/1',
        json={
            'nome': 'alice',
            'cpf': '11111111111',
            'data_nasc': '1999-12-31',
            'email': 'alice@example.com',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'nome': 'alice',
        'cpf': '11111111111',
        'data_nasc': '1999-12-31',
        'email': 'alice@example.com',
        'id': 1,
    }


def test_update_cliente_not_found(client):
    response = client.put(
        '/clientes/1',
        json={
            'nome': 'alice',
            'cpf': '11111111111',
            'data_nasc': '1999-12-31',
            'email': 'alice@example.com',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {
        'detail': 'Client not found',
    }


def test_delete_cliente(client, um_cliente):
    response = client.delete('/clientes/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'message': 'Client deleted',
    }


def test_delete_cliente_not_found(client):
    response = client.delete('/clientes/1')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {
        'detail': 'Client not found',
    }
