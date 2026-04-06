# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeLists(self, head1, head2):
        # each list is sorted in ascending order
        dummy_node = ListNode(val=-1)
        curr = dummy_node

        while head1 and head2:
            if head1.val<=head2.val:
                curr.next = head1
                head1 = head1.next
            else:
                curr.next = head2
                head2 = head2.next
            curr = curr.next
        
        while head1:
            curr.next = head1
            head1 = head1.next
            curr = curr.next
        
        while head2:
            curr.next = head2
            head2 = head2.next
            curr = curr.next
        
        return dummy_node.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        merged = None
        
        for lst in lists:
            merged = self.mergeLists(merged, lst)


        return merged    