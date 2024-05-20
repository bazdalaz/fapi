from typing import AsyncGenerator, Generator
from httpx import AsyncClient
import pytest

from fastapi.testclient import TestClient

from storeapi.main import app
from storeapi.routers.post import comment_table, post_table


@pytest.fixture(scope="session")
def anyio_backend() -> str:
    return "asyncio"


@pytest.fixture()
def client() -> Generator:
    yield TestClient(app)


@pytest.fixture(autouse=True, scope="session")
async def db() -> AsyncGenerator:
    post_table.clear()
    comment_table.clear()
    yield


@pytest.fixture()
async def async_client(client) -> AsyncGenerator:
    async with AsyncClient(app=app, base_url=client.base_url) as ac:
        yield ac
