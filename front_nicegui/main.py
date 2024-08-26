from front_nicegui import table
from front_nicegui import theme


from fastapi import FastAPI
from fast_zero.database import get_session
from fast_zero.routers import clientes
from nicegui import app, ui

from fastapi import Depends
from sqlalchemy.orm import Session
# import logging
# logger = logging.getLogger('uvicorn.error')
# logger.setLevel(logging.DEBUG)
# logger.debug({'debug-ui': clientes.read_clientes(session)})
def init(fastapi_app: FastAPI) -> None:
    
    @ui.page('/')
    def root():   
        with theme.frame('Homepage'):
            ... 
            
    
    @ui.page('/home')
    def show():   
        with theme.frame('Homepage'):
            
            ui.dark_mode().bind_value(app.storage.user, 'dark_mode')
            ui.checkbox('dark mode').bind_value(app.storage.user, 'dark_mode')
    
    @ui.page('/table')
    def tabela(session: Session = Depends(get_session)):
        ui.dark_mode().bind_value(app.storage.user, 'dark_mode') 
        with theme.frame('Homepage'):
            table.table(session)

    ui.run_with(
        fastapi_app,
        mount_path='/gui',  # NOTE this can be omitted if you want the paths
        # passed to @ui.page to be at the root
        storage_secret='pick your private secret here',  # NOTE setting a
        # secret is optional but allows for persistent storage per user
    )
