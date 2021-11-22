class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """

        if len(s) != len(goal):
            return False
        
        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)
                if len(diff) > 2:
                    return False
        
        if len(diff) == 2 and [s[diff[0]], s[diff[1]]] == [goal[diff[1]], goal[diff[0]]]:
            return True
        if len(diff) == 0 and len(set(s)) < len(s):
            return True 
        return False
        
"""
https://leetcode-cn.com/submissions/detail/241339320/

执行用时：12 ms, 在所有 Python 提交中击败了96.39%的用户
内存消耗：14.2 MB, 在所有 Python 提交中击败了20.48%的用户
通过测试用例：
34 / 34
"""
