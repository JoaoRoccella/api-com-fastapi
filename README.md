# Início rápido

Começando o projeto com FastAPI e Docker.

1. Criar um ambiente virtual
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1 # Windows
```

2. Instalar o FastAPI
```bash
pip install fastapi[standard]
```

3. Exportar as dependências
```bash
pip freeze > requirements.txt
```

4. Criar o arquivo `main.py` com o seguinte conteúdo:
```python
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

5. Executar a aplicação FastAPI
```bash
fastapi dev main.py
```

6. Criar o arquivo .gitignore com o seguinte conteúdo:
```
# Python
__pycache__/
.venv/
```
