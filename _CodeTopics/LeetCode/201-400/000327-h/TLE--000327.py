class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """

        # 题目里的说明是这么说的：
        # “说明: 最直观的算法复杂度是 O(n2) ，请在此基础上优化你的算法。”
        # 最直观的算法是 O(n3) 吧？遍历每对下标，然后求和。想要 O(n2) 除非用前缀和。
        # 而且这个目测只用一层前缀和不行，应该是要用类似dp思想的，二维数组来存每层的前缀和。

        length = len(nums)
        res = 0
        prefixSum = [[0 for _ in range(length+1)] for _ in range(length)]

        # 先处理下第一行的前缀和
        for j in range(1, length+1):
            if j == 1:
                prefixSum[0][j] = nums[0]
            else:
                prefixSum[0][j] = prefixSum[0][j-1] + nums[j-1]
            if lower <= prefixSum[0][j] <= upper:
                res += 1

        for i in range(1, length):
            for j in range(i+1, length+1):
                prefixSum[i][j] = prefixSum[i-1][j] - nums[i-1]
                if lower <= prefixSum[i][j] <= upper:
                    res += 1
        
        return res
        
"""
https://leetcode-cn.com/submissions/detail/121658305/

56 / 61 个通过测试用例
状态：超出时间限制
"""
"""
我还以为 O(n2) 的前缀和算法能过呢。。。
"""
