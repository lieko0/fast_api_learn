from fastapi import Depends, FastAPI
from nicegui import app, ui
from sqlalchemy.orm import Session

from fast_zero.database import get_session
from front_nicegui import table, theme


# import logging
# logger = logging.getLogger('uvicorn.error')
# logger.setLevel(logging.DEBUG)
# logger.debug({'debug-ui': clientes.read_clientes(session)})
def init(fastapi_app: FastAPI) -> None:
    @ui.page('/')
    def root():
        with theme.frame(''):
            ...

    @ui.page('/home')
    def show():
        with theme.frame('Home'):
            ...

    @ui.page('/table')
    def tabela(session: Session = Depends(get_session)):
        ui.dark_mode().bind_value(app.storage.user, 'dark_mode')
        with theme.frame('Tabela'):
            table.table(session)

    ui.run_with(
        fastapi_app,
        mount_path='/gui',  # NOTE this can be omitted if you want the paths
        # passed to @ui.page to be at the root
        storage_secret='pick your private secret here',  # NOTE setting a
        # secret is optional but allows for persistent storage per user
    )
