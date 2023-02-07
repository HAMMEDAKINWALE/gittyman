class Account:

    def __init__(self, filepath):
        self.filepath=filepath
        with open(filepath, 'r') as file:
            self.balance=int(file.read())

    def withdraw(self, amount):
        self.balance=self.balance - amount

    def deposit(self, amount):
        self.balance=self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

class checking(Account):
    def __init__(self, filepath):
        Account.__init__(self, filepath)

   def transfer(self, amount):
       self.balance=self.balance - amount 

checking=checking('balancelist.txt')
checking.deposit(10000)
print(checking.balance)    


