# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """

        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        
        subLenArr = [0 for _ in range(k)]
        i = 0
        while length > 0:
            subLenArr[i] += 1
            i = (i + 1) % k
            length -= 1

        res = [None for _ in range(k)]
        tmphead = head
        for i, subLen in enumerate(subLenArr):
            if subLen == 0:
                return res
            else:
                res[i] = tmphead
                tmp = tmphead
                while subLen > 1:
                    tmp = tmp.next
                    subLen -= 1
                tmphead = tmp.next
                tmp.next = None
        return res
        
"""
https://leetcode-cn.com/submissions/detail/221795500/

43 / 43 个通过测试用例
状态：通过
执行用时: 12 ms
内存消耗: 13.5 MB

执行用时：12 ms, 在所有 Python 提交中击败了98.33%的用户
内存消耗：13.5 MB, 在所有 Python 提交中击败了36.67%的用户
"""
