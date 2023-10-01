#
#  * Author: Aman Upadhyay
#  * Email: amanupadhyay0208@gmail.com
#  * GitHub: https://github.com/AmanxUpadhyay
#

# Write a Python program to print factorial of a number.
def Factorial(n):
    fact = 1
    while n > 0:
        fact = fact * n
        n -= 1
    return fact

# Driver code
Number = int(input("Enter a number: "))
print("Factorial of the number is: ", Factorial(Number))