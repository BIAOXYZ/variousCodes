class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        
        oneDimensionArr = [i for arr in grid for i in arr]
        if len(set(oneDimensionArr)) == 1:
            return 0
        
        length = len(oneDimensionArr)
        remainder = oneDimensionArr[0] % x
        for i in range(1, length):
            if oneDimensionArr[i] % x != remainder:
                return -1
        
        oneDimensionArr.sort()
        if length % 2 == 1:
            targetIndexes = [length / 2]
        else:
            targetIndexes = [length / 2 - 1, length / 2]
        
        res = float('inf')
        for ind in targetIndexes:
            tmp = 0
            for i in range(length):
                tmp += abs(oneDimensionArr[i] - oneDimensionArr[ind]) / x
            res = min(res, tmp)
        return res
    
"""
https://leetcode-cn.com/submissions/detail/227348089/

42 / 42 个通过测试用例
状态：通过
执行用时: 300 ms
内存消耗: 33.3 MB
"""
