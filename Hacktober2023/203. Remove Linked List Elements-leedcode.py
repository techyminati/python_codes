Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr=head
        prev=head
        if(head==None):
            return
        while head:
            if(head.val==val):
                head=head.next
            else:
                break
        while curr:
            if(curr.val==val):
                prev.next=curr.next
                curr=prev
            prev=curr
            curr=curr.next
        return head