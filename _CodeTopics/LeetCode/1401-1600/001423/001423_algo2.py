class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """

        # 上一个dp之所以会超时，是因为时间复杂度是O(n^2)。本来以为那个dp二维数组那些中间变量的计算也少不了，
        # 后来想了想，直接左边预计算前k个数的和，右边预计算后k个数的和，都存起来。然后根据两边各选几个直接加就行了。
        # 这样是O(n)的复杂度（准确说是O(k)的复杂度）。

        dpPrefixsumLeft = [0 for _ in range(k+1)]
        dpPrefixsumRight = [0 for _ in range(k+1)]
        res = [0 for _ in range(k+1)]

        for i in range(1, k+1):
            dpPrefixsumLeft[i] = dpPrefixsumLeft[i-1] + cardPoints[i-1]
            dpPrefixsumRight[i] = dpPrefixsumRight[i-1] + cardPoints[-i]
        for i in range(k+1):
            res[i] = dpPrefixsumLeft[i] + dpPrefixsumRight[k-i]
        return max(res)
        
"""
https://leetcode-cn.com/submissions/detail/144132186/

40 / 40 个通过测试用例
状态：通过
执行用时: 76 ms
内存消耗: 24.3 MB

执行用时：76 ms, 在所有 Python 提交中击败了37.93%的用户
内存消耗：24.3 MB, 在所有 Python 提交中击败了5.17%的用户
"""
