class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        length, summ = len(nums), sum(nums)
        if length == 1 or summ % 2 != 0:
            return False
        
        target = summ / 2
        if max(nums) > target:
            return False

        # 这里 range 里的范围值一个是“加一型”，一个是“非加一型”，还是挺特殊的。
        # 行表示 nums 数组里可以取的数，从第一个到最后一个，所以需要用“非加一型”；
        # 第 j 列表示和为j，因为和可能是从 [0, target]，所以需要用“加一型”。
        dp = [[False for _ in range(target + 1)] for _ in range(length)]
        
        # 初始化：第一列全部为True；第一行只有两个值为True，其他都是False
        for i in range(length):
            dp[i][0] = True
        dp[0][nums[0]] = True

        for i in range(1, length):
            for j in range(1, target + 1):
                if j < nums[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i]]
        return dp[length-1][target]
        
"""
https://leetcode-cn.com/submissions/detail/184604038/

116 / 116 个通过测试用例
状态：通过
执行用时: 1816 ms
内存消耗: 29.3 MB

执行用时：1816 ms, 在所有 Python 提交中击败了36.77%的用户
内存消耗：29.3 MB, 在所有 Python 提交中击败了10.84%的用户
"""
