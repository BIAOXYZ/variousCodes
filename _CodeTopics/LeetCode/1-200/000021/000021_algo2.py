# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        
"""
https://leetcode-cn.com/submissions/detail/125048748/

208 / 208 个通过测试用例
状态：通过
执行用时: 32 ms
内存消耗: 13.1 MB

执行用时：32 ms, 在所有 Python 提交中击败了22.97%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了17.36%的用户
"""
