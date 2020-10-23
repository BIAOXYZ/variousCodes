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

        # 这个感觉还不如 `000206.py`
        if not head or not head.next:
            return head
        pre = head.next
        curr = head.next.next
        head.next.next = head
        head.next = None

        while curr:
            next = curr.next
            curr.next = pre
            pre = curr
            curr = next
        return pre
        
"""
https://leetcode-cn.com/submissions/detail/118131729/

27 / 27 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 15 MB

执行用时：20 ms, 在所有 Python 提交中击败了87.28%的用户
内存消耗：15 MB, 在所有 Python 提交中击败了28.62%的用户
"""
