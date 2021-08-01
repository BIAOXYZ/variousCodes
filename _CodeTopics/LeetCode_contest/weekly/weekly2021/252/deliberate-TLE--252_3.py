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
        
            
        while neededApples > 0:
            curr_1_8_apples = sum(range(1, i)) + i * (i-1)
            currSum = 8 * curr_1_8_apples + (i + i*2) * 4
            if neededApples <= currSum:
                return i * 8
            else:
                neededApples -= currSum
                i += 1
    
"""
https://leetcode-cn.com/submissions/detail/201941232/

7 / 304 个通过测试用例
状态：超出时间限制

最后执行的输入：
215073301725407
"""
