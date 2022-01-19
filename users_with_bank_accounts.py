class bank_account:
    def __init__(self, initBal = 0, intRate = .02, type = "checking") -> None:
        self.account_balance = initBal
        self.interest_rate = intRate
        self.accountType = type
    def deposit(self, amount):
        self.account_balance += amount
        return self
    def withdraw(self, amount):
        self.account_balance -= amount
        return self
    def display_account_info(self):
        print(f'Current account balance: ${self.account_balance}')
        print(f'Current interest rate: {self.interest_rate * 100}%')
        return self
    def yield_interest(self):
        self.account_balance = self.account_balance + (self.account_balance * self.interest_rate)
        return self

class user:
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
        self.account = bank_account()
        self.account2 = bank_account(0, .02, "savings")
    def make_deposit(self, type, amount):
        if type == "checking":
            self.account.account_balance += amount
        else:
            self.account2.account_balance += amount
        return self
    def make_withdrawal(self, type, amount):
        if type == "checking":
            self.account.account_balance -= amount
        else:
            self.account2.account_balance -= amount
        return self
    def display_user_balance(self):
        print(f'User: {self.name}, {self.account.accountType}: ${self.account.account_balance}')
        print(f'User: {self.name}, {self.account2.accountType}: ${self.account2.account_balance}')
        return self
    def transfer_money(self, otherUser, amount):
        print(f'{self.name} transferred ${amount} to {otherUser.name}')
        self.account.account_balance -= amount
        otherUser.account_balance += amount
        print(f'User: {self.name}, ${self.account_balance}')
        print(f'User: {otherUser.name}, ${otherUser.account.account_balance}')
        return self

ron = user("Ron Steak", "ron@kebobs.com")

ron.make_deposit("savings", 320).make_deposit("checking", 150).make_deposit("checking", 804).make_withdrawal("checking", 600).display_user_balance()