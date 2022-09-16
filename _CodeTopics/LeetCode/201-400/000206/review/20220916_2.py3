# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return head
        pre = head
        cur = head.next
        pre.next = None

        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

        """
        if not head or not head.next:
            return head
        res = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return res
        """
        
"""
https://leetcode.cn/submissions/detail/363574405/

执行用时：
32 ms
, 在所有 Python3 提交中击败了
95.93%
的用户
内存消耗：
16 MB
, 在所有 Python3 提交中击败了
80.43%
的用户
通过测试用例：
28 / 28
"""
