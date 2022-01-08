# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        
        tmplis = []
        while head:
            tmplis.append(head.val)
            head = head.next
        
        n = len(tmplis)
        res = 0
        for i in range(n/2):
            res = max(res, tmplis[i] + tmplis[n-1-i])
        return res
    
"""
https://leetcode-cn.com/submissions/detail/256384967/

46 / 46 个通过测试用例
状态：通过
执行用时: 1216 ms
内存消耗: 90.3 MB
"""
