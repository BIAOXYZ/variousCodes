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
            res += (fruit[1] / limit + 1) * time[fruit[0]]
        return res
    
"""
https://leetcode-cn.com/contest/season/2022-spring/submissions/304274052/

提交结果：解答错误 
输入：
Not available during contest.
输出：
Not available during contest.
预期：
Not available during contest.
标准输出：
Not available during contest.
"""
