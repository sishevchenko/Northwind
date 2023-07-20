import fastapi
from fastapi import FastAPI

from src.config import DEBUG, API_VERSION

from src.employees.router import router as employees_router
from src.categories.router import router as categories_router
from src.customers.router import router as customers_router
from src.orders.router import router as orders_router
from src.products.router import router as products_router
from src.region.router import router as region_router
from src.shippers.router import router as shippers_router

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
app.include_router(customers_router)
app.include_router(orders_router)
app.include_router(products_router)
app.include_router(region_router)
app.include_router(shippers_router)
