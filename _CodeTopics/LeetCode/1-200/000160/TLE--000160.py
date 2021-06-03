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

        currA = headA
        while currA:
            currB = headB
            while currB and currB != currA:
                currB = currB.next
            if currB == currA:
                return currB
            else:
                currA = currA.next
        return None
        
"""
https://leetcode-cn.com/submissions/detail/183811148/

35 / 39 个通过测试用例
状态：超出时间限制
"""
