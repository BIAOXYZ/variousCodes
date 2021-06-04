# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        while head and head.val == val:
            head = head.next
        if not head:
            return None

        curr = head
        prev = ListNode(0)
        prev.next = curr
        while curr:
            if curr.val != val:
                curr = curr.next
                prev = prev.next
            else:
                prev.next = curr.next
                curr = curr.next
        return head
        
"""
https://leetcode-cn.com/submissions/detail/184103141/

66 / 66 个通过测试用例
状态：通过
执行用时: 64 ms
内存消耗: 19.9 MB

执行用时：64 ms, 在所有 Python 提交中击败了29.12%的用户
内存消耗：19.9 MB, 在所有 Python 提交中击败了10.56%的用户
"""
