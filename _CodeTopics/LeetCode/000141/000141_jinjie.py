# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if not head or (head and not head.next):
            return False
         
        fast, slow = head.next.next, head.next
        while fast:
            if fast == slow:
                return True
            else:
                if not fast.next:
                    return False
                fast = fast.next.next
                slow = slow.next
        return False
        
"""
https://leetcode-cn.com/submissions/detail/114198359/

17 / 17 个通过测试用例
状态：通过
执行用时: 44 ms
内存消耗: 18.6 MB

执行用时：44 ms, 在所有 Python 提交中击败了51.06%的用户
内存消耗：18.6 MB, 在所有 Python 提交中击败了48.70%的用户
"""
