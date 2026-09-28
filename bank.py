class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
<<<<<<< HEAD
        return self.balance
=======
        return self.balance
>>>>>>> 3339de85db8880492d3e781012925aa2d58c54c2
