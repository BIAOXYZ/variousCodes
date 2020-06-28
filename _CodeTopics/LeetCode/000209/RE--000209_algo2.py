class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
      
        length = len(nums)
        if length == 0:
            return 0

        # 直接两重循环会超时，那就先用O(n)的复杂度把和缓存下，
        # 后面直接通过一次减法算出来连续子数组的和。
        # 但是其实还是有一定的危险性超时。。。
        sumresults = [0]
        for i in range(length):
            newsum = sumresults[-1] + nums[i]
            sumresults.append(newsum)
        sumresults.remove(0)

        if sumresults[-1] < s:
            return 0
        
        res = length
        for i in range(length-1):
            if nums[i] >= s:
                return 1
            # 根据这组输入: s = 7, nums = [2,3,1,2,4,3]
            # 带进去大概看看就直到为啥这里以及下面是 2 了。
            j = i + res - 2
            while sumresults[j] - sumresults[i] + nums[i] >= s:
                j -= 1
            res = min(res, j - i + 2)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/82817602/

4 / 15 个通过测试用例
状态：执行出错

执行出错信息：Line 32: IndexError: list index out of range
最后执行的输入：15
              [1,2,3,4,5]
"""
