# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        curr, dic = head, {}
        while curr:
            if dic.has_key(curr):
                return curr
            dic[curr] = 1
            curr = curr.next
        return None
        
"""
https://leetcode-cn.com/submissions/detail/114508334/

16 / 16 个通过测试用例
状态：通过
执行用时: 52 ms
内存消耗: 19.6 MB

执行用时：52 ms, 在所有 Python 提交中击败了20.26%的用户
内存消耗：19.6 MB, 在所有 Python 提交中击败了5.15%的用户
"""
