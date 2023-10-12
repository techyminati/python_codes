x=13
#x= int(input())
k=(x//2)

for i in range (k+1):
    print((" "*(i))+("* "*(i+1)))
for i in range (k):
    print((" "*(k-i-1))+("* "*(k-i)))
