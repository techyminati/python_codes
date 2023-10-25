Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def pairSum(self, head: Optional[ListNode]) -> int:
        slow=head
        s=0
        fast=head
        a=head
        b=None
        while fast and fast.next:
            b=slow
            slow=slow.next
            fast=fast.next.next
        prev=None
        curr=slow
        nxt=None
        while(curr!=None):
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        while prev:
            s=max(s,prev.val+head.val)
            head=head.next
            prev=prev.next
        return s