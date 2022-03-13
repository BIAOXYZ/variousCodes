class Solution(object):
    def maximumTop(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        if k == 0:
            return nums[0]
        n = len(nums)
        if n == 1:
            return -1
        if len(set(nums)) == 1:
            if k < n or (k > n and (k - n) % 2 == 1): return nums[0]
            else: return -1
        
        maxnum = max(nums)
        if k > n:
            return maxnum
        
        l, se = nums[:k-1], set(nums[k-1:])
        ## print(l, se)
        l.sort(reverse=True)
        res = nums[k]
        for num in l:
            if num not in se:
                res = max(res, num)
                break
        return res
    
"""
https://leetcode-cn.com/submissions/detail/282233494/

49 / 195 个通过测试用例
状态：解答错误

输入：
[31,15,92,84,19,92,55]
4
输出：
31
预期：
92
"""
