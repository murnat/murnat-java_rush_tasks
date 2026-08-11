# Банкир.

# Создайте класс BankAccount с конструктором, который принимает параметры account_number и initial_balance.
# Добавьте метод deposit(amount), который пополняет счет, и метод withdraw(amount), который снимает средства со счета.
# Создайте объект этого класса и выполните несколько операций пополнения и снятия средств.

class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.initial_balance = initial_balance

    def deposit(self, amount):
        self.initial_balance = self.initial_balance + amount

    def withdraw(self, amount):
        if amount > self.initial_balance:
            print(f'Insufficient balance!')
        else:
            self.initial_balance = self.initial_balance - amount

new_bank_account = BankAccount('1', 100)
new_bank_account.deposit(4)
print(f'Current balance of account number {new_bank_account.account_number} is {new_bank_account.initial_balance}')
new_bank_account.deposit(15)
print(f'Current balance of account number {new_bank_account.account_number} is {new_bank_account.initial_balance}')
new_bank_account.withdraw(9)
print(f'Current balance of account number {new_bank_account.account_number} is {new_bank_account.initial_balance}')
new_bank_account.withdraw(5)
print(f'Current balance of account number {new_bank_account.account_number} is {new_bank_account.initial_balance}')
new_bank_account.withdraw(200)

