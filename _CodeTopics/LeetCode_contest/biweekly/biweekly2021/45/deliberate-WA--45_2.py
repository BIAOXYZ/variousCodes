class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        length = len(nums)
        prefixSum = [nums[0]]
        for i in range(1, length):
            prefixSum.append(prefixSum[-1] + nums[i])
        print prefixSum
                
        maxPositive = maxPositive2 = 0
        minNegative = minNegative2 = 0
        posInd = posInd2 = 0
        negInd = negInd2 = 0
        for i, summ in enumerate(prefixSum):
            if summ > 0:
                if summ >= maxPositive:
                    maxPositive2 = maxPositive; maxPositive = summ
                    posInd2 = posInd; posInd = i
            elif summ < 0:
                if summ <= minNegative:
                    minNegative2 = minNegative; minNegative = summ
                    negInd2 = negInd; negInd = i
        
        print posInd, posInd2
        print negInd, negInd2
        absPos = prefixSum[posInd] - prefixSum[posInd2-1] if posInd2 != 0 else prefixSum[posInd]
        absNeg = abs(prefixSum[negInd] - prefixSum[negInd2-1]) if negInd2 != 0 else abs(prefixSum[negInd])
        return max(absPos, absNeg)
    
"""
https://leetcode-cn.com/submissions/detail/144269487/

3 / 64 个通过测试用例
状态：解答错误

输入：
[1,-3,2,3,-4]
输出：
3
预期：
5
"""
