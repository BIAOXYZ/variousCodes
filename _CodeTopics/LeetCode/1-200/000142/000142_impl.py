# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        """
        # sum既可以做函数名，也可以用作变量名。但是看起来set是不行的，只能用sets了。

        UnboundLocalError: local variable 'set' referenced before assignment
            curr, set = head, set()
        Line 15 in detectCycle (Solution.py)
            result = Solution().detectCycle(head)
        Line 47 in _driver (Solution.py)
            _driver()
        Line 74 in <module> (Solution.py)
        """

        curr, sets = head, set()
        while curr:
            if curr in sets:
                return curr
            sets.add(curr)
            curr = curr.next
        return None
        
"""
https://leetcode-cn.com/submissions/detail/114508785/

16 / 16 个通过测试用例
状态：通过
执行用时: 32 ms
内存消耗: 19.2 MB

执行用时：32 ms, 在所有 Python 提交中击败了97.58%的用户
内存消耗：19.2 MB, 在所有 Python 提交中击败了8.63%的用户
"""
