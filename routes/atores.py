from typing import Optional
from fastapi import APIRouter, HTTPException
from models.atores import Ator

router = APIRouter(prefix="/atores", tags=["Atores"])

@router.post(
    path="/", 
    response_model=Ator, 
    summary="Criar um novo ator", 
    description="Cria um novo ator no banco de dados.",
    status_code=201,
    response_description="Ator criado com sucesso.",
    responses={
        201: {
            "description": "Ator criado com sucesso.",
            "content": {
                "application/json": {
                    "example": {
                        "id": 123,
                        "nome": "Robert Downey Jr."
                    }
                }
            },
        },
        500: {
            "description": "Erro interno do servidor",
            "content": {
                "application/json": {
                    "example": {"detail": "Erro ao salvar o ator no banco de dados."}
                }
            }
        }
    }
)
async def criar_ator(ator: Ator) -> Optional[Ator]:
    """Cria um novo ator."""
    try:
        ator.salvar_ator()
        return ator
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))