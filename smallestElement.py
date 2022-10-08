arr = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
  
    arr.append(ele)    
min = arr[0];      
for i in range(0, len(arr)):       
   if(arr[i] < min):    
       min = arr[i];    
     
print("Smallest element present in given array: " + str(min));  
