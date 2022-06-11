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
            if flag:
                res.append(word)
        return res
        
"""
https://leetcode.cn/submissions/detail/324277470/

39 / 47 个通过测试用例
状态：解答错误

输入：
["abc","deq","mee","aqq","dkd","ccc"]
"abb"
输出：
["abc","deq","mee","aqq"]
预期结果：
["mee","aqq"]
"""
