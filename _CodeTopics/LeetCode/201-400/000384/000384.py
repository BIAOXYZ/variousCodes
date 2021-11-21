import random
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.numsBak = nums[:]
        ##print 111, self.nums, self.numsBak
        
    def reset(self):
        """
        :rtype: List[int]
        """
        ##print 222, self.nums, self.numsBak
        return self.numsBak
        
    def shuffle(self):
        """
        :rtype: List[int]
        """
        random.shuffle(self.nums)
        ##print 333, self.nums, self.numsBak
        return self.nums
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

"""
https://leetcode-cn.com/submissions/detail/240972693/

执行用时：284 ms, 在所有 Python 提交中击败了95.34%的用户
内存消耗：18.6 MB, 在所有 Python 提交中击败了83.42%的用户
通过测试用例：
10 / 10
"""
