from typing import Optional
from fastapi import APIRouter, HTTPException
from models.series import Serie

router = APIRouter(prefix="/series", tags=["Séries"])

@router.post("/", response_model=Serie)
async def criar_serie(serie: Serie) -> Optional[Serie]:
    """Cria uma nova série."""
    try:
        if serie.salvarSerie():
            return serie
        else:
            raise HTTPException(status_code=500, detail="Erro ao salvar a série.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
