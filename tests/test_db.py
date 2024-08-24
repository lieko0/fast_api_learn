from datetime import date

from sqlalchemy import select

from fast_zero.models import Cliente, User


def test_create_user(session):
    new_user = User(username='alice', password='secret', email='teste@test')
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'alice'))

    assert user.username == 'alice'


def test_create_cliente(session):
    new_cliente = Cliente(
        nome='alice',
        cpf='secret',
        data_nasc=date(1999, 12, 31),
        email='teste@test',
    )
    session.add(new_cliente)
    session.commit()

    cliente = session.scalar(select(Cliente).where(Cliente.nome == 'alice'))

    assert cliente.nome == 'alice'
