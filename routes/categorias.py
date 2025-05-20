from typing import Optional
from fastapi import APIRouter, HTTPException
from models.categorias import Categoria

router = APIRouter(prefix="/categorias", tags=["Categorias"])

@router.post("/", response_model=Categoria)
async def criar_categoria(categoria: Categoria) -> Optional[Categoria]:
    """Cria uma nova categoria."""
    try:
        if categoria.salvarCategoria():
            return categoria
        else:
            raise HTTPException(status_code=500, detail="Erro ao salvar a categoria.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))