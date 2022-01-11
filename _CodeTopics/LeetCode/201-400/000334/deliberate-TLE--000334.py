class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        # 这个和 `LC300. 最长递增子序列` 类似。
        # 先写一个动态规划的，由于输出太大，应该会超时。
        # （主要这里在大于等于3就可以结束，所以也有不超时的希望？）

        length = len(nums)
        # dp[i] 表示恰好以第 i 个元素结尾的最长子序列的长度
        dp = [1 for _ in range(length)]
        for i in range(1, length):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    if dp[i] >= 3:
                        return True
        return False
        
"""
https://leetcode-cn.com/submissions/detail/257494350/

75 / 76 个通过测试用例
状态：超出时间限制
"""
"""
注：这个在 LC300 里是可以的，就是输入规模问题了，详见：
https://leetcode-cn.com/submissions/detail/145896286/
"""
