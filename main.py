import fastapi
from fastapi import FastAPI

from src.config import DEBUG, API_VERSION

app = FastAPI(
    title="Northwind",
    debug=DEBUG,
    version=API_VERSION
)


@app.get("/")
async def redirect():
    return fastapi.responses.RedirectResponse(
        "/docs#")
