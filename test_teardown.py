import pytest

@pytest.fixture
def setup_teardown():
    print("\n[setup]")
    yield
    print("\n[teardown]")

def test_one(setup_teardown):
    print("Running test_one")
    assert True

def test_two(setup_teardown):
    print("Running test_two")
    assert True