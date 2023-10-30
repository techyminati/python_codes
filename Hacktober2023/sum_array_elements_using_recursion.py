# Recursive function to sum elements of an array in Python

#Function Definiton
def sum_array(ary):
    # Base case: if the array is empty, the sum is 0
    if len(ary) == 0:
        return 0
    # Recursive case: add the first element to the sum of the rest of the array
    else:
        return ary[0] + sum_array(ary[1:])

# Example:
my_array = [11, 31, 55, 72, 98 , 11, 13, 51, 71, 91, 99, 745, 429, 658]
result = sum_array(my_array)
print("The sum of the array is:", result)

