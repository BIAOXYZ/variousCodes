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
            # 这里 fast 移动了两步，有可能是个空节点，从而取 fast.val 时候报错
            # 所以需要先确定 fast 不是空节点时再去取值。
            if fast and fast.val == slow.val:
                return True
        return False
        
"""
https://leetcode.cn/submissions/detail/321138018/

19 / 21 个通过测试用例
状态：解答错误

输入：
[1,1,1,1]
-1
输出：
true
预期结果：
false
"""
