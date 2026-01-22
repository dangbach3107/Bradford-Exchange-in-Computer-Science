class BankAccount:
    def __init__(self,Number,Name,Balance):
        self.__accountNumber=Number
        self.__accountName=Name
        self.__balance=Balance
    def getAccountNumber(self):
        return self.__accountNumber
    def getAccountName(self):
        return self.__accountName
    def getBalance(self):
        return self.__balance
    def deposit(self,dep):
        self.__balance = self.__balance + dep
    def withdraw(self,withdrawamount):
        if withdrawamount<=self.__balance:
            self.__balance = self.__balance-withdrawamount
            return True
        else:
            return False
        
class VIPBankAccount(BankAccount):
    def __init__(self,Number,Name,Balance,Limit):
        super(VIPBankAccount,self).__init__(Number,Name,Balance)
        self.__creditlimit=Limit
    def withdraw(self, withdrawamount):
        if withdrawamount <= super(VIPBankAccount, self).getBalance():
            return super(VIPBankAccount, self).withdraw(withdrawamount)
        elif withdrawamount <= super(VIPBankAccount,self).getBalance()+self.__creditlimit:
            self.__creditlimit = self.__creditlimit-(withdrawamount-super(VIPBankAccount,self).getBalance())
            return super(VIPBankAccount, self).withdraw(super(VIPBankAccount, self).getBalance())
        else:
            return False
    def getCredit(self):
        return self.__creditlimit

