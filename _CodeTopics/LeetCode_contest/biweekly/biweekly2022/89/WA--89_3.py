class Solution(object):
    def minimizeArrayValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        # 如果第一个比后面部分的平均值还大，那也没有挪动的意义了，越挪动，至少第一个就可能越大
        # 还不如把后面的部分都搞成他们除去第一个数外的平均值
        if nums[0] * (n-1) > sum(nums[1:]):
            return nums[0]
        
        summ = sum(nums)
        avg = summ / n
        return avg if summ % n == 0 else avg + 1
    
"""
https://leetcode.cn/submissions/detail/373365295/

29 / 68 个通过测试用例
状态：解答错误

输入：
[13,13,20,0,8,9,9]
输出：
13
预期：
16
"""
