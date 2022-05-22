class Solution(object):
    def maximumBags(self, capacity, rocks, additionalRocks):
        """
        :type capacity: List[int]
        :type rocks: List[int]
        :type additionalRocks: int
        :rtype: int
        """
        
        n = len(rocks)
        curr = [capacity[i] - rocks[i] for i in range(n)]
        curr.sort()
        
        res = 0
        for i, num in enumerate(curr):
            if num == 0:
                res += 1
                continue
            if additionalRocks >= num:
                res += 1
                additionalRocks -= num
                continue
            else:
                break
        return res
    
"""
https://leetcode.cn/submissions/detail/316528149/

79 / 79 个通过测试用例
状态：通过
执行用时: 128 ms
内存消耗: 20.1 MB
"""
