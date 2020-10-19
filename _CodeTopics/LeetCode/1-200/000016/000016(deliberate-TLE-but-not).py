class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # 朴素的三重循环应该肯定会超时，但是我也打算先写了试试再说。
        length = len(nums)
        mindiff = nums[0] + nums[1] + nums[2] - target

        for i in range(length-2):
            for j in range(i+1,length-1):
                for k in range(j+1,length):
                    currdiff = nums[i] + nums[j] + nums[k] - target
                    if abs(currdiff) < abs(mindiff):
                        mindiff = currdiff
        return mindiff + target

"""
https://leetcode-cn.com/submissions/detail/82190463/

131 / 131 个通过测试用例
状态：通过
执行用时：8680 ms
内存消耗：12.7 MB
"""
"""
# 结果竟然没超时。。。

执行用时：8680 ms, 在所有 Python 提交中击败了5.05%的用户
内存消耗：12.7 MB, 在所有 Python 提交中击败了12.50%的用户
"""
