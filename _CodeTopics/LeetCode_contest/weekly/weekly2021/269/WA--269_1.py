class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            if num == target:
                res.append(i)
            if num > target:
                return res
    
"""
https://leetcode-cn.com/submissions/detail/242995842/

200 / 216 个通过测试用例
状态：解答错误

输入：
[1,2,5,2,3]
5
输出：
null
预期：
[4]
"""
