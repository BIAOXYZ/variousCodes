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
            # 这个if分支主要是为了处理nums里重复的数字
            if insertedNum >= num:
                insertedNum = num + 1
                continue
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
https://leetcode-cn.com/submissions/detail/278093524/

87 / 87 个通过测试用例
状态：通过
执行用时: 116 ms
内存消耗: 21.4 MB
"""
