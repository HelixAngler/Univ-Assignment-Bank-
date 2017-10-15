#Customer Class
class Customer(object):
    def __init__(self,listing):
        self.categories = listing
        self.check=""
        while True:
            try:
                self.first=input("First").upper()
                self.last=input("Last").upper()
                self.check=self.first+"_"+self.last
                self.entry=self.categories[self.check]
                break
            except:
                print("Invalid")
                continue
        self.activity=Account(self.categories[self.check])
    def firstname(self):
        return self.first
    def lastname(self):
        return self.last
    def acc(self):
        while True:
            print("\nBalance: ",self.activity.getBalance())
            try:
                decision=int(input("Options\n1. Deposit\n2. Withdrawal\n3. Log Out"))
            except:
                print("Invalid")
                continue
            if decision==1:
                self.categories[self.check],self.boolcheck = self.activity.deposit()
            elif decision==2:
                self.categories[self.check],self.boolcheck = self.activity.withdrawal()
            elif decision==3:
                break
            if self.boolcheck:
                print("Success")
#Account Class
class Account(object):
    def __init__(self,entr):
        self.bal=float(entr)
    def getBalance(self):
        return self.bal
    def deposit(self):
        while True:
            try:
                self.storing=float(input("How Many?"))
                break
            except:
                print("Invalid")
                continue
        self.bal=float(self.bal+self.storing)
        self.bool=True
        return self.bal,self.bool
    def withdrawal(self):
        if self.bal==0:
            print("Your Balance is Empty")
            self.bool=False
        else:
            while True:
                try:
                    self.taking=float(input("How Many?"))
                except:
                    print("error")
                if self.taking>self.bal:
                    print("Insufficient")
                else:
                    self.bal=float(self.bal-self.taking)
                    self.bool=True
                    break
        return self.bal,self.bool
#Bank Class
class Bank(object):
    def __init__(self,datbas,bankname):
        self.customer=datbas
        self.bankname=bankname
        print("Welcome to %s"%(self.bankname))
        self.cus=0
        for i in datbas.keys():
            self.cus+=1
        print("Customers : %d"%self.cus)
    def addcustomer(self):
        f=input("First Name").upper()
        l=input("Last Name").upper()
        self.naming=f+"_"+l
        self.customer[self.naming]=float(0)
    def getcustomerscount(self):
        return self.cus
    def getcustomer(self):
        checkup=Customer(self.customer)
        fn=checkup.firstname()
        ln=checkup.lastname()
        print("%s %s"%(fn,ln))
        checkup.acc()
#Main Program
golg={}
nm="Absurd Bank"
while True:
    sogr=Bank(golg,nm)
    gorgon=input("Select options:\n1. New Account\n2. Check How Many of Our Customers\n3. Start Transactions\nOthers for exit")
    if gorgon=="1":
        sogr.addcustomer()
    elif gorgon=="2":
        cust=sogr.getcustomerscount()
        print(cust)
    elif gorgon=="3":
        sogr.getcustomer()
    else:
        break