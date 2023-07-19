import fastapi
from fastapi import FastAPI

from src.config import DEBUG, API_VERSION

from src.employees.routers import router as employees_routers

app = FastAPI(
    title="Northwind",
    debug=DEBUG,
    version=API_VERSION
)


@app.get("/")
async def redirect():
    return fastapi.responses.RedirectResponse(
        "/docs#")

app.include_router(employees_routers)
