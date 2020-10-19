# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return head
        
        node1, node2 = head, head.next
        node1.next = self.swapPairs(node2.next)
        node2.next = node1
        return node2
        
"""
https://leetcode-cn.com/submissions/detail/115374304/

55 / 55 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 12.7 MB

执行用时：24 ms, 在所有 Python 提交中击败了43.33%的用户
内存消耗：12.7 MB, 在所有 Python 提交中击败了5.00%的用户
"""
