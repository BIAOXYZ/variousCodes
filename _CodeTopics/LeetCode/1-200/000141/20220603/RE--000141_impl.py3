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
            if slow.val == fast.val:
                return True
        return False
        
"""
https://leetcode.cn/submissions/detail/321137854/

6 / 21 个通过测试用例
状态：执行出错

执行出错信息：
AttributeError: 'NoneType' object has no attribute 'val'
    if slow.val == fast.val:
Line 17 in hasCycle (Solution.py)
    ret = Solution().hasCycle(param_1)
Line 44 in _driver (Solution.py)
    _driver()
Line 57 in <module> (Solution.py)
最后执行的输入：
[1,2]
-1
"""
