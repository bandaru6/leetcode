class Bank:

    def __init__(self, balance: list[int]):
        self.balance = balance
        self.n = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        n = self.n
        if account1 < 1 or account1 > n or account2 < 1 or account2 > n:
            return False
        a1 = self.balance[account1 - 1]
        a2 = self.balance[account2 - 1]
        if a1 >= money:
            self.balance[account1 - 1] -= money
            self.balance[account2 - 1] += money
            return True
        return False
        

    def deposit(self, account: int, money: int) -> bool:
        n = self.n
        if account < 1 or account > n:
            return False
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        n=self.n
        if account < 1 or account > n:
            return False
        if money <= self.balance[account - 1]:
            self.balance[account - 1] -= money
            return True
        return False
        
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)