import fastapi
import uvicorn
from fastapi import FastAPI

from src.config import DEBUG, API_VERSION, API_HOST, API_PORT, BASE_DIR

from src.employees.router import router as employees_router
from src.categories.router import router as categories_router
from src.customers.router import router as customers_router
from src.orders.router import router as orders_router
from src.products.router import router as products_router
from src.region.router import router as region_router
from src.shippers.router import router as shippers_router
from src.suppliers.router import router as suppliers_router
from src.order_details.router import router as order_details_router

app = FastAPI(
    title="Northwind",
    debug=DEBUG,
    version=API_VERSION
)


@app.get("/")
async def redirect():
    return fastapi.responses.RedirectResponse(
        "/docs#")

app.include_router(categories_router)
app.include_router(customers_router)
app.include_router(employees_router)
app.include_router(order_details_router)
app.include_router(orders_router)
app.include_router(products_router)
app.include_router(region_router)
app.include_router(shippers_router)
app.include_router(suppliers_router)


if __name__ == "__main__":
    try:
        uvicorn.run(app, host=API_HOST, port=API_PORT)
    except KeyboardInterrupt as ex:
        print(ex)
    except Exception as ex:
        print(ex)
