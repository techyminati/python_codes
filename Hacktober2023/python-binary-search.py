#Python-DSA---Simple Binary Search --- works best on sorted list
# Python don't have Arrays, as built-in DS, but list[] as built-in DS, similar to that of array in other languages, like C.

def binary_search(list, item):
    low = 0
    high = len(list) -1
    while low <= high:
        mid = (low + high) // 2  # Use integer division to find the middle index --- The mid should be calculated as (low + high) // 2 to find the middle index correctly.
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return -1  # Return -1 to indicate that the item was not found in the list


my_list = [1, 3, 5, 7, 9, 20, 23, 45, 75, 81, 89, 93, 110, 745, 777, 7563, 569, 7452, 45, 53, 40, 1025]

#ml returns the index-position of the element in the list starting from 0
ml = binary_search(my_list, 23)

print("Length of the list is:", len(my_list))

#If list index is not Empty condition.
if ml !=-1 :
    #print("Index position of the list item is:", ml)
    print(f" List item {my_list[ml]}, found at the index position of {ml} from the list.")
else:
    print("Item not found in the list.")