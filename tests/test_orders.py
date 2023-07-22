from httpx import AsyncClient

APPS = "orders"
TABLE_ID = "order_id"


async def test_get_all(async_client: AsyncClient):
    response = await async_client.get(f"/{APPS}/get_all")
    assert response.status_code == 200


async def test_get_one(async_client: AsyncClient):
    objects = await async_client.get(f"/{APPS}/get_all")
    for obj in objects.json():
        customers = obj[TABLE_ID]
        response = await async_client.get(f"/{APPS}/get/{customers}")
        assert response.status_code == 200


async def test_create(async_client: AsyncClient):
    pass


async def test_update(async_client: AsyncClient):
    pass


async def test_delete(async_client: AsyncClient):
    pass
