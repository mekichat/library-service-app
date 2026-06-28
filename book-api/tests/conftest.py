import os
from pathlib import Path
from dotenv import load_dotenv

# Must happen before importing app
os.environ["ENV_FILE"] = ".env.test"

env_file = Path(__file__).parent.parent / ".env.test"

if env_file.exists():
    load_dotenv(env_file)

from app import models
from app.main import app
from app.database import Base, engine
from fastapi.testclient import TestClient
import pytest


# Create tables before the test session starts
@pytest.fixture(autouse=True)
def setup_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    yield

    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def client():
    return TestClient(app)