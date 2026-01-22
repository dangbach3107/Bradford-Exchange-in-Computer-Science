import math
class Point: 
    total=0
    #Constructs a Point at the given x/y location.
    def __init__(self,initialX,initialY):
        self.x= initialX
        self.y= initialY
        Point.total+=1
    @staticmethod
    def status():
        print('total number of points created', Point.total)
        
    def setLocation(self,newX,newY):
        self.x= newX
        self.y= newY

    def translate(self,dx,dy):
        self.setLocation(self.x + dx, self.y + dy)
        return self.x,self.y
    
    def distance(self,p):
        dx = self.x-p.x
        dy= self.y-p.y
        return math.sqrt(dx * dx + dy* dy)
    
    def distanceFromOrigin(self):
        return math.sqrt(self.x**2 + self.y**2)
#Question 2  
    def isVertical(self,p):
        if (self.x==p.x):
            return true
        else:
            return false
#Question 3      
   def slope(self,p):
       return ((p.x - self.x)/p.y-self.y))

#Question 4       
class Line:
    def __init__(self,newp1,newp2):
        self.p1=newp1
        self.p2=newp2
        
    def getP1(self):
        return self.p1
    
    def getP2(self):
        return self.p2
    def getSlope(self):
        xslope = (self.p2.x - self.p1.x)
        yslope = (self.p2.y - self.p1.y)
        slope = xslope/yslope
        return slope
    def getLength(self,p):
        return math.sqrt(p.x**2 + p.y**2)


#Question 5
class BankAccount:
    def __init__(self,accountNumber,accountName,balance):
        self.__accountNumber = accountNumber
        self.__accountName = accountName
        self.__balance = balance

    def getAccountNumber(self):
        return self.__accountNumber
    
    def getAccountName(self):
        return accountName
    
    def getBalance(self):
        return self.__balance
    
    def deposit(self,amount):
        self.__balance += amount
        
    def withdraw(self,amount):
        if self.__balance > amount:
            self.__balance -=amount
            return amount
        else:
            return("Insuffifin=ent fund.....")


#Bank account objects
customer1 = BankAccount("111","Abba G", 1200.0)
customer2 = BankAccount("112","Habiba", 5000.0)
customer3 = BankAccount("113","Ummi", 4200.0)

#Transactions
customer1.deposit(2000)
print("Previous balance is : ", customer1.getBalance())
print("you withdrawned  : ", customer1.withdraw(200))
print("New  balance is :", customer1.getBalance())
