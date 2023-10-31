#Radix sort implementation in python

#counting sort method
def Count_Sort(arr, m):
    n = len(arr) 
    new = [1 for i in range(n)]
    c = [0] * (10)
    for i in range(0, n): 
        index = (arr[i]//m) 
        c[(index)%10] += 1
    for i in range(1,10): 
        c[i] += c[i-1]
    i = n-1
    while i>=0: 
        index = (arr[i]//m) 
        new[ c[ (index)%10 ] - 1] = arr[i] 
        c[ (index)%10 ] -= 1
        i -= 1
    i = 0
    for i in range(0,len(arr)): 
        arr[i] = new[i]


def Radix_sort(arr):
    largest_num = max(arr) 
    place_value = 1
    while largest_num/place_value > 0: 
        Count_Sort(arr,place_value) 
        place_value *= 10

#input the array
arr=list(map(int, input("elements of array:-").strip().split()))

#sort the array
Radix_sort(arr)

#print the sorted array
print ("Array after implementation of radix sort is:")
for i in range(len(arr)):
   print (arr[i])
