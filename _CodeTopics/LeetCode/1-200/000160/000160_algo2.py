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

        # 一个简单题，两重循环还超时，服了。。。然后想了下应该是想考察先反转链表，然后倒着比较。
        # 怒了，我偏要先用别的办法。

        lisA, lisB = [], []
        currA, currB = headA, headB
        while currA:
            lisA.append(currA)
            currA = currA.next
        while currB:
            lisB.append(currB)
            currB = currB.next
        
        i = -1
        res = None
        while len(lisA) >= abs(i) and len(lisB) >= abs(i) and lisA[i] == lisB[i]:
            res = lisA[i]
            i -= 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/183813179/

39 / 39 个通过测试用例
状态：通过
执行用时: 172 ms
内存消耗: 42.3 MB

执行用时：172 ms, 在所有 Python 提交中击败了85.27%的用户
内存消耗：42.3 MB, 在所有 Python 提交中击败了17.49%的用户
"""
