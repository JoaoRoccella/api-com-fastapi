from math import e
from typing import Optional
from fastapi import APIRouter, HTTPException
from models.series import Serie

router = APIRouter(prefix="/series", tags=["Séries"])

@router.post(
    path="/", 
    response_model=Serie,
    summary="Cria uma nova série",
    description="Insere uma nova série na base de dados, criando também a categoria caso necessário.",
    status_code=201,
    response_description="Série criada com sucesso.",
    responses={
        201: {
            "description": "Série criada com sucesso.",
            "content": {
                "application/json": {
                    "example": {
                        "id": 42,
                        "titulo": "Stranger Things",
                        "descricao": "Série de ficção científica e terror ambientada nos anos 80.",
                        "ano_lancamento": 2016,
                        "id_categoria": 3,
                        "nome_categoria": "Ficção Científica"
                    }
                }
            }
        },
        500: {
            "description": "Erro interno ao salvar a série.",
            "content": {
                "application/json": {
                    "example": {"detail": "Erro ao executar inserção da série no banco de dados."}
                }
            }
        }
    }
)
async def criar_serie(serie: Serie) -> Optional[Serie]:
    """Cria uma nova série."""
    try:
        if serie.salvar_serie():
            return serie
        else:
            raise HTTPException(status_code=500, detail="Erro ao salvar a série.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
