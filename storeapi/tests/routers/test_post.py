from httpx import AsyncClient
import pytest



async def create_post(body: str, async_client: AsyncClient) -> dict:
    response = await async_client.post(
        "/posts/",
        json={"body": body},
    )

    return response.json()


@pytest.fixture()
async def created_post(async_client: AsyncClient) -> dict:
    return await create_post("test", async_client)


@pytest.mark.anyio
async def test_create_post(async_client: AsyncClient):
    body = "test post"
    response = await async_client.post(
        "/post",
        json={"body": body},
    )

    assert response.status_code == 200
    assert {"id": 0, "body": body}.items() <= response.json().items()



@pytest.mark.anyio
async def test_crate_post_missing_data(async_client: AsyncClient):
    response = await async_client.post("/post")

    assert response.status_code == 422 # 422 Unprocessable Entity
  

@pytest.mark.anyio
async def test_get_all_post(async_client: AsyncClient, created_post: dict):
    response = await async_client.get("/post")

    assert response.status_code == 200
    assert created_post ==  response.json()