# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        if not head.next:
            return None
        
        slow, fast = head, head.next
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return head
    
"""
https://leetcode-cn.com/submissions/detail/245379101/

70 / 70 个通过测试用例
状态：通过
执行用时: 1912 ms
内存消耗: 89.6 MB
"""
