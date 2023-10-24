Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def mySqrt(self, x: int) -> int:
        i=0
        j=x
        while(i<=j):
            mid=i+(j-i)//2
            if(mid*mid==x):
                return mid
            elif(mid*mid<x):
                i=mid+1
            else:
                j=mid-1
        return i-1