class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        # 1 + 2 + ... + 9 = 45
        if n > 45 or n < 1 or k > 9 or k < 1:
            return []
        
        res = []

        def dfs_find_sum_equals_n(currSum, currList, startNum):
            if currSum == n:
                if len(currList) == k:
                    res.append(currList[:])
                return
            elif currSum > n or len(currList) > k:
                return
            else:    
                for num in range(startNum, 10):
                    currSum += num
                    currList.append(num)
                    dfs_find_sum_equals_n(currSum, currList, num+1)
                    currSum -= num
                    currList.pop()

        dfs_find_sum_equals_n(0, [], 1)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/107106985/

18 / 18 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 12.7 MB
"""
"""
执行用时：28 ms, 在所有 Python 提交中击败了29.65%的用户
内存消耗：12.7 MB, 在所有 Python 提交中击败了57.24%的用户
"""
