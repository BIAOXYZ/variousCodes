class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        length = len(nums)
        res = []

        def backtrace(currArr, leftArr):
            if not leftArr:
                res.append(currArr[:])
                return
            for num in leftArr:
                currArr.append(num)
                leftArr.remove(num)
                backtrace(currArr, leftArr)
                currArr.remove(num)
                leftArr.append(num)

        backtrace([], nums)
        return res
"""
https://leetcode-cn.com/submissions/detail/109198666/

1 / 25 个通过测试用例
状态：解答错误

输入：
[1,2,3]
输出：
[[1,2,3],[1,2,3],[2,3,1],[2,3,1],[2,1,3],[2,1,3]]
预期：
[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""
