# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                # 说明肯定有环，此时可以引入第三个指针（当然也可以复用fast指针，但是没必要），思路分析参考了这个：
                # https://leetcode.cn/problems/linked-list-cycle-ii/solution/linked-list-cycle-ii-kuai-man-zhi-zhen-shuang-zhi-/
                third = head
                while slow != third:
                    slow = slow.next
                    third = third.next
                return third
        return None
        
"""
https://leetcode.cn/submissions/detail/321138635/

执行用时：
56 ms
, 在所有 Python3 提交中击败了
56.80%
的用户
内存消耗：
18.6 MB
, 在所有 Python3 提交中击败了
57.80%
的用户
通过测试用例：
16 / 16
"""
