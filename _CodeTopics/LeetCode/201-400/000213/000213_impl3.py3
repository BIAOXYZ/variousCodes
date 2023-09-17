class Solution:
    def rob(self, nums: List[int]) -> int:

        # https://leetcode.cn/problems/house-robber-ii/solutions/2445622/jian-ji-xie-fa-zhi-jie-diao-yong-198-ti-qhvri/
        ## 我的上一个版本（就是下面注释掉的那行）和这个题解里的版本的主要区别就是我的版本会多算一部分。
        ## 多算了哪一部分呢？我们以首尾两个节点在不在选择里的情况进行分类，一共四种情况：
        ## 1.首尾都在 2.首尾都不在 3.首在尾不在 4.首不在尾在
        ## 链接里的版本其实就是计算： max(情况3, 情况2和情况4一起)；
        ## 我的版本其实就是计算： max(情况2和情况4一起, 情况2和情况3一起)。

        def basic_rob(nums):
            n = len(nums)
            dp = [nums[0]] + [0] * (n - 1)
            for i in range(1, n):
                dp[i] = max(dp[i-1], nums[i] + dp[i-2])
            return dp[n-1]            

        n = len(nums)
        if n <= 3:
            return max(nums)
        # return max(basic_rob(nums[1:]), basic_rob(nums[:n-1]))
        return max(nums[0] + basic_rob(nums[2:-1]), basic_rob(nums[1:]))
        
"""
https://leetcode.cn/problems/house-robber-ii/submissions/467203558/?envType=daily-question&envId=2023-09-17

时间
详情
44ms
击败 55.80%使用 Python3 的用户
内存
详情
15.65MB
击败 56.17%使用 Python3 的用户
"""
