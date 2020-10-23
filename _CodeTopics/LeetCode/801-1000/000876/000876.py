# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # 偶数个节点的情况
        if not fast:
            middle = middleRight = slow
        # 奇数个节点的情况
        else:
            middle = slow
        return middle
        
"""
https://leetcode-cn.com/submissions/detail/118150174/

15 / 15 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 13.2 MB

执行用时：16 ms, 在所有 Python 提交中击败了78.43%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了6.09%的用户
"""
