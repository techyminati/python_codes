str = input("Enter the string : ")

vowels = 'aeiou'

# returns the string with same case for proper comparison 
str = str.casefold()

# Create a new dictionary with keys from vowels and value set to 0 
count = {}.fromkeys(vowels, 0)

# Count each character in given string 
for char in str:
    if char in count:
        count[char] += 1

print(count)