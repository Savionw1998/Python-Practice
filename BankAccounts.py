class BankAccount:
        def __init__(self, int_rate, balance):
                self.intrest = int_rate
                self.balance = balance
                self.yieldint = 0
        def deposit(self, amount):
                self.balance += amount
                return self
        def withdraw(self, amount):
                self.balance -= amount
                return self
        def display_account_info(self):
                print(self.balance)
                return self
        def yield_interest(self):
                self.yield_int = self.yieldint*self.balance
                return self
class User:
        def __init__(self, name, email_address):
                self.name = name
                self.email = email_address
                self.account= BankAccount(int_rate=0, balance=0)
        def make_deposit(self, amount):
                self.account.deposit(amount)
                return self
        def make_withdrawal(self, amount):
                self.account.withdraw(amount)
                return self
        def display_user_balance(self):
                print(self.account.balance)
                return self
        def transfer_money(self, other_user, amount):
                self.account.balance -=amount
                other_user.account.balance +=amount
                return self

Savion = User("Savion", "winstonsavion@gmail.com")
Rose = User("Rose", "Tenten@gmail.com")
Amoi = User("Amoi", "AmoiGordon@gmail.com")

Savion = BankAccount(.10, 5000)
Amoi = BankAccount(.5, 200)
Rose = BankAccount(0.5, 35000)

Savion.deposit(100).deposit(150).deposit(150).withdraw(50)
Amoi.deposit(140).deposit(160).withdraw(100).withdraw(100)

print(Savion.balance)
print(Amoi.balance)
print(Rose.balance)