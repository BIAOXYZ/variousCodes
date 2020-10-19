class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length = len(nums)

        # 把数组里的0和负数都变成length+1。这里如果变成None，后面处理可能要麻烦得多。
        for i in range(length):
            if nums[i] <= 0:
                nums[i] = length + 1
        
        for i in range(length):
            if abs(nums[i]) <= length:
                nums[abs(nums[i])-1] *= -1

        for i in range(length):
            if nums[i] > 0:
                return i + 1
        return length + 1

"""
https://leetcode-cn.com/submissions/detail/82438498/

113 / 165 个通过测试用例
状态：解答错误

输入：[1,1]
输出：1
预期：2
"""
