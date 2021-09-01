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

        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        
        curr = head
        for _ in range(length - k):
            curr = curr.next
        return curr
        
"""
https://leetcode-cn.com/submissions/detail/214083453/

208 / 208 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.2 MB

执行用时：20 ms, 在所有 Python 提交中击败了67.79%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了15.98%的用户
"""
