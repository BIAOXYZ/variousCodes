class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # pick()表示在面对以start开头，以end结尾的数组时，先手能获得的最大分数。
        def pick(start, end):
            if start == end:
                return nums[start]
            sumChooseStart = nums[start] - pick(start + 1, end)
            sumChooseEnd = nums[end] - pick(start, end - 1)
            return max(sumChooseStart, sumChooseEnd)
        
        return pick(0, len(nums)-1) >= 0
        
"""
https://leetcode-cn.com/submissions/detail/103797744/

62 / 62 个通过测试用例
状态：通过
执行用时: 3684 ms
内存消耗: 12.7 MB
"""
"""
执行用时：3684 ms, 在所有 Python 提交中击败了12.16%的用户
内存消耗：12.7 MB, 在所有 Python 提交中击败了55.56%的用户
"""
