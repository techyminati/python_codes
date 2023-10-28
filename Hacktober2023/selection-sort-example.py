#python selection sort example

def selection_sort(arr):
    # Traverse through all elements in the array
    for i in range(len(arr)):
        # Assume the current element is the minimum
        min_index = i

        # Search for the minimum element in the remaining unsorted part
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the current element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage

my_list = [64, 25, 12, 22, 11, 65, 78, 999, 456, 42, 88, 2, 5, 1 ]
selection_sort(my_list)
print("Sorted array:", my_list)


