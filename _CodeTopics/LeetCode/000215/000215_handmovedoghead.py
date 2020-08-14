class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        nums.sort(reverse=True)
        return nums[k-1]

"""
https://leetcode-cn.com/submissions/detail/82887642/

32 / 32 个通过测试用例
状态：通过
执行用时：24 ms
内存消耗：12.9 MB
"""
"""
# 大python终于站起来了！:sunflower::chicken:（手动狗头。。。
# 一会手写一下排序- -不然这题还有啥意思- -

执行用时：24 ms, 在所有 Python 提交中击败了84.44%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了16.67%的用户
"""
