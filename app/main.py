from fastapi import FastAPI
from routes.atores import router as atores_router
from routes.series import router as series_router
from routes.categorias import router as categorias_router

app = FastAPI()

app.include_router(atores_router)
app.include_router(series_router)
app.include_router(categorias_router)