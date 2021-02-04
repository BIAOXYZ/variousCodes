class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """

        # 这个我猜会超时，因为题目标签里有 Sliding Window，但是这个只是暴力。

        length = len(s)
        res = 0

        for start in range(length):
            currCost = 0
            for i in range(length - start):
                currCost += abs(ord(s[start+i]) - ord(t[start+i]))
                if currCost > maxCost:
                    break
            res = max(res, i)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/143826377/

31 / 37 个通过测试用例
状态：解答错误

输入：
"krpgjbjjznpzdfy"
"nxargkbydxmsgby"
14
输出：
3
预期：
4
"""
