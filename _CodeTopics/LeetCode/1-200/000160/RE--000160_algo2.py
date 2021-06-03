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
        while lisA[i] == lisB[i]:
            res = lisA[i]
            i -= 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/183813071/

12 / 39 个通过测试用例
状态：执行出错

执行出错信息：
IndexError: list index out of range
    while lisA[i] == lisB[i]:
Line 28 in getIntersectionNode (Solution.py)
    intersection_node = Solution().getIntersectionNode(listA, listB);
Line 80 in _driver (Solution.py)
    _driver()
Line 102 in <module> (Solution.py)
最后执行的输入：
1
[1]
[1]
0
0
"""
