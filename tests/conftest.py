import pytest
from fastapi.testclient import TestClient

from maniaperfumaria.app import app


@pytest.fixture
def client():
    return TestClient(app)
