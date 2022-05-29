class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n <= 1:
            return 0
        
        res = 0
        pre, preind = nums[0], 0
        i = 1
        flag = 0
        while i < n:
            if nums[i] >= pre:
                res = max(res, flag)
                pre, preind = nums[i], i
                flag = 0
            elif nums[i] < pre:
                if i-1 == preind or (i-1 > preind and nums[i] >= nums[i-1]):
                    flag += 1
                else:
                    res = max(res, flag)
                    pre, preind = nums[i], i
                    flag = 0
            i += 1
        res = max(res, flag)
        return res
    
"""
https://leetcode.cn/submissions/detail/319347832/

41 / 86 个通过测试用例
状态：解答错误

输入：
[7,14,4,14,13,2,6,13]
输出：
1
预期：
3
"""
