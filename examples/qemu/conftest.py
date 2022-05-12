import pytest

@pytest.fixture(scope='session')
def command(target):
    strategy = target.get_driver('ShellStrategy')
    strategy.transition("shell")
    shell = target.get_driver('CommandProtocol')
    return shell
