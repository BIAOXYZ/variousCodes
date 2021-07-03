class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        length = len(nums)
        dic = {i:0 for i in range(1, length+1)}
        for num in nums:
            dic[num] += 1
        
        res = [-1] * 2
        for k, v in dic.items():
            if v == 2:
                res[0] = k
            if v == 0:
                res[1] = k
        return res
        
"""
https://leetcode-cn.com/submissions/detail/192053554/

49 / 49 个通过测试用例
状态：通过
执行用时: 64 ms
内存消耗: 15.2 MB

执行用时：64 ms, 在所有 Python 提交中击败了34.55%的用户
内存消耗：15.2 MB, 在所有 Python 提交中击败了7.87%的用户
"""
