import random

from httpx import AsyncClient

APPS = "customers"
TABLE_ID = "customer_id"


async def test_get_all(async_client: AsyncClient):
    response = await async_client.get(f"/{APPS}/get_all")
    assert response.status_code == 200


async def test_get_one(async_client: AsyncClient):
    objects = await async_client.get(f"/{APPS}/get_all")
    objects = objects.json()
    test_num = len(objects) // 2 if len(objects) <= 15 else random.randint(5, 10)
    for obj in random.sample(objects, test_num):
        customers = obj[TABLE_ID]
        response = await async_client.get(f"/{APPS}/get/{customers}")
        assert response.status_code == 200


async def test_create(async_client: AsyncClient):
    pass


async def test_update(async_client: AsyncClient):
    pass


async def test_delete(async_client: AsyncClient):
    pass
