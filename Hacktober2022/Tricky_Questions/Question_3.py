#
#  * Author: Aman Upadhyay
#  * Email: amanupadhyay0208@gmail.com
#  * GitHub: https://github.com/AmanxUpadhyay
#

#  Write a Python program for displaying reversal of a number n.
def reverse(n):
    rev = 0
    while n > 0:
        dig = n % 10
        rev = rev * 10 + dig
        n = n // 10
    return rev

# Driver code
n = int(input("Enter a number: "))
print("Reverse of the number is: ", reverse(n))