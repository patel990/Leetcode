# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        start = rev = ListNode(0)
        while l1 or l2 or carry:
            val1, val2 = 0,0 
            if l1:
                val1 = l1.val 
                l1 = l1.next 
            if l2:
                val2 = l2.val 
                l2 = l2.next 
            carry,rem = divmod((val2+val1+ carry), 10)
            rev.next = ListNode(rem)
            rev = rev.next
        return start.next
#Memory Usage: 14.1 MB, less than 98.13% of Python3 online submissions for Add Two Numbers.
