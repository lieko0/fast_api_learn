import json
from nicegui import events, ui
from fast_zero.routers import clientes
from sqlalchemy.orm import Session
from fast_zero.database import get_session
from fast_zero import schemas
from fastapi import Depends
from fast_zero.models import Cliente

import logging
logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)
# logger.debug({'debug-ui': clientes.read_clientes(session)})


def table(session: Session = Depends(get_session)) -> None:
    
    columns = [
        {'name': 'id', 'label': 'ID', 'field': 'id'},
        {'name': 'nome', 'label': 'Nome', 'field': 'nome'},
        {'name': 'cpf', 'label': 'CPF', 'field': 'cpf'},
        {'name': 'data_nasc', 'label': 'Data Nasc.', 'field': 'data_nasc'},
        {'name': 'actions', 'label': 'Ações', 'field': 'actions'},
    ]
    table_one =  ui.table(title='Clientes',columns=columns,rows=[],row_key='id').classes('w-96')
    
    # https://github.com/zauberzeug/nicegui/blob/main/examples/table_and_slots/main.py
    # https://github.com/zauberzeug/nicegui/blob/main/examples/editable_table/main.py

    def update_table():
        logger.debug({'debug-ui': clientes.read_clientes(session)})
        cliente_list = clientes.read_clientes(session)['clientes']
        logger.debug({'debug-ui': cliente_list})
        table_one.clear()
        for cliente in cliente_list:
            c : Cliente = cliente
            logger.debug({'debug-ui': c})
            table_one.add_rows(
                {
                    'id': c.id,
                    'nome': c.nome,
                    'cpf': c.cpf,
                    'data_nasc': c.data_nasc,
                    'actions': 1
                }
            )


    update_table()
    
