# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        # 由于和主站 160 题相同，后续都只在那里更新。
        # 这里直接用了 `000160_algo3.py` 的提交（https://leetcode-cn.com/submissions/detail/184201024/）

        setA = set()
        while headA:
            setA.add(headA)
            headA = headA.next
        while headB:
            if headB in setA:
                return headB
            headB = headB.next
        return None
        
"""
https://leetcode-cn.com/submissions/detail/198022204/

45 / 45 个通过测试用例
状态：通过
执行用时: 156 ms
内存消耗: 42.6 MB

执行用时：156 ms, 在所有 Python 提交中击败了93.87%的用户
内存消耗：42.6 MB, 在所有 Python 提交中击败了5.05%的用户
"""
