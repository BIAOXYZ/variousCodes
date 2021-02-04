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
            ##print start, i
            # 如果是自然结束（也就是非break出去的），并且最后一位加上也合法的。
            if start + i == length - 1 and currCost + abs(ord(s[-1]) - ord(t[-1])) <= maxCost:
                res = max(res, i+1)
            else:
                res = max(res, i)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/143827436/

36 / 37 个通过测试用例
状态：超出时间限制
"""
