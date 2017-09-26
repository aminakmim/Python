class Trnx(object):
    def __init__(self,t,amount):
        self.t = t
        self.amount = amount
    def __str__(self):
        s = self.t + " "+ str(self.amount)
        return s

class Account(object):
    id = 1000
    def __init__(self,name,balance):
            self.name = name
            self.balance = balance
            Account.id += 1
            self.id = Account.id
            self.transactions = []
    def deposit(self,amount):
        self.balance += amount
        temp = Trnx("Deposit",amount)
        self.transactions.append(temp)
        
    def withdraw(self,amount):
        if self.balance > 0:
            self.balance -= amount
            temp = Trnx("Withdraw",amount)
            self.transactions.append(temp)
        else :
            print("Not enough balance to withdraw.")
    
    def history(self):
        if (self.transactions):
            for t in self.transactions:
                print(t)      
        
    def __str__(self):
            s = "Id: "+str(self.id)+" Name : "+self.name+" Balance : "+str(self.balance)
            return s
    def print(self):
            s = "Id: "+str(self.id)+" Name : "+self.name+" Balance : "+str(self.balance)
            print(s)

acc1 = Account("Bruce",100909)
acc1.withdraw(100)
#print(acc1)
acc1.deposit(500)
#print(acc1)
acc1.withdraw(400)
#print(acc1)
acc1.deposit(900)
acc1.withdraw(100)
#print(acc1)
acc1.withdraw(100)
acc1.history()
#print(acc1.transactions)
'''acc2 = Account("Tony",1045384)

print(acc2)
acc3 = Account("Emma",99934567)

print(acc3)'''
