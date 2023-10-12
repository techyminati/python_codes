#
#  * Author: Aman Upadhyay
#  * Email: amanupadhyay0208@gmail.com
#  * GitHub: https://github.com/AmanxUpadhyay
#

# Write a Python program to check given number is palindrome or not.
def PalindromeCheck(n):
    rev = 0
    while n > 0:
        dig = n % 10
        rev = rev * 10 + dig
        n = n // 10
    if rev == n:
        return True
    else:
        return False

# Driver code
n = int(input("Enter a number: "))
if PalindromeCheck(n):
    print("Number is palindrome")
else:
    print("Number is not palindrome")