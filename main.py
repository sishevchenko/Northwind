import fastapi
from fastapi import FastAPI

from src.config import DEBUG, API_VERSION

from src.employees.router import router as employees_router
from src.categories.router import router as categories_router

app = FastAPI(
    title="Northwind",
    debug=DEBUG,
    version=API_VERSION
)


@app.get("/")
async def redirect():
    return fastapi.responses.RedirectResponse(
        "/docs#")

app.include_router(employees_router)
app.include_router(categories_router)
