class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 该函数出自 LC461
        def hamming_distance(x, y):
            res = 0
            tmp = x ^ y
            while tmp:
                tmp &= tmp - 1
                res += 1
            return res
        
        res = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                res += hamming_distance(nums[i], nums[j])
        return res
        
"""
https://leetcode-cn.com/submissions/detail/181519637/

35 / 46 个通过测试用例
状态：超出时间限制
"""
"""
注：即使用最快的计算两数之间汉明距离的实现都超时了，所以 “二重循环 + 每次计算” 肯定不行。
"""
