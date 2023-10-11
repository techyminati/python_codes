#program to check if the number entered is a Disarium number.(89 = 8^1+ 9^2)
a=n=int(input("enter the number:-"))
s=0
while n>0: #to revese a number
  d=n%10
  s=s*10+d
  n=n//10
b=1
d=0
while s!=0:
  c=s%10
  d+=c**b
  b+=1
  s=s//10
if d==a:
  print("Disarium")
else:
  print("not Disarium")
