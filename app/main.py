from typing import Union
from fastapi import FastAPI

# Documentação oficial: https://fastapi.tiangolo.com/
# Tarefa: https://gist.github.com/a698548559aaca644e9ebe11b8de81ca.git

app = FastAPI()

@app.get('/')
def read_hello():
    return {"Hello": "World"}

@app.get('/items/{item_id}/{query}')
def read_item(item_id: int, query: Union[str, None] = None):
    return {"item_id": item_id, "query": query}