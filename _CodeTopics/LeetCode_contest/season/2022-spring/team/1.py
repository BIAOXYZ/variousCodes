class Solution(object):
    def getMinimumTime(self, time, fruits, limit):
        """
        :type time: List[int]
        :type fruits: List[List[int]]
        :type limit: int
        :rtype: int
        """
        
        res = 0
        for fruit in fruits:
            if fruit[1] % limit > 0:
                res += (fruit[1] / limit + 1) * time[fruit[0]]
            else:
                res += (fruit[1] / limit) * time[fruit[0]]
        return res
    
"""
https://leetcode-cn.com/contest/season/2022-spring/submissions/304276623/

提交结果：通过
"""
