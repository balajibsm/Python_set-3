#calc.py

import math

def add(a,b):
  print("Sum of a and b is",a+b)
    
def diff(a,b):
  print("Difference of a and b is",a-b)
    
def multiply(a,b):
  print("Multiplication of a and b is",a*b)


def div(a,b):
  print("Division of a and  b is",a/b)
    
def sqroot(a):
    print("Square root of the number",a,"is", math.sqrt(a))
    
def floor_div(a,b):
    print("Floor division of a and b is", a//b)
    
def fib(nterms):
  a=0
  b=1
  if nterms<=0:
    print("please enter positive number")
  elif nterms==1:
    print("Fibonacci series:",a)
  elif nterms==2:
    print(a)
    print(b)
  else:
    print(a)
    print(b)
    while(nterms>2):
      numnext=a+b
      print(numnext)
      a=b
      b=numnext
      nterms=nterms-1



def isprime(num):
   if num > 1:
     for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           break
       else:
           print(num,"is a prime number")
           break
       
   else:
      print(num,"is not a prime number")


      


 
        


