import pytest


def pytest_addoption(parser):
    print("Adding --model_dir commandline option")
    parser.addoption("--model_dir", action="store")


@pytest.fixture(scope='session')
def model_dir(request):
    return request.config.getoption("--model_dir")
