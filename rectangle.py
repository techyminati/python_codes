#!/bin/python3
#Simple program to print rectangle of desired width and length
l = int(input("Enter Length : "))
b = int(input("Enter Breadth : "))
x = 1
print("*"*b)
if b > 3 :
    for i in range(1,l-1):
        print("*"," "*(b-4),"*")
        x = x+1
elif b == 3:
    for i in range(1,l-1):
        print("*","*")
        x = x+1
else :
    for i in range(1,l-1):
        print("*"*b)
        x = x+1
if l > 1:
    print("*"*b)
