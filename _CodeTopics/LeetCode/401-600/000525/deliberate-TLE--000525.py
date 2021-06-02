class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 不知道plain的从最长的可能长度开始试会不会超时，感觉大概率会超时，因为两重循环里还有个count运算。

        length = len(nums)
        res = 0
        if length % 2 == 0:
            res = length
        else:
            res = length - 1

        while res:
            for i in range(length - res + 1):
                currArr = nums[i:i+res]
                if currArr.count(1) == res / 2:
                    return res
            res -= 2
        return 0
        
"""
https://leetcode-cn.com/submissions/detail/183466550/

31 / 564 个通过测试用例
状态：超出时间限制
"""
