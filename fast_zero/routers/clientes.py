from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from fast_zero.database import get_session
from fast_zero.models import Cliente
from fast_zero.schemas import (
    ClienteList,
    ClientePublic,
    ClienteSchema,
    Message,
)

Session = Annotated[Session, Depends(get_session)]
router = APIRouter(prefix='/clientes', tags=['clientes'])

# Nome;
#  CPF;
#  Data de nascimento;
#  E-mail.


@router.post('/', status_code=HTTPStatus.CREATED, response_model=ClientePublic)
def create_cliente(session: Session, cliente: ClienteSchema):
    db_cliente = session.scalar(
        select(Cliente).where(
            (Cliente.cpf == cliente.cpf) | (Cliente.email == cliente.email)
        )
    )

    if db_cliente:
        if db_cliente.cpf == cliente.cpf:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='CPF already exists',
            )
        elif db_cliente.email == cliente.email:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Email already exists',
            )

    db_cliente = Cliente(
        nome=cliente.nome,
        cpf=cliente.cpf,
        data_nasc=cliente.data_nasc,
        email=cliente.email,
    )
    session.add(db_cliente)
    session.commit()
    session.refresh(db_cliente)

    return db_cliente


@router.get('/', response_model=ClienteList)
def read_clientes(session: Session, skip: int = 0, limit: int = 100):
    clientes = session.scalars(select(Cliente).offset(skip).limit(limit)).all()
    return {'clientes': clientes}


@router.get('/{cliente_id}', response_model=ClientePublic)
def read_cliente_by_id(cliente_id: int, session: Session):
    db_cliente = session.scalar(
        select(Cliente).where(Cliente.id == cliente_id)
    )
    if not db_cliente:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Client not found'
        )

    return db_cliente


@router.get('/cpf/', response_model=ClientePublic)
def read_cliente_by_cpf(cpf: str, session: Session):
    db_cliente = session.scalar(select(Cliente).where(Cliente.cpf == cpf))
    if not db_cliente:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Client not found'
        )

    return db_cliente


@router.put('/{cliente_id}', response_model=ClientePublic)
def update_cliente(cliente_id: int, cliente: ClienteSchema, session: Session):
    db_cliente = session.scalar(
        select(Cliente).where(Cliente.id == cliente_id)
    )
    if not db_cliente:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Client not found'
        )

    db_cliente.nome = cliente.nome
    db_cliente.cpf = cliente.cpf
    db_cliente.data_nasc = cliente.data_nasc
    db_cliente.email = cliente.email
    session.commit()
    session.refresh(db_cliente)

    return db_cliente


@router.delete('/{cliente_id}', response_model=Message)
def delete_cliente(cliente_id: int, session: Session):
    db_cliente = session.scalar(
        select(Cliente).where(Cliente.id == cliente_id)
    )

    if not db_cliente:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Client not found'
        )

    session.delete(db_cliente)
    session.commit()

    return {'message': 'Client deleted'}
