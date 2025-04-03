import pytest
from dotenv import load_dotenv


@pytest.fixture(scope="session", autouse=True)
def init_all_tests():
    """Load the configuration from the .env file."""
    load_dotenv(override=True)
