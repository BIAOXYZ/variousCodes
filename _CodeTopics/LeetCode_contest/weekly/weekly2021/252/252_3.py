class Solution(object):
    def minimumPerimeter(self, neededApples):
        """
        :type neededApples: int
        :rtype: int
        """
        
        i = 1
        curr_1_8_apples = 0
        currSum = 8 * curr_1_8_apples + (i + i*2) * 4
        if neededApples <= currSum:
            return i * 8
        else:
            neededApples -= currSum
            i += 1
        
        curr_1_8_apples = 3
        currSum = 8 * curr_1_8_apples + (i + i*2) * 4
        if neededApples <= currSum:
            return i * 8
        else:
            neededApples -= currSum
            i += 1
        
        while True:
            #curr_1_8_apples = sum(range(1, i)) + i * (i-1)
            curr_1_8_apples += (i-2) + i + (i-1)
            currSum = 8 * curr_1_8_apples + (i + i*2) * 4
            if neededApples <= currSum:
                return i * 8
            else:
                neededApples -= currSum
                i += 1
    
"""
https://leetcode-cn.com/submissions/detail/202075513/

304 / 304 个通过测试用例
状态：通过
执行用时: 1264 ms
内存消耗: 12.8 MB
"""
