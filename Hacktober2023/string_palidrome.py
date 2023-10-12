def palindrome(n):
    n=n.lower()
    l=len(n)
    mid=l//2
    rev=-1
    for i in range(mid):
        if n[i]==n[rev]:
            rev-=1
        else:
            print(n,'is not a palindrome')
            break
    else:
        print(n,'is a palindrome')
s=input('Enter string: ')
palindrome(s)