from fastapi import FastAPI
from routes.atores import router as atores_router
from routes.series import router as series_router
from routes.categorias import router as categorias_router

app = FastAPI(
    title="API de Séries",
    description="API para gerenciar séries, atores e categorias.",
    version="0.1.0",
    openapi_tags=[
        {
            "name": "Atores",
            "description": "Operações relacionadas a atores."
        },
        {
            "name": "Séries",
            "description": "Operações relacionadas a séries."
        },
        {
            "name": "Categorias",
            "description": "Operações relacionadas a categorias."
        }
    ]
)

app.include_router(atores_router)
app.include_router(series_router)
app.include_router(categorias_router)