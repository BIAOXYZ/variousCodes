class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """

        # 手动狗头题。
        return min(len(set(candyType)), len(candyType) / 2)
        
"""
https://leetcode-cn.com/submissions/detail/234188648/

执行用时：76 ms, 在所有 Python 提交中击败了65.50%的用户
内存消耗：15.1 MB, 在所有 Python 提交中击败了6.43%的用户
通过测试用例：
206 / 206
"""
