from OMPython import OMCSessionZMQ

class TestSimpleModel:

    omc = None

    @classmethod
    def setup_class(cls)
        omc = OMCSessionZMQ()
        cmds = [
            'loadFile("~/model/simple.mo")',
        ]
        
        for cmd in cmds:
            answer = omc.sendExpression(cmd)
            printf("{'\n'} {cmd}: {'\n'}{answer}")
