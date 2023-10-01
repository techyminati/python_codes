#
#  * Author: Aman Upadhyay
#  * Email: amanupadhyay0208@gmail.com
#  * GitHub: https://github.com/AmanxUpadhyay
#

# Write a Python program to print sum of N natural numbers.
def NaturalNumber(n):
    i = 1
    sum = 0
    while i <= n:
        sum = sum + i
        i += 1
    return sum

# Driver code
Number = int(input("Enter a number: "))
print("Sum of the number is: ", NaturalNumber(Number))