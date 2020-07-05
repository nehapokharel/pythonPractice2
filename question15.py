class bank_account:
    def __init__(self):
        self.balance = 0
        print("Welcome!!")

    def account_info(self):
        account_holder = input("Enter name: ")
        account_number = int(input("Enter account number: "))
        self.name = account_holder
        self.acc_num = account_number
        return self.name, self.acc_num

    def deposit(self):
        amount = int(input("Enter the amount you want to deposit: "))
        self.balance += amount
        return self.balance


z = bank_account()
print("Account name and number " + str(z.account_info()))
print("Deposited amount " + str(z.deposit()))