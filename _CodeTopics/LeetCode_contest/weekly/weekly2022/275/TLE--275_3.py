class Solution(object):
    def wordCount(self, startWords, targetWords):
        """
        :type startWords: List[str]
        :type targetWords: List[str]
        :rtype: int
        """
        
        dic1 = defaultdict(list)
        for w in startWords:
            dic1[len(w)].append(Counter(w))
        ##print dic1
        
        res = 0
        for wt in targetWords:
            n = len(wt)
            for ctr in dic1[n-1]:
                diff = ctr - Counter(wt)
                if not diff:
                    res += 1
                    break
        return res
    
"""
https://leetcode-cn.com/submissions/detail/256500519/

73 / 93 个通过测试用例
状态：超出时间限制
"""
