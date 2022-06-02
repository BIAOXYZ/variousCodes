# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # 官方答案是让 fast 先走一步，这里写一个不用先走的

        slow = fast = head
        while fast and fast.next:
            # 这里要先移动再比较，否则开始时候都在 head 那里，肯定相等。
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
        
"""
https://leetcode.cn/submissions/detail/321138133/

执行用时：
48 ms
, 在所有 Python3 提交中击败了
97.31%
的用户
内存消耗：
18.6 MB
, 在所有 Python3 提交中击败了
43.85%
的用户
通过测试用例：
21 / 21
"""
