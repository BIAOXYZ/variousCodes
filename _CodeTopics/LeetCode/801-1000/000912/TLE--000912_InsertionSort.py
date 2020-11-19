class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # 其实完全可以不用引入curr和prev，只要把while循环第二个条件改下就好。
        # 但是这里主要是为了易读性。
        length = len(nums)
        for i in range(1, length):
            curr, prev = nums[i], nums[i-1]
            while i - 1 >= 0 and curr < prev:
                nums[i], nums[i-1] = nums[i-1], nums[i]
                i -= 1
                curr, prev = nums[i], nums[i-1]
        return nums
        
"""
https://leetcode-cn.com/submissions/detail/124807153/

10 / 11 个通过测试用例
状态：超出时间限制
"""
"""
这题的限制搞笑呢。。。从冒泡排序到插入排序，给我超时两个了。。。
"""
