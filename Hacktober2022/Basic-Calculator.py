n = 0
while n != 5 :
    n = int(input("Enter the number for operation\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Divison\n5. Exit\n"))
    if n != 5 :
     num1 = int(input("Enter 1st number\n"))
     num2 = int(input("Enter 2nd number\n"))
     if n == 1 :
         print(num1, "+", num2, "=", num1 + num2)
     elif n == 2 :
         print(num1, "-", num2, "=", num1 - num2)
     elif n == 3 :
         print(num1, "x", num2, "=", num1 * num2)
     elif n == 4 :
         print(num1, "/", num2, "=", num1 / num2)
