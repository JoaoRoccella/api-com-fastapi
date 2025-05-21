from typing import Optional, List
from fastapi import APIRouter, HTTPException
from models.atores import Ator

router = APIRouter(prefix="/atores", tags=["Atores"])

@router.get(
    path="/",
    response_model=List[Ator],
    summary="Listar todos os atores",
    description="Retorna uma lista de todos os atores cadastrados no banco de dados.",
    status_code=200,
    response_description="Lista de atores encontrada com sucesso.",
    responses={
        200: {
            "description": "Lista de atores encontrada com sucesso.",
            "content": {
                "application/json": {
                    "example": [
                        {
                            "id_ator": 123,
                            "nome": "Robert Downey Jr."
                        },
                        {
                            "id_ator": 456,
                            "nome": "Chris Evans"
                        }
                    ]
                }
            },
        },
        404: {
            "description": "Erro de requisição",
            "content": {
                "application/json": {
                    "example": {"detail": "Nenhum ator encontrado."}
                }
            }
        },
        500: {
            "description": "Erro interno do servidor",
            "content": {
                "application/json": {
                    "example": {"detail": "Erro ao buscar os atores no banco de dados."}
                }
            }
        }
    }
)
async def listar_atores() -> List['Ator']:
    """Lista todos os atores cadastrados no banco de dados."""
    try:
        atores = Ator().buscar_atores()
        if atores:
            return atores
        else:
            raise HTTPException(status_code=404, detail="Nenhum ator encontrado.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.get(
    path="/{id_ator}", 
    response_model=Ator, 
    summary="Buscar ator pelo ID", 
    description="Busca um ator pelo ID no banco de dados.",
    status_code=200,
    response_description="Ator encontrado com sucesso.",
    responses={
        200: {
            "description": "Ator encontrado com sucesso.",
            "content": {
                "application/json": {
                    "example": {
                        "id_ator": 123,
                        "nome": "Robert Downey Jr."
                    }
                }
            },
        },
        404: {
            "description": "Ator não encontrado",
            "content": {
                "application/json": {
                    "example": {"detail": "Ator não encontrado."}
                }
            }
        },
        500: {
            "description": "Erro interno do servidor",
            "content": {
                "application/json": {
                    "example": {"detail": "Erro ao buscar o ator no banco de dados."}
                }
            }
        }
    }
)
async def buscar_ator(id_ator: int) -> Optional[Ator]:
    """Busca um ator pelo ID."""
    try:
        ator = Ator().buscar_ator_pelo_id(id_ator)
        if ator:
            return ator
        else:
            raise HTTPException(status_code=404, detail="Ator não encontrado.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

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
                        "id_ator": 123,
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