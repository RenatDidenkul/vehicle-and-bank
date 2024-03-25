class BankAccount:
    def __init__(self, balance, owner):
        self.balance = "100%"
        self.owner = "Renat"
       
class CheckingAccount:
    def __init__(self):
        self.withdraw = 100

class SavingsAccount:
    def __init__(self):
        self.deposit = 100
       
ba = BankAccount("100%", "Renat")
ca = CheckingAccount()
print(ca.withdraw)
sa = SavingsAccount()
print(sa.deposit)