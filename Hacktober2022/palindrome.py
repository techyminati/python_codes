#python program to check if an integre is palindrome or not.
#A number is a palindrome if it is same when forward or backward. For example: 121,12321,3443,543212345


#First coding approach

def pal(n):
    t=int(n)
    p=0
    while n>0:
        d=n%10     #finds out the digit at ones place. ex: 121%10=1
        p=p*10+d   #p=0*10+1=1 for the first iteration of the loop then p=1*10+2=12 and then p=12*10+1=121
        n=n//10    #to remove the last digit from the number. for example: 121//10=12 

    if t==p:      #if the reversed and the original integers are equal then the integer is a palindrome
        return True
    else:
        return False


#Second Coding approach

def pal_2(x):
    if x>0:
        return str(x)==str(x)[::-1]  #storing the integer in a string and then reversing it and checking if both are equal or not 
    elif x<0:
        x=x*(-1)                     #this is done to remove the negative sign(-121 becomes 121) so that it can be stored as a string and negative sign is not present as a character
        return str(x)==str(x)[::-1]

