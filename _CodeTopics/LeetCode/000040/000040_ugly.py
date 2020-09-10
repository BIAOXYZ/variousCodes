class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        length = len(candidates)
        res = []

        def dfs_find_sum_equals_target(currSum, currArr, pos):
            if currSum == target:
                elem = []
                for ind in currArr:
                    elem.append(candidates[ind])
                elem.sort()
                if elem not in res:
                    res.append(elem)
                return
            elif currSum > target:
                return
            else:
                for i in range(pos, length):
                    currSum += candidates[i]
                    currArr.append(i)
                    dfs_find_sum_equals_target(currSum, currArr, i+1)
                    currSum -= candidates[i]
                    currArr.pop()
        
        dfs_find_sum_equals_target(0, [], 0)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/106824237/

172 / 172 个通过测试用例
状态：通过
执行用时: 204 ms
内存消耗: 12.6 MB
"""
"""
执行用时：204 ms, 在所有 Python 提交中击败了17.60%的用户
内存消耗：12.6 MB, 在所有 Python 提交中击败了86.87%的用户
"""
