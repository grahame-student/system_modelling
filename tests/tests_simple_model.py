from unittest import TestCase
from hamcrest import assert_that, is_, not_

from OMPython import OMCSessionZMQ


class TestSimpleModel(TestCase):

    omc = None

    @classmethod
    def setup_class(cls):
        print("Setting up...")
        omc = OMCSessionZMQ()
        cmds = [
            'loadFile("~/model/simple.mo")',
        ]
        
        for cmd in cmds:
            answer = omc.sendExpression(cmd)
            print(f"\n{cmd}:\n {answer}")

    def test_omc_initialised(self):
        assert_that(TestSimpleModel.omc, is_(not_(None)))
