#
#  * Author: Aman Upadhyay
#  * Email: amanupadhyay0208@gmail.com
#  * GitHub: https://github.com/AmanxUpadhyay
#

# Write a Python program to generate n-th Fibonacci number.
def Fibonacci(n):
    a = 0
    b = 1
    i = 0
    while i < n:
        print(a)
        a, b = b, a + b
        i += 1

# Driver code
Number = int(input("Enter a number: "))
Fibonacci(Number)