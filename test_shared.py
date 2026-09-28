def test_deposit_increases_funded_account_balance(funded_account):
    funded_account.deposit(200)

    assert funded_account.balance == 1200


def test_withdraw_decreases_funded_account_balance(funded_account):
    funded_account.withdraw(300)

    assert funded_account.balance == 700