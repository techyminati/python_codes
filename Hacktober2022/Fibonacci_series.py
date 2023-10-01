# A python program for finding fibonacci series easily.

def fibonacci(n):
    a,b=0,1
    print('Fibonacci series:',a,b,end=' ')
    for i in range(1,n-1):
        s=a+b
        print(s,end=' ')
        a=b
        b=s
n=int(input('Enter limit: '))
fibonacci(n)