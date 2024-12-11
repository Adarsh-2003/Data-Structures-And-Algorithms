class bank:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def get_balance(self):
        return self.balance
    
    def credit(self, amount):
        self.balance += amount
        print(amount, "has been credited from your account", self.account_no)
        print("Remaining balance :", self.get_balance())

    def debit(self, amount):
        self.balance -= amount
        print(amount, "has been debited from your account", self.account_no)
        print("Remaining balance :", self.balance())

c1 = bank(100, 5214)
c1.credit(200)