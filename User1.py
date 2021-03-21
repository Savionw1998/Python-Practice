class User1:
    def __init__(self, name, email_address):# now our method has 2 parameters!
        self.name = name			# and we use the values passed in to set the name attribute
        self.email = email_address		# and the email attribute
        self.account_balance = 0		# the account balance is set to $0, so no need for a third parameter
        # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received
        return self
    def make_withdrawal(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance -= amount	# the specific user's account increases by the amount of the value received
        #adding display balance method
        return self
    def display_user_balance(self):
        print(self.account_balance)
        return self
    def transfer_money(self, other_user, amount):
        self.account_balance -=amount
        other_user.account_balance +=amount
        return self

Savion = User1("Savion", "winstonsavion@gmail.com")
Rose = User1("Rose", "Tenten@gmail.com")
Amoi = User1("Amoi", "AmoiGordon@gmail.com")

Savion.make_deposit(100).make_deposit(15000).make_deposit(1500).transfer_money(Rose, 7770)
Rose.make_deposit(1560).make_deposit(16300)
Rose.make_withdrawal(9800).make_withdrawal(1600)
Amoi.make_deposit(163400).make_withdrawal(1600).make_withdrawal(1100).make_withdrawal(1670)

print(Savion.account_balance)
print(Rose.account_balance)
print(Amoi.account_balance)
