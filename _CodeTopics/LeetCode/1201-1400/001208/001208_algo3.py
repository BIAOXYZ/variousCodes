import bisect
class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """

        length = len(s)
        res = 0
        prefixSum = [0]
        for i in range(1, length+1):
            prefixSum.append(prefixSum[-1] + abs(ord(s[i-1]) - ord(t[i-1])))

        # 上面先求出前缀和，然后对于每一个left，用二分查找找到最右边的right。
        # 该right需满足： prefixSum[right] - prefixSum[left] <= maxCost。
        for left in range(length):
            right = bisect.bisect(prefixSum, maxCost + prefixSum[left])
            res = max(res, right - left - 1)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/144234370/

37 / 37 个通过测试用例
状态：通过
执行用时: 88 ms
内存消耗: 19.8 MB

执行用时：88 ms, 在所有 Python 提交中击败了22.45%的用户
内存消耗：19.8 MB, 在所有 Python 提交中击败了6.12%的用户
"""
