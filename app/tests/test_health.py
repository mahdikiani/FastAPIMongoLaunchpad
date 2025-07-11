import httpx
import pytest


@pytest.mark.asyncio
async def test_health(client: httpx.AsyncClient):
    """Test the /api/v1/health endpoint."""
    response = await client.get("/health")
    assert response.status_code == 200
    assert response.json().get("status") == "up"
