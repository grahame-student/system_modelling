import pytest
from hamcrest import assert_that, is_, not_

from OMPython import ModelicaSystem


@pytest.fixture
def get_model(model_dir):
    model_under_test = f"{model_dir}/simple.mo"
    model = ModelicaSystem(model_under_test, "FirstOrder")

    yield model


def test_omc_initialised(get_model):
    model = get_model
    assert_that(model, is_(not_(None)))

def test_model_simulation_runs(get_model):
    model = get_model
    model.simulate()
