class BankAccount:
    def __init__(self, acc_number, balance):
        self.__acc_number = acc_number
        self.__balance = balance

    @property
    def acc_number(self):
        return self.__acc_number

    @property
    def balance(self):
        return self.__balance

    @acc_number.setter
    def acc_number(self, new_number):
        self.__acc_number = str(new_number)

        if self.__acc_number.isdigit() and len(self.__acc_number) == 12:
            self.__acc_number = new_number
        else:
            print("Invalid account number. Account number must be at 12 digits.")

    @balance.setter
    def balance(self, new_balance):
        if new_balance >= 0:
            self.__balance = new_balance
        else:
            print("Invalid balance. Balance cannot be negative.")

account = BankAccount(123456789, 1000.0)

account.acc_number = "123456789"
account.balance = -100.0

print(account.acc_number)
print(account.balance)