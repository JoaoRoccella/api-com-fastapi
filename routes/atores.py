from typing import Optional
from fastapi import APIRouter, HTTPException
from models.atores import Ator

router = APIRouter(prefix="/atores", tags=["Atores"])

@router.post("/", response_model=Ator)
async def criar_ator(ator: Ator) -> Optional[Ator]:
    """Cria um novo ator."""
    try:
        ator.salvarAtor()
        return ator
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))