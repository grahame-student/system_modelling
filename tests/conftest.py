import pytest


def pytest_addoption(parser):
    parser.addoption("--model_dir", action="store")


@pytest.fixture(scope='session')
def model_dir(request):
    return request.config.getoption("--model_dir")
