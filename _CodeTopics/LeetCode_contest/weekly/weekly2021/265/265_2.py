# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        
        cur = head
        vals = []
        while cur:
            vals.append(cur.val)
            cur = cur.next
        
        n = len(vals)
        if n <= 2:
            return [-1, -1]
        
        inds = []
        for i in range(1, n-1):
            if (vals[i-1] < vals[i] and vals[i] > vals[i+1]) or (vals[i-1] > vals[i] and vals[i] < vals[i+1]):
                inds.append(i)
        if len(inds) < 2:
            return [-1, -1]
        maxdis = mindis = inds[-1] - inds[0]
        for i in range(1, len(inds)):
            mindis = min(mindis, inds[i] - inds[i-1])
        return [mindis, maxdis]
    
"""
https://leetcode-cn.com/submissions/detail/233968968/

136 / 136 个通过测试用例
状态：通过
执行用时: 1128 ms
内存消耗: 92.1 MB
"""
