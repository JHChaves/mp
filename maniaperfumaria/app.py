from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def ler():
    return {'message': 'Meu belíssimo mundo!!!'}
