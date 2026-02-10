class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.__balance=balance #Private variable
    def deposit(self,amount):
        self.__balance += amount
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
            print("withdrawen amount",amount)
        else:
            print("NoFunds you Broke Ass")
    def get_balance(self):
        return self.__balance