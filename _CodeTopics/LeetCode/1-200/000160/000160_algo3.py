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

        # 答案的哈希集合法，其实我觉得和我上一个（000160_algo2.py）区别不大————反正都是要引入外部存储，就是用这个快点而已。

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
https://leetcode-cn.com/submissions/detail/184201024/

39 / 39 个通过测试用例
状态：通过
执行用时: 152 ms
内存消耗: 42.7 MB

执行用时：152 ms, 在所有 Python 提交中击败了99.42%的用户
内存消耗：42.7 MB, 在所有 Python 提交中击败了5.12%的用户
"""
