By: @agam778
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
nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
