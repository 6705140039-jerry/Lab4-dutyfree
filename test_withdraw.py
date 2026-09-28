import pytest
from bank_account import BankAccount


@pytest.fixture
def account():
    return BankAccount(100)


def test_withdraw(account):
    account.withdraw(40)
    assert account.balance == 60


def test_overdraft(account):
    with pytest.raises(ValueError):
        account.withdraw(150)