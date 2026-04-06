# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        curr = head
        newHead = None
        tail = None

        while curr:
            # check if there are at least k nodes in the ground
            temp = curr
            count = 0
            while temp and count<k:
                temp = temp.next
                count += 1
            
            if count<k:
                if tail:
                    tail.next = curr
                break

            groupHead = curr
            prev = None
            continued = None
            count = 0

            while curr and count<k:
                continued = curr.next
                curr.next = prev
                prev = curr
                curr = continued
                count += 1
            
            if not newHead:
                newHead = prev
            
            if tail:
                tail.next = prev
            
            tail = groupHead
        
        return newHead
