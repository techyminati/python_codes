def karatsuba_multiply(x, y):
    # Base case: If x or y is less than 10, perform simple multiplication and return the result
    if x < 10 or y < 10:
        return x * y

    # Calculate the length of the numbers (number of digits)
    n = max(len(str(x)), len(str(y)))

    # Calculate the middle point (half) to split the numbers into two halves
    half = (n + 1) // 2

    # Split the input numbers into four parts: a, b, c, and d
    a = x // 10**half
    b = x % 10**half
    c = y // 10**half
    d = y % 10**half

    # Recursively calculate the products of the halves and the cross product
    ac = karatsuba_multiply(a, c)
    bd = karatsuba_multiply(b, d)
    adbc = karatsuba_multiply(a + b, c + d) - ac - bd

    # Combine the results to calculate the final product using Karatsuba algorithm
    return ac * 10**(2 * half) + adbc * 10**half + bd

def main():
    # Prompt the user to enter the first number
    x = int(input("Enter the first number: "))

    # Prompt the user to enter the second number
    y = int(input("Enter the second number: "))

    # Calculate the product using the Karatsuba algorithm
    product = karatsuba_multiply(x, y)

    # Display the result
    print("Product:", product)

if __name__ == "__main__":
    main()
