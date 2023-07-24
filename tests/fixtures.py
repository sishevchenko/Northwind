import random

import pytest
from httpx import AsyncClient


@pytest.fixture(params=["apps", "table_id"])
class CRUDFixture:
    @staticmethod
    async def test_get_all(apps: str, async_client: AsyncClient):
        response = await async_client.get(f"/{apps}/get_all")
        assert response.status_code == 200

    @staticmethod
    async def test_get_one(apps: str, table_id: str, async_client: AsyncClient):
        objects = await async_client.get(f"/{apps}/get_all")
        objects = objects.json()
        test_num = len(objects) // 2 if len(objects) <= 15 else random.randint(5, 10)
        for obj in random.sample(objects, test_num):
            customers = obj[table_id]
            response = await async_client.get(f"/{apps}/get/{customers}")
            assert response.status_code == 200

    @staticmethod
    async def test_create(async_client: AsyncClient):
        pass

    @staticmethod
    async def test_update(async_client: AsyncClient):
        pass

    @staticmethod
    async def test_delete(async_client: AsyncClient):
        pass
