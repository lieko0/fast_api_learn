from fastapi import FastAPI

app = FastAPI()

# cd fast_zero
# poetry shell
# task run


@app.get('/')
def read_root():
    return {'message': 'Hello World'}
