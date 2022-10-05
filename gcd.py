
# Python code to demonstrate naive
# method to compute gcd ( recursion )
 
def hcfnaive(a, b):
    if(b == 0):
        return abs(a)
    else:
        return hcfnaive(b, a % b)
 
a = int(input("Enter a number:"))
b = int(input("Enter another number:"))
 
# prints 12
print("The gcd of first and second number is : ", end="")
print(hcfnaive(a,b))