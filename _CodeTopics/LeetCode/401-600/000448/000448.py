class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
    
        dic = {i:0 for i in range(1, len(nums)+1)}
        for num in nums:
            dic[num] += 1
        
        res = []
        for k, v in dic.items():
            if v == 0:
                res.append(k)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/145560361/

34 / 34 个通过测试用例
状态：通过
执行用时: 412 ms
内存消耗: 27.1 MB

执行用时：412 ms, 在所有 Python 提交中击败了11.63%的用户
内存消耗：27.1 MB, 在所有 Python 提交中击败了5.08%的用户
"""
