class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        length = len(nums)
        res = []

        def backtrace(currArr, leftArr):
            if not leftArr:
                tmpArr = currArr[:]
                if tmpArr not in res:
                    res.append(tmpArr)
                return
            for ind, num in enumerate(leftArr):
                currArr.append(num)
                leftArr.remove(num)
                backtrace(currArr, leftArr)
                currArr.remove(num)
                leftArr.insert(ind, num)

        backtrace([], nums)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/109327042/

16 / 30 个通过测试用例
状态：解答错误

输入：
[2,2,1,1]
输出：
[[2,2,1,1],[2,1,2,1],[2,1,1,2],[1,2,2,1],[1,1,2,2]]
预期：
[[1,1,2,2],[1,2,1,2],[1,2,2,1],[2,1,1,2],[2,1,2,1],[2,2,1,1]]
"""
