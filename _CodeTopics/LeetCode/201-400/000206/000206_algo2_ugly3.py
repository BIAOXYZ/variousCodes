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

        # 下面两种都可以。会分别注释掉并提交两次。

        def reverse_adjacency(pre, curr):
            if not curr or not curr.next:
                return pre, curr
            pre = curr
            curr = curr.next
            _, end = reverse_adjacency(pre, curr)
            curr.next = pre
            pre.next = None
            return _, end

        pre = None
        curr = head
        _, end = reverse_adjacency(pre, head)
        return end

        """
        def reverse_adjacency(pre, curr):
            if not curr or not curr.next:
                return curr
            pre = curr
            curr = curr.next
            end = reverse_adjacency(pre, curr)
            curr.next = pre
            pre.next = None
            return end

        pre = None
        curr = head
        end = reverse_adjacency(pre, head)
        return end
        """
        
"""
https://leetcode-cn.com/submissions/detail/105010156/

27 / 27 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 19.3 MB
"""
"""
执行用时：28 ms, 在所有 Python 提交中击败了47.12%的用户
内存消耗：19.3 MB, 在所有 Python 提交中击败了5.07%的用户
"""
