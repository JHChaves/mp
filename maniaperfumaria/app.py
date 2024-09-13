from http import HTTPStatus

from fastapi import FastAPI

from maniaperfumaria.schemas.schemas import (
    Message,
    UserDB,
    UserPublic,
    UserSchema,
)

app = FastAPI()

database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def ler():
    return {'message': 'Meu belíssimo mundo!!!'}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)

    database.append(user_with_id)

    return user_with_id
