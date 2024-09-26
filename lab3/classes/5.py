class account():
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, sum):
        if(sum>self.balance):
            print("Withdraw is exceed the available balance.\n The available balance = ", self.balance)
        else:
            self.balance -= sum
            print("Withdrawal completed successfully!.")
            print("Remaining balance = ", self.balance)

first=account("Damir", 1000000000)

first.deposit(980000)

first.withdraw(999999)