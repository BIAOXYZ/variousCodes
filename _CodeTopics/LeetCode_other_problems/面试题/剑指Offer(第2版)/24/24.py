# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return []
        
        next = head.next
        head.next = None
        pre = head
        curr = next

        while curr:
            next = curr.next
            curr.next = pre
            pre = curr
            curr = next 
        return pre
        
"""
https://leetcode-cn.com/submissions/detail/104850843/

27 / 27 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 14.8 MB
"""
"""
执行用时：16 ms, 在所有 Python 提交中击败了96.96%的用户
内存消耗：14.8 MB, 在所有 Python 提交中击败了37.05%的用户
"""
