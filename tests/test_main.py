from httpx import AsyncClient


async def test_redirect(async_client: AsyncClient):
    response = await async_client.get("/")
    assert response.status_code == 307
