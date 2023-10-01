def isPalindrome(x):
    n = x
    pd = 0
    if n < 0:
        return "Not a palindrome"
    while x > 0:
        d = x % 10
        pd = pd * 10 + d
        x = x// 10
    if pd == n:
        return f"{n} is a palindrome"
    else:
        return 'Not a palindrome'

x = int(input('Enter to number to check: '))
print(isPalindrome(x))
