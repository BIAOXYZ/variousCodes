# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        # 利用栈实现
        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next
        
        for i in range(n):
            stack.pop()
        
        if not stack:
            return head.next
        else:
            stack[-1].next = stack[-1].next.next
            return head
        
"""
https://leetcode-cn.com/submissions/detail/116730310/

208 / 208 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 12.9 MB

执行用时：24 ms, 在所有 Python 提交中击败了64.93%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了5.26%的用户
"""
