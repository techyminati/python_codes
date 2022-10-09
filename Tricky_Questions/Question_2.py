#
#  * Author: Aman Upadhyay
#  * Email: amanupadhyay0208@gmail.com
#  * GitHub: https://github.com/AmanxUpadhyay
#

# Write a Python program using loop to print the decimal equivalents of 1/2, 1/3, 1/4 ,....... 1/n
def decimal(n):
    i = 1
    while i <= n:
        print(1 / i)
        i += 1

# Driver code
Number = int(input("Enter a number: "))
decimal(Number)