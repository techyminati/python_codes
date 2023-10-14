x=int(input("Enter the number: "))
temp=x
rev=0
while(temp>0):
    dig=temp%10
    rev=rev*10+dig
    temp=temp//10

if(rev==x):
    print("The number is palindrome")
else:
    print("The number is not palindrome")
