class Account():

    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return(f"{self.name} has balance {self.balance}")

    def deposit(self,dep_amt):
        self.balance = self.balance + dep_amt
        return ("Old Balance = {} , New Balance = {} ".format(self.balance - dep_amt,self.balance))
    
    def withdraw(self,wid_amt):
        if wid_amt <= self.balance:
            self.balance = self.balance - wid_amt
            return ("Old Balance = {} , New Balance = {} ".format(self.balance + wid_amt,self.balance))
        else:
            print("Not enough Balance!!!")
    
acc1 = Account('Jose',100)
print(acc1)
acc1.deposit(200)
print(acc1)
acc1.withdraw(400)
print(acc1)


    
