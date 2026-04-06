# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            continued = curr.next
            curr.next = prev
            prev = curr
            curr = continued
        
        return prev
    
    def reorderList(self, head: Optional[ListNode]) -> None:

        
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next # slow is the mid

        second_half = self.reverse(slow.next)
        slow.next = None

        first_half = head
        while second_half:
            continued1, continued2 = first_half.next, second_half.next
            first_half.next = second_half
            second_half.next = continued1

            first_half = continued1
            second_half = continued2
        