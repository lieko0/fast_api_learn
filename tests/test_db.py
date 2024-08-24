from datetime import date

from sqlalchemy import select

from fast_zero.models import Cliente


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
