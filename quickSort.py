
def partition (arr,l,u):
    pivot = arr[u]
    idx = l-1
    for i in range(l,u):
        if (arr[i]<pivot):
            (arr[idx+1],arr[i]) = (arr[i],arr[idx+1])
            idx = idx + 1
    (arr[u],arr[idx+1])=(arr[idx+1],arr[u])
    return idx+1

def quickSort(arr,l,u):
    if(l<u):
        pivot = partition(arr,l,u)

        quickSort(arr,l,pivot-1)
        quickSort(arr,pivot+1,u)



arr = [55, 84, 44, 11, 8, 7, 8687, 5, 9, 67, 43, 34]

quickSort(arr,0,len(arr)-1)
print("Sorted array is:")
print(arr)
