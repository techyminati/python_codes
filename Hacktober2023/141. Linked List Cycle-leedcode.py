Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def hasCycle(self, head: Optional[ListNode]) -> bool:
        list=[]
        a=head
        while a!=None:
            if(a in list):
                return True
            else:
                list.append(a)
            a=a.next
        return False