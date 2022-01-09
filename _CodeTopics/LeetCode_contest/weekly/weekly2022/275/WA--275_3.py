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
                if Counter(wt) - ctr:
                    res += 1
                    break
        return res
    
"""
https://leetcode-cn.com/submissions/detail/256490940/

19 / 93 个通过测试用例
状态：解答错误

输入：
["mox","bj","rsy","jqsh"]
["trk","vjb","jkr"]
输出：
3
预期：
1
"""
