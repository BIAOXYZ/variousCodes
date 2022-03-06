class Solution(object):
    def minimalKSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        def series_sum(start, end):
            if end < start:
                return 0
            return (start + end) * (end - start + 1) / 2
        
        n = len(nums)
        nums.sort()
        res = 0
        insertedNum = 1
        
        for i, num in enumerate(nums):
            dis = num-insertedNum
            if dis <= k:
                res += series_sum(insertedNum, num-1)
                k -= dis
            else:
                res += series_sum(insertedNum, insertedNum + k - 1)
                k = 0
            if k == 0:
                break
            else:
                insertedNum = num + 1
        if k > 0:
            res += series_sum(num+1, num+k)
        return res
    
"""
https://leetcode-cn.com/submissions/detail/278081042/

40 / 87 个通过测试用例
状态：解答错误

输入：
[96,44,99,25,61,84,88,18,19,33,60,86,52,19,32,47,35,50,94,17,29,98,22,21,72,100,40,84]
35
输出：
843
预期：
794
"""
