# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        slow = fast = head
        for i in range(k):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        return slow
        
"""
https://leetcode-cn.com/submissions/detail/214082845/

208 / 208 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 13 MB

执行用时：24 ms, 在所有 Python 提交中击败了38.02%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了53.24%的用户
"""
