# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gcd(self, a, b):
        while b!=0:
            a, b = b, a%b
        
        return a
    
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current and current.next:
            adjacent = current.next
            gcd_val = self.gcd(current.val, adjacent.val)

            new_node = ListNode(val=gcd_val)
            current.next = new_node
            new_node.next = adjacent

            current = adjacent
        
        return head
            
        