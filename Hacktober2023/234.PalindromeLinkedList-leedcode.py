Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        nxt=None
        curr=slow.next
        prev=None
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        h1=head
        h2=prev
        while h2:
            if(h1.val!=h2.val):
                return False
            h1=h1.next
            h2=h2.next
        return True