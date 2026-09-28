import pytest


@pytest.fixture
def account():
    print("[setup]")
    yield
    print("[teardown]")


def test_setup_teardown_one(account):
    assert True


def test_setup_teardown_two(account):
    assert 100 + 50 == 150
