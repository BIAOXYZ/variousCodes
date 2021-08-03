import bisect
class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        length = len(nums)
        res = 0
        for i in range(length-2):
            for j in range(i+1, length-1):
                target = nums[i] + nums[j] - 1
                k = bisect.bisect_right(nums, target)
                res += k - 1 - j
        return res
        
"""
https://leetcode-cn.com/submissions/detail/202958246/

158 / 241 个通过测试用例
状态：解答错误

最后执行的输入：
[0,0,0]
输出：
-2
预期结果：
0
"""
