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
            j = min(i + res - 1, length - 1)
            while sumresults[j] - sumresults[i] + nums[i] >= s:
                j -= 1
                # s=15, nums=[1,2,3,4,5]这组输入之所以会错，就是因为后面i一直增大，j
                # 一直不变，那么res总会减小。
                # 后来想了想只能把这句移到while循环里面，牺牲一些效率。
                # 也可以加flag，但是太丑陋而且容易混淆。
                res = min(res, j + 1 - i + 1)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/82838848/

15 / 15 个通过测试用例
状态：通过
执行用时：48 ms
内存消耗：15.7 MB
"""
"""
# 都用了前缀和数组了，这内存消耗还能超100%。。。

执行用时：48 ms, 在所有 Python 提交中击败了32.81%的用户
内存消耗：15.7 MB, 在所有 Python 提交中击败了100.00%的用户
"""
