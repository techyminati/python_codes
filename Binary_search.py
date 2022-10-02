

# Returns index of x in arr if present, else -1
def binary_search(arr, low, high, x):

	# Check base case
	if high >= low:

		#finding the middle element
		mid = low + (high-low)// 2

		# If element is present at the middle itself
		if arr[mid] == x:
			return mid

		# If element is smaller than mid, then it can only
		# be present in left subarray
		elif arr[mid] > x:
			return binary_search(arr, low, mid - 1, x)

		# Else the element can only be present in right subarray
		else:
			return binary_search(arr, mid + 1, high, x)

	else:
		# Element is not present in the array
		return -1

# takes array from user
arr = []

n = int(input("Enter number of elements: "))

for i in range(n):
    inp = int(input("Enter elements: "))
    arr.append(inp)

x = int(input("Enter element to be searched: "))

# Function call
result = binary_search(arr, 0, n - 1, x)

if result != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")
