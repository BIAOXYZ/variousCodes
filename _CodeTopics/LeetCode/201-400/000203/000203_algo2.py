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

        # 递归法实现：假定后面的都已经删好了。

        if not head:
            return None
        elif head.val != val:
            head.next = self.removeElements(head.next, val)
        else:
            return self.removeElements(head.next, val)
        return head
        
"""
https://leetcode-cn.com/submissions/detail/184190237/

66 / 66 个通过测试用例
状态：通过
执行用时: 52 ms
内存消耗: 27.4 MB

执行用时：52 ms, 在所有 Python 提交中击败了82.48%的用户
内存消耗：27.4 MB, 在所有 Python 提交中击败了5.10%的用户
"""
