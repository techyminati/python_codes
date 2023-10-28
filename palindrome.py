def is_palindrome(n):
    return str(n) == str(n)[::-1]

def palindrome_series(start, end):
    palindromes = []
    for num in range(start, end + 1):
        if is_palindrome(num):
            palindromes.append(num)
    return palindromes

# Example usage:
start_range = 100
end_range = 2000
result = palindrome_series(start_range, end_range)
print(f"Palindrome series between {start_range} and {end_range}:")
print(result)
