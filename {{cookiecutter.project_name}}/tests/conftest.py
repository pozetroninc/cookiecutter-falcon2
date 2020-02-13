from falcon.testing import TestClient
import pytest

from {{cookiecutter.project_slug}}.app import app


@pytest.fixture
def client():
    return TestClient(app)
