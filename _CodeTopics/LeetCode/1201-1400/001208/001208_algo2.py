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
        currCost = 0
        left = right = 0

        while right <= length - 1:
            currCost += abs(ord(s[right]) - ord(t[right]))
            if currCost <= maxCost:
                right += 1
            else:
                res = max(res, right - left)
                currCost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
                right += 1
        # 这里额外多算一次，同样是为了处理最后一位也合法，但是已经自然结束的情形。
        res = max(res, right - left)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/143829200/

37 / 37 个通过测试用例
状态：通过
执行用时: 72 ms
内存消耗: 13.8 MB

执行用时：72 ms, 在所有 Python 提交中击败了37.78%的用户
内存消耗：13.8 MB, 在所有 Python 提交中击败了100.00%的用户
"""
