# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        # 2021.01.03 每日一题重新写的版本

        dummyHeadSamll, dummyHeadLarge = ListNode(0), ListNode(0)
        small, large, curr = dummyHeadSamll, dummyHeadLarge, head

        while curr:
            nxt = curr.next
            if curr.val < x:
                small.next = curr
                small = small.next
            else:
                large.next = curr
                large = large.next
            curr.next = None
            curr = nxt
        
        small.next = dummyHeadLarge.next
        return dummyHeadSamll.next
        
"""
https://leetcode-cn.com/submissions/detail/135503456/

166 / 166 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 12.9 MB

执行用时：24 ms, 在所有 Python 提交中击败了60.66%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了78.22%的用户
"""
