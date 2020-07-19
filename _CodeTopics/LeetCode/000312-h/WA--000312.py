class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        假定剩三个元素[a, b, c]时，两边的两个元素a和c的大小关系是 c >= a。
        去中间时最大值为：abc + ac + c (1)
        去两边时最大值为：ab + bc + c (2) 或 ab + bc + b (3)
        
        若 c >= b，则(1)最大；
        即使c < b，(1)也在大部分情况下比(2)、(3)大。因为ac大部分情况下大于a+c。
        但是肯定是存在(2)、(3)比(1)大的情况，所以还得比一下。
        """
        
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == 0:
                nums.pop(i)
        
        length = len(nums)
        if length == 0:
            return 0
        elif length == 1:
            return nums[0]
        elif length == 2:
            return nums[0] * nums[1] + max(nums)
        elif length == 3:
            a, b, c = min(nums[0],nums[2]), nums[1], max(nums[0],nums[2])
            if c >= b:
                return a*b*c + a*c + c
            else:
                return max(a*b*c + a*c + c, a*b + b*c + b)
        else:
            minimum = min(nums)
            ind = nums.index(minimum)
            if ind == 0:
                res = nums[0] * nums[1]
            elif ind == length - 1:
                res = nums[-1] * nums[-2]
            else:
                res = nums[ind-1] * nums[ind] * nums[ind+1]
            nums.pop(ind)
            return res + self.maxCoins(nums)
            
"""
https://leetcode-cn.com/submissions/detail/89371493/

10 / 70 个通过测试用例
状态：解答错误

输入：[9,76,64,21]
输出：104500
预期：116718
"""
