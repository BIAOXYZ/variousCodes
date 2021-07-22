class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """

        # 参考官方答案，这个很不好想，除非再接触一些同类题，不然肯定是忘。

        diff = [0] * 52   # 差分数组
        for l, r in ranges:
            diff[l] += 1
            diff[r+1] -= 1
        # 前缀和
        curr = 0
        for i in range(1, 51):
            curr += diff[i]
            if left <= i <= right and curr <= 0:
                return False
        return True
        
"""
https://leetcode-cn.com/submissions/detail/198790768/

105 / 105 个通过测试用例
状态：通过
执行用时: 12 ms
内存消耗: 12.9 MB

执行用时：12 ms, 在所有 Python 提交中击败了100.00%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了78.38%的用户
"""
