class Solution(object):
    def wonderfulSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        
        # 我感觉这个大概率超时。。。
        n = len(word)
        res = n
        
        for i in range(n-1):
            dic = {word[i]:1}
            for j in range(i+1, n):
                dic[word[j]] = dic.setdefault(word[j], 0) + 1
                flag = 0
                incr = 1
                for v in dic.values():
                    if v % 2 == 1:
                        flag += 1
                        if flag > 1:
                            incr = 0
                            break
                res += incr
        return res
    
"""
https://leetcode-cn.com/submissions/detail/190084336/

57 / 88 个通过测试用例
状态：超出时间限制
"""
