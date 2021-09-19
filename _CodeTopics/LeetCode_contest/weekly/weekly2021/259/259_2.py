from collections import deque
class Solution(object):
    def sumOfBeauties(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        currLeftMax = [0]
        currRightMin = deque([10**5+1])
        
        for i in range(1, n-1):
            currLeftMax.append(max(nums[i-1], currLeftMax[-1]))
        for j in range(n-2, 0, -1):
            currRightMin.appendleft(min(nums[j+1], currRightMin[0]))
        currRightMin.appendleft('placeholder')
        ##print currLeftMax,currRightMin
        
        res = 0
        for i in range(1, n-1):
            if currLeftMax[i] < nums[i] < currRightMin[i]:
                res += 2
            elif nums[i-1] < nums[i] < nums[i+1]:
                res += 1
        return res
    
"""
https://leetcode-cn.com/submissions/detail/220969057/

57 / 57 个通过测试用例
状态：通过
执行用时: 488 ms
内存消耗: 22.5 MB
"""
