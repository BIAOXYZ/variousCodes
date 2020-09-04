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

        pre = None
        curr = head

        while curr:
            next = curr.next
            curr.next = pre
            pre = curr
            curr = next 
        return pre
        
"""
https://leetcode-cn.com/submissions/detail/104875935/

27 / 27 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 14.9 MB
"""
"""
执行用时：28 ms, 在所有 Python 提交中击败了47.11%的用户
内存消耗：14.9 MB, 在所有 Python 提交中击败了34.45%的用户
"""
