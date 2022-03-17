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
        # 少了下面这行就要在 121212 之间死循环了。
        pre.next = None
        
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre
        
"""
https://leetcode-cn.com/submissions/detail/284902256/

执行用时：44 ms, 在所有 Python3 提交中击败了30.22%的用户
内存消耗：16 MB, 在所有 Python3 提交中击败了51.27%的用户
通过测试用例：
28 / 28
"""
"""
2022.03.17 微软三面第一题
"""
