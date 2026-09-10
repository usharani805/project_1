class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance   # Private variable

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited:", amount)
        else:
            print("Invalid deposit amount")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance or invalid amount")

    # Method to view balance
    def get_balance(self):
        return self.__balance


# Creating an object
account = BankAccount("Rahul", 5000)

print("Account Holder:", account.account_holder)
print("Initial Balance:", account.get_balance())

account.deposit(2000)
print("Balance after deposit:", account.get_balance())

account.withdraw(1500)
print("Balance after withdrawal:", account.get_balance())