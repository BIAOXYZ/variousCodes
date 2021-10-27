import collections
class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """

        maxNum = 10**9
        possible_power_of_two = set()
        i = 0
        while 2**i < maxNum + 1:
            possible_power_of_two.add(str(2**i))
            i += 1
        
        tmp = collections.Counter(str(n))
        for elem in possible_power_of_two:
            if tmp == collections.Counter(elem):
                return True
        return False
        
"""
https://leetcode-cn.com/submissions/detail/233035238/

执行用时：32 ms, 在所有 Python 提交中击败了37.50%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了50.00%的用户
通过测试用例：
136 / 136
"""
