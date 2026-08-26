# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        # Step 1: Find middle using slow/fast pointers
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Copy second half into a list
        vals = []
        while slow:
            vals.append(slow.val)
            slow = slow.next

        # Step 3: Compare with first half
        curr = head
        while vals:
            if curr.val != vals.pop():  # compare with last element
                return False
            curr = curr.next

        return True
