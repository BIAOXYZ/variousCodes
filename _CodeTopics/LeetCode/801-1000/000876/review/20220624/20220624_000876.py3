# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:

        # 引入 dummyHead 的版本

        dummyHead = ListNode(0)
        dummyHead.next = head
        slow = fast = dummyHead
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow if not fast else slow.next
        
"""
https://leetcode.cn/submissions/detail/328812397/

执行用时：
40 ms
, 在所有 Python3 提交中击败了
40.48%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
28.27%
的用户
通过测试用例：
36 / 36
"""
