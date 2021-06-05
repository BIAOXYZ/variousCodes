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

        # 答案的双指针法，还是挺巧的。
        # 如果两个没交点，A走完自己再走B，最后走到空节点；B走完自己再走A，最后走到空节点。
        # 如果两个有交点，假设交集是C，那么：
        ## A走完自己独有的A1线路部分，然后C，然后B1，下一个就是交集部分C的第一个节点；
        ## B走完自己独有的B1线路部分，然后C，然后A1，下一个也是交集部分C的第一个节点。

        if not headA or not headB:
            return None
        currA, currB = headA, headB

        while True:
            if not currA and currB:
                currA = headB
            if not currB and currA:
                currB = headA
            # 其实这里相等的时候直接返回 currA 就行了，这么写主要是为了思路更明晰。
            if currA == currB:
                if not currA:
                    return None
                else:
                    return currA
            currA = currA.next
            currB = currB.next
        
"""
https://leetcode-cn.com/submissions/detail/184217627/

39 / 39 个通过测试用例
状态：通过
执行用时: 188 ms
内存消耗: 42.2 MB

执行用时：188 ms, 在所有 Python 提交中击败了46.99%的用户
内存消耗：42.2 MB, 在所有 Python 提交中击败了58.06%的用户
"""
