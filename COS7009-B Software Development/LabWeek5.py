#exercise 1
print('exercise 1')
a = [int(x) for x in input('Enter a list of integers: ').split()]
print('The maximum value is: ', max(a))

#exercise 2
print('exercise 2')
a = [int(x) for x in input('Enter a list of integers: ').split()]
print('The average value is: ', sum(a)/len(a))

#exercise 3
print('exercise 3')
a = [int(x) for x in input('Enter a list of integers: ').split()]
a.reverse()
print('Reverse list: ', a)

#exercise 4
print('exercise 4')
def check1(a,b):
   c = 0
   if len(a) == len(b):
       for i in range(len(a)):
           if a[i] < b[i]:
               c=c+1
           else:
               c=c
       if c == len(a):
           return True
       else:
           return False
   else:
       return False

a = [int(x) for x in input('Enter integer list 1: ').split()]
b = [int(y) for y in input('Enter integer list 2: ').split()]
print(check1(a,b))

#exercise 5
print('exercise 5')
def swap1(a,x,y):
   if x < len(a) and y < len(a): 
       c = a[x]
       a[x] = a[y]
       a[y] = c
   else:
       print('index out of bound')

a = [int(x) for x in input('Enter an integer list: ').split()]
x = int(input('Enter index 1: '))
y = int(input('Enter indes 2: '))
swap1(a,x,y)
print(a)

#exercise 6
print('exercise 6')
def adder(a,b):
   return a+b

a = [int(x) for x in input('Enter integer list 1: ').split()]
b = [int(y) for y in input('Enter integer list 2: ').split()]
print(adder(a,b))

#exercise 7
print('exercise 7')
def myIndex(a, num):
   if a.count(num) > 0:
       i = a.index(num)
       while a[(i+1):].count(num) > 0:
           i = i + 1 + a[(i+1):].index(num)
       return i
   else:
       return -1
a = [74,85,102,99,101,85,56]
print(myIndex(a,85))

#exercise 8
print('exercise 8')
def myRange(a):
   return max(a)-min(a) + 1

a = [36,12,25,19,46,31,22]
print(myRange(a))

#exercise 9
print('exercise 9')
def myCount(li,a,b):
   c = 0
   for i in range(len(li)):
       if li[i] >= a and li[i] <= b:
           c=c+1
       else:
           c=c
   return c
li = [14,1,22,17,36,7,-43,5]
print(myCount(li,4,17))

#exercise 10
print('exercise 10')
def isSorted(li):
   return sorted(li) == li

a = [16.1,12.3,22.2,14.4]
b = [1.5,4.3,7.0,19.5,25.1,46.2]
print(isSorted(a))
print(isSorted(b))



