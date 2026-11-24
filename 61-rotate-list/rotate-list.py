# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or not head.next or k==0:
            return head
        length=1
        tail=head
        while tail.next:
            tail=tail.next
            length+=1
        k=k%length
        if k==0:
            return head
        tail.next=head
        steps=length-k
        new=head
        for _ in range(steps-1):
            new=new.next
        newh=new.next
        new.next=None
        return newh


        