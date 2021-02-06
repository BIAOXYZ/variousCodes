class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        flag = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                flag += 1
                if flag > 1:
                    return False
                if i >= 1 and nums[i-1] > nums[i+1]:
                    # return False
                    """
                    # 这里不应该直接return False，而且走另一种策略（比如对用例[5,7,1,8]来说）：
                    # 把 nums[i+1] 增大，变成等于 nums[i]。
                    # 另一种策略其实就是对应这个if分支：把 nums[i] 减小到 nums[i+1]。
                    # 然后看新的 nums[i]（也就是nums[i+1]了）和 nums[i-1] 的关系。
                    """
                    nums[i+1] = nums[i]
        return True
        
"""
https://leetcode-cn.com/submissions/detail/144281837/

335 / 335 个通过测试用例
状态：通过
执行用时: 40 ms
内存消耗: 13.9 MB

执行用时：40 ms, 在所有 Python 提交中击败了36.14%的用户
内存消耗：13.9 MB, 在所有 Python 提交中击败了53.63%的用户
"""
