def swap_first_and_last(start, end, array):
    # Calculate the number of iterations needed to reverse the list
    num_reversals = end - start + 1

    # Swap the first and last elements by incrementing the count value
    count = 0
    while (num_reversals) // 2 != count:
        array[start + count], array[end - count] = array[end - count], array[start + count]
        count += 1
    return array

def left_rotate_array(array, size, rotations):
    # Reverse the entire list
    start = 0
    end = size - 1
    array = swap_first_and_last(start, end, array)

    # Divide the array into two sub-arrays based on the number of rotations
    # Divide the first sub-array and reverse it
    start = 0
    end = size - rotations - 1
    array = swap_first_and_last(start, end, array)

    # Divide the second sub-array and reverse it
    start = size - rotations
    end = size - 1
    array = swap_first_and_last(start, end, array)
    return array

original_array = [1, 2, 3, 4, 5, 6, 7, 8]
array_size = 8
print("Original array is [1, 2, 3, 4, 5, 6, 7, 8]")
rotations=int(input("Enter the number of rotations: "))
print('Original array:', original_array)

# Handle cases where the number of rotations is greater than the array size
if rotations <= array_size:
    print('Rotated array: ', left_rotate_array(original_array, array_size, rotations))
else:
    rotations = rotations % array_size
    print('Rotated array: ', left_rotate_array(original_array, array_size, rotations))
