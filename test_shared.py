def test_shared_account_has_funds(funded_account):
    assert funded_account.balance == 1000


def test_shared_account_can_deposit(funded_account):
    funded_account.deposit(100)
    assert funded_account.balance == 1100
