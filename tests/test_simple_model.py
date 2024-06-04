import pytest
from hamcrest import assert_that, is_, not_

from OMPython import ModelicaSystem


@pytest.fixture
def get_model(model_dir):
    print("Setting up...")
    model_under_test = f"{model_dir}/simple.mo"
    print(model_under_test)
    model = ModelicaSystem(model_under_test, "FirstOrder")

    yield model


def test_omc_initialised(get_model):
    model = get_model
    assert_that(model, is_(not_(None)))
