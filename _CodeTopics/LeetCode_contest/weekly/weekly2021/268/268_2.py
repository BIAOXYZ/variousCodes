class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        
        n = len(plants)
        res = 0
        currWater, currPos = capacity, -1
        i = 0
        while i < n:
            if currWater >= plants[i]:
                res += i - currPos
                currPos = i
                currWater -= plants[i]
                i += 1
            else:
                res += currPos - (-1)
                currPos = -1
                currWater = capacity
        return res
    
"""
https://leetcode-cn.com/submissions/detail/240704683/

40 / 40 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 13 MB
"""
