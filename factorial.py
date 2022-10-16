#// Author :RUDRANSH SRIVASTAVA
def factorial(n):
    if n==0 or n==1:
        fact=1
    else:
        fact=n*factorial(n-1)
    return fact

num=int(input())
fact=factorial(num)
print(fact)
