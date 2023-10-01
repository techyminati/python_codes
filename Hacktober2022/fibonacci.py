# By: @agam778

input_number = int(input("Enter the number of fibonacci numbers to be generated: "))
first_number = 0
second_number = 1
print()
print("Fibonacci series of", input_number, "numbers is:")
print(first_number)
print(second_number)
for i in range(2, input_number):
    next_number = first_number + second_number
    print(next_number)
    first_number = second_number
    second_number = next_number
