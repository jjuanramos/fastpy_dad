import os

import pytest
from starlette.testclient import TestClient

from fastpy import main
from fastpy.config import get_settings, Settings


def get_settings_override():
    return Settings(testing=1, database_url=os.environ.get("DATABASE_TEST_URL"))


@pytest.fixture(scope="module")
def test_app():
     main.app.dependency_overrides[get_settings] = get_settings_override
     with TestClient(main.app) as test_client:
         
         yield test_client
