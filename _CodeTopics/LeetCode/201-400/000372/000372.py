class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """

        if a % 1337 == 0:
            return 0
        if a == 1:
            return 1
        if a == -1:
            return 1 if b[-1] % 2 == 0 else -1

        length = len(b)
        exponent = 0
        for i in range(length):
            exponent *= 10
            exponent += b[i]
        
        # 1337 = 7 * 191，所以其欧拉函数值 \phi(1337) = 6 * 190 = 1140
        exponent = exponent % 1140
        return a**exponent % 1337
        
"""
https://leetcode-cn.com/submissions/detail/245327223/

执行用时：24 ms, 在所有 Python 提交中击败了97.06%的用户
内存消耗：13.3 MB, 在所有 Python 提交中击败了76.47%的用户
通过测试用例：
55 / 55
"""
