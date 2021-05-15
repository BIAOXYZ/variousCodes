class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 先来trivial的，看输入量级是 2*10^4，所以 O(n^2) 算法也有可能不超时。
        # 但是如果两个循环就搞定了，似乎也不应该是中等啊。。。

        res = 0
        length = len(nums)
        for i in range(length-1):
            for j in range(i+1, length):
                res = max(res, nums[i] ^ nums[j])
        return res
        
"""
https://leetcode-cn.com/submissions/detail/177830345/

31 / 39 个通过测试用例
状态：超出时间限制
"""
