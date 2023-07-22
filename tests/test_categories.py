from httpx import AsyncClient


async def test_get_all(async_client: AsyncClient):
    response = await async_client.get("/categories/get_all")
    assert response.status_code == 200


async def test_get_one(async_client: AsyncClient):
    for i in range(1, 6):
        response = await async_client.get(f"/categories/get/{i}")
        assert response.status_code == 200


async def test_create(async_client: AsyncClient):
    pass


async def test_update(async_client: AsyncClient):
    pass


async def test_delete(async_client: AsyncClient):
    pass
