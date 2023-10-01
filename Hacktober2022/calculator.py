# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("What do you want to do?")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
	# take input from the user
	choice = input("Enter choice(1/2/3/4): ")

	# check if choice is one of the four options
	if choice in ('1', '2', '3', '4'):
		num1 = float(input("Enter first number: "))
		num2 = float(input("Enter second number: "))

	if choice == '1':
		print(num1, "added to", num2)
		print("Sum:", add(num1, num2))

	elif choice == '2':
		print(num2, "subtracted from", num1)
		print("Difference:", subtract(num1, num2))

	elif choice == '3':
		print(num1, "multiplied", num2)
		print("Product:", multiply(num1, num2))

	elif choice == '4':
		print(num1, "divided by", num2)
		print("Result:", divide(num1, num2))

	else:
		print("Invalid input, retrying") #if the value isn't one of the four options
		continue
	# check if user wants another calculation
	while True:
		another = input("Another calculation?(y/N)")
		if another == 'y':
			break
		elif another == 'n':
			print("Thank you!")
			exit()
		else:
			print("Thank you!")
			exit()
