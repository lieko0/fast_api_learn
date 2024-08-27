# import logging

from fastapi import Depends
from nicegui import events, ui
from sqlalchemy.orm import Session

from fast_zero.database import get_session
from fast_zero.models import Cliente
from fast_zero.routers import clientes

# logger = logging.getLogger('uvicorn.error')
# logger.setLevel(logging.DEBUG)
# # logger.debug({'debug-ui': clientes.read_clientes(session)})


# https://quasar.dev/vue-components/dialog


def table(session: Session = Depends(get_session)) -> None:
    # https://github.com/zauberzeug/nicegui/blob/main/examples/table_and_slots/main.py
    # https://github.com/zauberzeug/nicegui/blob/main/examples/editable_table/main.py

    def update_table():
        # logger.debug({'debug-ui': clientes.read_clientes(session)})
        try:
            cliente_list = clientes.read_clientes(session)['clientes']
            ui.notify(message='read_clientes', position='top')
            # logger.debug({'debug-ui': cliente_list})
            for cliente in cliente_list:
                c: Cliente = cliente
                # logger.debug({'debug-ui': c})
                table_one.add_rows({
                    'id': c.id,
                    'nome': c.nome,
                    'cpf': c.cpf,
                    'data_nasc': c.data_nasc,
                    'email': c.email,
                    'actions': c.id,
                })
        except Exception as ex:
            ui.notify(message=ex, position='left')

    def create(e: events.GenericEventArguments) -> None:
        ui.run_javascript('location.reload();')
        ui.notify('not implemented, ma frend')

    def update(e: events.GenericEventArguments) -> None:
        table_one.update()
        ui.notify('not implemented, ma frend')

    async def delete(e: events.GenericEventArguments) -> None:
        try:
            msg = clientes.delete_cliente(
                cliente_id=e.args['id'], session=session
            )
            ui.notify(message=f'OK: {msg}')
            ui.run_javascript(
                code='setTimeout(() => {  location.reload(); }, 5000);'
            )

        except Exception as ex:
            ui.notify(message=ex, position='left')

    columns = [
        {'name': 'id', 'label': 'ID', 'field': 'id'},
        {'name': 'nome', 'label': 'Nome', 'field': 'nome'},
        {'name': 'cpf', 'label': 'CPF', 'field': 'cpf'},
        {'name': 'data_nasc', 'label': 'Data Nasc.', 'field': 'data_nasc'},
        {
            'name': 'email',
            'label': 'Email',
            'field': 'email',
            'align': 'center',
        },
        {'name': 'actions', 'label': 'Ações', 'field': 'actions'},
    ]
    table_one = ui.table(
        title='Clientes', columns=columns, rows=[], row_key='id'
    ).classes('h-full')

    table_one.add_slot(
        'body',
        r"""
        <q-tr :props="props">
            <q-td key="id" :props="props">
                {{ props.row.id }}
            </q-td>
            <q-td key="nome" :props="props">
                {{ props.row.nome }}
                <q-popup-edit buttons v-model="props.row.nome" v-slot="scope"
                @update:model-value="() => $parent.$emit('rename', props.row)"
                >
                    <q-input
                        type="text"
                        v-model="scope.value"
                        autofocus
                        counter
                        @keyup.enter.stop
                    />
                </q-popup-edit>
            </q-td>
            <q-td key="cpf" :props="props">
                {{ props.row.cpf }}
            </q-td>
            <q-td key="data_nasc" :props="props">
                {{ props.row.data_nasc }}
                <q-popup-edit v-model="props.row.data_nasc" v-slot="scope"
                @update:model-value="() => $parent.$emit('rename', props.row)"
                >
                    <q-input v-model="scope.value" dense autofocus counter
                       @keyup.enter="scope.set" />
                </q-popup-edit>
            </q-td>
            <q-td key="email" :props="props">
                {{ props.row.email }}
            </q-td>
            <q-td key="actions" :props="props" >
                <q-btn size="sm" color="warning" round dense icon="delete"
                    @click="() => $parent.$emit('delete', props.row)"
                />
            </q-td>
        </q-tr>
    """,
    )

    # table_one.add_slot('bottom', r'''
    #     <div class="q-pa-md q-gutter-sm" :props="props" color="blue">
    #         <q-dialog v-model="prompt">
    #             <q-card style="min-width: 350px">
    #                 <q-card-section>
    #                     <div class="text-h6">Your address</div>
    #                 </q-card-section>

    #                 <q-card-section class="q-pt-none">
    #                     <q-input dense v-model="address" autofocus
    #                       @keyup.enter="prompt = false" />
    #                 </q-card-section>

    #                 <q-card-actions align="right" class="text-primary">
    #                     <q-btn flat label="Cancel" v-close-popup />
    #                     <q-btn flat label="Add address" v-close-popup />
    #                 </q-card-actions>
    #             </q-card>
    #         </q-dialog>
    #     </div>
    # ''')

    # table_one.add_slot('bottom', r'''
    #     <q-btn class="full-width" color="primary" label="Adicionar"
    #         @click="() => $parent.$emit('add_row')"
    #     />
    #     <q-space />
    # ''')

    table_one.on('add_row', create)
    table_one.on('rename', update)
    table_one.on('delete', delete)

    update_table()
