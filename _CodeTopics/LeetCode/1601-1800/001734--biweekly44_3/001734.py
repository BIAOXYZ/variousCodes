class Solution(object):
    def decode(self, encoded):
        """
        :type encoded: List[int]
        :rtype: List[int]
        """

        n = len(encoded) + 1
        total = 0
        for i in range(1, n+1):
            total ^= i
        
        total_without_first = 0
        for i in range(1, n, 2):
            total_without_first ^= encoded[i]
        
        perm = [total ^ total_without_first]
        for elem in encoded:
            perm.append(elem ^ perm[-1])
        return perm
        
"""
https://leetcode-cn.com/submissions/detail/176280148/

63 / 63 个通过测试用例
状态：通过
执行用时: 172 ms
内存消耗: 32.2 MB

执行用时：172 ms, 在所有 Python 提交中击败了100.00%的用户
内存消耗：32.2 MB, 在所有 Python 提交中击败了100.00%的用户
"""
"""
完全没想到会是双百。。。感觉都没有优化其实- -比如求前n个数的异或total的时候，应该有更快的办法。
"""
