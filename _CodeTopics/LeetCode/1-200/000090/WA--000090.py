class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # 和`LC78. 子集`的主要区别就是这题的nums里有重复元素。

        se = set()
        def check_if_in_and_add_not_in(lis):
            if tuple(lis) in se:
                return True  
            else:
                se.add(tuple(lis))
                return False
        
        res = [[]]
        length = len(nums)
        
        def backtrack(currList, startPos):
            if startPos == length:
                return
            for ind in range(startPos, length):
                currList.append(nums[ind])
                if not check_if_in_and_add_not_in(currList):
                    res.append(currList[:])
                    backtrack(currList, ind + 1)
                currList.pop()
        
        backtrack([], 0)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/161978081/

15 / 19 个通过测试用例
状态：解答错误

输入：
[4,4,4,1,4]
输出：
[[],[4],[4,4],[4,4,4],[4,4,4,1],[4,4,4,1,4],[4,4,4,4],[4,4,1],[4,4,1,4],[4,1],[4,1,4],[1],[1,4]]
预期：
[[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]
"""
