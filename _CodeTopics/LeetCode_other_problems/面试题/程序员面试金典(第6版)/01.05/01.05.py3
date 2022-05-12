class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:

        len1, len2 = len(first), len(second)
        if abs(len1 - len2) >= 2:
            return False
        elif len1 == len2:
            return sum(first[i] != second[i] for i in range(len1)) <= 1
        
        if len1 > len2:
            longWord, shortWord = first, second
            shortLen = len2
        else:
            longWord, shortWord = second, first
            shortLen = len1
        i, j, diff = 0, 0, 0
        while i < shortLen:
            if shortWord[i] != longWord[j]:
                diff += 1
                if diff > 1:
                    return False
                j += 1
            else:
                i += 1
                j += 1
        return True
        
"""
https://leetcode.cn/submissions/detail/312794763/

执行用时：
40 ms
, 在所有 Python3 提交中击败了
67.77%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
84.27%
的用户
通过测试用例：
1146 / 1146
"""
