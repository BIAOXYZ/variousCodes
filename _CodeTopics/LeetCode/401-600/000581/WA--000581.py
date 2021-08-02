class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 找到最左边和最右边首先出现的需要排列的两个数（左取大，右取小），然后整个中间的就是结果了。

        length = len(nums)
        left, right = 0, length - 1
        while left < length - 1 and nums[left] <= nums[left+1]:
            left += 1
        if left == length - 1:
            return 0
        while right > left and nums[right] >= nums[right-1]:
            right -= 1
        return right - left + 1
        
"""
https://leetcode-cn.com/submissions/detail/202561610/

119 / 307 个通过测试用例
状态：解答错误

最后执行的输入：
[1,3,2,2,2]
输出：
2
预期结果：
4
"""
