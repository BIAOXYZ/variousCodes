class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        res = []
        for word in words:
            dic = {}
            flag = True
            for i, ch in enumerate(word):
                if ch not in dic:
                    dic[ch] = pattern[i]
                else:
                    if dic[ch] != pattern[i]:
                        flag = False
                        break
            if flag and len(dic.values()) == len(set(dic.values())):
                res.append(word)
        return res
        
"""
https://leetcode.cn/submissions/detail/324277790/

执行用时：
40 ms
, 在所有 Python3 提交中击败了
55.56%
的用户
内存消耗：
15.1 MB
, 在所有 Python3 提交中击败了
8.47%
的用户
通过测试用例：
47 / 47
"""
