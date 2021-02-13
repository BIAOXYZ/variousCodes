class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        bigNum = sys.maxint
        for i, num in enumerate(nums):
            tmpInd = num % bigNum
            nums[tmpInd-1] += bigNum
        
        res = []
        for i, num in enumerate(nums):
            if num < bigNum:
                res.append(i+1)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/145558464/

34 / 34 个通过测试用例
状态：通过
执行用时: 388 ms
内存消耗: 20.6 MB

执行用时：388 ms, 在所有 Python 提交中击败了15.43%的用户
内存消耗：20.6 MB, 在所有 Python 提交中击败了36.58%的用户
"""
