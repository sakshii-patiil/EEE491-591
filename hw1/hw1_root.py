from numpy import abs
'''
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
n = int (input("Enter a number whose factorial is desired: : "))
print(factorial(n))
'''
N = float (input("\nEnter a number whose square root is desired:"))
g = float (input("Enter an initial guess:"))

def my_sqrt(n,N):
    n1=float (n+(N/n))/2
    if  abs(n1-n) < 0.01 : 
        return n1
    else:
        return my_sqrt(n1,N)

root = round(my_sqrt(g,N),2)
print("\nThe square root of ",N , " is ",root)
