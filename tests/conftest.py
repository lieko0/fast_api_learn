import pytest
from fastapi.testclient import TestClient

from fast_zero.app import app

# princípio DRY (Don't Repeat Yourself)


@pytest.fixture()
def client():
    return TestClient(app)
