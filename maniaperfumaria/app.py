from http import HTTPStatus

from fastapi import FastAPI

from maniaperfumaria.routers import auth, todos, users
from maniaperfumaria.schemas import Message

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(todos.router)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Meu belíssimo mundo!!!'}
