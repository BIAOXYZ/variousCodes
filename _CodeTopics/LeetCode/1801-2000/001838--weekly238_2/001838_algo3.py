import bisect
class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # 第 238 周周赛第二题。 
        
        # 滑动窗口实现。和之前的 “前缀和 + 二分查找” 的实现有点像吧，不过肯定不是同一种，细节上还是很不一样的。

        length = len(nums)
        nums.sort()

        maxFreq = 1
        left = 0
        currDistance = 0
        for right in range(1, length):
            currDistance += (nums[right] - nums[right-1]) * (right - left)
            while currDistance > k:
                # 这里要先算新的distance，然后left再加一。
                currDistance -= nums[right] - nums[left]
                left += 1
            maxFreq = max(maxFreq, right - left + 1)
        return maxFreq
        
"""
https://leetcode-cn.com/submissions/detail/201234636/

71 / 71 个通过测试用例
状态：通过
执行用时: 340 ms
内存消耗: 21.3 MB

执行用时：340 ms, 在所有 Python 提交中击败了75.84%的用户
内存消耗：21.3 MB, 在所有 Python 提交中击败了47.30%的用户
"""
