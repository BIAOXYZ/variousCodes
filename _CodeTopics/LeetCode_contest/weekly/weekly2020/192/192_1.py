class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        
        x = [0]*n
        y = [0 for i in range(n)]
        for i in range(2*n):
            if i < n:
                x[i] = nums[i]
            else:
                y[i-n] = nums[i]
        
        res = list()
        for i in range(n):
            res.append(x[i])
            res.append(y[i])
        return res
    
"""
# https://leetcode-cn.com/submissions/detail/76912363/

53 / 53 个通过测试用例
	状态：通过
执行用时：28 ms
内存消耗：12.7 MB
"""
