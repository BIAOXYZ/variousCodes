class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        # 作为对比的：如果在python2里（因为不方便用functools模块里的lru_cache()函数）进行记忆化搜索
        # 的时候不去手动缓存结果，其表现和第一个超时的程序 deliberate-TLE--000140.py 是一样的：
        # 短的用例可以过去，那个一堆aaaa中间一个b的长用例过不去。
        
        # 下面的实现和 000140_algo3.py 相比就少了四行，也就是用哈希表缓存结果的四行。
        # 我们故意运行一下，它会超时。留个备份算是。

        res = []
        length = len(s)

        """
        dic = {}
        """
        wordSet = set(wordDict)

        def backtrack(pos):
            """
            if pos in dic:
                return dic[pos]
            """
            if pos == length:
                return [[]]
            res = []
            for end in range(pos+1, length+1):
                currStr = s[pos:end]
                if currStr in wordSet:
                    tmplist = backtrack(end)
                    for wordlist in tmplist:
                        res.append([currStr] + wordlist)
            """
            dic[pos] = res
            """
            return res

        res = backtrack(0)
        res = [' '.join(elem) for elem in res]
        return res
        
"""
https://leetcode-cn.com/submissions/detail/120541131/

31 / 36 个通过测试用例
状态：超出时间限制

最后执行的输入：
"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
"""
