# Python program to determine whether the number is Armstrong number or not

# Function to calculate x raised to the power y
def power(m, n):
	
	if n == 0:
		return 1
	if n % 2 == 0:
		return power(m, n // 2) * power(m, n // 2)
		
	return m * power(m, n // 2) * power(m, n // 2)

# Function to calculate order of the number
def order(m):

	# Variable to store of the number
	n = 0
	while (m != 0):
		n = n + 1
		m = m // 10
		
	return n

# Function to check whether the given number is Armstrong number or not
def isArmstrong(m):
	
	n = order(m)
	temp = m
	sum = 0
	
	while (temp != 0):
		digit = temp % 10
		sum = sum + power(digit, n)
		temp = temp // 10

	# If condition satisfies
	return (sum == m)

# Driver code
num = int(input("Enter a number: "))
print(isArmstrong(num))


