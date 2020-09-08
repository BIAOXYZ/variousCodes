class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        if k > n:
            return []
        
        universe = range(1, n+1)
        combination = []
        res = []

        def calculate_ith_number(i, canBeUsed):
            if i == k:
                res.append(copy.deepcopy(combination))
                return
            for num in canBeUsed:
                combination.append(num)
                canBeUsed.remove(num)
                if canBeUsed:
                    calculate_ith_number(i+1, canBeUsed)
                    combination.pop()
        
        calculate_ith_number(0, universe)
        return res
"""
https://leetcode-cn.com/submissions/detail/106155898/

0 / 27 个通过测试用例
状态：解答错误

输入：
4
2
输出：
[[1,2],[1,4]]
预期：
[[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
"""
