class bank:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def get_balance(self):
        print("Remaining balance : Rs", self.balance)
    
    def credit(self, amount):
        self.balance += amount
        print(f"Rs {amount} has been credited to your account XXXXX{self.account_no}")
        self.get_balance()

    def debit(self, amount):
        if  amount > self.balance:
            print("Insufficient balance")
            self.get_balance()
        else:
            self.balance -= amount
            print(f"Rs {amount} has been debited from your account XXXXX{self.account_no}")
            self.get_balance()
# balance , acc number
c1 = bank(500, 5214)
# c1.credit(200)
c1.debit(100)