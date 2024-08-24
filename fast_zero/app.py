from http import HTTPStatus

from fastapi import FastAPI

from fast_zero.routers import users
from fast_zero.schemas import Message

app = FastAPI()

# cd fast_zero
# poetry shell
# task run

app.include_router(users.router)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'hello hello'}
