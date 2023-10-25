Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def isLongPressedName(self, name: str, typed: str) -> bool:
        i=0
        j=0
        while(j<len(typed)):
            if(i<len(name) and name[i]==typed[j] ):
                i+=1
                j+=1
            elif(j>0 and typed[j]==typed[j-1]):
                j+=1
            else:
                return False
        return i==len(name)