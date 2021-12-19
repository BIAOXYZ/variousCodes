class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """

        ans = []
        idx = 0
        tmp = list(s)
        for i, k in enumerate(tmp):
            if idx < len(spaces) and i == spaces[idx]:
                idx += 1
                ans.append(' ')
            ans.append(k)
        return "".join(ans)
        
"""
https://leetcode-cn.com/submissions/detail/249898043/

执行用时：280 ms, 在所有 Python 提交中击败了100.00%的用户
内存消耗：43.7 MB, 在所有 Python 提交中击败了100.00%的用户
通过测试用例：
66 / 66
"""
