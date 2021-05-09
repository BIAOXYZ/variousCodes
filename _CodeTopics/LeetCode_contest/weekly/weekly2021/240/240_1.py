class Solution(object):
    def maximumPopulation(self, logs):
        """
        :type logs: List[List[int]]
        :rtype: int
        """
        
        dic = {}
        for log in logs:
            for k in range(log[0], log[1]):
                dic[k] = dic.setdefault(k, 0) + 1
        
        maxval = max(dic.values())
        for year in range(1950, 2050):
            if dic.has_key(year) and dic[year] == maxval:
                return year
    
"""
https://leetcode-cn.com/submissions/detail/175679669/

50 / 50 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 13 MB
"""
