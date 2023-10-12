#
#  * Author: Aman Upadhyay
#  * Email: amanupadhyay0208@gmail.com
#  * GitHub: https://github.com/AmanxUpadhyay
#

# Write a Python program to check given number is Armstrong or not.
def ArmstrongCheck(n):
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if sum == n:
        return True
    else:
        return False

# Driver code
n = int(input("Enter a number: "))
if ArmstrongCheck(n):
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")