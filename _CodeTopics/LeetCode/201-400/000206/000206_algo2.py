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

        if head == None or head.next == None:
            return head
        end = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return end
        
"""
https://leetcode-cn.com/submissions/detail/104878447/

27 / 27 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 18.3 MB
"""
"""
执行用时：24 ms, 在所有 Python 提交中击败了70.68%的用户
内存消耗：18.3 MB, 在所有 Python 提交中击败了13.50%的用户
"""
