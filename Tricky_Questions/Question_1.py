#
#  * Author: Aman Upadhyay
#  * Email: amanupadhyay0208@gmail.com
#  * GitHub: https://github.com/AmanxUpadhyay
#

# Write a Python program for finding biggest of three numbers.
def Biggest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


# Driver code
x, y, z = [int(x) for x in input("Enter three numbers: ").split()]
print("Biggest number is: ", Biggest(x, y, z))