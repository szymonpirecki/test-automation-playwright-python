import os

import pytest
import yaml
from dotenv import load_dotenv

load_dotenv()

_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def _require_env(key: str) -> str:
    value = os.getenv(key)
    if value is None:
        pytest.fail(
            f"Required environment variable '{key}' is not set. "
            f"Copy .env.example to .env and fill in the values."
        )
    return value


@pytest.fixture(scope="session")
def variables() -> dict:
    config_path = os.path.join(_ROOT_DIR, "properties.yaml")
    try:
        with open(config_path) as f:
            data: dict = yaml.safe_load(f)
    except (FileNotFoundError, yaml.YAMLError) as e:
        pytest.fail(f"Cannot load test configuration from '{config_path}': {e}")

    data['users']['standard']['username'] = _require_env('STANDARD_USERNAME')
    data['users']['standard']['password'] = _require_env('STANDARD_PASSWORD')
    data['users']['locked_out']['username'] = _require_env('LOCKED_OUT_USERNAME')
    data['users']['locked_out']['password'] = _require_env('LOCKED_OUT_PASSWORD')

    return data
