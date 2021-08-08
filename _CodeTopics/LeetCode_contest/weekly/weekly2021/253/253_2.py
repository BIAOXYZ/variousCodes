import heapq
class Solution(object):
    def minStoneSum(self, piles, k):
        """
        :type piles: List[int]
        :type k: int
        :rtype: int
        """
        
        newpiles = [-pile for pile in piles]
        heapq.heapify(newpiles)
        while k > 0:
            k -= 1
            tmp = -heapq.heappop(newpiles)
            if tmp % 2 == 1:
                tmp += 1
            tmp >>= 1
            heapq.heappush(newpiles, -tmp)
        return -sum(newpiles)
    
"""
https://leetcode-cn.com/submissions/detail/204493150/

59 / 59 个通过测试用例
状态：通过
执行用时: 2548 ms
内存消耗: 21.2 MB
"""
