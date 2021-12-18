from collections import defaultdict
class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """

        # 官方答案方法一，除了算法不同外，感觉确实写得不错。而且那个next用的也很少见。

        inDegrees = Counter(y for _, y in trust)
        outDegrees = Counter(x for x, _ in trust)
        return next((i for i in range(1, n + 1) if inDegrees[i] == n - 1 and outDegrees[i] == 0), -1)
        
"""
https://leetcode-cn.com/submissions/detail/249806696/

执行用时：112 ms, 在所有 Python 提交中击败了17.21%的用户
内存消耗：16.5 MB, 在所有 Python 提交中击败了72.13%的用户
通过测试用例：
92 / 92
"""
