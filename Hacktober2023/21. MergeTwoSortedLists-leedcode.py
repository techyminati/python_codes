Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l=ListNode()
        tail=l
        while list1 and list2:
            if(list1.val<list2.val):
                tail.next=list1
                list1=list1.next
            else:
                tail.next=list2
                list2=list2.next
            tail=tail.next
        if(list1):
            tail.next=list1
        if(list2):
            tail.next=list2
        return l.next
index = 0
node_values = {}
current = head
while current:
    node_values[index] = current.val
    current = current.next
    index += 1
max_sum = 0
for i in range(index):
    for j in range(i + 2, index):
        pair_sum = node_values[i] + node_values[j]
        max_sum = max(max_sum, pair_sum)
