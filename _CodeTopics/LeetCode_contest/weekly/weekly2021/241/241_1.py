class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        res = 0
        for i in range(1, 2**n):
            s = bin(i)[2:]
            m = len(s)
            while m < n:
                s = "0" + s
                m += 1
            tmp = 0
            for i, ch in enumerate(s):
                if ch == "1":
                    tmp ^= nums[i]
            res += tmp
        return res
    
"""
https://leetcode-cn.com/submissions/detail/177886214/

47 / 47 个通过测试用例
状态：通过
执行用时: 136 ms
内存消耗: 13.1 MB
"""
