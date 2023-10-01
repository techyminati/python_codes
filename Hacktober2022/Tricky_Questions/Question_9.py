#
#  * Author: Aman Upadhyay
#  * Email: amanupadhyay0208@gmail.com
#  * GitHub: https://github.com/AmanxUpadhyay
#

# Write a Python program to generate prime numbers of series up to n.
def PrimeNumber(n):
    i = 2
    while i <= n:
        j = 2
        while j <= (i // 2):
            if i % j == 0:
                break
            j += 1
        else:
            print(i)
        i += 1

# Driver code
Number = int(input("Enter a number: "))
PrimeNumber(Number)