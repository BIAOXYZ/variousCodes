class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        binary = []
        while n > 0:
            binary.append(n % 2)
            n /= 2
        return len(filter(lambda x : x == 1, binary))
        
"""
https://leetcode-cn.com/submissions/detail/158116613/

601 / 601 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 13 MB

执行用时：16 ms, 在所有 Python 提交中击败了79.06%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了39.63%的用户
"""
